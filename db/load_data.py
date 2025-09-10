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
    

def load_json_from_db(login_id: int, routine_ids: list[int]) -> dict:
    
    conn = sqlite3.connect('./db/stress_db')  
    cursor = conn.cursor()
    data = []
    try:
        placeholders = ','.join(['?'] * len(routine_ids))
        query = f"SELECT id, url, romaneio_data_id, operacao FROM playwright_routine WHERE id IN ({placeholders})"
        cursor.execute(query, routine_ids)
        routine_rows = cursor.fetchall()
        routine_dict = []
        for row in routine_rows:
            id, url, romaneio_data_id, operacao = row
            routine_dict.append({
                "id": id,
                "url": url,
                "romaneio_data_id": romaneio_data_id,
                "operacao": operacao
            })

        cursor.execute("SELECT username, password, username_id, password_id FROM auth_credentials WHERE id in (?)", (login_id,))
        login_rows = cursor.fetchone()
        login = {
                "username": login_rows[0],
                "password": login_rows[1],
                "username_id": login_rows[2],
                "password_id": login_rows[3]
            }
        for routine in routine_dict:

            if routine['operacao'] == '700 - Entrada Spot': 
                data.append(query_romaneio_data_op_700(routine, cursor, conn, login))
            elif routine['operacao'] == '001 - VENDAS':
                data.append(query_romaneio_data_op_405(routine, cursor, conn, login))
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
        "romaneio": romaneio
    }

    return result_dict


def query_romaneio_data_op_405(routine_dict: dict, cursor: sqlite3.Cursor, conn: sqlite3.Connection, login: dict) -> dict:
    cursor.execute("""
        SELECT motorista, motorista_data_label, motorista_input_id, motorista_ul_id,
                veiculo, veiculo_data_label, veiculo_input_id, veiculo_ul_id, reboque, reboque_input_id,
                btn_salvar_id, nr_ordem_venda, ordem_venda_input_id, btn_incluir_ordem_venda,
                transportadora, transportadora_data_label, transportadora_input_id, transportadora_ul_id
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
            "transportadora_ul_id": row[17]
        })
    
    result_dict = {
        "url": routine_dict['url'],
        "login": login,
        "romaneio": romaneio
    }
    return result_dict



print(load_json_from_db(1, [1,2]))