from playwright.sync_api import sync_playwright
from utils.page_utils import *
from routines.starter_routines import start_new_romaneio, login_to_site
from routines.operacao_700.preencher_romaneio import criar_romaneio as criar_romaneio_700
import time
import threading
import argparse
from db.load_data import load_json_from_db

def main(data, romaneio):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        login_to_site(data[0]['url'], data[0]['login']['username'], data[0]['login']['password'], data[0]['login']['username_id'], data[0]['login']['password_id'], page)
        
        start_new_romaneio(data[0]['url'], data[0]['login']['username'], data[0]['login']['password'], data[0]['login']['username_id'], data[0]['login']['password_id'], page, romaneio['operacao'])
        match (romaneio['operacao']):
            case '700 - Entrada Spot':
                criar_romaneio_700(page, romaneio)
            case _:
                raise ValueError(f"Operação {romaneio['operacao']} não suportada")
        browser.close()

def run_test(num_threads: int):
    threads = []
    data = load_json_from_db(1, [1, 2, 3])
    for romaneio in data[0]['romaneio']:
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
    parser.add_argument('--threads', type=int, default=3, help='Number of threads to run')
    args = parser.parse_args()
    run_test(args.threads)