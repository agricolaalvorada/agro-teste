
from utils.page_utils import *
from playwright.sync_api import Page
import time
from db.save_telemetry import save_telemetry

def pesagem_romaneio(page: Page):
    start_time = time.time()
    print('Pesando romaneio')
    page.click(f'a[href="#abaPesagem"]')
    wait_for_page_load(page)
    fill_input_by_id('j_idt26875', '100', page)
    set_transgenia(page)
    end_time = time.time()
    print(f"Duração pesagem_romaneio: {end_time - start_time:.2f} seconds")

def set_transgenia(page: Page):
    start_time = time.time()
    print('Preenchendo transgenia')
    click_element_by_id(romaneio['transgenia_pesagem'], page)
    simulate_key_press(page, 'ArrowDown')
    simulate_key_press(page, 'Enter')
    select_and_click_li_from_ul('transgenia_pesagem_items', '01 - Intacta', page)
    click_element_by_id('j_idt27349', page)
    end_time = time.time()
    print(f"Duração set_transgenia: {end_time - start_time:.2f} seconds")