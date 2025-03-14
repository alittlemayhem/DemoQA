import time
from msilib.schema import RadioButton
from typing import List

from selenium.webdriver.remote.webelement import WebElement

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage
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

    class TestCheckBox:
        def test_checkbox(self, driver):
            checkbox_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
            checkbox_page.open()
            checkbox_page.open_full_list()
            checkbox_page.click_random_checkbox()
            input_checkbox: List[str] = checkbox_page.get_checked_checkboxes()
            output_result: List[str] = checkbox_page.get_output_result()

            assert input_checkbox == output_result, "Checkboxes have not been selected "

    class TestRadioButton:
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
            radio_button_page.open()
            #button: str = radio_button_page.select_random_radiobutton()
            #output_result: str = radio_button_page.get_output_result()
            #assert button == output_result

            radio_button_page.click_radio_button("yes")
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_radio_button("impressive")
            output_impressive = radio_button_page.get_output_result()
            radio_button_page.click_radio_button("no")
            output_no = radio_button_page.get_output_result()

            assert output_yes == "Yes", "Yes have not been selected"
            assert output_impressive == "Impressive", "Impressive have not been selected"
            assert output_no == "No", "No have not been selected"

    class TestWebTable:
        def test_webt_add_person(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            table_result = web_table_page.check_new_added_person()
            print(new_person)
            print(table_result)
            assert new_person in table_result
