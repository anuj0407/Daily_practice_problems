'''
Task: Use map() and a lambda function to take a list of names 
and return them in "Title Case" (e.g., ["alice", "BOB"] becomes ["Alice", "Bob"]).
'''

name_list = ["alice" , "BOB"]
print("List : ",name_list)

# Changing string in list to title case
title_list = list(map(lambda x: x.title(),name_list))
print("List in title case : ",title_list)
