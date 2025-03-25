
import json


class Transaction:
    def __init__(self, data) -> None:
        self.data = data

    def make_transaction(self):
        transaction = {
            "hash": transaction_hash,
            "header": transaction_header,
            "payment": payment,
            "session": session,
            "approvals": approvals
        }

        return json.dumps(transaction)
