from playwright.sync_api import sync_playwright
from utils.page_utils import *
from routines.starter_routines import start_new_romaneio, login_to_site
from routines.operacao_700.preencher_romaneio import criar_romaneio
import time
import threading
import argparse

def main(url, username, password, username_id, password_id):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        login_to_site(url, username, password, username_id, password_id, page)
        start_new_romaneio(url, username, password, username_id, password_id, page, '700 - Entrada Spot')
        criar_romaneio(page) 
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
    parser = argparse.ArgumentParser()
    parser.add_argument('--threads', type=int, default=3, help='Number of threads to run')
    args = parser.parse_args()
    run_test(args.threads)