import time
from auth_page import AuthPage
from auth_page import RegistrationCode
from auth_page import ReselectKey
from auth_page import RegistrationMyRt
from auth_page import RostSmartHouse
from conftest import browserChrome
from conftest import browserFirefox
from settings import email
from settings import telethon
from settings import password
from settings import personal_account
from settings import new_telethon


def test_check_phone_search_positiv(browserChrome):
    # 1 "Проверить авторизациюна сайте с корректным телефоном и пароль(проверяем вкладку телефон)"
    page = AuthPage(browserChrome)
    page.tab_phone_click()
    page.enter_user(telethon)
    page.enter_pass(password)
    time.sleep(5)
    page.btn_login()
    time.sleep(10)
    page.go_bask()
    assert page.go_bask()
    assert page.get_current_url()
    print(page.get_current_url())


def test_check_phone_search_negativ1(browserChrome):
    # 2 "Проверить авторизациюна сайте с некорректным телефоном и корректным пароль(проверяем вкладку телефон)"
    page = AuthPage(browserChrome)
    page.tab_phone_click()
    page.enter_user("9999999997879900008 ")
    page.enter_pass(password)
    page.btn_login()
    time.sleep(5)
    page.invald_login()
    assert page.invald_login()
    assert (page.get_current_url())


def test_check_phone_search_negativ2(browserFirefox):
    # 3 "Проверить авторизациюна сайте с некорректным телефоном и корректным пароль(проверяем вкладку телефон)"
    page = AuthPage(browserFirefox)
    page.tab_phone_click()
    page.enter_user("самолет")
    page.enter_pass(password)
    page.btn_login()
    time.sleep(5)
    page.invald_login()
    time.sleep(5)
    assert page.invald_login()
    print(page.get_current_url())


def test_check_mail_search_positiv(browserChrome):
    # 4 "Проверить авторизациюна сайте с корректным email и корректным пароль(проверяем вкладку почта )"
    page = AuthPage(browserChrome)
    page.tab_email_click()
    page.enter_user(email)
    page.enter_pass(password)
    page.btn_login()
    time.sleep(15)
    page.go_bask()
    assert page.go_bask()
    assert page.get_current_url()
    print(page.get_current_url())


def test_check_mail_search_negativ1(browserFirefox):
    # 5 "Проверить авторизациюна сайте с некорректным email(нет знака @) и корректным пароль(проверяем вкладку почта)"
    page = AuthPage(browserFirefox)
    page.tab_email_click()
    page.enter_user("cc44hhcmail.ru")
    page.enter_pass(password)
    page.btn_login()
    time.sleep(4)
    page.invald_login()
    time.sleep(5)
    assert page.invald_login()
    print(page.get_current_url())


def test_check_RostSmartHouse_regist_pozitiv(browserChrome):
    #6 "Проверить регистрации сайте ("https://lk.rt.ru/"), корректный ввод данных"
    page = AuthPage(browserChrome)
    time.sleep(5)
    page.tab_regist()
    time.sleep(5)
    page.tab_name('Андрей')
    page.tab_surname('Тугов')
    time.sleep(5)
    page.enter_address(new_telethon)
    page.tab_password(password)
    page.tab_password_2(password)
    time.sleep(5)
    page.button_registr()
    time.sleep(10)
    mess = "Подтверждение телефона"
    assert page.error_message_phone_verification() == mess
    print(page.get_current_url())


def test_check_RostSmartHouse_regist_pozit(browserChrome):
    #7 "Проверить регистрации сайте ("https://lk.rt.ru/"), некорректный ввод данных"
    page = AuthPage(browserChrome)
    time.sleep(5)
    page.tab_regist()
    time.sleep(5)
    page.tab_name('BHGGUGUHUGIYGYYGUCIHCJYIX:KCHCGUGXIHXOCHKCHHHVCGVFYUGXYGXICVHVCKBCKJBCVGTVCVC')
    page.tab_surname('7665656889857676567')
    time.sleep(5)
    page.enter_address("пыпсгпшыгпмг")
    page.tab_password(password)
    page.tab_password_2(password)
    time.sleep(5)
    page.button_registr()
    time.sleep(10)
    mess = "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"
    assert page.error_message_phone_format() == mess
    assert page.find_element_error_name()
    assert page.find_element_error_fam()
    print(page.get_current_url())



def test_check_login_search_positiv(browserChrome):
    # 8 "Проверить авторизациюна сайте с корректным логином и корректным пароль(проверяем вкладку логин )"
    page = AuthPage(browserChrome)
    page.tab_login_click()
    page.enter_user(email)
    page.enter_pass(password)
    time.sleep(15)
    page.btn_login()
    time.sleep(15)
    assert (page.get_current_url()) == "https://start.rt.ru/?tab=main"


def test_check_login_search_negativ1(browserFirefox):
    # 9 "Проверить авторизациюна сайте с неверным логином(256 символов) и корректным пароль(проверяем вкладку логин)"
    page = AuthPage(browserFirefox)
    page.tab_login_click()
    page.enter_user("677634433453456734567866766666666554322222222111113245678"
                    "383774665748489339339939390202027777877:,.777787876667676"
                    "77878976234567893456789034567895678983838383838737477ррРРH"
                    "Yy33838389239393999393993939932002020202020020299338838388383"
                    "992929929299292992929")
    page.enter_pass("111222Qq")
    page.btn_login()
    time.sleep(5)
    page.invald_login()
    time.sleep(5)
    assert page.invald_login()
    print(page.get_current_url())


def test_check_ls_search_positiv(browserFirefox):
    # 10 "Проверить авторизациюна сайте с корректным лицевой счёт и корректным пароль(проверяем вкладку лицевой счёт)"
    page = AuthPage(browserFirefox)
    page.tab_ls_click()
    page.enter_user(personal_account)
    page.enter_pass(password)
    time.sleep(5)
    page.btn_login()
    time.sleep(15)
    assert (page.get_current_url()) == "https://start.rt.ru/?tab=main"


def test_check_ls_search_negativ1(browserChrome):
    # 11 "Проверить авторизациюна сайте с некорректным лицевой счёт(256 символов) и корректным пароль(проверяем вкладку лицевой счёт)"
    page = AuthPage(browserChrome)
    page.tab_ls_click()
    page.enter_user('.;.,:.;.,:.*:.!№:,.;(")')
    page.enter_pass(password)
    page.btn_login()
    time.sleep(5)
    page.invald_login()
    time.sleep(5)
    assert page.invald_login()
    print(page.get_current_url())


def test_check_forgot_password(browserChrome):
    # 20 "Проверить кнопку забыл пароль, кнопка кликабельна, при нажатие переходим на другую страницу"
    page = AuthPage(browserChrome)
    page.tab_phone_click()
    page.enter_user(telethon)
    page.enter_pass("gygj")
    time.sleep(5)
    page.btn_login()
    page.invald_login()
    page.btn_forgot_password()
    time.sleep(10)
    assert page.header_password_recovery()
    print(page.get_current_url())


def test_check_adress_positiv(browserFirefox):
    # 12 "Проверить авторизациюна сайте Ростелеком (авторизация по коду,https://start.rt.ru)"
    page_start = RegistrationCode(browserFirefox)
    page_start.enter_address(telethon)
    time.sleep(15)
    page_start.button_get_code()
    time.sleep(15)
    assert page_start.find_element()
    print(page_start.get_current_url())


def test_check_adress_negativ1(browserChrome):
    #-13 "Проверить авторизациюна сайте Ростелеком (авторизация по коду,https://start.rt.ru ), вводим неправильный номер"
    page_start = RegistrationCode(browserChrome)
    page_start.enter_address("79177777.,:()!")
    page_start.button_get_code()
    time.sleep(10)
    mess = "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"
    assert page_start.error_message_telefon() == mess


def test_check_rostelecom_key_positiv(browserFirefox):
    # 14 "Проверить авторизациюна сайте Ростелеком Ключ(авторизация по коду ), с корректными даннами"
    page_key = ReselectKey(browserFirefox)
    time.sleep(4)
    page_key.login_button()
    time.sleep(10)
    page_key.input_login(email)
    page_key.tab_code()
    time.sleep(10)
    assert page_key.head_confirm_code()


def test_check_rostelecomkey_negativ1(browserChrome):
    # 15"Проверить авторизациюна сайте Ростелеком Ключ(авторизация по коду ), с некорректными данными"
    page_key = ReselectKey(browserChrome)
    time.sleep(3)
    page_key.login_button()
    time.sleep(15)
    page_key.input_login('594554@mail..ru')
    page_key.tab_code()
    messag = "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"
    assert page_key.error_messag_telefon() == messag
    print(page_key.error_messag_telefon())

def test_check_adress_myrt_positiv(browserChrome):
    # 16 "Проверить авторизациюна сайте Мой Ростелеком (авторизация по коду, https://my.rt.ru)"
    pageMyRt = RegistrationMyRt(browserChrome)
    pageMyRt.enter_mail(email)
    time.sleep(10)
    pageMyRt.button_get_code()
    time.sleep(5)
    assert pageMyRt.find_element()
    print(pageMyRt.get_current_url())

def test_check_button_vk_pozitiv(browserFirefox):
    # 17 "Проверить авторизациюна сайте Мой Ростелеком (авторизация по коду, https://my.rt.ru)"
    pageMyRt = RegistrationMyRt(browserFirefox)
    pageMyRt.button_vk()
    time.sleep(5)
    assert pageMyRt.logo_vk()
    print(pageMyRt.get_current_url())


def test_check_adress_myrt_negativ1(browserChrome):
    # 18 "Проверить авторизациюна сайте Мой Ростелеком (авторизация по коду, https://my.rt.ru),с некорректными данными, вводим не зарегистрированную почту"
    pageMyRt = RegistrationMyRt(browserChrome)
    pageMyRt.enter_mail("kkkk@mail.ru")
    time.sleep(5)
    pageMyRt.button_get_code()
    time.sleep(5)
    assert pageMyRt.login_password()
    print(pageMyRt.get_current_url())


def test_check_adress_myrt_negativ2(browserChrome):
    #19 "Проверить авторизациюна сайте Мой Ростелеком (авторизация по коду,https://my.rt.ru),с некорректными данными, вводим некорректную почту"
    pageMyRt = RegistrationMyRt(browserChrome)
    pageMyRt.enter_mail("+78548ркрпкрп")
    time.sleep(5)
    pageMyRt.button_get_code()
    time.sleep(5)
    msg = "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"
    assert pageMyRt.error_message_mail() == msg
    print(pageMyRt.get_current_url())

def test_check_RostSmartHouse_addres_pozit(browserChrome):
    #21 "Проверить авторизациюна сайте Lk smarthome  Ростелеком (авторизация по коду,https://lk.smarthome.rt.ru/),с корректными данными"
    pageMyRt = RostSmartHouse(browserChrome)
    pageMyRt.enter_mail(telethon)
    time.sleep(12)
    pageMyRt.button_get_code()
    time.sleep(5)
    assert pageMyRt.find_element()
    print(pageMyRt.get_current_url())


def test_check_RostSmartHouse_addres_negativ(browserChrome):
    #22 "Проверить авторизациюна сайте Lk smarthome  Ростелеком (авторизация по коду, https://lk.smarthome.rt.ru/),с некорректными данными, вводим некорректный номер"
    pageMyRt = RostSmartHouse(browserChrome)
    pageMyRt.enter_mail("+78548")
    time.sleep(12)
    pageMyRt.button_get_code()
    time.sleep(5)
    msg = "Неверный формат телефона"
    assert pageMyRt.error_message_mail() == msg
    print(pageMyRt.get_current_url())


def test_check_RostSmHouse_regist_pozitiv(browserChrome):
    #23 "Проверить регистрации сайте (https://lk.smarthome.rt.ru), корректный ввод данных"
    pageMyRt = RostSmartHouse(browserChrome)
    pageMyRt.tab_login_pass()
    time.sleep(5)
    pageMyRt.tab_regist()
    time.sleep(5)
    pageMyRt.tab_name('Маргорита')
    pageMyRt.tab_surname('Турина')
    time.sleep(5)
    pageMyRt.enter_mail(new_telethon)
    pageMyRt.tab_password(password)
    pageMyRt.tab_password_2(password)
    time.sleep(5)
    pageMyRt.button_registr()
    time.sleep(10)
    mess = "Подтверждение телефона"
    assert pageMyRt.error_message_phone_verification() == mess
    print(pageMyRt.get_current_url())

def test_check_RostSmartHouse_regist_negativ(browserFirefox):
    #24 "Проверить регистрации сайте (https://lk.smarthome.rt.ru), некорректный ввод данных в нескольких полях"
    pageMyRt = RostSmartHouse(browserFirefox)
    pageMyRt.tab_login_pass()
    time.sleep(5)
    pageMyRt.tab_regist()
    time.sleep(5)
    pageMyRt.tab_name('М1256!,:,. :?')
    pageMyRt.tab_surname('')
    # "Вводим пустую строку"
    time.sleep(5)
    pageMyRt.enter_mail('89175553233ff')
    pageMyRt.tab_password(password)
    pageMyRt.tab_password_2(password)
    time.sleep(5)
    pageMyRt.button_registr()
    time.sleep(10)
    assert pageMyRt.find_element_error()
    print(pageMyRt.get_current_url())