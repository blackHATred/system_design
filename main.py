from random import choice

from User import User
from item_system.DB_inventory import inventory_orm
from item_system.item import Item

# для примера создадим предметы
item1 = Item("AWP Dragon Lore", "Прикольный предмет")
item2 = Item("AK-47 skin", "что-то из кс")
inventory_orm.create_item(item1)
inventory_orm.create_item(item2)

# Пример работы продавца с сервисом торговой площадки
vasya_items = [item1, item2]
vasya = User("Vasya", "Pupkin", [item.id for item in vasya_items], 5)
created_lot = vasya.i_want_to_create_lot(choice(vasya_items).id, 1000.1)

# Пример работы покупателя с сервисом торговой площадки
sanya = User("Sanya", "Nosok", [], 10000000)
sanya.i_want_to_see_description_of_item(item1.id)
sanya.i_want_to_buy_lot(created_lot)
