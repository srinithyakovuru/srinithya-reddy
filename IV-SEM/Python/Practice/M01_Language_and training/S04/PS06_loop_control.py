

#usename and password  validation with loop control statements 3 iterations
username="nithya"
password="nithya567"
for i in range(3):
    username=input("Enter a username:")
    password=input("Enter a password:")
    if username==username and password==password:
        print("Login successful")
        break
    else:
        print("Invalid username or password.Try again,")


