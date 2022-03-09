'''
name = input("What is your name? ")
age = input("How old are you? ")
is_new_pacient = input("Are you new here? ")
print ("Pacients name= " + name)
print ("Pacients age= " + age)
if is_new_pacient == "Yes" :
    print (name + " is a " + "New Pacient")
else:
    if is_new_pacient == "No" :
        print (name + " is not a " + "New Pacient")

#if/else above says wether the pacient is new to the hospital or not
'''
# ------------------------------------------------------------------------
'''                                          #code below checks if user is under 18yo
age = int(input("How old are you? "))
if age >= 18:
    print ("Good to go!")
elif age < 18:
        print ("Sorry, you're too young... :(")
'''
# ------------------------------------------------------------------------
'''
print (input("Press Enter to start your Log in"))
prev_username = str(input("Choose an Username: "))
import getpass
prev_password = getpass.getpass("Enter a Password: ")            #getpass hides user password while setting it
print ("Please log in")
login_username = str(input("Insert your Username: "))
while login_username != prev_username:
    print("Sorry, wrong Username. Please try again")
    login_username = str(input("Insert your Username: "))
login_password = getpass.getpass("Insert your Password: ")
while login_password != prev_password:
    print("Sorry, wrong Password. Please try again")
    login_password = getpass.getpass("Insert your Password: ")
if login_username == prev_username and login_password == prev_password:
    print("Welcome back!")
else:
    print ("Username or Password incorrect. Please try again!")
'''
# ------------------------------------------------------------------------
'''
weight_kg = input("Insert your weight in kilograms: ")            #converts weight from kg to lb
weight_lb = float(weight_kg) * 2.205
print ("Your weight in lbs is: " + str(weight_lb))
'''
# ------------------------------------------------------------------------
                  #this is how we print multiple lines
text = '''test
of
this
feature'''
print (text)
print(text.capitalize())        #this one capitalizes the variables string
print(len(text))                #and this counts the number of its caracters
