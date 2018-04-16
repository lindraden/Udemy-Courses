#List of known users
known_users = ["Alice", "Bob", "Claire", "Dan","Emma", "Fred", "Georgie", "Harry"]

while True:
    print("Hi! My name is Travis")
    user = input("What is your name?: ").strip().capitalize()

    if user in known_users:
        print("Hello {}!".format(user))
        
        #remove user
        remove = input("Would you like to be removed from the system (y/n)?:" ).lower().strip()

        
        if remove == "y":
            known_users.remove(user)
        elif remove == "n":
            print("No problem, I didn't want you to leave anyways!")
            
    else:
        print("Hmmm I don't think I have met you yet {}".format(user))
        add_user = input("Would you like to be added to the system (y/n)?: ").strip().lower()
        if add_user == "y":
            known_users.append(user)
        elif add_user == "n":
            print("No worries, see you around!")
