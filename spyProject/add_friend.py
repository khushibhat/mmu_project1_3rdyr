# importing spy and existing friends
from spy_details import Spy, friends
# importing regular expressions for proper validation
import re

# importing termcolor for colorful output
from termcolor import colored

# function to add new friends.
def add_friend():
    # using class spy
    new_friend = Spy(" ", " ", 0, 0.0)

    # ask user for name and salutation of friend
    new_friend.name = raw_input("Please add your friend's name: ")
    pattern_n = '^[a-zA-Z\s]+s'

    new_friend.salutation= raw_input("What do we call you Mr. or Ms.?: ")
    pattern_s = '^[a-zA-Z\s]+s'

    # concatination for full name
    new_friend.name = new_friend.salutation + " " + new_friend.name

    # ask for age of friend, int represents type casting in int
    new_friend.age = int(raw_input("Age? "))
    pattern_a = '^[0-9]+$'

    #ask for rating of friend, float represents type casting in float
    new_friend.rating = float(raw_input("Spy rating? "))
    pattern_r = '^[0-9]+\.[0-9]+$'

    # users input validations
    if len(new_friend.name) > 0 and new_friend.name.isdigit() == False and re.match(pattern_n,new_friend.name)!=None and re.match(pattern_s,new_friend.salutation)!=None and new_friend.age > 12 and new_friend.rating < 50 and re.match(pattern_a,new_friend.age)!=None and new_friend.salutation.isalpha() ==  True and new_friend.rating >= 0 and re.match(pattern_r,new_friend.rating)!=None:

        # add friend if conditions satisfies
        friends.append(new_friend)
        print (colored('Friend Added!', 'red'))
    else:
        print (colored('Sorry! Invalid entry. We can\'t add spy with the details you provided\n ', 'blue'))
    print (colored('Please enter the right data, don\'t make mistakes. ', 'blue'))

    # returning total no of friends.
    return len(friends)