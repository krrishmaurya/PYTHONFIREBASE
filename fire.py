import pyrebase 
firebaseConfig={

  # add apis here from firebase website #
}
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()


#sigin#
def signup():

    print("Sign up...")
    email = input("Enter email: ")
    password=input("Enter password: ")
    try:
        user = auth.create_user_with_email_and_password(email, password)
        ask=input("Do you want to login?[y/n]")
        if ask=='y':
            login()
    except: 
        print("Email already exists")
    return

 

#login
def login():
    print("Log in...")
    email=input("Enter email: ")
    password=input("Enter password: ")
    try:
        login = auth.sign_in_with_email_and_password(email, password)
        print("Successfully logged in!")
        
    except:
        print("Invalid email or password")
    return









#main

ans=input("Are you a new user?[y/n]")

if ans == 'n':
    login()
elif ans == 'y':
    signup()

