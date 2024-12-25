import pytest
from modules.common.database import Database


@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()


@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()

    print(users)


@pytest.mark.database
def test_check_user_by_name():
    db = Database()
    customer = db.get_user_address_by_name('Sergii')

    assert customer[0][0] == 'Maydan Nezalezhnosti 1'
    assert customer[0][1] == 'Kyiv'
    assert customer[0][2] == '3127'
    assert customer[0][3] == 'Ukraine'


@pytest.mark.database
def test_product_qty_update():
    db = Database()
    db.update_product_qty_by_id(1, 25)
    water_qty = db.select_product_qty_by_id(1)

    assert water_qty[0][0] == 25


@pytest.mark.database
def test_product_insert() :
    db = Database()
    db.insert_product(4, 'печиво', 'солодке', 30)
    water_qty = db.select_product_qty_by_id(4)
    assert water_qty [0][0] == 30


@pytest.mark.database
def test_product_delete():
    db = Database()
    db.insert_product(99, 'тестові', 'дані', 999)
    product_qty = db.select_product_qty_by_id(99)
    if product_qty [0][0] == 999:
        db.delete_product_by_id (99)
        qty = db.select_product_qty_by_id(99)
        assert len(qty) == 0
    else:
        print("Error while creating test data")


@pytest.mark.database
def test_detailed_orders():
    db = Database()
    orders = db.get_detailed_orders()
    print("Замовлення", orders)
    # Check quantity of orders equal to 1
    assert len(orders) == 1

    # Check data structure
    assert orders[0][0] == 1
    assert orders[0][1] == 'Sergii'
    assert orders[0][2] == 'солодка вода'
    assert orders[0][3] ==  'з цукром'
