import users.user as user

class Actions:
    def signup(self):
        print("Selected item: signup")
        name =      input("Your name: ")
        lastname =  input("Your last name: ")
        email =     input("Your email: ")
        password =  input("Choose a password: ")

        newUser = user.User(name, lastname, email, password)
        reg = newUser.register()

        if reg[0] >= 1:
            print(f"{reg[1].name}, you've been registered with email {reg[1].email}")
        else:
            print("Registration failed")
    
    def signin(self):
        
        try:
            email =     input("Email: ")
            password =  input("Password: ")

            existingUser = user.User('', '', email, password)
            login = existingUser.identify()

            # id | name | lastname | email | password | date
            if email == login[3]: 
                print(f"Welcome, {login[1]}")
        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print("Login failed")
    