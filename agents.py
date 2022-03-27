class ToilletPaperAg():

    def __init__(self,env) -> None:
        self.env = env
        self.price_average = 0
        self.current_percepts = env.initial_percepts()
        self.usage_average = self.current_percepts['tpnumber']
        self.usage = self.current_percepts['tpnumber']
        self.age = 0
        self.usage_std = 0
        self.to_buy = 0
        self.spendings = 0 

    def act(self):
         
        tpnumber_t_1 = self.current_percepts['tpnumber'] 
        
        self.usage_std = 100

        if self.current_percepts['price'] <= (10 + self.current_percepts['clock']*0.01 + 0.5):
            if self.current_percepts['tpnumber'] < (self.current_percepts['max_capacity']*0.5):
                self.to_buy = max((self.usage_average + self.usage_std*4 - self.current_percepts['tpnumber'])*2,0)                
            else:
                self.to_buy = max((self.usage_average + self.usage_std*4 - self.current_percepts['tpnumber'])*1.7,0)
        elif self.current_percepts['price'] <= (10 + self.current_percepts['clock']*0.01 + 1):
            if self.current_percepts['tpnumber'] < (self.current_percepts['max_capacity']*0.5):
                self.to_buy = max((self.usage_average + self.usage_std*4 - self.current_percepts['tpnumber'])*1.5,0)                
            else:
                self.to_buy = max((self.usage_average + self.usage_std*4 - self.current_percepts['tpnumber'])*1.2,0)
        else:
            self.to_buy = max((self.usage_average + self.usage_std*4 - self.current_percepts['tpnumber']),0)


        self.spendings = self.to_buy * self.current_percepts['price']

        action = {'to_buy':self.to_buy}
        
        self.current_percepts = self.env.change_state(action)
        self.age += 1
        
        tpnumber_t = self.current_percepts['tpnumber']
        
        self.usage = tpnumber_t_1 + self.to_buy - tpnumber_t 
        self.usage_average = (self.usage_average * (self.age - 1) + self.usage)/self.age