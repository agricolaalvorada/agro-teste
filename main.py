from playwright.sync_api import sync_playwright
from utils.page_utils import *
from routines.starter_routines import start_new_romaneio, login_to_site
from routines.operacao_700.preencher_romaneio import criar_romaneio as criar_romaneio_700
from routines.operacao_405.preencher_romaneio import criar_romaneio as criar_romaneio_405
import time
import threading
import argparse
from db.load_data import load_json_from_db
import random

def main(data, romaneio):
    with sync_playwright() as p:
        time.sleep(random.uniform(0, 10))
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        login_to_site(data[0]['url'], data[0]['login']['username'], data[0]['login']['password'], data[0]['login']['username_id'], data[0]['login']['password_id'], page)
        start_new_romaneio(data[0]['url'], data[0]['login']['username'], data[0]['login']['password'], data[0]['login']['username_id'], data[0]['login']['password_id'], page, data[0]['operacao'])
        if data[0]['operacao'] == '700 - Entrada Spot':
            criar_romaneio_700(page, romaneio['romaneio'][0])
        elif data[0]['operacao'] == '001 - VENDAS':
            criar_romaneio_405(page, romaneio['romaneio'][0])
        else:
            raise ValueError(f"Operação {data[0]['operacao']} não suportada")
        browser.close()

def run_test():
    threads = []
    data = load_json_from_db([3]) #4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28
    for romaneio in data:
        thread = threading.Thread(
            target=main,
            args=(data, romaneio)
        )
        threads.append(thread)
        thread.start()    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    run_test()