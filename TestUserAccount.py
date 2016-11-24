#This script performs some simple tests on the UserAccount class.
from UserAccount import *

#Two things are missing from the line below - fill them in
my_user=UserAccount("user" ,"123" ,"secret" )

#Call the print_password method (function) - it takes one input - a guess for the password.
my_user.print_password("12345")
#Use the wrong password as input here
my_user.password=12345

#Use the right password here
my_user.password=123
