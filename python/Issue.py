from datetime import date

# Issue - list of roles / skills required - to solve the issue

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
