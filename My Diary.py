import textwrap             # module-to-display-output-as-paragraph
count = 5                   # number-of-tries-to-guess-password
while count != 0:
    pwd = input("Please enter password to access: ")
    if pwd == "your name":
        print("\n===WELCOME TO YOUR OWN DIARY===")
        print("\nHere you can write anything you want, anyway you want, without any interruption whatsoever.")
        print("\nNow, what do you want to do?")
        print("\n*****MAIN MENU*****")
        print("1. Write a new entry(s)")
        print("2. Access a previous entry")
        print("3. Modify a previous entry")
        print("4. Delete a previous entry")
        print("5. Print all entries")
        print("6. Delete all entries")


        def new_entry():        # function-to-write-new-entries
            num = int(input("\nDo you want to make a single entry or multiple entries: "))
            if num > 1:
                for i in range(num):
                    diary = open("diary.txt", "a")
                    diary.write("\nYour Entry: ")
                    date = input("\nEnter your date: ")
                    entry = input("\nEnter your entry: ")
                    diary.write(date + " - " + entry + "\n")
            else:
                diary = open("diary.txt", "a")
                diary.write("\nYour Entry: ")
                date = input("\nEnter your date: ")
                entry = input("\nEnter your entry: ")
                diary.write(date + " - " + entry + "\n")


        def read_entry():       # function-to-read-a-specific-entry
            diary = open("diary.txt", "r")
            lines = diary.readlines()
            entries = []
            print("\n(Psst. If you cannot remember a certain date or keyword of an entry, "
                  "just type can't remember or don't remember)")
            date = input("\nEnter date of entry you wish to access: ")

            if date == "can't remember" or date == "don't remember":
                key_word = input("\nThat's okay! Enter specific key word(s) of entry you wish to access: ")
                if key_word == "can't remember" or key_word == "don't remember":
                    print("\nHere are all your entries to alleviate your confusion: ")
                    all_entry()
                else:
                    for line in lines:
                        if key_word in line:
                            entries.append(line)
                        else:
                            continue

                    for i in range(len(entries)):
                        output = textwrap.fill(entries[i], width=125)
                        print(output)

            else:
                for line in lines:
                    if date in line:
                        entries.append(line)
                    else:
                        continue

                for i in range(len(entries)):
                    output2 = textwrap.fill(entries[i], width=125)
                    print(output2)

            diary.close()


        def mod_entry():        # function-to-modify-a-specific-entry
            diary = open("diary.txt", "r")
            lines = diary.readlines()
            entries = []
            print("\nDo you want to modify: ")
            print("1. A specific portion of an entry")
            print("2. The entire entry")
            want = int(input("\nEnter your choice: "))
            if want == 1:
                print("\n(Psst. If you cannot remember a certain date or keyword of an entry, "
                      "just type can't remember or don't remember)")
                date = input("\nEnter date of entry you wish to modify: ")

                if date == "can't remember" or date == "don't remember":
                    key_word = input("\nThat's okay! Enter specific key word(s) of entry you wish to modify: ")
                    if key_word == "can't remember" or key_word == "don't remember":
                        print("\nHere are all your entries to alleviate your confusion: ")
                        all_entry()
                        mod_entry()
                    else:
                        for line in lines:
                            if key_word in line:
                                entries.append(line)
                            else:
                                continue

                        for i in range(len(entries)):
                            output3 = textwrap.fill(entries[i], width=125)
                            print(output3)

                        rep1 = input("\nEnter the specific key word(s) of the previous entry that you wish to modify: ")
                        mod1 = input("\nEnter your modification: ")
                        mod_diary = open("diary.txt", "w")

                        for line in lines:
                            if rep1 not in line.rstrip():
                                mod_diary.write(line)
                            else:
                                line = line.replace(rep1, mod1)
                                mod_diary.write(line)
                        mod_diary.close()

                else:
                    for line in lines:
                        if date in line:
                            entries.append(line)
                        else:
                            continue

                    for i in range(len(entries)):
                        output4 = textwrap.fill(entries[i], width=125)
                        print(output4)

                    rep2 = input("\nEnter the specific key word(s) of the entry you wish to modify: ")
                    mod2 = input("\nEnter your modification: ")
                    mod_diary = open("diary.txt", "w")
                    for line in lines:
                        if rep2 not in line.rstrip():
                            mod_diary.write(line)
                        else:
                            line = line.replace(rep2, mod2)
                            mod_diary.write(line)
                    mod_diary.close()

            elif want == 2:
                print("\n(Psst. If you cannot remember a certain date or keyword of an entry, "
                      "just type can't remember or don't remember)")
                date = input("\nEnter date of entry you wish to modify: ")

                if date == "can't remember" or date == "don't remember":
                    key_word = input("\nThat's okay! Enter specific key word(s) of entry you wish to modify: ")
                    if key_word == "can't remember" or key_word == "don't remember":
                        print("\nHere are all your entries to alleviate your confusion: ")
                        all_entry()
                        mod_entry()
                    else:
                        for line in lines:
                            if key_word in line:
                                entries.append(line)
                            else:
                                continue

                        for i in range(len(entries)):
                            output5 = textwrap.fill(entries[i], width=125)
                            print(output5)

                        mod = input("\nEnter your modification with date: ")
                        mod_diary = open("diary.txt", "w")

                        for line in lines:
                            if key_word not in line.rstrip():
                                mod_diary.write(line)
                            else:
                                mod_diary.write("\nYour Entry: ")
                                line = line.replace(line, mod)
                                mod_diary.write(line + "\n")
                        mod_diary.close()

                else:
                    for line in lines:
                        if date in line:
                            entries.append(line)
                        else:
                            continue

                    for i in range(len(entries)):
                        output6 = textwrap.fill(entries[i], width=125)
                        print(output6)

                    key_word = input("\nEnter the key word(s) of the specific entry you wish to modify: ")
                    mod = input("\nEnter your modification with date: ")
                    mod_diary = open("diary.txt", "w")
                    for line in lines:
                        if key_word not in line.rstrip():
                            mod_diary.write(line)
                        else:
                            mod_diary.write("Your Entry: ")
                            line = line.replace(line, mod)
                            mod_diary.write(line + "\n")
                    mod_diary.close()


        def del_entry():        # function-to-delete-a-specific-entry
            diary = open("diary.txt", "r")
            lines = diary.readlines()
            entries = []
            print("\n(Psst. If you cannot remember a certain date or keyword of an entry, "
                  "just type can't remember or don't remember)")
            date = input("\nEnter date of entry you wish to delete: ")

            if date == "can't remember" or date == "don't remember":
                key_word = input("\nThat's okay! Enter specific key word(s) of entry you wish to delete: ")
                if key_word == "can't remember" or key_word == "don't remember":
                    print("\nHere are all your entries to alleviate your confusion: ")
                    all_entry()
                    del_entry()
                else:
                    for line in lines:
                        if key_word in line:
                            entries.append(line)
                        else:
                            continue

                    for i in range(len(entries)):
                        output7 = textwrap.fill(entries[i], width=125)
                        print(output7)

                    key_word = input("\nEnter specific key word(s) of the previous entry that you wish to delete: ")
                    del_diary = open("diary.txt", "w")
                    for line in lines:
                        if key_word not in line.rstrip():
                            del_diary.write(line)
                        else:
                            print("\nEntry Successfully Deleted.")
                    del_diary.close()

            else:
                for line in lines:
                    if date in line:
                        entries.append(line)
                    else:
                        continue

                for i in range(len(entries)):
                    output8 = textwrap.fill(entries[i], width=125)
                    print(output8)

                key_word = input("\nEnter specific key word(s) of the entry you wish to delete: ")
                del_diary = open("diary.txt", "w")
                for line in lines:
                    if key_word not in line.rstrip():
                        del_diary.write(line)
                    else:
                        print("\nEntry Successfully Deleted.")
                del_diary.close()


        def all_entry():        # function-to-print-all-entries
            diary = open("diary.txt", "r")
            lines = diary.readlines()
            for line in lines:
                read = textwrap.fill(line, width=125)
                print(read)


        def clear_entry():      # function-to-delete-all-entries
            diary = open("diary.txt", "r+")
            diary.truncate()
            print("\nAll entries successfully deleted. Thank you!")
            diary.close()


        choice = int(input("\nEnter Your Choice: "))        # choice-for-main-menu
        if choice == 1:                                     # calling-functions
            new_entry()

        elif choice == 2:
            read_entry()

        elif choice == 3:
            mod_entry()

        elif choice == 4:
            del_entry()

        elif choice == 5:
            all_entry()

        elif choice == 6:
            clear_entry()

        else:
            print("\nSorry. Choice invalid.")

        break


    elif pwd == "forgot password" or pwd == "forgot":
        print("\nYour password is your name. Try again.")
        break


    else:
        count = count - 1
        if count == 0:
            print("\nWrong password. You are not allowed access to the diary. Please try later.")
            print("\nA hint: your password is your name.")
        else:
            print("\nWrong password. Access Denied. Try again.")
            print("You have", count, "tries left.")
            print("\n")
