import numpy as np

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

        self.to_buy = max(self.usage_average + self.usage_std*4 - self.current_percepts['tpnumber'],0) 
        self.spendings = self.to_buy * self.current_percepts['price']

        action = {'to_buy':self.to_buy}
        
        self.current_percepts = self.env.change_state(action)
        self.age += 1
        
        tpnumber_t = self.current_percepts['tpnumber']
        
        self.usage = tpnumber_t_1 + self.to_buy - tpnumber_t 
        self.usage_average = (self.usage_average * (self.age - 1) + self.usage)/self.age

class MazeAgent():

    def __init__(self,env):
        self.env = env
        self.percepts = env.initial_percepts()
        self.F = [[self.percepts['position']]]

    def act(self):

        while self.F:
            path = self.F.pop(-1)

            self.percepts = self.env.change_state({'path':path.copy()})

            if self.percepts['goal']:
                break
            else:
                for n in self.percepts['available_neighbors']:
                    if n not in path:
                        self.F.insert(0,path + [n])

        self.env.run()


class MazeAgentBranchAndBound():

    def __init__(self,env,bound):
        self.env = env
        self.percepts = env.initial_percepts()
        self.F = [[self.percepts['position']]]
        self.cs = [0]
        self.hs = [self.heuristic(self.percepts['position'],self.percepts['goal'])]
        self.bound = bound
        self.best_path = []
        self.best_path_cost = np.inf

    def heuristic(self,point,goal):
        return np.linalg.norm(np.array(point)-np.array(goal),ord=1)

    def act(self):

        while self.F:
            path = self.F.pop(0)
            cost = self.cs.pop(0)
            h = self.hs.pop(0)

            if (cost + h) < self.bound:  

                self.percepts = self.env.change_state({'path':path.copy()})
            
                if self.percepts['goal']:
                    if cost < self.best_path_cost:
                        self.best_path_cost = cost
                        self.best_path = path.copy()
                        self.bound = cost
                else:
                    for n in self.percepts['available_neighbors']:
                        if n not in path:
                            self.F.insert(0,path + [n])
                            self.cs.insert(0,len(path)+1)
                            self.hs.insert(0,self.heuristic(n,self.percepts['goal']))

        self.env.draw_best(self.best_path)