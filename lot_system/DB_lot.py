from item_system.DB_inventory import inventory_orm
from lot_system.lot import Lot
from misc import db_transaction
from notification_system.notification import send_notification
from other_api.payment import payment_orm


class LotORM:
    def __init__(self, connection_params: dict):
        # Создали какую-то ОРМ, добавили параметры для подключения к БД
        self.connection_params = connection_params
        # Инвентари всех пользователей
        self.lots: list[Lot] = list()

    def add_lot(self, user_id: int, item_id: int, cost: float) -> int:
        with db_transaction() as transaction:
            if inventory_orm.has_item(user_id, item_id):
                new_lot = Lot(user_id, cost, item_id)
                self.lots.append(new_lot)
                inventory_orm.reserve_item(user_id, item_id)
                return new_lot.id
            else:
                print("Не-а, так нельзя")

    def buy_lot(self, user_id: int, lot_id: int):
        lot = [i for i in filter(lambda lot_: lot_.id == lot_id, self.lots)][0]
        if lot.status == "sold":
            print("Так нельзя")
            return
        with db_transaction() as transaction:
            # перекидываем деньги за вычетом комиссии, меняем статус лота и передаём предмет
            payment_orm.transfer_money(user_id, lot.seller_id, lot.cost*(1+lot.commission), lot.cost)
            lot.set_status("sold")
            inventory_orm.delete_reserved_item(lot.seller_id, lot.item_id)
            inventory_orm.add_item(user_id, lot.item_id)
            send_notification(lot.seller_id, "Твой предмет купили")


# Создали инстанс ормки, через которую будем взаимодействовать с БД
lot_orm = LotORM({"ip": "localhost", "port": 5432})
