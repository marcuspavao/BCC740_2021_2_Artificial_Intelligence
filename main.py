from environments import ToilletPaperEnv
from agents import ToilletPaperAg

env1 = ToilletPaperEnv(10,2000,10000)

env2 = ToilletPaperEnv(10,2000,5000)

agent = ToilletPaperAg(env1)

for i in range(1000):
    env1.change_state((agent.act()))
