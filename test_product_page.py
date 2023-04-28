from .pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                         # открываем страницу
    page.should_be_product_page_url()   # проверяем что находимся на страеице продукта
    page.should_cart_button()           # Проверяем что кнопка доступна
    page.save_amount_of_cart()          #Сохраняем значение сумму в корзине
    page.save_amount_of_good_price()    # Сохраняем стоимость товара
    page.click_to_cart_button()         # Кликаем по кнопке
    page.solve_quiz_and_get_code()      # Обрабатываем всплывающие окно
    page.expected_result_good_in_cart_info_check() #Ожидаемый результат товар который добавили == добавился с правильным названием в карзину.
    page.expected_result_good_price_add_to_cart() #ПРоверяем что товар по стоимость добавился в корзину
