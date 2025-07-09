from playwright.sync_api import Page, Locator, Response

def navigate_to_page(url: str, page: Page) -> Response:
    return page.goto(url)

def locate_element_by_id(element_id, page: Page) -> Locator:
    return page.locator(f'#{element_id}')

def fill_input_by_id(element_id: str, content: str, page: Page):
    page.fill(f'#{element_id}', content)

def type_input_by_id(element_id: str, content: str, page: Page):
    page.type(f'#{element_id}', content)

def loose_focus(page: Page):
    page.evaluate('document.activeElement.blur()')

def simulate_key_press(page: Page, key: str):
    page.keyboard.press(key)

def wait_for_page_load(page: Page, timeout: int = 30000):
    page.wait_for_load_state('load', timeout=timeout)


def click_first_row_by_table_label(table_label: str, page: Page):
    tr = page.locator(f'tr[data-item-label="{table_label}"]')
    tr.click()

def wait_for_element_by_id(element_id: str, page: Page):
    print('waiting for element')
    page.wait_for_selector(f'#{element_id}')
    print('element found')


def fill_login_fields(username, password, username_id, password_id, page: Page):
    fill_input_by_id(username_id, username, page)
    fill_input_by_id(password_id, password, page)
    entrar_span = locate_element_by_text('Entrar', page)
    parent_button = entrar_span.locator('xpath=..')
    parent_button.click()

def locate_element_by_text(text, page: Page) -> Locator:
    return page.locator('span', has_text=text)

def locate_element_by_xpath(xpath, page: Page) -> Locator:
    return page.locator(xpath)

def click_element_by_id(element_id: str, page: Page):
    element = locate_element_by_id(element_id, page)
    element.click()

def click_element_by_xpath(xpath: str, page: Page):
    element = locate_element_by_xpath(xpath, page)
    element.click()

def select_and_click_li_from_ul(ul_id: str, li_text: str, page: Page):
    ul_element = locate_element_by_id(ul_id, page)
    li_element = ul_element.locator(f'li[data-label="{li_text}"]')
    li_element.click()

def fill_input_after_labels(label1_text: str, label2_text: str, content: str, page: Page):
    label1 = page.locator(f'label:has-text("{label1_text}")')
    label2 = page.locator(f'label:has-text("{label2_text}")')
    input_element = page.locator(f'input:right-of(:has-text("{label1_text}")):right-of(:has-text("{label2_text}"))')
    input_element.fill(content)
