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

    DIRECTORY.append(["A", "1," + str(len(FILESYSTEM))])

    for x, y in enumerate(file_b_content, 1):
        block += y
        if x % 8 == 0 and x != 0:
            FILESYSTEM.append([block])
            block = ""
        if x == len(file_b_content):
            FILESYSTEM.append([block])
            block = ""

    DIRECTORY.append(["B", str(int(str(DIRECTORY[0][1]).split(",")[1]) + 1) + "," + str(len(FILESYSTEM))])

    for x, y in enumerate(file_c_content, 1):
        block += y
        if x % 8 == 0 and x != 0:
            FILESYSTEM.append([block])
            block = ""
        if x == len(file_c_content) and not y:
            FILESYSTEM.append([block])
            block = ""

    DIRECTORY.append(["C", str(int(str(DIRECTORY[1][1]).split(",")[1]) + 1) + "," + str(len(FILESYSTEM))])


def get_size(file):
    characters = 0
    for x, y in enumerate(DIRECTORY):
        if file == str(y[0]).casefold():
            blocks = int(str(y[1]).split(",")[1]) - (int(str(y[1]).split(",")[0])) + 1
            for z in FILESYSTEM[int(str(y[1]).split(",")[0]) - 1:int(str(y[1]).split(",")[1])]:
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
                for z in range(int(str(y).split(",")[0]) - 1, int(str(y).split(",")[1])):
                    print(FILESYSTEM[z])
            else:
                match arg.casefold():
                    case '/m':
                        print(FILESYSTEM[(int(str(y).split(",")[0]) - 1) + (((int(str(y).split(",")[1])) - ((int(str(y).split(",")[0])) - 1)) / 2).__floor__()])
                    case '/f':
                        print(FILESYSTEM[int(str(y).split(",")[0]) - 1])
                    case '/b':
                        print(FILESYSTEM[int(str(y).split(",")[1]) - 1])

            return
    print("File Not Found Or Incorrect Parameters")


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
                    print(choice.split(" ")[1])
                except IndexError:
                    print(choice.split(" ")[0])

            case "app":
                try:
                    print(choice.split(" ")[1])
                except IndexError:
                    print(choice.split(" ")[0])


menu()
