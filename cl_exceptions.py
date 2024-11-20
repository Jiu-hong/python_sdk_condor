class ExceptionExceedMaxValue(Exception):
    def __init__(self, data, num_type, message=" isn't in the range of "):
        self.data = data
        self.message = message
        self.num_type = num_type
        super().__init__(self.data + self.message + self.num_type)


class ExceptionCLNumber(Exception):
    def __init__(self, data, message="should be decimal or string(decimal)"):
        self.data = data
        self.message = message
        super().__init__(self.data + " => "+self.message)


class ExceptionInvalidBoolValue(Exception):
    def __init__(self, data, message="invalid bool value"):
        self.data = data
        self.message = message
        super().__init__(self.data + " => "+self.message)
