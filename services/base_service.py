class Action:
    command = "base_service"

    def __init__(self, params):
        self.params = params

    def run_action(self):
        raise NotImplementedError
