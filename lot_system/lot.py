from random import randint


class Lot:
    commission = .1

    def __init__(self, seller_id: int, cost: float, item_id: int):
        self.id = randint(1, 100000)
        self.seller_id = seller_id
        self.cost = cost
        self.item_id = item_id
        self.status = "active"

    def set_status(self, new_status: str):
        self.status = new_status

