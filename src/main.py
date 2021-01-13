"""
    TODO:
    *   Sign up [ ]
        -   Insert into DB
    *   Sign in [ ]
        -   Identify user
    *   Create, Read, Delete grades [ ]
"""

from users import actions

userActions = actions.Actions()

###### MENU ######
print("""
    Available options:
        - signup
        - signin
""")

###### LOGIN ######

action = input("Write your selected item: ")

if action == "signup":
    userActions.signup()    
    # Write to DB

elif action == "signin":
    userActions.signin()