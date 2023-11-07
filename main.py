import tableprint as tb

# Define constants
FILESYSTEM = []
DIRECTORY = []

# Define the file content
file_a_content = "The Power to Be Your Best."
file_b_content = "This program has performed an illegal operation and will be shut down."
file_c_content = "From tiny ACORNS mighty UNIX trees grow."


def file_innit():
    block = ""
    for x, y in enumerate(file_a_content, 1):
        block += y
        if x % 8 == 0 and x != 0:
            FILESYSTEM.append([block])
            block = ""
        if x == len(file_a_content):
            FILESYSTEM.append([block])
            block = ""

    DIRECTORY.append(["A", "0," + str(len(FILESYSTEM) - 1)])

    for x, y in enumerate(file_b_content, 1):
        block += y
        if x % 8 == 0 and x != 0:
            FILESYSTEM.append([block])
            block = ""
        if x == len(file_b_content):
            FILESYSTEM.append([block])
            block = ""

    DIRECTORY.append(["B", str(int(str(DIRECTORY[0][1]).split(",")[1]) + 1) + "," + str(len(FILESYSTEM) - 1)])

    for x, y in enumerate(file_c_content, 1):
        block += y
        if x % 8 == 0 and x != 0:
            FILESYSTEM.append([block])
            block = ""
        if x == len(file_c_content) and not y:
            FILESYSTEM.append([block])
            block = ""

    DIRECTORY.append(["C", str(int(str(DIRECTORY[1][1]).split(",")[1]) + 1) + "," + str(len(FILESYSTEM) - 1)])


def get_size(file):
    characters = 0
    for x, y in enumerate(DIRECTORY):
        if file == str(y[0]).casefold():
            blocks = int(str(y[1]).split(",")[1]) - (int(str(y[1]).split(",")[0])) + 1
            for z in FILESYSTEM[int(str(y[1]).split(",")[0]):int(str(y[1]).split(",")[1]) + 1]:
                for count2 in str(z):
                    if count2 != "[" and count2 != "]" and count2 != "'":
                        characters += 1
            print("File", file, "Size :", characters, "Characters,", blocks, "Blocks")
            break

    else:
        print("File Not In Filesystem")
    return 0


def read_file(file, arg):
    for x, y in DIRECTORY:
        if x == file.upper():
            if arg == "":
                for z in range(int(str(y).split(",")[0]), int(str(y).split(",")[1]) + 1):
                    print(FILESYSTEM[z])
            else:
                match arg.casefold():
                    case '/m':
                        print(FILESYSTEM[(int(str(y).split(",")[0])) + (
                                ((int(str(y).split(",")[1])) - ((int(str(y).split(",")[0])) - 1)) / 2).__floor__()])
                    case '/f':
                        print(FILESYSTEM[int(str(y).split(",")[0])])
                    case '/b':
                        print(FILESYSTEM[int(str(y).split(",")[1])])

            return
    print("File Not Found Or Incorrect Parameters")


def delete_block(file, arg):
    # noinspection PyShadowingNames
    def update_eof():
        eof = []
        temp = []
        for x, y in enumerate(FILESYSTEM):
            if str(y).count(".") == 1:
                eof.append(x)
                temp.append(x + 1)
        temp.pop(len(temp) - 1)

        DIRECTORY.clear()
        DIRECTORY.append(["A", "0," + str(eof[0])])
        DIRECTORY.append(["B", str(temp[0]) + "," + str(eof[1])])
        DIRECTORY.append(["C", str(temp[1]) + "," + str(eof[2])])

    count = 0
    if arg == "":
        print("File Not Found Or Incorrect Parameters")
        return

    for x, y in DIRECTORY:
        if x == file.upper():
            print("File", file, "before : ", end="")
            for z in range(int(str(y).split(",")[0]), int(str(y).split(",")[1]) + 1):
                print(str(FILESYSTEM[z]).replace("[", "").replace("'", "").replace("]", ""), end="")

            print("\nFile", file, "After : ", end="")
            match arg.casefold():
                case '/m':
                    temp = int(str(y).split(",")[0]) + (((int(str(y).split(", ")[0].split(",")[1])) - int(
                        str(y).split(", ")[0].split(",")[0])) / 2).__ceil__()
                    FILESYSTEM.pop(temp)
                    update_eof()
                    for z in range(int(str(y).split(",")[0]), int(str(y).split(",")[1])):
                        print(str(FILESYSTEM[z]).replace("[", "").replace("'", "").replace("]", ""), end="")

                    print()
                case '/f':
                    FILESYSTEM.pop(int(str(y).split(",")[0]))
                    update_eof()
                    for z in range(int(str(y).split(",")[0]), int(str(y).split(",")[1])):
                        print(str(FILESYSTEM[z]).replace("[", "").replace("'", "").replace("]", ""), end="")
                    print()

                case '/b':
                    FILESYSTEM.pop(int(str(y).split(",")[1]))
                    temp = str(FILESYSTEM[int(str(y).split(",")[1]) - 1]).replace("[", "").replace("'", "").replace("]",
                                                                                                                    "") + "."
                    FILESYSTEM.pop(int(str(y).split(",")[1]) - 1)
                    FILESYSTEM.insert(int(str(y).split(",")[1]) - 1, [temp])
                    update_eof()
                    for z in range(int(str(y).split(",")[0]), int(str(y).split(",")[1])):
                        print(str(FILESYSTEM[z]).replace("[", "").replace("'", "").replace("]", ""), end="")

                    print()
            break
        count += 1


def append_block(file, args, parameter):
    # noinspection PyShadowingNames
    def update_filesystem():
        eof = []
        temp = []
        for x, y in enumerate(FILESYSTEM):
            if str(y).count(".") == 1:
                eof.append(x)
                temp.append(x + 1)
        temp.pop(len(temp) - 1)

        DIRECTORY.clear()
        DIRECTORY.append(["A", "0," + str(eof[0])])
        DIRECTORY.append(["B", str(temp[0]) + "," + str(eof[1])])
        DIRECTORY.append(["C", str(temp[1]) + "," + str(eof[2])])

    if int(len(FILESYSTEM)) >= 29:
        print("No Available Space")
        return

    match args:
        case "/f":
            match file:
                case "a":
                    for x, y in DIRECTORY:
                        if file.upper() == x:
                            FILESYSTEM.insert(int(str(y).split(",")[0]), [parameter])
                            update_filesystem()
                            for z in range(int(str(DIRECTORY[0][1]).split(",")[0]),
                                           int(str(DIRECTORY[0][1]).split(",")[1]) + 1):
                                print(z + 1, ":", FILESYSTEM[z], end=" ")
                            break
                case "b":
                    for x, y in DIRECTORY:
                        if file.upper() == x:
                            FILESYSTEM.insert(int(str(y).split(",")[0]), [parameter])
                            update_filesystem()
                            for z in range(int(str(DIRECTORY[1][1]).split(",")[0]),
                                           int(str(DIRECTORY[1][1]).split(",")[1]) + 1):
                                print(z + 1, ":", FILESYSTEM[z], end=" ")
                            break
                case "c":
                    for x, y in DIRECTORY:
                        if file.upper() == x:
                            FILESYSTEM.insert(int(str(y).split(",")[0]), [parameter])
                            update_filesystem()
                            for z in range(int(str(DIRECTORY[2][1]).split(",")[0]),
                                           int(str(DIRECTORY[2][1]).split(",")[1]) + 1):
                                print(z + 1, ":", FILESYSTEM[z], end=" ")
                            break
        case "/m":
            match file:
                case "a":
                    for x, y in DIRECTORY:
                        if file.upper() == x:
                            midpoint = ((int(str(DIRECTORY[0][1]).split(",")[1]) - int(
                                str(DIRECTORY[0][1]).split(",")[0])) / 2).__ceil__()
                            FILESYSTEM.insert(midpoint, [parameter])
                            update_filesystem()
                            break
                case "b":
                    for x, y in DIRECTORY:
                        if file.upper() == x:
                            midpoint = (((int(str(DIRECTORY[1][1]).split(",")[1]) - int(
                                str(DIRECTORY[1][1]).split(",")[0])) / 2).__ceil__()) + int(
                                str(DIRECTORY[1][1]).split(",")[0])
                            print(midpoint)
                            FILESYSTEM.insert(midpoint, [parameter])
                            update_filesystem()
                            break
                case "c":
                    for x, y in DIRECTORY:
                        if file.upper() == x:
                            midpoint = (((int(str(DIRECTORY[2][1]).split(",")[1]) - int(
                                str(DIRECTORY[2][1]).split(",")[0])) / 2).__ceil__()) + int(
                                str(DIRECTORY[2][1]).split(",")[0])
                            print(midpoint)
                            FILESYSTEM.insert(midpoint, [parameter])
                            update_filesystem()
                            break

        case "/b":
            match file:
                case "a":
                    for x, y in DIRECTORY:
                        if file.upper() == x:
                            temp = str(FILESYSTEM[int(str(y).split(",")[1])])
                            temp = temp.replace("'", "").replace(".", "").replace("[", "").replace("]", "")
                            FILESYSTEM.pop(int(str(y).split(",")[1]))
                            if len(temp) < 8:
                                temp = temp + parameter + "."
                                a = ""
                                inside_counter = 0
                                for count, z in enumerate(temp):
                                    if count % 8 == 0 and a != "":
                                        FILESYSTEM.insert(int(str(y).split(",")[1]) + inside_counter, [a])
                                        inside_counter += 1
                                        a = ""
                                    a = a + z
                                FILESYSTEM.insert(int(str(y).split(",")[1]) + inside_counter, [a])
                            update_filesystem()
                            for z in range(int(str(DIRECTORY[0][1]).split(",")[0]),
                                           int(str(DIRECTORY[0][1]).split(",")[1]) + 1):
                                print(z + 1, ":", FILESYSTEM[z], end=" ")
                            break

                case "b":
                    for x, y in DIRECTORY:
                        if file.upper() == x:
                            temp = str(FILESYSTEM[int(str(y).split(",")[1])])
                            temp = temp.replace("'", "").replace(".", "").replace("[", "").replace("]", "")
                            FILESYSTEM.pop(int(str(y).split(",")[1]))
                            FILESYSTEM.insert(int(str(y).split(",")[1]), [temp])
                            a = ""
                            inner_counter = 1
                            for count, z in enumerate(parameter):
                                if count % 8 == 0 and a != "":
                                    FILESYSTEM.insert(int(str(y).split(",")[1]) + inner_counter, [a])
                                    inner_counter += 1
                                    a = ""
                                a += z

                            if len(a) < 7:
                                if a[len(a) - 1] == ".":
                                    FILESYSTEM.insert(int(str(y).split(",")[1]) + inner_counter, [a])
                                else:
                                    FILESYSTEM.insert(int(str(y).split(",")[1]) + inner_counter, [a + "."])
                            else:
                                FILESYSTEM.insert(int(str(y).split(",")[1]) + inner_counter, [a])
                                if a[len(a) - 1] != ".":
                                    FILESYSTEM.insert(int(str(y).split(",")[1]) + inner_counter + 1, ["."])

                            update_filesystem()
                            for z in range(int(str(DIRECTORY[1][1]).split(",")[0]),
                                           int(str(DIRECTORY[1][1]).split(",")[1]) + 1):
                                print(z + 1, ":", FILESYSTEM[z], end=" ")

                            break

                case "c":
                    print(FILESYSTEM)
                    for x, y in DIRECTORY:
                        if file.upper() == x:
                            temp = str(FILESYSTEM[int(str(y).split(",")[1])])
                            temp = temp.replace("'", "").replace(".", "").replace("[", "").replace("]", "")
                            FILESYSTEM.pop(int(str(y).split(",")[1]))
                            FILESYSTEM.insert(int(str(y).split(",")[1]), [temp])
                            a = ""
                            inner_counter = 1
                            for count, z in enumerate(parameter):
                                if count % 8 == 0 and a != "":
                                    FILESYSTEM.insert(int(str(y).split(",")[1]) + inner_counter, [a])
                                    inner_counter += 1
                                    a = ""
                                a += z

                            if len(a) < 7:
                                if a[len(a) - 1] == ".":
                                    FILESYSTEM.insert(int(str(y).split(",")[1]) + inner_counter, [a])
                                else:
                                    FILESYSTEM.insert(int(str(y).split(",")[1]) + inner_counter, [a + "."])
                            else:
                                FILESYSTEM.insert(int(str(y).split(",")[1]) + inner_counter, [a])
                                if a[len(a) - 1] != ".":
                                    FILESYSTEM.insert(int(str(y).split(",")[1]) + inner_counter + 1, ["."])

                            update_filesystem()
                            for z in range(int(str(DIRECTORY[2][1]).split(",")[0]),
                                           int(str(DIRECTORY[2][1]).split(",")[1]) + 1):
                                print(z + 1, ":", FILESYSTEM[z], end=" ")

                            break


def menu():
    file_innit()
    while 1:
        choice = input().casefold()
        if choice == 'help':
            tb.banner("  Commands : HELP, SIZE, [READ, DEL, APP] + optional -f (front) -m (middle) -b (back) ")
            continue

        match choice.split(" ")[0]:
            case "help":
                match choice.split(" ")[1]:
                    case "app":
                        print("Allows the user to append a word at the front, middle, or back")
                    case "size":
                        print("Typed alone will specify the total blocks used in the system, otherwise, it will "
                              "display the number of characters in the given file")
                    case "del":
                        print("Allows the user to delete a character at the front, middle, or back of a file")
                    case "read":
                        print("Allows the user to read all contents of a file or a specific character at the front, "
                              "middle, or back")
            case "size":
                try:
                    get_size(choice.split(" ")[1])
                except IndexError:
                    print("Total system blocks = ", len(FILESYSTEM))

            case "read":
                try:
                    read_file(choice.split(" ")[2], choice.split(" ")[1])

                except IndexError:
                    try:
                        print(choice.split(" ")[2])
                    except IndexError:
                        read_file(choice.split(" ")[1], "")

            case "del":
                try:
                    delete_block(choice.split(" ")[2], choice.split(" ")[1])
                except IndexError:
                    try:
                        delete_block(choice.split(" ")[1], "")
                    except IndexError:
                        delete_block("", "")

            case "app":
                try:
                    append_block(choice.split(" ")[2].casefold(), choice.split(" ")[1].casefold(), choice.split(" ")[3])
                except IndexError:
                    print("Invalid Command")


menu()
