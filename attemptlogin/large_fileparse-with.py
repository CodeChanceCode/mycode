#!/usr/bin/python3

# parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0 # counter for fails
login_get = 0 #counter for get success
login_post = 0
# open the file for reading
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:

    # loop over the file
    for line in kfile:
        # if this 'fail pattern' appears in the line...
        if "- - - - -] Authorization failed" in line:
            loginfail += 1 # this is the same as loginfail = loginfail + 1
        elif "GET http" in line:
            login_get += 1
        elif "POST http" in line:
            login_post += 1


print("The number of failed log in attempts is", loginfail)

print("The number of successful get attempts is", login_post)

print("The number of successful post attempts", login_post)
