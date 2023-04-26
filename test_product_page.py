from .pages.product_page import ProductPage

def test_guest_can_go_to_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                         # открываем страницу
    page.should_be_product_page_url()   # проверяем что находимся на страеице продукта
    page.should_cart_button()           # Проверяем что кнопка доступна
    page.click_to_cart_button()         # Кликаем по кнопке
    page.solve_quiz_and_get_code()      # Обрабатываем всплывающие окно
    page.expected_result_good_in_cart_info_check() #Ожидаемый результат товар который добавили == добавился с правильным названием в карзину.
