import time

from pages.elements_page import TextBoxPage
from conftest import driver


class TestElements:
    class TestTextBox:

        def test_textbox(self, driver):
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()
            text_box_page.fill_all_fields()

            output_name, output_email, output_cur_addr, output_perm_addr = text_box_page.check_filled_form()
            print(output_name)
            print(output_email)
            print(output_cur_addr)
            print(output_perm_addr)

