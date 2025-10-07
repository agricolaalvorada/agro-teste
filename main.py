from playwright.sync_api import sync_playwright
from utils.page_utils import *
from routines.starter_routines import start_new_romaneio, login_to_site
from routines.operacao_700.preencher_romaneio import criar_romaneio as criar_romaneio_700
from routines.operacao_405.preencher_romaneio import criar_romaneio as criar_romaneio_405
import time
import threading
import argparse
from db.load_data import load_data_from_db_by_user
import random


def main(routine_romaneio_data: dict):
    with sync_playwright() as p:
        time.sleep(random.uniform(0, 10))
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        login_to_site(routine_romaneio_data['playwright_routine_user']['url'], routine_romaneio_data['playwright_routine_user']['login']['username'], routine_romaneio_data['playwright_routine_user']['login']['password'], routine_romaneio_data['playwright_routine_user']['login']['username_id'], routine_romaneio_data['playwright_routine_user']['login']['password_id'], page)
        for romaneio_data in routine_romaneio_data['romaneio_data']:
            start_new_romaneio(routine_romaneio_data['playwright_routine_user']['url'], routine_romaneio_data['playwright_routine_user']['login']['username'], routine_romaneio_data['playwright_routine_user']['login']['password'], routine_romaneio_data['playwright_routine_user']['login']['username_id'], routine_romaneio_data['playwright_routine_user']['login']['password_id'], page, routine_romaneio_data['playwright_routine_user']['operacao'])
            if routine_romaneio_data['playwright_routine_user']['operacao'] == '700 - Entrada Spot':
                criar_romaneio_700(page, romaneio_data['romaneio'][0])
            elif routine_romaneio_data['playwright_routine_user']['operacao'] == '001 - VENDAS':
                criar_romaneio_405(page, romaneio_data['romaneio'][0])
            else:
                raise ValueError(f"Operação {routine_romaneio_data['playwright_routine_user']['operacao']} não suportada")
        browser.close()

def run_test():
    threads = []
    data = load_data_from_db_by_user([1,2])
    for routine_romaneio_data in data:
        thread = threading.Thread(
            target=main,
            args=(routine_romaneio_data,)

        )
        threads.append(thread)
        thread.start()    
    for thread in threads:
        thread.join()
        input('Pressione enter para confirmar o fim do teste')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    run_test()