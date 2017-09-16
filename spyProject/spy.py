print "Let's get started"
spy_name=raw_input("Provide your name here: ")
if len(spy_name)>0:
    spy_salutation=raw_input("Provied your salutation Mr./Mrs./Miss: ")
    if len(spy_salutation)>0:
        spy_name=spy_salutation+" "+spy_name
        spy_age=0
        spy_rating=0.0
        spy_online=False
        spy_age=int(raw_input("Enter your age: "))
        if spy_age>12 and spy_age<50:
            spy_rating=float(raw_input("Enter rating: "))
        else:
            "You are not in age to be a spy"
    else:
        print "Print a valid salutation"
else:
    print "Invalid name, please try again!"

print "Hello "+spy_name+" Your age is "+str(spy_age)+ " Your rating is "+str(spy_rating)
