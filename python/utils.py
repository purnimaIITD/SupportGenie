import random
from Issue import Issue
from Agent import Agent

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
    else:
        sortedAgentList = sorted(suitableAgents, key=lambda agent: agent.availableSince)
        #DEBUG - print (sortedAgentList)
        
    # Based on agentSelectionMode - select an agent.
    if (agentSelectionMode.lower() == "random"):
        #DEBUG: print("Random Selection Mode")
        allocatedAgent = sortedAgentList[random.randint(0,len(sortedAgentList) - 1)]
    elif (agentSelectionMode.lower() == "leastBusy".lower()):
        #DEBUG - print("least Busy Mode")
        allocatedAgent = sortedAgentList[0]
    elif (agentSelectionMode.lower() == "allAvailable".lower()):
        #DEBUG: print("all Available Mode")
        allocatedAgent = sortedAgentList
    else:
        print("You entered: "+agentSelectionMode)
        print("enter a valid Agent Selection Mode: allAvailable | leastBusy | random")
        
    return allocatedAgent
