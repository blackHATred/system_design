from misc import db_transaction


class PaymentORM:
    def __init__(self, connection_params: dict):
        # Создали какую-то ОРМ, добавили параметры для подключения к БД
        self.connection_params = connection_params
        # Кошельки всех пользователей
        self.wallets: dict[int, float] = dict()

    def add_user(self, user_id: int):
        self.wallets[user_id] = 0

    def add_money(self, user_id: int, amount: float):
        self.wallets[user_id] += amount

    def get_money(self, user_id: int) -> float:
        return self.wallets[user_id]

    def reduce_money(self, user_id: int, amount: float):
        if self.wallets[user_id] < amount:
            print("! Так нельзя")
        else:
            self.wallets[user_id] -= amount

    def transfer_money(self, from_user_id: int, to_user_id: int, from_amount: float, to_amount: float):
        with db_transaction() as transaction:
            self.reduce_money(from_user_id, from_amount)
            # где-то здесь через стороннее апи забираем комиссию себе
            self.add_money(to_user_id, to_amount)


# Создали инстанс ормки, через которую будем взаимодействовать с БД
payment_orm = PaymentORM({"ip": "localhost", "port": 5432})

