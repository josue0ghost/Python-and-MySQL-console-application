"""
    TODO:
    *   Sign up [x]
        -   Insert into DB
    *   Sign in [x]
        -   Identify user
    *   Create, Read, Delete grades [x]
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