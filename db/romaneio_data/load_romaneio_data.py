import sqlite3

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


def query_romaneio_data_op_700_by_id(romaneio_data_id: int) -> dict:
    conn = sqlite3.connect('./db/stress_db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT safra, safra_data_label, safra_input_id, parceiro, parceiro_data_label, parceiro_input_id, parceiro_ul_id,
                material, material_data_label, material_ul_id, motorista, motorista_data_label, motorista_input_id, motorista_ul_id,
                veiculo, veiculo_data_label, veiculo_input_id, veiculo_ul_id, reboque, reboque_input_id,
                deposito, deposito_input_id, deposito_data_label, deposito_ul_id, depositante_copy_id, btn_salvar_id
    FROM romaneio_data
    WHERE id = ?
    ORDER BY id ASC
    """, (romaneio_data_id,))
    romaneio_rows = cursor.fetchall()
    romaneio = {}
    for row in romaneio_rows:
        safra, safra_data_label, safra_input_id, parceiro, parceiro_data_label, parceiro_input_id, parceiro_ul_id,material, material_data_label, material_ul_id, motorista, motorista_data_label, motorista_input_id, motorista_ul_id,veiculo, veiculo_data_label, veiculo_input_id, veiculo_ul_id, reboque, reboque_input_id,deposito, deposito_input_id, deposito_data_label, deposito_ul_id, depositante_copy_id, btn_salvar_id = row
        romaneio = {
            "safra": safra,
            "safra_data_label": safra_data_label,
            "safra_input_id": safra_input_id,
            "parceiro": parceiro,
            "parceiro_data_label": parceiro_data_label,
            "parceiro_input_id": parceiro_input_id,
            "parceiro_ul_id": parceiro_ul_id,
            "material": material,
            "material_data_label": material_data_label,
            "material_ul_id": material_ul_id,
            "motorista": motorista,
            "motorista_data_label": motorista_data_label,
            "motorista_input_id": motorista_input_id,
            "motorista_ul_id": motorista_ul_id,
            "veiculo": veiculo,
            "veiculo_data_label": veiculo_data_label,
            "veiculo_input_id": veiculo_input_id,
            "veiculo_ul_id": veiculo_ul_id,
            "reboque": reboque,
            "reboque_input_id": reboque_input_id,
            "deposito": deposito,
            "deposito_input_id": deposito_input_id,
            "deposito_data_label": deposito_data_label,
            "deposito_ul_id": deposito_ul_id,
            "depositante_copy_id": depositante_copy_id,
            "btn_salvar_id": btn_salvar_id
        }
    return romaneio


def query_romaneio_data_op_405_by_id(romaneio_data_id: int) -> dict:
    conn = sqlite3.connect('./db/stress_db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT motorista, motorista_data_label, motorista_input_id, motorista_ul_id,
                veiculo, veiculo_data_label, veiculo_input_id, veiculo_ul_id, reboque, reboque_input_id,
                btn_salvar_id, nr_ordem_venda, ordem_venda_input_id, btn_incluir_ordem_venda, 
                transportadora, transportadora_data_label, transportadora_input_id, transportadora_ul_id, btn_incluir_item_nf_pedido
    FROM romaneio_data
    WHERE id = ?
    ORDER BY id ASC
    """, (romaneio_data_id,))
    romaneio_rows = cursor.fetchall()
    romaneio = {}
    for row in romaneio_rows:
        romaneio = {
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
        }
    
    return romaneio

def query_romaneio_data_op_302_by_id(romaneio_data_id: int) -> dict:
    conn = sqlite3.connect('./db/stress_db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT motorista, motorista_data_label, motorista_input_id, motorista_ul_id,
                veiculo, veiculo_data_label, veiculo_input_id, veiculo_ul_id, reboque, reboque_input_id,
                btn_salvar_id, nr_nota_fiscal, nota_fiscal_input_id, nr_pedido, pedido_input_id
                transportadora, transportadora_data_label, transportadora_input_id, transportadora_ul_id, btn_incluir_item_nf_pedido
    FROM romaneio_data
    WHERE id = ?
    ORDER BY id ASC
    """, (romaneio_data_id,))
    romaneio_rows = cursor.fetchall()
    romaneio = {}
    for row in romaneio_rows:
        romaneio = {
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
        }
    
    return romaneio