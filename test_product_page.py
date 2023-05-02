from .pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                         # открываем страницу
    page.should_be_product_page_url()   # проверяем что находимся на страеице продукта
    page.should_cart_button()           # Проверяем что кнопка доступна
    expected_price = page.save_amount_of_good_with_current_cart()          #Сохраняем значения суммы корзины
    name_of_product = page.save_name_of_product()        #Сохраняем название товара
    page.click_to_cart_button()         # Кликаем по кнопке
    page.solve_quiz_and_get_code()      # Обрабатываем всплывающие окно
    page.expected_result_good_in_cart_add_notify_same(name_of_product) #Ожидаемый результат товар который добавили == добавился с правильным названием в карзину.
    page.expected_result_good_price_add_notify_same(expected_price) #ПРоверяем что товар по стоимость добавился в корзину
