# Agent 
# is_available - true / false
# available_since - num of days
# roles - list of spanish speaker, sales, support, marketing etc

#agent = [string name, bool isAvailable, date availableSince, list roleList]

import datetime
from datetime import date, timedelta

class Agent:
    
    def __init__(self, name, isAvailable, availableSince, roleList):
        self.name = name
        self.isAvailable = isAvailable
        
        # If the agent is not Available, then availableSince value is not applicable - hence using MAXYEAR
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

