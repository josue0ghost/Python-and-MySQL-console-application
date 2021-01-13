"""
    TODO:
    *   Sign up [ ]
        -   Insert into DB
    *   Sign in [ ]
        -   Identify user
    *   Create, Read, Delete grades [ ]
"""

# menu
print("""
    Available options:
        - signup
        - signin
""")

action = input("Write your selected item: ")

if action == "signup":
    print("Selected item: signup")
    name =      input("Your name: ")
    lastname =  input("Your last name: ")
    email =     input("Your email: ")
    password =  input("Choose a password: ")

    # Write to DB

elif action == "signin":
    print("Selected item: signin")
    email =     input("Email: ")
    password =  input("Password: ")