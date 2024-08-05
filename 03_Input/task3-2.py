# In our unit on variables, we wrote a program that assigns your first and your last name to 2 separate variables with suitable names and output your full name as well as your initials using one print statement.
# Modify the following code to allow the user to enter his/her first and last name.

fname = "Homer"
lname = "Simpson"

fullname = fname + " " + lname
initials = fname[:1] + lname[:1]

print(f"Hi {fullname}. Your initials are {initials}!")
