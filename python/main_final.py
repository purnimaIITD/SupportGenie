from Agent import Agent
from Issue import Issue
from datetime import date
from utils import *

from csv import reader

##################################################################
# Agent(String name, bool isAvailable, date availableSince, list roleList)
# Issue(list roleList) 
# agentSelectionMode: allAvailable | random | leastBusy
# allocateAgents(Issue, list[Agent], agentSelectionMode)
####################################################################
customAgentList = str(input("""=======================
Welcome to the Language Agent allocation system.
We have many agents proficient in many languages.
Based on your Issue - this Algorithm will allocate suitable Agents (from the List).
Would you like to enter a custom Agent list? (Yes / No)
""" ))

agentFile = "defaultAgentList.csv"
if (customAgentList.lower() == 'yes'):
	print("""The agent CSV file format should be: 
	String name, bool isAvailable, date availableSince, role1, role2, role3 ...""")
	print("""Example: 
	A, True, date(2020,5,1), hindi, english, french
	B, False, date.today(), spanish, chinese, tamil
	""")
	agentFile = str(input("Enter the file name containing Agent details in CSV format: "))

agentList = []
with open(agentFile, 'r') as f:
	reader = reader(f)
	for row in reader:
		# 1 Agent information - parse and make a agent - append to agentList
		# DEBUG - print(row)
		# Check the length - parse
		# first element as name
		name = str(row[0].strip())
		# second element as isAvailable
		if (row[1].strip() == 'T'):
			isAvailable = True
		elif(row[1].strip() == 'F'):
			isAvailable = False
		# third element as date
		if (isAvailable):
			csvDate = row[2].split("/")
			day = int(csvDate[0].strip())
			month = int(csvDate[1].strip())
			year = int(csvDate[2].strip())
			availableSince = date(year, month, day)
		else:
			availableSince = "NA"
		# and elements after that - add as roles
		roleList = []
		for i in range(3, len(row)):
			roleList.append(row[i].strip().lower())
			
		# make a Agent element and add to agentList
		agent = Agent(name, isAvailable, availableSince, roleList)
		print(agent)
		agentList.append(agent)
		print("==============================================================")
		

print("Above mentioned " + str(len(agentList)) + " number of agents are available with the system.")
print("")
print("Kindly enter your issue details - for us to allocate appropriate Agent.")

# Getting Issue Details from command prompt
issueList = []
n = int(input("How many roles does the current Issue have? "))

print("Kindly enter them below, one at a time, preferably in lower case")
# Reading the issueList
for i in range(0,n):
	role = str(input())
	issueList.append(role.strip().lower())

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
