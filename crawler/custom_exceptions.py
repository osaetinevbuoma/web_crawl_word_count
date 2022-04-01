class UrlNotFoundException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class UrlNotProvidedException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
