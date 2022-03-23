class ToilletPaperAg():

    def __init__(self,env) -> None:
        self.price_average = 0
        self.usage_average = 0
        self.current_percepts = env.initial_percepts()

    def act(self):

        percepts = self.current_percepts()
        self.price = percepts.price
        self.TPNumber = percepts.tpnumber
        self.capacity = percepts.maxcapacity
        self.clock = percepts.clock

        self.usage_average = (self.TPNumber)/self.clock
        
        self.price_average = (self.price)/self.clock
        
        if self.TPNumber < (0.3*self.capacity) :      
            self.tobuy = self.capacity - self.TPNumber        

        self.clock += 1
        
        return self.tobuy
