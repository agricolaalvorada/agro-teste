from utils.page_utils import *
from playwright.sync_api import Page
import time



def criar_romaneio(page: Page, romaneio: dict):

        set_nota_fiscal(page, romaneio)
        wait_for_page_load(page)
        set_pedido(page, romaneio)
        wait_for_page_load(page)
        set_motorista(page, romaneio)
        set_veiculo(page, romaneio)
        set_transportadora(page, romaneio)
        wait_for_page_load(page)
        wait_for_element_by_id(romaneio['depositante_copy_id'], page) # copiar deposittante
        click_element_by_id(romaneio['depositante_copy_id'], page) # copiar deposittante
        click_element_by_id(romaneio['btn_incluir_item_nf_pedido'], page)
        wait_for_page_load(page)
        click_element_by_id(romaneio['btn_salvar_id'], page)  # salvar
        wait_for_page_load(page)


def set_nota_fiscal(page: Page, romaneio: dict):
    print('Preenchendo nota fiscal')
    print(f'{romaneio["nr_nota_fiscal"]} {romaneio["nota_fiscal_input_id"]}')
    fill_input_by_id(romaneio['nota_fiscal_input_id'], str(romaneio['nr_nota_fiscal']), page)
    wait_for_page_load(page)


def set_pedido(page: Page, romaneio: dict):
    print('Preenchendo pedido')
    print(f'{romaneio["nr_pedido"]} {romaneio["pedido_input_id"]}')
    fill_input_by_id(romaneio['pedido_input_id'], str(romaneio['nr_pedido']), page)
    wait_for_page_load(page)


def set_transportadora (page: Page, romaneio: dict):
    print('Preenchendo transportadora')
    fill_input_by_id(romaneio['transportadora_input_id'], str(romaneio['transportadora']), page)
    simulate_key_press(page, 'Space')
    wait_for_element_by_id(romaneio['transportadora_ul_id'], page)
    click_first_row_by_table_label(romaneio['transportadora_data_label'], page)
    page.wait_for_selector('div.ui-dialog[widgetvar="statusDialog"]', state='hidden')


def set_motorista(page: Page, romaneio: dict):
    print('Preenchendo motorista')
    fill_input_by_id(romaneio['motorista_input_id'], str(romaneio['motorista']), page)
    simulate_key_press(page, 'Space')
    wait_for_element_by_id(romaneio['motorista_ul_id'], page)
    click_first_row_by_table_label(romaneio['motorista_data_label'], page)
    page.wait_for_selector('div.ui-dialog[widgetvar="statusDialog"]', state='hidden')

def set_veiculo(page: Page, romaneio: dict):
    print('Preenchendo veiculo')
    fill_input_by_id(romaneio['veiculo_input_id'], str(romaneio['veiculo']), page)
    simulate_key_press(page, 'Space')
    wait_for_element_by_id(romaneio['veiculo_ul_id'], page)
    click_first_row_by_table_label(romaneio['veiculo_data_label'], page)
    page.wait_for_selector('div.ui-dialog[widgetvar="statusDialog"]', state='hidden')
    wait_for_input_value(romaneio['reboque_input_id'], romaneio['reboque'], page)


def wait_for_input_value(element_id: str, expected_value: str, page: Page, timeout: int = 5000):
    start_time = time.time()
    while time.time() - start_time < timeout:
        actual_value = page.input_value(f'#{element_id}')
        if actual_value == expected_value:
            return
        time.sleep(0.1)
    raise TimeoutError(f"Input {element_id} did not get value {expected_value} within {timeout}ms")
