from MenuRepository import MenuRepository
from Order import Order
from Menu import Menu


def test_get_user_input():
    result = "1 2".split(" ")
    assert len(result) == 2
    assert result[0].isnumeric() == True
    assert result[1].isnumeric() == True


def test_get_total_price():
    menu_repository = MenuRepository()
    hot_dog = Menu(1, "Hot dog", 4.00)
    menu_repository.set_menu_item(hot_dog)
    order = Order(1, 3)

    assert hot_dog.price * order.quantity == 12
