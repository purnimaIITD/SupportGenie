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

#########
# Create a list of Agents 
# agent = Agent(String name, bool isAvailable, date availableSince, list roleList)
# Example: 
# a0 = Agent ('X', True, date.today(), ['hindi', 'english', 'spanish', 'french', 'chinese', 'tamil'])
# a9 = Agent ('Z', False, date(2020,1,1), ['hindi', 'english', 'spanish', 'french', 'chinese', 'tamil'])
# agentList = [a0, a9]
#########

#########
# Create a Issue with appropriate roles
# issue = Issue(list roleList)
# Example: 
# testIssue = Issue(['french','hindi'])
#########

#########
# Call the allocateAgents method from utils - to get the Solution
# allocateAgents(Issue, list[Agent], agentSelectionMode)
# where agentSelectionMode: allAvailable | random | leastBusy
# Example:
# agent = allocateAgents(testIssue, agentList, 'allAvailable')
#########

# TODO - Uncomment the following to print the solution on the prompt- 
'''
if type(agent) is list:
    print("Following agents are available for this issue:")
    for a in agent:
        print(a)
elif type(agent) is Agent:
    print("The algorithm has selected the following Agent:")
    print(agent)
'''
