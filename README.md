# SupportGenie
SupportGenie's Problem Statement (refer the pdf file attached) 
My Solution for the 2nd Problem Set.
Author: Purnima (purnima.iitd2003@gmail.com)

# Problem Statement:
Agent selector
You are given the following data for agents
agent
- is_available
- available_since (the time since the agent is available)
- roles (a list of roles the user has, e.g. spanish speaker, sales, support etc.)

When an issue comes in we need to present the issue to 1 or many agents based on an agent
selection mode. An agent selection mode can be 
- all available: the issue is presented to all agents so they pick the issue if they want.
- least busy: the issue is presented to the agent that has been available for the longest. 
- random: we randomly pick an agent. 

An issue also has one or many roles (sales/support e.g.).

Issues are presented to agents only with matching roles. Please write a function that takes an input the list of agents with their data, agent selection mode and returns a list of agents the issue should be presented to.

# Solution Assumption:
The test cases that I have made and the basic underlying assumption to solve this initially is:
  - Lets' imagine an agency that provides (agents) translators for diff languages                  
  - Therefore the agents roles (skills) herein - is based on what all languages the agent knows    
  - When a job / issue comes in - then the agent is matched based on role and agent selection mode 
But the program should be able to work with any other set of roles as well - just that the roles have been considered as String and preferably in lower case.

# To Execute
## Option1 - Jupyter Notebook:
The Solution file (./SupportGenie_Purnima.ipynb) is compatible with Jupyter Notebook & can be executed using that.

## Option2 - Command Line Interactive:
Execute the file main_final.py
#### python main_final.py
and follow the command line arguments.
Please note - there's a defaultAgentList.csv already present - so for testing - you can use that too.
Or else do feel free to create another. Enjoy!

## Option3 - Command Line Interactive:
If you don't wish to enter the agentList and just wish to play with the Issue's role List & agent selection mode - execute:
#### python main_cmd.py

## Option4 - Basic:
Or you can just execute the basic main.py and code a customised one (based on main_template.py) - for direct execution. 
#### python main.py

