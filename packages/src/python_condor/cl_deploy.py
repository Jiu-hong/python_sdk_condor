import json


class Deploy:
    def __init__(self, data) -> None:
        self.data = data

    def make_deploy(self):
        deploy = {
            "hash": deploy_hash,
            "header": deploy_header,
            "payment": payment,
            "session": session,
            "approvals": approvals
        }

        return json.dumps(deploy)
