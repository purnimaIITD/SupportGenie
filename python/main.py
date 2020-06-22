from Agent import Agent
from Issue import Issue
from datetime import date
from utils import *

# Master agent - Knows everything - has been free the least
a0 = Agent ('X', True, date.today(), ['hindi', 'english', 'spanish', 'french', 'chinese', 'tamil'])
# List of agents
a1 = Agent('A', True, date(2020,5,1), ['hindi','english','spanish'] )
a2 = Agent('B', True, date(2020,5,1), ['hindi', 'french', 'english'])
a3 = Agent('C', True, date(2020,6,3), 'french')
a4 = Agent('D', True, date.today(), ['chinese', 'tamil', 'spanish'])
a5 = Agent('E', True, date.today(), ['chinese', 'french', 'english'])
a6 = Agent('M', False, "NA", ['spanish', 'french', 'english'])
a7 = Agent('N', False, 'NA' , ['tamil', 'french', 'english'])
a8 = Agent('O', False, '', ['chinese', 'french', 'hindi'])
# Master agent - Knows everything - has been free the longest
a9 = Agent ('Z', True, date(2020,1,1), ['hindi', 'english', 'spanish', 'french', 'chinese', 'tamil'])

agentList = [a0,a1,a2,a3,a4,a5,a6,a7,a8,a9]

testIssue = Issue(['french'])

agent = allocateAgents(testIssue, agentList, 'random')

if type(agent) is list:
    print("Following agents are available for this issue:")
    for a in agent:
        print(a)
else:
    print("The algorithm has selected the following Agent:")
    print(agent)
    
# TODO
    #print("Kindly check and confirm the allotment to make necessary updation")
