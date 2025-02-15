import random
import time
from typing import List

from selenium.webdriver.remote.webelement import WebElement

from generator.generator import generated_person
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self) -> tuple[str, str, str, str]:
        person_info = next(generated_person())
        full_name: str = person_info.full_name
        email: str = person_info.email
        current_address: str = person_info.current_address
        permanent_address: str = person_info.permanent_address

        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    def check_filled_form(self) -> tuple[str, str, str, str]:
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address

class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    def click_random_checkbox(self):
        item_list: List = self.elements_are_visible(self.locators.ITEMS_LIST)
        count: int = 21
        while count != 0:
            item = item_list[random.randint(1, 15)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break

    def get_checked_checkboxes(self) -> List[str]:
        checked_list : List[WebElement] = self.elements_are_present(self.locators.CHECKED_ITEMS)
        data: List[str] = []
        for box in checked_list:
            title_item = box.find_element("xpath" ,self.locators.TITLE_ITEM)
            data.append(title_item.text.replace(' ', '').replace('.doc', '').lower())
        return data

    def get_output_result(self) -> List[str]:
        result_list: List[WebElement] = self.elements_are_present(self.locators.OUTPUT_RESULT)
        data: List[str] = []
        for item in result_list:
            data.append(item.text.lower())
        return data

class RadioButtonPage(BasePage):
    # my solution
    '''locators = RadioButtonPageLocators()

    def select_random_radiobutton(self) -> str:
        buttons_list: List[WebElement] = self.elements_are_present(self.locators.RADIO_BUTTONS)
        button = buttons_list[random.randint(0,2)]
        self.driver.execute_script("arguments[0].click();", button)
        return button.find_element("xpath", self.locators.RADIOBUTTON_TITLE).text

    def get_output_result(self) -> str:
        return self.element_is_visible(self.locators.OUTPUT_RESULT).text'''
    locators = RadioButtonPageLocators()

    def click_radio_button(self, choice):
        choices = {"yes": self.locators.YES,
        "impressive": self.locators.IMPRESSIVE,
        "no": self.locators.NO}

        self.element_is_visible(choices[choice]).click()

    def get_output_result(self):
        return self.element_is_visible(self.locators.OUTPUT_RESULT).text