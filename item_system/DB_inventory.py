from item_system.item import Item
from misc import db_transaction


class InventoryORM:
    def __init__(self, connection_params: dict):
        # Создали какую-то ОРМ, добавили параметры для подключения к БД
        self.connection_params = connection_params
        # Все предметы
        self.items = []
        # Инвентари всех пользователей
        self.inventories: dict[int, list] = dict()
        # Зарезервированные предметы - они во владении пользователей, но их пока нельзя использовать
        self.reserved_inventories: dict[int, list[int]] = dict()

    def create_item(self, item: Item):
        self.items.append(item)

    def get_description(self, item_id: int) -> str:
        return [i for i in filter(lambda item: item.id == item_id, self.items)][0].description

    def get_3d_model(self, item_id: int):
        return [i for i in filter(lambda item: item.id == item_id, self.items)][0].model

    def add_item(self, user_id: int, item_id: int):
        if user_id not in self.inventories:
            self.inventories[user_id] = [item_id]
        else:
            self.inventories[user_id].append(item_id)

    def get_user_inventory(self, user_id: int) -> tuple:
        if user_id not in self.inventories:
            return ()
        return tuple(self.inventories[user_id])

    def has_item(self, user_id: int, item_id: int):
        return user_id in self.inventories and item_id in self.inventories[user_id]

    def reserve_item(self, user_id: int, item_id: int):
        with db_transaction() as transaction:
            if user_id not in self.reserved_inventories:
                self.reserved_inventories[user_id] = []
            self.reserved_inventories[user_id].append(item_id)
            self.inventories[user_id].remove(item_id)

    def delete_reserved_item(self, user_id: int, item_id: int):
        self.reserved_inventories[user_id].remove(item_id)


# Создали инстанс ормки, через которую будем взаимодействовать с БД
inventory_orm = InventoryORM({"ip": "localhost", "port": 5432})

