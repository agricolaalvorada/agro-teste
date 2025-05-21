from utils.page_utils import navigate_to_page, login_to_site, click_element_by_id, select_and_click_li_from_ul
from playwright.sync_api import Page

def start_new_romaneio(url: str, username: str, password: str, username_id: str, password_id: str, page: Page, operacao: str):
        navigate_to_page(url, page)
        login_to_site(username, password, username_id, password_id, page)
        navigate_to_page('http://10.1.1.28:1015/itss-agro/paginas/romaneio/inicial.jsf', page)
        click_element_by_id('tipo', page)
        select_and_click_li_from_ul('tipo_items', operacao, page)
        click_element_by_id('btnCadastrar', page)