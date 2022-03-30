from pyamaze import maze,COLOR,agent
from environments import Maze
from agents import MazeAgent


env = Maze(12,12)
ag = MazeAgent(env)
ag.act()


#m=maze(10,10)
#m.CreateMaze() 
#a=agent(m,shape='arrow',footprints=True,color=COLOR.green)
#b=agent(m,shape='arrow',footprints=True)


#colors = [COLOR.green,COLOR.blue,COLOR.yellow]
#for c in colors:
#    path = m.path
#    m.tracePath({agent(m,shape='arrow',footprints=True,color=c):path},delay=5,kill=True)
    
#m.run()


#neighbors = m.maze_map[(10,10)]
#print(neighbors)

#available = [coordinate for coordinate in neighbors if neighbors[coordinate] == 1]

#print(available)
