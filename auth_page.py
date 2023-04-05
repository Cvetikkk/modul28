import os
from base import WebPage
from elements import WebElement


class AuthPage(WebPage):
    tab_phone = WebElement(id='t-btn-tab-phone')
    # "вкладка телефон"
    tab_user = WebElement(id="username")
    # "ввод имени"
    password = WebElement(id="password")
    # "ввод пароль"
    btn_ls = WebElement(id="widget_bar")
    # "зашли в аккаунт появилась кнопка поддержка
    invalid_login = WebElement(id="form-error-message")
    # "неверный логин или пароль"
    button_login = WebElement(id="kc-login")
    # "кнопка войти"
    tab_mail = WebElement(id='t-btn-tab-mail')
    # "регистрация маил"
    tab_login = WebElement(id='t-btn-tab-login')
    # "регистрация логина"
    tab_ls = WebElement(id='t-btn-tab-ls')
    # "регистрация лицевого счета"
    tab_forgot_password = WebElement(id="forgot_password")
    # "кнопку забыли пароль"
    password_header = WebElement(css_selector="#page-right > div > div > h1")
    # "Появился заголовок Восстановление пароля"
    tab_addres = WebElement(id="address")

    tab_registr = WebElement(id="kc-register")
    # "Кнопка  Зарегистрироваться на странице авторизация"
    name = WebElement(name="firstName")
    surname = WebElement(name="lastName")
    password_2 = WebElement(id="password-confirm")
    new_registr = WebElement(name="register")
    # "Кнопка зарегистрироваться на страницы регистрации"
    error_n = WebElement(xpath="/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[1]/span")
    # "выходит ошибка ввода 'Необходимо заполнить поле кириллицей. От 2 до 30 символов"
    error_f = WebElement(xpath="/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[2]/span")
    # "выходит ошибка ввода 'Необходимо заполнить поле кириллицей. От 2 до 30 символов"
    error_tel = WebElement(xpath="/ html / body / div[1] / main / section[2] / div / div / div / form / div[3] / span")
    # "выходит ошибка ввода 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'"
    phone_verification = WebElement(xpath='/ html / body / div[1] / main / section[2] / div / div / h1')
    # "Поиск заголовка 'подтверждение телефона'"


    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or "https://lk.rt.ru/"

        super().__init__(web_driver, url)

    def tab_phone_click(self):
        self.tab_phone.click()

    def enter_user(self, value):
        self.tab_user.send_keys(value)

    def enter_pass(self, value):
        self.password.send_keys(value)

    def invald_login(self):
        text = self.invalid_login.find()
        return text

    def go_bask(self):
        support_button = self.btn_ls.find()
        return support_button
        # Зашли на сайт,есть кнопка поддержки

    def tab_email_click(self):
        self.tab_mail.click()

    def btn_login(self):
        self.button_login.click()
        # 'кнопка войти! нужна при каждом заходе'

    def tab_login_click(self):
        self.tab_login.click()

    def tab_ls_click(self):
        self.tab_ls.click()

    def url(self):
        self.get_current_url()

    def btn_forgot_password(self):
        self.tab_forgot_password.click()
    # "Нажимаем кнопку забыли пароль"

    def header_password_recovery(self):
        a = self.password_header.find()
        return a
        # "Ищем элемент восстановление пароля"

    def enter_address(self, value):
        self.tab_addres.send_keys(value)


    def tab_regist(self):
        self.tab_registr.click()
    # "Нажать на кнопку Зарегистрироваться"


    def tab_name(self, value):
        self.name.send_keys(value)
    # "Нажать на кнопку имя"


    def tab_surname(self, value):
        self.surname.send_keys(value)
    # "Нажать на кнопку фамилия"


    def tab_password(self, value):
        self.password.send_keys(value)
    # "Вводим пароль"


    def tab_password_2(self, value):
        self.password_2.send_keys(value)
    # "Вводим подтверждение пароля"


    def button_registr(self):
        self.new_registr.click()
    # "Кнопка зарегистрироваться на странице регистрации"


    def find_element_error_name(self):
        fin_elemen = self.error_n.find()
        return fin_elemen
    # "Появилась надпись под именем 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'"

    def find_element_error_fam(self):
        fin_elemen = self.error_f.find()
        return fin_elemen
    # "Появилась надпись под фамилией 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'"

    def error_message_phone_format(self):
        phone_format = self.error_tel.find()
        return phone_format.get_attribute('innerHTML')

    # "Появляеться тект подтверждение телефона"

    def error_message_phone_verification(self):
        phone_verific = self.phone_verification.find()
        return phone_verific.get_attribute('innerHTML')
    # "Появляеться тект подтверждение телефона"


class RegistrationCode(WebPage):
    fine_error = WebElement(xpatch='//*[@id="page-right"]/div/div/div/form/div[1]/span/text()')
    # (text="Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru")
    fine_element = WebElement(name="otp_back_phone")
    tab_get_code = WebElement(id="otp_get_code")
    tab_addres = WebElement(id="address")
    fine_error_tel = WebElement(css_selector="#page-right > div > div > div > form > div.rt-input-container.rt-input-container--error.email-or-phone.otp-form__address > span")

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or "https://start.rt.ru"

        super().__init__(web_driver, url)

    def enter_address(self, value):
        self.tab_addres.send_keys(value)

    def button_get_code(self):
        self.tab_get_code.click()

    def find_element(self):
        fin_element = self.fine_element.find()
        return fin_element
    # "Зашли на страницу код подтверждения отправлен"

    def error_message_telefon(self):
        tab_mes_tel = self.fine_error_tel.find()
        print('tab_mes_mail get_text', tab_mes_tel.get_attribute('innerHTML'))
        return tab_mes_tel.get_attribute('innerHTML')
    # "Находим текст что ввели номер неверно"

class ReselectKey(WebPage):
    tab_login = WebElement(xpath="/html/body/section/div/div[2]/a[1]")
    input_loginn = WebElement(id="address")
    tab_get_code = WebElement(id="otp_get_code")
    header_confirmation_code = WebElement(css_selector='#page-right > div > div > h1')
    error_messag = WebElement(css_selector="#page-right > div > div > div > form > div.rt-input-container."
                                           "rt-input-container--error.email-or-phone.otp-form__address > span")

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or "https://key.rt.ru/"

        super().__init__(web_driver, url)

    def login_button(self):
        self.tab_login.click()
        # self.a.click()

    def input_login(self, value):
        self.input_loginn.send_keys(value)

    def tab_code(self):
        self.tab_get_code.click()

    def head_confirm_code(self):
        a = self.header_confirmation_code.find()
        return a
    # "Появилась кнопка изменить номер"

    def error_messag_telefon(self):
        mes_tel = self.error_messag.find()
        return mes_tel.get_attribute('innerHTML')
        # "Появилася заголовок что неправильно введен номер или емаил"

class RegistrationMyRt(WebPage):
    bt_vk = WebElement(id="oidc_vk")
    str_vk = WebElement(xpath='/html/body/div/div/div/div[1]/a')
    fine_error = WebElement(css_selector='#page-right > div > div > div > form > div.rt-input-container.rt-input-'
                                         'container--error.email-or-phone.otp-form__address > span')
    input_mail = WebElement(id="address")
    tab_get_code = WebElement(id="otp_get_code")
    fine_element = WebElement(name="otp_back_phone")
    incorrect_email = WebElement(id="form-error-message")
    tab_login_password = WebElement(id="standard_auth_btn")

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or "https://my.rt.ru"

        super().__init__(web_driver, url)

    def enter_mail(self, value):
        self.input_mail.send_keys(value)

    def button_get_code(self):
        self.tab_get_code.click()

    def find_element(self):
        fin_element = self.fine_element.find()
        return fin_element
    # "Зашли на страницу код подтверждения отправлен, есть кнопка изменить номер"

    def button_vk(self):
        self.bt_vk.click()
    # "Нажимаем кнопку вк"

    def logo_vk(self):
        find_logo = self.str_vk.find()
        return find_logo
    # "Переход на официальную страницу вк"

    def error_message(self):
        incorrect_mail = self.incorrect_email.find()
        return incorrect_mail
    # "Зашли на страницу получить код, кнопка изменить номер"

    def login_password(self):
        tab_lg_pass = self.tab_login_password.is_clickable()
        return tab_lg_pass
    # "Есть кнопка войти с паролем и она кликабельна"

    def error_message_mail(self):
        tab_mes_mail = self.fine_error.find()
        print('tab_mes_mail get_text', tab_mes_mail.get_attribute('innerHTML'))
        return tab_mes_mail.get_attribute('innerHTML')
    # "Появляеться тект как правильно писать почту"

class RostSmartHouse(WebPage):
    fine_error = WebElement(css_selector='#page-right > div > div > div > form > div.rt-input-container.rt-input-container--error.'
                                         'email-or-phone.otp-form__address > span')
    # "Появляеться ошибка неверный номер"

    input_mail = WebElement(id="address")
    tab_get_code = WebElement(id="otp_get_code")
    fine_element = WebElement(css_selector="#page-right > div > div > h1")
    # "Заголовок код подверждения отправлен"
    tab_login_password = WebElement(id="standard_auth_btn")
    # "Кнопка войти с паролем"
    tab_registr = WebElement(id="kc-register")
    # "Кнопка  Зарегистрироваться на странице авторизация по коду"
    name = WebElement(name="firstName")
    surname = WebElement(name="lastName")
    password = WebElement(id="password")
    password_2 = WebElement(id="password-confirm")
    new_registr = WebElement(name="register")
    # "Кнопка зарегистрироваться на страницы регистрации"
    error = WebElement(xpath="/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[1]/span")
    # "выходит ошибка ввода 'Необходимо заполнить поле кириллицей. От 2 до 30 символов"
    phone_verification = WebElement(xpath='/ html / body / div[1] / main / section[2] / div / div / h1')
    # "Поиск заголовка 'подтверждение телефона'"


    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or "https://lk.smarthome.rt.ru/"

        super().__init__(web_driver, url)

    def enter_mail(self, value):
        self.input_mail.send_keys(value)

    def button_get_code(self):
        self.tab_get_code.click()

    def find_element(self):
        fin_element = self.fine_element.find()
        return fin_element
    # "Зашли на страницу код подтверждения отправлен, есть кнопка изменить номер

    def error_message_mail(self):
        tab_mes_mail = self.fine_error.find()
        print('tab_mes_mail get_text', tab_mes_mail.get_attribute('innerHTML'))
        return tab_mes_mail.get_attribute('innerHTML')
    # "Появляеться тект как правильно писать номер"

    def tab_login_pass(self):
        self.tab_login_password.click()
        # "Нажать на кнопку войти с паролем"

    def tab_regist(self):
        self.tab_registr.click()
        # "Нажать на кнопку Зарегистрироваться"

    def tab_name(self, value):
        self.name.send_keys(value)
        # "Нажать на кнопку имя"

    def tab_surname(self, value):
        self.surname.send_keys(value)
        # "Нажать на кнопку фамилия"

    def tab_password(self, value):
        self.password.send_keys(value)
        # "Вводим пароль"

    def tab_password_2(self, value):
        self.password_2.send_keys(value)
        # "Вводим подтверждение пароля"

    def button_registr(self):
        self.new_registr.click()
        # "Кнопка зарегистрироваться на странице регистрации"

    def find_element_error(self):
        fin_elemen = self.error.find()
        return fin_elemen
        # "Зашли на страницу код подтверждения отправлен, есть кнопка изменить номер

    def error_message_phone_verification(self):
        phone_verific = self.phone_verification.find()
        return phone_verific.get_attribute('innerHTML')
    # "Появляеться тект подтверждение телефона"

