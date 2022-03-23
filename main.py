from environments import ToilletPaperEnv
from agents import ToilletPaperAg

env1 = ToilletPaperEnv(10,2000,10000)

env2 = ToilletPaperEnv(10,2000,5000)

agent = ToilletPaperAg(env1)

for i in range(1000):
<<<<<<< HEAD
    env1.change_state((agent.act()))
=======
    env1.chage_state(agent.act())
>>>>>>> 5ab7d645b51db1f23375a7d8cb63eab7dce368c9
