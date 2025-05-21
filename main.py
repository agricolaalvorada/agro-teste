from playwright.sync_api import sync_playwright
from utils.page_utils import *
from routines.starter_routines import start_new_romaneio
from routines.operacao_700.preencher_romaneio import criar_romaneio
import time
import threading

def main(url, username, password, username_id, password_id):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=['--start-maximized'])
        page = browser.new_page()
        start_new_romaneio(url, username, password, username_id, password_id, page, '700 - Entrada Spot')
        criar_romaneio(page)
        print('Teste finalizado')
        browser.close()

def run_test(num_threads: int):
    threads = []
    for i in range(num_threads):
        thread = threading.Thread(
            target=main,
            args=('http://10.1.1.28:1015/itss-agro/', 'cciliato', 'Alvorada@1234', 'username', 'password')
        )
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    #main('http://10.1.1.28:1015/itss-agro/', 'cciliato', 'Alvorada@1234', 'username', 'password')
    run_test(3)