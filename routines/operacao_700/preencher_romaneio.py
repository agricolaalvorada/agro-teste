from utils.page_utils import *
from playwright.sync_api import Page
import time



def criar_romaneio(page: Page):
        set_safra(page, '2025', '24/25-SAFRA')
        wait_for_page_load(page)
        set_parceiro(page, '3000011')
        set_material(page, 'material_700', '100000 - SOJA EM GRAOS')
        set_motorista(page, '3002222', '3002222 - RONI LUCAS CICHELERO')
        set_veiculo(page, 'LEO0722', 'LEO0722', 'LEO0723')
        set_deposito(page, 'deposito_700', '01 - GrãoTransgênico', 'deposito_700_items')
        wait_for_page_load(page)
        wait_for_element_by_id('j_idt3199', page) # copiar deposittante
        click_element_by_id('j_idt3199', page) # copiar deposittante
        wait_for_page_load(page)
        click_element_by_id('j_idt26494', page)  # salvar


def set_parceiro(page: Page, cod_parceiro: str):
    print('Preenchendo parceiro')
    fill_input_by_id('j_idt3091_input', cod_parceiro, page)
    simulate_key_press(page, 'Space')
    wait_for_element_by_id('j_idt3091_panel', page)
    click_first_row_by_table_label('3000011 - TIAGO BOTTON', page)
    page.wait_for_selector('div.ui-dialog[widgetvar="statusDialog"]', state='hidden')

def set_safra(page: Page, cod_safra: str, data_label: str):
    print('Preenchendo safra')
    type_input_by_id('safra_700_input', cod_safra, page)
    click_first_row_by_table_label(data_label, page)


def set_material(page: Page, cod_material: str, data_label: str):
    print('Preenchendo material')
    click_element_by_id(cod_material, page)
    select_and_click_li_from_ul(cod_material + '_items', data_label, page)
    simulate_key_press(page, 'Enter')

def set_motorista(page: Page, cod_motorista: str, data_label: str):
    print('Preenchendo motorista')
    fill_input_by_id('motorista_700_input', cod_motorista, page)
    simulate_key_press(page, 'Space')
    wait_for_element_by_id('motorista_700_panel', page)
    click_first_row_by_table_label(data_label, page)
    page.wait_for_selector('div.ui-dialog[widgetvar="statusDialog"]', state='hidden')

def set_veiculo(page: Page, cod_veiculo: str, data_label: str, reboque: str):
    print('Preenchendo veiculo')
    fill_input_by_id('campoPlacaCavalo_700_input', cod_veiculo, page)
    simulate_key_press(page, 'Space')
    wait_for_element_by_id('campoPlacaCavalo_700_panel', page)
    click_first_row_by_table_label(data_label, page)
    page.wait_for_selector('div.ui-dialog[widgetvar="statusDialog"]', state='hidden')
    wait_for_input_value('campoPlacaUm700_input', reboque, page)


def wait_for_input_value(element_id: str, expected_value: str, page: Page, timeout: int = 5000):
    start_time = time.time()
    while time.time() - start_time < timeout:
        actual_value = page.input_value(f'#{element_id}')
        if actual_value == expected_value:
            return
        time.sleep(0.1)
    raise TimeoutError(f"Input {element_id} did not get value {expected_value} within {timeout}ms")

def set_deposito(page: Page, cod_deposito: str, data_label: str, ul_id: str):
    print('Preenchendo deposito')
    click_element_by_id(cod_deposito, page)
    simulate_key_press(page, 'ArrowDown')
    simulate_key_press(page, 'Enter')
    select_and_click_li_from_ul(ul_id, data_label, page)
