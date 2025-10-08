import json
from pathlib import Path
import sqlite3
from typing import Dict, Any
from db.romaneio_data.load_romaneio_data import query_romaneio_data_op_700_by_id, query_romaneio_data_op_405_by_id, query_romaneio_data_op_302_by_id

def load_json_from_path(json_path: str) -> dict:
    path = Path(json_path)
    
    if not path.exists():
        raise FileNotFoundError(f"JSON file not found: {json_path}")
    
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)
    

# def load_json_from_db(routine_ids: list[int]) -> dict:
    
#     conn = sqlite3.connect('./db/stress_db')  
#     cursor = conn.cursor()
#     data = []
#     try:
#         placeholders = ','.join(['?'] * len(routine_ids))
#         query = f"SELECT pr.id, pr.url, pr.romaneio_data_id, pr.operacao, pr.login_id, ac.username, ac.password, ac.username_id, ac.password_id FROM playwright_routine pr join auth_credentials ac on pr.login_id = ac.id WHERE pr.id IN ({placeholders})"
#         cursor.execute(query, routine_ids)
#         routine_rows = cursor.fetchall()
#         routine_dict = []
#         checker = set()
#         unique_users = []
#         for row in routine_rows:
#             id, url, romaneio_data_id, operacao, login_id, username, password, username_id, password_id = row
#             user_data = {}
#             if username not in checker:
#                 user_data = {
#                     "username": username,
#                     "password": password,
#                     "username_id": username_id,
#                     "password_id": password_id
#                 }
#                 checker.add(username)
#                 unique_users.append(user_data)
#             routine_dict.append({
#                 "id": id,
#                 "url": url,
#                 "romaneio_data_id": romaneio_data_id,
#                 "operacao": operacao,
#                 "login_id": next((user for user in unique_users if user["username"] == username), None)
#             })
#         print(routine_dict)
#         input('Pressione enter para continuar')
        
#         for routine in routine_dict:

#             if routine['operacao'] == '700 - Entrada Spot': 
#                 data.append(query_romaneio_data_op_700(routine, cursor, conn, routine['login_id']))
#             elif routine['operacao'] == '001 - VENDAS':
#                 data.append(query_romaneio_data_op_405(routine, cursor, conn, routine['login_id']))
#             elif routine['operacao'] == '302 - EM - Compras p/ Pedido':
#                 data.append(query_romaneio_data_op_302(routine, cursor, conn, routine['login_id']))
#             else:
#                 raise ValueError(f"Operação {routine['operacao']} não suportada")
#         return data
#     finally:
#         cursor.close()
#         conn.close()


def load_data_from_db_by_user(routine_ids: list[int]) -> dict:

    routine_romaneio_data = query_routine_romaneio_data(routine_ids)
    # romaneio_data = query_romaneio_data([row['romaneio_data_id'] for row in routine_romaneio_data])
    playwright_routine_user = query_playwright_routine_user([row['playwright_routine_user_id'] for row in routine_romaneio_data])
    
    return routine_romaneio_data



def query_routine_romaneio_data(routine_ids: list[int]) -> dict:
    conn = sqlite3.connect('./db/stress_db')
    cursor = conn.cursor()
    query = """
        SELECT playwright_routine_user_id, romaneio_data_id FROM routine_romaneio_data WHERE playwright_routine_user_id IN ({placeholders})
    """
    placeholders = ','.join(['?'] * len(routine_ids))
    cursor.execute(query.format(placeholders=placeholders), routine_ids)
    routine_romaneio_data_rows = cursor.fetchall()
    routine_romaneio_data = []
    checker = set()
    unique_users = []
    for row in routine_romaneio_data_rows:
        playwright_routine_user_id, romaneio_data_id = row

        playwright_routine_user = query_playwright_routine_user([playwright_routine_user_id])[0]
        romaneio_data = query_romaneio_data(romaneio_data_id, playwright_routine_user['operacao'])
        if playwright_routine_user_id not in checker:
            checker.add(playwright_routine_user_id)
            unique_users.append(playwright_routine_user_id)
            routine_romaneio_data.append({
                "playwright_routine_user_id": playwright_routine_user_id,
                "romaneio_data": [romaneio_data],
                "playwright_routine_user": playwright_routine_user
            })
        else:
            idx = next((i for i, d in enumerate(routine_romaneio_data) if d["playwright_routine_user_id"] == playwright_routine_user_id), None)
            routine_romaneio_data[idx]['romaneio_data'].append(romaneio_data)

    return routine_romaneio_data

def query_romaneio_data(romaneio_data_id: int, operacao: str) -> dict:
    conn = sqlite3.connect('./db/stress_db')
    cursor = conn.cursor()
    if operacao == '700 - Entrada Spot': 
        romaneio_data = query_romaneio_data_op_700_by_id(romaneio_data_id)
    elif operacao == '001 - VENDAS':
        romaneio_data = query_romaneio_data_op_405_by_id(romaneio_data_id)
    elif operacao == '302 - EM - Compras p/ Pedido':
        romaneio_data = query_romaneio_data_op_302_by_id(romaneio_data_id)
    else:
        raise ValueError(f"Operação {operacao} não suportada")
    return romaneio_data

def query_playwright_routine_user(playwright_routine_user_ids: list[int]) -> dict:
    conn = sqlite3.connect('./db/stress_db')
    cursor = conn.cursor()
    query = """
        SELECT url, login_id, operacao FROM playwright_routine_user WHERE id IN ({placeholders})
    """
    placeholders = ','.join(['?'] * len(playwright_routine_user_ids))
    cursor.execute(query.format(placeholders=placeholders), playwright_routine_user_ids)
    playwright_routine_user_rows = cursor.fetchall()
    playwright_routine_user = []
    for row in playwright_routine_user_rows:
        url, login_id, operacao = row
        login = query_auth_credentials([login_id])[0]
        playwright_routine_user.append({
            "url": url,
            "login": login,
            "operacao": operacao
        })
    return playwright_routine_user

def query_auth_credentials(auth_credentials_ids: list[int]) -> dict:
    conn = sqlite3.connect('./db/stress_db')
    cursor = conn.cursor()
    query = """
        SELECT username, password, username_id, password_id FROM auth_credentials WHERE id IN ({placeholders})
    """
    placeholders = ','.join(['?'] * len(auth_credentials_ids))
    cursor.execute(query.format(placeholders=placeholders), auth_credentials_ids)
    auth_credentials_rows = cursor.fetchall()
    auth_credentials = []
    for row in auth_credentials_rows:
        username, password, username_id, password_id = row
        auth_credentials.append({
            "username": username,
            "password": password,
            "username_id": username_id,
            "password_id": password_id
        })
    return auth_credentials

# print(load_data_from_db_by_user([1]))