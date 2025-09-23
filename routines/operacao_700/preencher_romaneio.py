from utils.page_utils import *
from playwright.sync_api import Page
import time



def criar_romaneio(page: Page, romaneio: dict):
    start_time = time.time()
    set_safra(page, romaneio)
    wait_for_page_load(page)
    set_parceiro(page, romaneio)
    set_material(page, romaneio)
    set_motorista(page, romaneio)
    set_veiculo(page, romaneio)
    set_deposito(page, romaneio)
    wait_for_page_load(page)
    wait_for_element_by_id(romaneio['depositante_copy_id'], page) # copiar deposittante
    click_element_by_id(romaneio['depositante_copy_id'], page) # copiar deposittante
    wait_for_page_load(page)
    wait_for_page_load(page)
    click_element_by_id(romaneio['btn_salvar_id'], page)  # salvar
    input(f'debug pos salvar')
    end_time = time.time()
    print(f"Duração criar_romaneio: {end_time - start_time:.2f} seconds")


def set_parceiro(page: Page, romaneio: dict):
    start_time = time.time()
    print('Preenchendo parceiro')
    fill_input_by_id(romaneio['parceiro_input_id'], str(romaneio['parceiro']), page)
    simulate_key_press(page, 'Space')
    wait_for_element_by_id(romaneio['parceiro_ul_id'], page)
    click_first_row_by_table_label(romaneio['parceiro_data_label'], page)
    page.wait_for_selector('div.ui-dialog[widgetvar="statusDialog"]', state='hidden')
    end_time = time.time()
    print(f"Duração set_parceiro: {end_time - start_time:.2f} seconds")

def set_safra(page: Page, romaneio: dict):
    start_time = time.time()
    print('Preenchendo safra')
    print(f"romaneio: {romaneio}")
    print(f"safra_input_id: {romaneio['safra_input_id']}")
    print(f"safra_data_label: {romaneio['safra_data_label']}")
    input(f"debug")
    type_input_by_id(romaneio['safra_input_id'], str(romaneio['safra']), page)
    click_first_row_by_table_label(romaneio['safra_data_label'], page)
    end_time = time.time()
    print(f"Duração set_safra: {end_time - start_time:.2f} seconds")


def set_material(page: Page, romaneio: dict):
    start_time = time.time()
    print('Preenchendo material')
    click_element_by_id(romaneio['material'], page)
    select_and_click_li_from_ul(romaneio['material_ul_id'], romaneio['material_data_label'], page)
    simulate_key_press(page, 'Enter')
    end_time = time.time()
    print(f"Duração set_material: {end_time - start_time:.2f} seconds")

def set_motorista(page: Page, romaneio: dict):
    start_time = time.time()
    print('Preenchendo motorista')
    fill_input_by_id(romaneio['motorista_input_id'], str(romaneio['motorista']), page)
    simulate_key_press(page, 'Space')
    wait_for_element_by_id(romaneio['motorista_ul_id'], page)
    click_first_row_by_table_label(romaneio['motorista_data_label'], page)
    page.wait_for_selector('div.ui-dialog[widgetvar="statusDialog"]', state='hidden')
    end_time = time.time()
    print(f"Duração set_motorista: {end_time - start_time:.2f} seconds")

def set_veiculo(page: Page, romaneio: dict):
    start_time = time.time()
    print('Preenchendo veiculo')
    fill_input_by_id(romaneio['veiculo_input_id'], str(romaneio['veiculo']), page)
    simulate_key_press(page, 'Space')
    wait_for_element_by_id(romaneio['veiculo_ul_id'], page)
    click_first_row_by_table_label(romaneio['veiculo_data_label'], page)
    page.wait_for_selector('div.ui-dialog[widgetvar="statusDialog"]', state='hidden')
    wait_for_input_value(romaneio['reboque_input_id'], romaneio['reboque'], page)
    end_time = time.time()
    print(f"Duração set_veiculo: {end_time - start_time:.2f} seconds")


def wait_for_input_value(element_id: str, expected_value: str, page: Page, timeout: int = 5000):
    start_time = time.time()
    while time.time() - start_time < timeout:
        actual_value = page.input_value(f'#{element_id}')
        if actual_value == expected_value:
            return
        time.sleep(0.1)
    raise TimeoutError(f"Input {element_id} did not get value {expected_value} within {timeout}ms")

def set_deposito(page: Page, romaneio: dict):
    start_time = time.time()
    print('Preenchendo deposito')
    click_element_by_id(romaneio['deposito_input_id'], page)
    simulate_key_press(page, 'ArrowDown')
    simulate_key_press(page, 'Enter')
    select_and_click_li_from_ul(romaneio['deposito_ul_id'], romaneio['deposito_data_label'], page)
    end_time = time.time()
    print(f"Duração set_deposito: {end_time - start_time:.2f} seconds")
