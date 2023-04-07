import allure

from utils.elements.button import Button
from utils.elements.input import Input
from utils.elements.text_area import TextArea
from pages.page_base import BasePage


class PageTextBox(BasePage):

    @allure.step("Пеоеход на страницу")
    def step_1_transition(self):
        self._all_transition("Elements", "Text Box")

    @allure.step("Ввод имени")
    def step_2_input_name(self, name):
        input_full_name = Input(xpath="//input[@id='userName']", driver=self._driver)
        input_full_name.val_input(name)

    @allure.step("Ввод email")
    def step_3_input_email(self, email):
        input_email = Input(xpath="//input[@id='userEmail']", driver=self._driver)
        input_email.val_input(email)

    @allure.step("Ввод адреса")
    def step_4_input_current_address(self, address):
        textarea_current_address = TextArea(xpath="//textarea[@id='currentAddress']", driver=self._driver)
        textarea_current_address.val_text_area(address)

    @allure.step("Ввод постоянго адреса")
    def step_5_input_permanent_address(self, address):
        textarea_permanent_address = TextArea(xpath="//textarea[@id='permanentAddress']", driver=self._driver)
        textarea_permanent_address.val_text_area(address)

    @allure.step("нажатие на кнопку")
    def step_6_click_submit(self):
        button_submit = Button(xpath="//button[@id='submit']", driver=self._driver)
        print(button_submit.is_visible())
        button_submit.click_button()
