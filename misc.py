class db_transaction(object):
    def __enter__(self):
        print("Начали транзакцию")
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        print("Закончили транзакцию")

    def __float__(self):
        return "Объект транзакции"
