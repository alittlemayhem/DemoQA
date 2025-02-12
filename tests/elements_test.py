import time

from pages.elements_page import TextBoxPage
from conftest import driver


class TestElements:
    class TestTextBox:

        def test_textbox(self, driver):
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_cur_addr, output_perm_addr = text_box_page.check_filled_form()

            assert full_name == output_name, "Full name does not match"
            assert email == output_email, "Email does not match"
            assert current_address == output_cur_addr, "Current address does not match"
            assert permanent_address == output_perm_addr, "Permanent address does not match"