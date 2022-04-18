from pyamaze import maze,COLOR,agent
from environments import Maze
from agents import MazeAgentDFS, MazeAgentBranchAndBound, MazeAgentAStar


env = Maze(8,8)
ag = MazeAgentAStar(env)
#ag = MazeAgentBranchAndBound(env,40)
#ag = MazeAgentDFS(env)
ag.act()
