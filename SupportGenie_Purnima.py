
# coding: utf-8

# In[1]:

###################### Problem Definition ###########################
#####################################################################
# Agent 
# is_available - true / false
# available_since - num of days
# roles - list of spanish speaker, sales, support, marketing etc

# Issue - list of roles required

# Agent Selection Mode - allAvailable / least busy / random
# allAvailable - whoever matches with the issue's roles
# leastBusy - agent who has been free the longest
# random 

# Process to be followed #
# 1. Find the list of Agents that match for the Issue - suitableAgents
# 2. Based on the Agent Selection Mode - find the agent / list of Agents the issue should be presented to

##################################################################################################
# Lets' imagine an agency that provides (agents) translators for diff languages                  #
# Therefore the agents roles (skills) herein - is based on what all languages the agent knows    #
# When a job / issue comes in - then the agent is matched based on role and agent selection mode #
##################################################################################################


# In[2]:

#agent = [string name, bool isAvailable, date availableSince, list roleList]
import datetime
from datetime import date, timedelta

class Agent:
    
    def __init__(self, name, isAvailable, availableSince, roleList):
        self.name = name
        self.isAvailable = isAvailable
        
        # If the agent is not Available, then availableSince value is not valid
        if (isAvailable):
            self.availableSince = availableSince
        else:
            self.availableSince = datetime.MAXYEAR
            
        # Assuming roleList will be either a list of roles (list) or a single role (string)
        if (isinstance(roleList, list)):
            self.roleList = roleList
        else: 
            self.roleList = [roleList]
            
    def __repr__(self):
        return repr((self.name, self.isAvailable, self.availableSince, self.roleList))
        
    def numDaysFree(self):
        if (self.isAvailable):
            return "The agent [" + self.name + "] has been available for " + str(date.today() - self.availableSince)
        else:
            return "The agent [" + str(self.name) + "] is currently not available."
        
    # Set isAvailable Status to True   
    def setAvailabilityToTrue(self):
        self.isAvailable = True
        self.availableSince = date.today()

    # Set isAvailable Status to False   
    def setAvailabilityToFalse(self):
        self.isAvailable = False
        self.availableSince = datetime.MAXYEAR
        
    # Add role to roleList
    # TODO - Update to append List after checking for duplicate entries
    def addRole(self, role):
        if (role in self.roleList):
            print(role + " already present. Hence not adding again.")            
        else:
            self.roleList.append(role)
        
    # Delete role from roleList
    def deleteRole(self, role):
        if (role in self.roleList):
            self.roleList.remove(role)
        else:
            print(role + " not present. Hence not deleting.")            
        
# Update isAvailable with availableSince date
# isAvailable should ONLY be updated using the methods not otherwise (to ensure correct updation of availableSince)


# In[3]:

# List of agents
a1 = Agent('A', True, date(2020,5,1), ['hindi','english','spanish'] )
a2 = Agent('B', True, date(2020,5,1), ['hindi', 'french', 'english'])
a3 = Agent('C', True, date(2020,6,3), 'french')
a4 = Agent('D', True, date.today(), ['chinese', 'tamil', 'spanish'])
a5 = Agent('E', True, date.today(), ['chinese', 'french', 'english'])
a6 = Agent('M', False, "NA", ['spanish', 'french', 'english'])
a7 = Agent('N', False, 'NA' , ['tamil', 'french', 'english'])
a8 = Agent('O', False, '', ['chinese', 'french', 'hindi'])

# Master agent - Knows everything - has been free the least
a0 = Agent ('X', True, date.today(), ['hindi', 'english', 'spanish', 'french', 'chinese', 'tamil'])

# Master agent - Knows everything - has been free the longest
a9 = Agent ('Z', True, date(2020,1,1), ['hindi', 'english', 'spanish', 'french', 'chinese', 'tamil'])

########## Agent Test Cases #########
# Scenario's Tested:
# Not available
# Available from today itself
# Available since long
# addRole - when role is present / not present in the roleList
# deleteRole - when role is present / not present in the roleList
#####################################
print(a8.numDaysFree())    # Not available
print(a0.numDaysFree())    # Available from today
print(a9.numDaysFree())    # Available since long

#addRole - one at a time
a3.addRole('french')       # role is present
print(a3.roleList)
a3.addRole('hindi')        # new role
print(a3.roleList)

#deleteRole
a3.deleteRole('english')   # role is not present
print(a3.roleList)
a3.deleteRole('hindi')     # role is present
print(a3.roleList)


# In[4]:

class Issue:
    
    # instance attributes
    def __init__(self, roleList):
        self.date = date.today()
        self.roleList = roleList
    
    # Add role to roleList
    def addRole(self, role):
        if (role in self.roleList):
            print(role + " already present. Hence not adding again.")            
        else:
            self.roleList.append(role)
        
    # Delete role from roleList
    def deleteRole(self, role):
        if (role in self.roleList):
            self.roleList.remove(role)
        else:
            print(role + " not present. Hence not deleting.")            
        


# In[5]:

# Issue - Initialization Testing

roleList = ['english', 'spanish']        
issue1 = Issue(roleList)

issue2 = Issue(['english','spanish', 'gujrati'])

# Issue updation - Adding 
issue1.addRole('english')   # Already present
print(issue1.roleList)
issue1.addRole('tamil')     # New
print(issue1.roleList)

# Issue updation - Deleting
issue1.deleteRole('hindi')  # not present
print(issue1.roleList)
issue1.deleteRole('tamil')  # present
print(issue1.roleList)


# In[10]:

import random

# Find Agents suitable for the Issue
# i.e. the ones who are available & has the required skillSet
def findSuitableAgents(issue, agentList):
    #Make a list of available Agents
    availableAgents = []
    for agent in agentList:
        if agent.isAvailable:
            availableAgents.append(agent)
            #print(agent.name)
            
    if(len(availableAgents) == 0):
        print("Sorry no available agents. Check with admin.")
        return
    
    # From the availableAgents, find the suitableAgents for the issue
    # i.e. check whose roleList matches with issue's roleList
    suitableAgents = set() # This is a Set not a list - to avoid duplication
    #print(type(suitableAgents))
    
    for agent in availableAgents:
        # Pick 1 agent from the list

        #DEBUG: print("============ Checking for Agent: " + agent.name + "===================")
        #DEBUG: print(agent.roleList)
        
        for role in issue.roleList:
        # iterate through the issue Role list & check if the current agent is suitable
        # if yes - add that to the suitableAgent Set

            #DEBUG: print("Checking for " + role)            
            if role in agent.roleList:
                #DEBUG: print("Matched")
                suitableAgents.add(agent)
            else:
                suitableAgents.discard(agent)
                #DEBUG: print("not matched - Discarding")
                break
       
    return suitableAgents

def allocateAgents(issue, agentList, agentSelectionMode):
        
    allocatedAgent = None    
        
    # Find Suitable Agents
    suitableAgents = findSuitableAgents(issue, agentList)
    print(str(len(suitableAgents)) + " Suitable Agents found")
    
    if (len(suitableAgents) == 0):
        print("No Agents found for the issue. Please try again.")
        return allocatedAgent
    else:
        sortedAgentList = sorted(suitableAgents, key=lambda agent: agent.availableSince)
        #DEBUG - print (sortedAgentList)
        
    # Based on agentSelectionMode - select an agent.
    if (agentSelectionMode.lower() == "random"):
        #DEBUG: print("Random Selection Mode")
        allocatedAgent = sortedAgentList[random.randint(0,len(sortedAgentList))]
    elif (agentSelectionMode.lower() == "leastBusy".lower()):
        #DEBUG - print("least Busy Mode")
        allocatedAgent = sortedAgentList[0]
    elif (agentSelectionMode.lower() == "allAvailable".lower()):
        #DEBUG: print("all Available Mode")
        allocatedAgent = sortedAgentList
    else:
        print("You entered: "+agentSelectionMode.strip().lower())
        print("enter a valid Agent Selection Mode: allAvailable | leastBusy | random")
        
    return allocatedAgent


# In[12]:

agentList = [a0,a1,a2,a3,a4,a5,a6,a7,a8,a9]

testIssue = Issue(['french'])

agent = allocateAgents(testIssue, agentList, 'random')

if type(agent) is list:
    print("Following agents are available for this issue:")
    for a in agent:
        print(a)
elif type(agent) is Agent:
    print("The algorithm has selected the following Agent:")
    print(agent)
    
# TODO
    #print("Kindly check and confirm the allotment to make necessary updation")


# In[ ]:



