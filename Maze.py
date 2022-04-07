from pyamaze import maze,COLOR,agent
from environments import Maze
from agents import MazeAgentDFS, MazeAgentBranchAndBound


env = Maze(15,15)
ag = MazeAgentBranchAndBound(env,40)
#ag = MazeAgentDFS(env)
ag.act()
