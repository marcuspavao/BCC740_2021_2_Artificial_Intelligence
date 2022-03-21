class ToilletPaperAg():

    def __init__(self,env) -> None:
        self.price_average = 0
        self.usage_average = 0
        self.current_percepts = env.initial_percepts()

    def act(self):
        pass