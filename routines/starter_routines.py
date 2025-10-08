from utils.page_utils import navigate_to_page, fill_login_fields, click_element_by_id, select_and_click_li_from_ul, wait_for_page_load
from playwright.sync_api import Page
import time

def start_new_romaneio(url: str, username: str, password: str, username_id: str, password_id: str, page: Page, operacao: str):        
        romaneio_start = time.time()
        navigate_to_page(f'{url}paginas/romaneio/inicial.jsf', page)
        wait_for_page_load(page)
        romaneio_end = time.time()
        print(f"Carregar pagina romaneio: {romaneio_end - romaneio_start:.2f} seconds")
        click_element_by_id('tipo', page)
        select_and_click_li_from_ul('tipo_items', operacao, page)
        
        button_start = time.time()
        click_element_by_id('btnCadastrar', page)
        wait_for_page_load(page)
        button_end = time.time()
        print(f"Abrir Tela de Operação: {button_end - button_start:.2f} seconds")
        
        end_time = time.time()
        
        print(f"Tempo Total: {romaneio_end - romaneio_start:.2f} seconds")
        
        

def login_to_site(url: str, username: str, password: str, username_id: str, password_id: str, page: Page):
                
        start_time = time.time()
        nav_start = time.time()

        navigate_to_page(url, page)
        nav_end = time.time()

        print(f"Carregando a tela de login: {nav_end - nav_start:.2f} seconds")
        
        login_start = time.time()
        fill_login_fields(username, password, username_id, password_id, page)
        login_end = time.time()
        print(f"tempo de login: {login_end - login_start:.2f} seconds")