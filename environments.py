from matplotlib.style import available
import numpy as np
from pyamaze import maze,agent

class ToilletPaperEnv():

    def __init__(self, price , 
        tpnumber,max_capacity) -> None:
        
        self.price = price
        self.TPNumber = tpnumber
        self.max_capacity = max_capacity
        self.clock = 0

    def initial_percepts(self) -> dict[float,int,int]:

        percepts = {'price':self.price,
                    'tpnumber': self.TPNumber,
                    'max_capacity':self.max_capacity}
        
        return percepts

    def change_state(self,action) -> dict[float,int,int]:

    
        self.TPNumber += action['to_buy']

        usage = min(1000 + np.random.randn()*100,self.TPNumber)

        self.TPNumber -= usage if usage > 0 else 0

        self.price = 10 + self.clock*0.01 + 0.5 + np.random.randn() * 0.1

        percepts = {'price':self.price,
                    'tpnumber': self.TPNumber,
                    'max_capacity':self.max_capacity}
        

        self.clock += 1

        return percepts

class Maze():
    
    def __init__(self,n,m) -> None:
        self.start = (n,m)
        self.maze  = maze(n,m)
        self.maze.CreateMaze(loopPercent=60)
        self.goal = self.maze._goal
        
    def initial_percepts(self) -> dict:

        return {'position': self.start,
                'available_neighbors':self.get_available_neighboors(self.start),
                'goal':False}

    def get_available_neighboors(self,pos):

        neighbors = self.maze.maze_map[pos]
        available = [coordinate for coordinate in neighbors if neighbors[coordinate] == 1]

        available_neighbors = []
        new_pos = list(pos)
        for a in available:
            aux = new_pos.copy()
            if a == 'N':
                aux[0] -= 1
            elif a == 'S':
                aux[0] += 1
            elif a == 'W':
                aux[1] -= 1
            elif a == 'E':
                aux[1] += 1
            available_neighbors.append(tuple(aux))

        return available_neighbors

    def change_state(self,action):

        goal = True if action['path'][-1] == self.maze._goal else False
        position = action['path'][-1]

        #self.maze.tracePath({agent(self.maze,shape='arrow',footprints=True):action['path']},kill = True,delay=5)
     
        return {'position': position,
                'available_neighbors':self.get_available_neighboors(position),
                'goal':goal}

    def run(self):
        self.maze.run()

    def draw_best(self,path):
        self.maze.tracePath({agent(self.maze,shape='arrow',footprints=True):path},kill = False,delay=5)
        self.maze.run()





