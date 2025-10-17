from utils.page_utils import *
from playwright.sync_api import Page
import time
from db.save_telemetry import save_telemetry

def classificacao_romaneio(page: Page):
    start_time = time.time()
    print('Classificando romaneio')
    click_element_by_xpath('//a[@href="#abaClassificacao"]', page)
    wait_for_page_load(page)
    page.wait_for_selector("#origemClass", state="visible", timeout=10000)
    set_classificacao(page)
    end_time = time.time()
    save_telemetry('classificacao', '', '', int((end_time - start_time) * 1000))
    print(f"Duração classificacao_romaneio: {end_time - start_time:.2f} seconds")

def set_classificacao(page: Page):
    start_time = time.time()
    print('Preenchendo classificacao')
    page.wait_for_selector('//input[@id="dtTableIdClass:0:indiceOutros"]', state="visible")
    fill_classificacao_indice_outros(page)
    xpath = '//div[@id="dtTableIdClass:11:indiceComboBox"]'
    click_element_by_xpath(xpath, page)
    click_element_by_xpath('//li[@id="dtTableIdClass:11:indiceComboBox_1"]', page)
    page.wait_for_function(
        "selector => document.querySelector(selector)?.value === '0'",
        arg='#dtTableIdClass\\:11\\:desconto'
    )
    wait_for_page_load(page)
    click_element_by_id('transgenia_classificacao', page)
    click_element_by_id('transgenia_classificacao_1', page)
    wait_for_page_load(page)
    
    click_element_by_id('j_idt27349', page) # salvar
    wait_for_page_load(page)
    page.wait_for_selector('div#modalPersisteClassificacaoDesconto', state='visible')
    page.get_by_role("button", name="Sim").click()
    wait_for_page_load(page)
    page.wait_for_selector('.ui-growl-item', state='visible')
    end_time = time.time()
    print(f"Duração set_classificacao: {end_time - start_time:.2f} seconds")

def fill_classificacao_indice_outros(page: Page):
    indexes = [0, 1, 2, 3, 5, 6, 9, 10]
    for index in indexes:
        current_value = page.locator(f'//input[@id="dtTableIdClass:{index}:indiceOutros"]').input_value()
        if current_value in ("", "0", "0.0", "0,0"):
            fill_input_by_xpath(f'//input[@id="dtTableIdClass:{index}:indiceOutros"]', '1,5', page)
#    input('PRESS ENTER')
#    page.wait_for_function(
#    "selector => document.querySelector(selector)?.value === '0'",
#    arg='#dtTableIdClass\\:0\\:desconto'
#    )
