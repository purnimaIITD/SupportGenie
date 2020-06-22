# SupportGenie
My SupportGenie's Problem Statement Solutions
Author: Purnima (purnima.iitd2003@gmail.com)

# Question2:
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

# Solution:
Lets' imagine an agency that provides (agents) translators for diff languages                  
Therefore the agents roles (skills) herein - is based on what all languages the agent knows    
When a job / issue comes in - then the agent is matched based on role and agent selection mode 

# To Execute
Option1:
The Solution file (SupportGenie_Purnima.ipynb) is compatible with Jupyter Notebook & can be executed using that.
Option2:
In the folder 'python' - you can customise your main.py and execute that on the command prompt
$ python main.py
Option3:
If you prefer the command line entry of Issue's role List & agent selection mode - in the folder python execute:
$ python main_cmd.py

