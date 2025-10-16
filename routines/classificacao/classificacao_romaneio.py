from utils.page_utils import *
from playwright.sync_api import Page
import time
from db.save_telemetry import save_telemetry

def classificacao_romaneio(page: Page):
    start_time = time.time()
    print('Classificando romaneio')
    click_element_by_xpath('//a[@href="#abaClassificacao"]', page)
    wait_for_page_load(page)
    page.screenshot(path="debug_initial_classificacao.png")
    page.wait_for_selector("#origemClass", state="visible", timeout=10000)
    set_classificacao(page)
    end_time = time.time()
    print(f"Duração classificacao_romaneio: {end_time - start_time:.2f} seconds")

def set_classificacao(page: Page):
    start_time = time.time()
    print('Preenchendo classificacao')
    page.screenshot(path="debug_before_classificacao.png")
    page.wait_for_selector('//input[@id="dtTableIdClass:0:indiceOutros"]', state="visible")
    page.screenshot(path="debug_after_render_classificacao.png")
    fill_classificacao_indice_outros(page, [14.5, 0.5, 3, 4.5, 1.5, 1, 1, 1])

    # dtTableIdClass:11:indiceComboBox
    xpath = '//div[@id="dtTableIdClass:11:indiceComboBox"]'
    click_element_by_xpath(xpath, page)
    select_and_click_li_from_ul('//div[@id="dtTableIdClass:11:indiceComboBox_items"]', '0 a 3 Sementes', page)
    end_time = time.time()
    print(f"Duração set_classificacao: {end_time - start_time:.2f} seconds")

def fill_classificacao_indice_outros(page: Page, values):
    inputs = page.locator('tbody#dtTableIdClass_data input[id$=":indiceOutros"]:not([disabled])')
    count = inputs.count()
    if len(values) != count:
        raise ValueError(f"Length of values ({len(values)}) does not match number of enabled fields ({count})")
    for i in range(count):
        inputs.nth(i).fill(str(values[i]))
        inputs.nth(i).evaluate("el => el.blur()")