from random import randint

from item_system.DB_inventory import inventory_orm
from lot_system.DB_lot import lot_orm
from other_api.payment import payment_orm


class User:
    def __init__(self, name: str, surname: str, inventory: list[int], wallet: float):
        self.user_id = randint(1, 100000)
        self.name = name
        self.surname = surname
        payment_orm.add_user(self.user_id)
        payment_orm.add_money(self.user_id, wallet)
        # Для примера сразу скажем, что у пользователя есть такие предметы
        for item_id in inventory:
            inventory_orm.add_item(self.user_id, item_id)

    def i_want_to_create_lot(self, item_id: int, cost: float) -> int:
        return lot_orm.add_lot(self.user_id, item_id, cost)

    def i_want_to_buy_lot(self, lot_id: int):
        lot_orm.buy_lot(self.user_id, lot_id)

    @staticmethod
    def i_want_to_see_description_of_item(item_id: int):
        return inventory_orm.get_description(item_id)