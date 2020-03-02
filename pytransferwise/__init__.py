api_key = None
environment = "sandbox"


class Client(object):
    def add_resources(self):
        from pytransferwise.borderless_account import BorderlessAccount

        self.borderless_accounts = BorderlessAccount()

    def __init__(self):
        if api_key is None:
            raise KeyError("You must provide a value for pytransferwise.api_key")

        if environment not in ("sandbox", "live"):
            raise KeyError("pytransferwise.environment must be 'sandbox' or 'live'")

        self.add_resources()
