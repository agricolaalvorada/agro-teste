import json
from pathlib import Path
import sqlite3
from typing import Dict, Any

def load_json_from_path(json_path: str) -> dict:
    path = Path(json_path)
    
    if not path.exists():
        raise FileNotFoundError(f"JSON file not found: {json_path}")
    
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)
    

def load_json_from_db(routine_ids: list[int]) -> dict:
    
    conn = sqlite3.connect('./db/stress_db')  
    cursor = conn.cursor()
    data = []
    try:
        placeholders = ','.join(['?'] * len(routine_ids))
        query = f"SELECT pr.id, pr.url, pr.romaneio_data_id, pr.operacao, pr.login_id, ac.username, ac.password, ac.username_id, ac.password_id FROM playwright_routine pr join auth_credentials ac on pr.login_id = ac.id WHERE pr.id IN ({placeholders})"
        cursor.execute(query, routine_ids)
        routine_rows = cursor.fetchall()
        routine_dict = []
        checker = set()
        unique_users = []
        for row in routine_rows:
            id, url, romaneio_data_id, operacao, login_id, username, password, username_id, password_id = row
            user_data = {}
            if username not in checker:
                user_data = {
                    "username": username,
                    "password": password,
                    "username_id": username_id,
                    "password_id": password_id
                }
                checker.add(username)
                unique_users.append(user_data)
            routine_dict.append({
                "id": id,
                "url": url,
                "romaneio_data_id": romaneio_data_id,
                "operacao": operacao,
                "login_id": next((user for user in unique_users if user["username"] == username), None)
            })
        print(routine_dict)
        input('Pressione enter para continuar')
        
        for routine in routine_dict:

            if routine['operacao'] == '700 - Entrada Spot': 
                data.append(query_romaneio_data_op_700(routine, cursor, conn, routine['login_id']))
            elif routine['operacao'] == '001 - VENDAS':
                data.append(query_romaneio_data_op_405(routine, cursor, conn, routine['login_id']))
            elif routine['operacao'] == '302 - EM - Compras p/ Pedido':
                data.append(query_romaneio_data_op_302(routine, cursor, conn, routine['login_id']))
            else:
                raise ValueError(f"Operação {routine['operacao']} não suportada")
        return data
    finally:
        cursor.close()
        conn.close()

def query_romaneio_data_op_700(routine_dict: dict, cursor: sqlite3.Cursor, conn: sqlite3.Connection, login: dict) -> dict:
            
    cursor.execute("""
        SELECT safra, safra_data_label, safra_input_id, parceiro, parceiro_data_label, parceiro_input_id, parceiro_ul_id,
                material, material_data_label, material_ul_id, motorista, motorista_data_label, motorista_input_id, motorista_ul_id,
                veiculo, veiculo_data_label, veiculo_input_id, veiculo_ul_id, reboque, reboque_input_id,
                deposito, deposito_input_id, deposito_data_label, deposito_ul_id, depositante_copy_id, btn_salvar_id
    FROM romaneio_data
    WHERE id = ?
    ORDER BY id ASC
    """, (routine_dict['romaneio_data_id'],))
    romaneio_rows = cursor.fetchall()
    romaneio = []
    for row in romaneio_rows:
        romaneio.append({
            "safra": row[0],
            "safra_data_label": row[1],
            "safra_input_id": row[2],
            "parceiro": row[3],
            "parceiro_data_label": row[4],
            "parceiro_input_id": row[5],
            "parceiro_ul_id": row[6],
            "material": row[7],
            "material_data_label": row[8],
            "material_ul_id": row[9],
            "motorista": row[10],
            "motorista_data_label": row[11],
            "motorista_input_id": row[12],
            "motorista_ul_id": row[13],
            "veiculo": row[14],
            "veiculo_data_label": row[15],
            "veiculo_input_id": row[16],
            "veiculo_ul_id": row[17],
            "reboque": row[18],
            "reboque_input_id": row[19],
            "deposito": row[20],
            "deposito_input_id": row[21],
            "deposito_data_label": row[22],
            "deposito_ul_id": row[23],
            "depositante_copy_id": row[24],
            "btn_salvar_id": row[25]
        })
    result_dict = {
        "url": routine_dict['url'],
        "login": login,
        "romaneio": romaneio,
        "operacao": routine_dict['operacao']
    }
    return result_dict


def query_romaneio_data_op_405(routine_dict: dict, cursor: sqlite3.Cursor, conn: sqlite3.Connection, login: dict) -> dict:
    cursor.execute("""
        SELECT motorista, motorista_data_label, motorista_input_id, motorista_ul_id,
                veiculo, veiculo_data_label, veiculo_input_id, veiculo_ul_id, reboque, reboque_input_id,
                btn_salvar_id, nr_ordem_venda, ordem_venda_input_id, btn_incluir_ordem_venda, 
                transportadora, transportadora_data_label, transportadora_input_id, transportadora_ul_id, btn_incluir_item_nf_pedido
    FROM romaneio_data
    WHERE id = ?
    ORDER BY id ASC
    """, (routine_dict['romaneio_data_id'],))
    romaneio_rows = cursor.fetchall()
    romaneio = []
    for row in romaneio_rows:
        romaneio.append({
            "motorista": row[0],
            "motorista_data_label": row[1],
            "motorista_input_id": row[2],
            "motorista_ul_id": row[3],
            "veiculo": row[4],
            "veiculo_data_label": row[5],
            "veiculo_input_id": row[6],
            "veiculo_ul_id": row[7],
            "reboque": row[8],
            "reboque_input_id": row[9],
            "btn_salvar_id": row[10],
            "nr_ordem_venda": row[11],
            "ordem_venda_input_id": row[12],
            "btn_incluir_ordem_venda": row[13],
            "transportadora": row[14],
            "transportadora_data_label": row[15],
            "transportadora_input_id": row[16],
            "transportadora_ul_id": row[17],
            "btn_incluir_item_nf_pedido": row[18]
        })
    
    result_dict = {
        "url": routine_dict['url'],
        "login": login,
        "romaneio": romaneio,
        "operacao": routine_dict['operacao']
    }
    return result_dict

def query_romaneio_data_op_302(routine_dict: dict, cursor: sqlite3.Cursor, conn: sqlite3.Connection, login: dict) -> dict:
    cursor.execute("""
        SELECT motorista, motorista_data_label, motorista_input_id, motorista_ul_id,
                veiculo, veiculo_data_label, veiculo_input_id, veiculo_ul_id, reboque, reboque_input_id,
                btn_salvar_id, nr_nota_fiscal, nota_fiscal_input_id, nr_pedido, pedido_input_id
                transportadora, transportadora_data_label, transportadora_input_id, transportadora_ul_id, btn_incluir_item_nf_pedido
    FROM romaneio_data
    WHERE id = ?
    ORDER BY id ASC
    """, (routine_dict['romaneio_data_id'],))
    romaneio_rows = cursor.fetchall()
    romaneio = []
    for row in romaneio_rows:
        romaneio.append({
            "motorista": row[0],
            "motorista_data_label": row[1],
            "motorista_input_id": row[2],
            "motorista_ul_id": row[3],
            "veiculo": row[4],
            "veiculo_data_label": row[5],
            "veiculo_input_id": row[6],
            "veiculo_ul_id": row[7],
            "reboque": row[8],
            "reboque_input_id": row[9],
            "btn_salvar_id": row[10],
            "nr_nota_fiscal": row[11],
            "nota_fiscal_input_id": row[12],
            "nr_pedido": row[13],
            "pedido_input_id": row[14],
            "transportadora": row[15],
            "transportadora_data_label": row[16],
            "transportadora_input_id": row[17],
            "transportadora_ul_id": row[18],
            "btn_incluir_item_nf_pedido": row[19],
            "transportadora": row[14],
            "transportadora_data_label": row[15],
            "transportadora_input_id": row[16],
            "transportadora_ul_id": row[17],
            "btn_incluir_item_nf_pedido": row[18]
        })
    
    result_dict = {
        "url": routine_dict['url'],
        "login": login,
        "romaneio": romaneio,
        "operacao": routine_dict['operacao']
    }
    return result_dict


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
        romaneio_data = query_romaneio_data([romaneio_data_id])
        if playwright_routine_user_id not in checker:
            checker.add(playwright_routine_user_id)
            unique_users.append(playwright_routine_user_id)
            routine_romaneio_data.append({
                "playwright_routine_user_id": playwright_routine_user_id,
                "romaneio_data": romaneio_data,
                "playwright_routine_user": playwright_routine_user
            })
        else:
            idx = next((i for i, d in enumerate(routine_romaneio_data) if d["playwright_routine_user_id"] == playwright_routine_user_id), None)
            
            routine_romaneio_data[idx]['romaneio_data'].append(romaneio_data)

    return routine_romaneio_data

def query_romaneio_data(romaneio_data_ids: list[int]) -> dict:
    conn = sqlite3.connect('./db/stress_db')
    cursor = conn.cursor()
    query = """
        SELECT * FROM romaneio_data WHERE id IN ({placeholders})
    """
    placeholders = ','.join(['?'] * len(romaneio_data_ids))
    cursor.execute(query.format(placeholders=placeholders), romaneio_data_ids)
    romaneio_data_rows = cursor.fetchall()
    romaneio_data = []
    for row in romaneio_data_rows:
        romaneio_data.append(row)
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
        playwright_routine_user.append({
            "url": row[0],
            "login_id": row[1],
            "operacao": row[2]
        })
    return playwright_routine_user

print(load_data_from_db_by_user([1, 2]))