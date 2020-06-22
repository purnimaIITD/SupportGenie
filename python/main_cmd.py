from Agent import Agent
from Issue import Issue
from datetime import date
from utils import *

##################################################################
# Agent(String name, bool isAvailable, date availableSince, list roleList)
# Issue(list roleList) 
# agentSelectionMode: allAvailable | random | leastBusy
# allocateAgents(Issue, list[Agent], agentSelectionMode)
####################################################################

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

# Getting Issue Details from command prompt
issueList = []
n = int(input("How many roles does this Issue have? "))

print("Kindly enter them below, one at a time, preferably in lower case")
# Reading the issueList
for i in range(0,n):
	role = str(input())
	issueList.append(role)

print("The issue needs following roles: ")
print(issueList)
testIssue = Issue(issueList)

print("")
agentSelectionMode = str(input("Enter an Agent Selection Mode to proceed: allAvailable | random | leastBusy: "))

agent = allocateAgents(testIssue, agentList, agentSelectionMode)

print("")
if type(agent) is list:
    print("Following agents are available for this issue:")
    for a in agent:
        print(a)
elif type(agent) is Agent:
    print("The algorithm has selected the following Agent:")
    print(agent)
    
# TODO
    #print("Kindly check and confirm the allotment to make necessary updation")
