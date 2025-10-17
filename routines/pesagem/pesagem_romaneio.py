
from utils.page_utils import *
from playwright.sync_api import Page
import time
from db.save_telemetry import save_telemetry

def pesagem_romaneio(page: Page):
    start_time = time.time()
    print('Pesando romaneio')
    page.click(f'a[href="#abaPesagem"]')
    wait_for_page_load(page)
    fill_input_by_id('j_idt26875', '101', page)
    click_element_by_id('transgenia_pesagem', page)
    click_element_by_id('transgenia_pesagem_1', page)
    input('Pressione Enter para continuar')
    fill_input_by_id('txtPesoFinal', '1', page)
    page.locator('#j_idt26875').evaluate("el => el.blur()")
    locator = page.locator("#j_idt26886")
    page.wait_for_function(
        "selector => document.querySelector(selector)?.value === '100'",
        arg="#j_idt26886"
    )
    click_element_by_id('j_idt27349', page) # salvar
    page.wait_for_selector('.ui-growl-item', state='visible')
    # set_transgenia(page)
    end_time = time.time()
    print(f"Duração pesagem_romaneio: {end_time - start_time:.2f} seconds")

# def pesagem_completa_romaneio(page: Page):
#     start_time = time.time()
#     print('Pesando romaneio completo')
#     page.click(f'a[href="#abaPesagem"]')
#     wait_for_page_load(page)
# 
#     page.locator('#j_idt26875').evaluate("el => el.value = '101'")
#     page.locator('#txtPesoFinal').evaluate("el => el.value = '1'")
#     wait_for_page_load(page)
#     end_time = time.time()
#     click_element_by_id('j_idt27349', page) # salvar
#     page.wait_for_selector('.ui-growl-item', state='visible')
#     print(f"Duração pesagem_completa_romaneio: {end_time - start_time:.2f} seconds")