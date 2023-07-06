print("----------------------------------------------------------------------------------------------------------------")
print("|                             W E L C O M E   T O  T H E  P R O J E C T                                        |")
print("|                                      TO CHECK EMAIL VALIDATION                                               |")
print("|                                                                                                              |")
print("|                                                                                                              |")
print("|                                                                                                              |")
print("----------------------------------------------------------------------------------------------------------------")
play = 1
while (play == 1):
    email = input("Enter your Email: ")
    space = 0
    upr = 0
    other = 0
    if len(email) >= 6:
        if email[0].isalpha():
            if ('@' in email) and (email.count('@') == 1):
                if (email[-3] == '.') ^ (email[-4] == '.'):
                    for i in email:
                        if i == ' ':
                            print("There should no free spaces")
                            space = 1
                        elif i.isalpha():
                            if i == i.upper():
                                print("There should no UPPER case letter")
                                upr = 1
                        elif (i.isdigit()) or (i == '_' or i == '.' or i == '@'):
                            continue  # skip digits / special symbol if any
                        else:
                            print("There should no any special symbol")
                            other = 1

                    if space == 1 or upr == 1 or other == 1:

                        print("XXXXXXXXX Wrong Email XXXXXXXXX")
                    else:
                        print("-- Y O U  E N T E R E D  R I G H T  E M A I L--")

                else:
                    print("X Wrong Email X   ")
                    print("(.) must be 3rd or forth last symbol")
            else:
                print("X Wrong Email X   ")
                print("There must be @ symbol")
        else:
            print("X Wrong Email X   ")
            print("First character should not in upper case")
    else:
        print("X Wrong Email X  ")
        print("Length is too short")
    play = int(input("Press 1 to TRY AGAIN and 0 to EXIT: "))
