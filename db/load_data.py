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
        query = f"SELECT id, url, romaneio_data_id FROM playwright_routine WHERE id IN ({placeholders})"
        cursor.execute(query, routine_ids)
        routine_rows = cursor.fetchall()
        routine_dict = []
        for row in routine_rows:
            id, url, romaneio_data_id = row
            routine_dict.append({
                "id": id,
                "url": url,
                "romaneio_data_id": romaneio_data_id
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
            cursor.execute("""
                SELECT safra, safra_data_label, safra_input_id, parceiro, parceiro_data_label, parceiro_input_id, parceiro_ul_id,
                       material, material_data_label, material_ul_id, motorista, motorista_data_label, motorista_input_id, motorista_ul_id,
                       veiculo, veiculo_data_label, veiculo_input_id, veiculo_ul_id, reboque, reboque_input_id,
                       deposito, deposito_input_id, deposito_data_label, deposito_ul_id, depositante_copy_id, btn_salvar_id, operacao
            FROM romaneio_data
            WHERE id = ?
            ORDER BY id ASC
        """, (routine['romaneio_data_id'],))
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
                    "btn_salvar_id": row[25],
                    "operacao": row[26]
                })
            
            result_dict = {
                "url": routine['url'],
                "login": login,
                "romaneio": romaneio
            }
            data.append(result_dict)
        
        return data
        
    finally:
        cursor.close()
        conn.close()

print(load_json_from_db(1, [1]))