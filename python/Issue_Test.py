from Issue import Issue

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
