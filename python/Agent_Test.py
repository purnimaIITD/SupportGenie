from Agent import Agent
from datetime import date

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