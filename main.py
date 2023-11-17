#Name : Shaval Brown
#ID : 2001407

import tableprint as tb
import tqdm
from time import sleep

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
    if len(FILESYSTEM) == 0:
        print("Error, File Empty")

    for x, y in DIRECTORY:
        if x == file.upper():
            print("File ", file, ": ", end="")
            if arg == "":
                for z in range(int(str(y).split(",")[0]), int(str(y).split(",")[1]) + 1):
                    print(str(FILESYSTEM[z]).replace("[","").replace("]","").replace("'",""), end="")
                print()
            else:
                match arg.casefold():
                    case '/m':
                        print(str(FILESYSTEM[(int(str(y).split(",")[0])) + (
                                ((int(str(y).split(",")[1])) - ((int(str(y).split(",")[0])) - 1)) / 2).__floor__()]).replace("[","").replace("]","").replace("'",""))
                    case '/f':
                        print(str(FILESYSTEM[int(str(y).split(",")[0])]).replace("[","").replace("]","").replace("'",""))
                    case '/b':
                        print(str(FILESYSTEM[int(str(y).split(",")[1])]).replace("[","").replace("]","").replace("'",""))

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

    if len(FILESYSTEM) == 0:
        print("Error, File Empty")
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
            print(FILESYSTEM)
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
                            a = ""
                            temp = parameter
                            inner_counter = 1
                            for count, w in enumerate(FILESYSTEM):
                                temp = temp + str(w).replace("[", "").replace("]", "").replace("'", "")
                                if str(w).count(".") == 1:
                                    for count2 in range(count + 1):
                                        FILESYSTEM.pop(0)
                                    break
                            parameter = temp
                            for count, z in enumerate(parameter):
                                if int(len(FILESYSTEM)) >= 30:
                                    print("Space Unavailable")
                                    update_filesystem()
                                    return

                                if count == 8:
                                    FILESYSTEM.insert(int(str(y).split(",")[0]), [a])
                                    a = ""
                                elif count % 8 == 0 and count != 0:
                                    FILESYSTEM.insert(int(str(y).split(",")[0]) + inner_counter, [a])
                                    a = ""
                                    inner_counter += 1
                                a = a + z

                            pbar = tqdm.tqdm(FILESYSTEM)
                            for t in pbar:
                                sleep(.1)
                                pbar.set_description("Appending To File A %s" % t)

                            if a[int(len(a)) - 1] == ".":
                                a = a.replace(".", "")
                            if len(parameter) < 8:
                                FILESYSTEM.insert(int(str(y).split(",")[0]), [a])
                            else:
                                FILESYSTEM.insert(int(str(y).split(",")[0]) + inner_counter, [a + "."])
                            update_filesystem()
                            for z in range(int(str(DIRECTORY[0][1]).split(",")[0]),
                                           int(str(DIRECTORY[0][1]).split(",")[1]) + 1):
                                print(z + 1, ":", FILESYSTEM[z], end=" ")
                            print()
                            break

                case "b":
                    for x, y in DIRECTORY:
                        if file.upper() == x:
                            a = ""
                            temp = parameter
                            inner_counter = 1
                            for count in range(int(str(DIRECTORY[1][1]).split(",")[0]),
                                               int(str(DIRECTORY[1][1]).split(",")[1]) + 1):
                                temp = temp + str(FILESYSTEM[count]).replace("[", "").replace("]", "").replace("'", "")
                            for count in range(int(str(DIRECTORY[1][1]).split(",")[0]),
                                               int(str(DIRECTORY[1][1]).split(",")[1]) + 1):
                                FILESYSTEM.pop(int(str(DIRECTORY[1][1]).split(",")[0]))
                            parameter = temp
                            for count, z in enumerate(parameter):
                                if int(len(FILESYSTEM)) >= 30:
                                    print("Space Unavailable")
                                    update_filesystem()
                                    return

                                if count == 8:
                                    FILESYSTEM.insert(int(str(DIRECTORY[1][1]).split(",")[0]), [a])
                                    a = ""
                                elif count % 8 == 0 and count != 0:
                                    FILESYSTEM.insert(int(str(DIRECTORY[1][1]).split(",")[0]) + inner_counter, [a])
                                    a = ""
                                    inner_counter += 1
                                a = a + z

                            pbar = tqdm.tqdm(FILESYSTEM)
                            for t in pbar:
                                sleep(.1)
                                pbar.set_description("Appending To File B %s" % t)

                            if a[int(len(a)) - 1] == ".":
                                a = a.replace(".", "")
                            if len(parameter) < 8:
                                FILESYSTEM.insert(int(str(DIRECTORY[1][1]).split(",")[0]), [a])
                            else:
                                FILESYSTEM.insert(int(str(DIRECTORY[1][1]).split(",")[0]) + inner_counter, [a + "."])
                            update_filesystem()
                            for z in range(int(str(DIRECTORY[1][1]).split(",")[0]),
                                           int(str(DIRECTORY[1][1]).split(",")[1]) + 1):
                                print(z + 1, ":", FILESYSTEM[z], end=" ")
                            print()
                            break

                case "c":
                    for x, y in DIRECTORY:
                        if file.upper() == x:
                            a = ""
                            temp = parameter
                            inner_counter = 1
                            for count in range(int(str(DIRECTORY[2][1]).split(",")[0]),
                                               int(str(DIRECTORY[2][1]).split(",")[1]) + 1):
                                temp = temp + str(FILESYSTEM[count]).replace("[", "").replace("]", "").replace("'", "")
                            for count in range(int(str(DIRECTORY[2][1]).split(",")[0]),
                                               int(str(DIRECTORY[2][1]).split(",")[1]) + 1):
                                FILESYSTEM.pop(int(str(DIRECTORY[2][1]).split(",")[0]))
                            parameter = temp
                            for count, z in enumerate(parameter):
                                if int(len(FILESYSTEM)) >= 30:
                                    print("Space Unavailable")
                                    update_filesystem()
                                    return

                                if count == 8:
                                    FILESYSTEM.insert(int(str(DIRECTORY[2][1]).split(",")[0]), [a])
                                    a = ""
                                elif count % 8 == 0 and count != 0:
                                    FILESYSTEM.insert(int(str(DIRECTORY[2][1]).split(",")[0]) + inner_counter, [a])
                                    a = ""
                                    inner_counter += 1
                                a = a + z

                            pbar = tqdm.tqdm(FILESYSTEM)
                            for t in pbar:
                                sleep(.1)
                                pbar.set_description("Appending To File C %s" % t)

                            if a[int(len(a)) - 1] == ".":
                                a = a.replace(".", "")
                            if len(parameter) < 8:
                                FILESYSTEM.insert(int(str(DIRECTORY[2][1]).split(",")[0]), [a])
                            else:
                                FILESYSTEM.insert(int(str(DIRECTORY[2][1]).split(",")[0]) + inner_counter, [a + "."])
                            update_filesystem()
                            for z in range(int(str(DIRECTORY[2][1]).split(",")[0]),
                                           int(str(DIRECTORY[2][1]).split(",")[1]) + 1):
                                print(z + 1, ":", FILESYSTEM[z], end=" ")
                            print()
                            break
        case "/m":
            match file:
                case "a":
                    for x, y in DIRECTORY:
                        if file.upper() == x:
                            a = ""
                            temp = ""
                            for count in range(int(str(DIRECTORY[0][1]).split(",")[0]),
                                               int(str(DIRECTORY[0][1]).split(",")[1]) + 1):
                                temp = temp + str(FILESYSTEM[count]).replace("[", "").replace("]", "").replace("'", "")
                            for count in range(int(str(DIRECTORY[0][1]).split(",")[0]),
                                               int(str(DIRECTORY[0][1]).split(",")[1]) + 1):
                                FILESYSTEM.pop(int(str(DIRECTORY[0][1]).split(",")[0]))
                            # print(FILESYSTEM[((int(str(DIRECTORY[0][1]).split(",")[1]) - int(str(DIRECTORY[0][1]).split(",")[0])) / 2).__ceil__()])
                            temp2 = []
                            for count, z in enumerate(temp):
                                if count % 8 == 0 and a != "":
                                    temp2.append([a])
                                    a = ""
                                a = a + z
                            temp2.append([a])
                            temp2.insert((int(len(temp2)) / 2).__ceil__(), [parameter])
                            temp = ""
                            for count in temp2:
                                temp = temp + str(count).replace("[", "").replace("]", "").replace("'", "")
                            inner_counter = 0
                            temp2 = ""
                            for count, z in enumerate(temp):
                                if count % 8 == 0 and temp2 != "":
                                    FILESYSTEM.insert(inner_counter, [temp2])
                                    inner_counter += 1
                                    temp2 = ""
                                temp2 = temp2 + z

                            if temp2 != "":
                                FILESYSTEM.insert(inner_counter, [temp2])

                            pbar = tqdm.tqdm(FILESYSTEM)
                            for t in pbar:
                                sleep(.1)
                                pbar.set_description("Appending To File A %s" % t)

                            update_filesystem()
                            for z in range(int(str(DIRECTORY[0][1]).split(",")[0]),
                                           int(str(DIRECTORY[0][1]).split(",")[1]) + 1):
                                print(z + 1, ":", FILESYSTEM[z], end=" ")
                            print()
                            break

                case "b":
                    for x, y in DIRECTORY:
                        if file.upper() == x:
                            a = ""
                            temp = ""
                            for count in range(int(str(DIRECTORY[1][1]).split(",")[0]),
                                               int(str(DIRECTORY[1][1]).split(",")[1]) + 1):
                                temp = temp + str(FILESYSTEM[count]).replace("[", "").replace("]", "").replace("'", "")
                            for count in range(int(str(DIRECTORY[1][1]).split(",")[0]),
                                               int(str(DIRECTORY[1][1]).split(",")[1]) + 1):
                                FILESYSTEM.pop(int(str(DIRECTORY[1][1]).split(",")[0]))
                            # print(FILESYSTEM[((int(str(DIRECTORY[0][1]).split(",")[1]) - int(str(DIRECTORY[0][1]).split(",")[0])) / 2).__ceil__()])
                            temp2 = []
                            for count, z in enumerate(temp):
                                if count % 8 == 0 and a != "":
                                    temp2.append([a])
                                    a = ""
                                a = a + z
                            temp2.append([a])
                            temp2.insert((int(len(temp2)) / 2).__ceil__(), [parameter])
                            temp = ""
                            eof = []
                            for count, z in enumerate(FILESYSTEM):
                                if str(z).count(".") == 1:
                                    eof.append(count)
                            for count in temp2:
                                temp = temp + str(count).replace("[", "").replace("]", "").replace("'", "")
                            inner_counter = int(eof[0]) + 1
                            temp2 = ""
                            for count, z in enumerate(temp):
                                if count % 8 == 0 and temp2 != "":
                                    FILESYSTEM.insert(inner_counter, [temp2])
                                    inner_counter += 1
                                    temp2 = ""
                                temp2 = temp2 + z

                            if temp2 != "":
                                FILESYSTEM.insert(inner_counter, [temp2])

                            pbar = tqdm.tqdm(FILESYSTEM)
                            for t in pbar:
                                sleep(.1)
                                pbar.set_description("Appending To File B %s" % t)
                            update_filesystem()
                            for z in range(int(str(DIRECTORY[1][1]).split(",")[0]),
                                           int(str(DIRECTORY[1][1]).split(",")[1]) + 1):
                                print(z + 1, ":", FILESYSTEM[z], end=" ")
                            print()
                            break

                case "c":
                    for x, y in DIRECTORY:
                        if file.upper() == x:
                            a = ""
                            temp = ""
                            for count in range(int(str(DIRECTORY[2][1]).split(",")[0]),
                                               int(str(DIRECTORY[2][1]).split(",")[1]) + 1):
                                temp = temp + str(FILESYSTEM[count]).replace("[", "").replace("]", "").replace("'", "")
                            for count in range(int(str(DIRECTORY[2][1]).split(",")[0]),
                                               int(str(DIRECTORY[2][1]).split(",")[1]) + 1):
                                FILESYSTEM.pop(int(str(DIRECTORY[2][1]).split(",")[0]))
                            # print(FILESYSTEM[((int(str(DIRECTORY[0][1]).split(",")[1]) - int(str(DIRECTORY[0][1]).split(",")[0])) / 2).__ceil__()])
                            temp2 = []
                            for count, z in enumerate(temp):
                                if count % 8 == 0 and a != "":
                                    temp2.append([a])
                                    a = ""
                                a = a + z
                            temp2.append([a])
                            temp2.insert(((int(len(temp2)) / 2).__ceil__()) - 1, [parameter])
                            temp = ""
                            eof = []
                            for count, z in enumerate(FILESYSTEM):
                                if str(z).count(".") == 1:
                                    eof.append(count)
                            for count in temp2:
                                temp = temp + str(count).replace("[", "").replace("]", "").replace("'", "")
                            inner_counter = int(eof[1]) + 1
                            temp2 = ""
                            for count, z in enumerate(temp):
                                if count % 8 == 0 and temp2 != "":
                                    FILESYSTEM.insert(inner_counter, [temp2])
                                    inner_counter += 1
                                    temp2 = ""
                                temp2 = temp2 + z

                            if temp2 != "":
                                FILESYSTEM.insert(inner_counter, [temp2])

                            pbar = tqdm.tqdm(FILESYSTEM)
                            for t in pbar:
                                sleep(.1)
                                pbar.set_description("Appending To File C %s" % t)
                            update_filesystem()
                            for z in range(int(str(DIRECTORY[2][1]).split(",")[0]),
                                           int(str(DIRECTORY[2][1]).split(",")[1]) + 1):
                                print(z + 1, ":", FILESYSTEM[z], end=" ")
                            print()
                            break

        case "/b":
            match file:
                case "a":
                    for x, y in DIRECTORY:
                        if file.upper() == x:
                            a = ""
                            temp = ""
                            for count in range(int(str(DIRECTORY[0][1]).split(",")[0]),
                                               int(str(DIRECTORY[0][1]).split(",")[1]) + 1):
                                temp = temp + str(FILESYSTEM[count]).replace("[", "").replace("]", "").replace("'", "")
                            for count in range(int(str(DIRECTORY[0][1]).split(",")[0]),
                                               int(str(DIRECTORY[0][1]).split(",")[1]) + 1):
                                FILESYSTEM.pop(int(str(DIRECTORY[0][1]).split(",")[0]))
                            temp2 = []
                            for count, z in enumerate(temp):
                                if count % 8 == 0 and a != "":
                                    temp2.append([a])
                                    a = ""
                                a = a + z
                            if a[int(len(a)) - 1].count(".") == 1:
                                a = a.replace(".", "")
                            temp2.append([a])
                            temp2.insert(len(temp2), [parameter + "."])
                            temp = ""
                            for count in temp2:
                                temp = temp + str(count).replace("[", "").replace("]", "").replace("'", "")
                            inner_counter = 0
                            temp2 = ""
                            for count, z in enumerate(temp):
                                if count % 8 == 0 and temp2 != "":
                                    FILESYSTEM.insert(inner_counter, [temp2])
                                    inner_counter += 1
                                    temp2 = ""
                                temp2 = temp2 + z

                            if temp2 != "":
                                FILESYSTEM.insert(inner_counter, [temp2])

                            pbar = tqdm.tqdm(FILESYSTEM)
                            for t in pbar:
                                sleep(.1)
                                pbar.set_description("Appending To File A %s" % t)
                            update_filesystem()
                            for z in range(int(str(DIRECTORY[0][1]).split(",")[0]),
                                           int(str(DIRECTORY[0][1]).split(",")[1]) + 1):
                                print(z + 1, ":", FILESYSTEM[z], end=" ")
                            print()
                            break

                case "b":
                    for x, y in DIRECTORY:
                        if file.upper() == x:
                            a = ""
                            temp = ""
                            for count in range(int(str(DIRECTORY[1][1]).split(",")[0]),
                                               int(str(DIRECTORY[1][1]).split(",")[1]) + 1):
                                temp = temp + str(FILESYSTEM[count]).replace("[", "").replace("]", "").replace("'", "")
                            for count in range(int(str(DIRECTORY[1][1]).split(",")[0]),
                                               int(str(DIRECTORY[1][1]).split(",")[1]) + 1):
                                FILESYSTEM.pop(int(str(DIRECTORY[1][1]).split(",")[0]))
                            temp2 = []
                            for count, z in enumerate(temp):
                                if count % 8 == 0 and a != "":
                                    temp2.append([a])
                                    a = ""
                                a = a + z
                            if a[int(len(a)) - 1].count(".") == 1:
                                a = a.replace(".", "")
                            temp2.append([a])
                            temp2.insert(len(temp2), [parameter + "."])
                            temp = ""
                            eof = []
                            for count, z in enumerate(FILESYSTEM):
                                if str(z).count(".") == 1:
                                    eof.append(count)
                            for count in temp2:
                                temp = temp + str(count).replace("[", "").replace("]", "").replace("'", "")
                            inner_counter = int(eof[0] + 1)
                            temp2 = ""
                            for count, z in enumerate(temp):
                                if count % 8 == 0 and temp2 != "":
                                    FILESYSTEM.insert(inner_counter, [temp2])
                                    inner_counter += 1
                                    temp2 = ""
                                temp2 = temp2 + z

                            if temp2 != "":
                                FILESYSTEM.insert(inner_counter, [temp2])

                            pbar = tqdm.tqdm(FILESYSTEM)
                            for t in pbar:
                                sleep(.1)
                                pbar.set_description("Appending To File B %s" % t)
                            update_filesystem()
                            for z in range(int(str(DIRECTORY[1][1]).split(",")[0]),
                                           int(str(DIRECTORY[1][1]).split(",")[1]) + 1):
                                print(z + 1, ":", FILESYSTEM[z], end=" ")
                            print()
                            break

                case "c":
                    for x, y in DIRECTORY:
                        if file.upper() == x:
                            a = ""
                            temp = ""
                            for count in range(int(str(DIRECTORY[2][1]).split(",")[0]),
                                               int(str(DIRECTORY[2][1]).split(",")[1]) + 1):
                                temp = temp + str(FILESYSTEM[count]).replace("[", "").replace("]", "").replace("'", "")
                            for count in range(int(str(DIRECTORY[2][1]).split(",")[0]),
                                               int(str(DIRECTORY[2][1]).split(",")[1]) + 1):
                                FILESYSTEM.pop(int(str(DIRECTORY[2][1]).split(",")[0]))
                            temp2 = []
                            for count, z in enumerate(temp):
                                if count % 8 == 0 and a != "":
                                    temp2.append([a])
                                    a = ""
                                a = a + z
                            if a[int(len(a)) - 1].count(".") == 1:
                                a = a.replace(".", "")
                            temp2.append([a])
                            temp2.insert(len(temp2), [parameter + "."])
                            temp = ""
                            eof = []
                            for count, z in enumerate(FILESYSTEM):
                                if str(z).count(".") == 1:
                                    eof.append(count)
                            for count in temp2:
                                temp = temp + str(count).replace("[", "").replace("]", "").replace("'", "")
                            inner_counter = int(eof[1] + 1)
                            temp2 = ""
                            for count, z in enumerate(temp):
                                if count % 8 == 0 and temp2 != "":
                                    FILESYSTEM.insert(inner_counter, [temp2])
                                    inner_counter += 1
                                    temp2 = ""
                                temp2 = temp2 + z

                            if temp2 != "":
                                FILESYSTEM.insert(inner_counter, [temp2])
                            pbar = tqdm.tqdm(FILESYSTEM)
                            for t in pbar:
                                sleep(.1)
                                pbar.set_description("Appending To File C %s" % t)
                            update_filesystem()
                            for z in range(int(str(DIRECTORY[2][1]).split(",")[0]),
                                           int(str(DIRECTORY[2][1]).split(",")[1]) + 1):
                                print(z + 1, ":", FILESYSTEM[z], end=" ")
                            print()
                            break


def menu():
    tb.banner("Type Command Or /exit to exit  ")
    file_innit()
    while 1:
        choice = input().casefold()
        # choice = "app"
        if choice == 'help':
            tb.banner("/f (front) /m (middle) /b (back) {FileName} ")
            headers = ["Commands ", " Example"]
            data = [["Size ", "Size /f a"], ["Read ", "Read /m b"], ["Del ", "Del /b c"], ["App ", "app /f a test"]]
            tb.table(data, headers)
            continue

        match choice.split(" ")[0]:
            case "help":
                match choice.split(" ")[1]:
                    case "app":
                        tb.banner("Allows the user to append a word at the front, middle, or back")
                    case "size":
                        tb.banner("Typed alone will specify the total blocks used in the system, otherwise, it will "
                                  "display the number of characters in the given file")
                    case "del":
                        tb.banner("Allows the user to delete a character at the front, middle, or back of a file")
                    case "read":
                        tb.banner(
                            "Allows the user to read all contents of a file or a specific character at the front, "
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
                    temp = ""
                    for x in range(3, len(choice.split(" "))):
                        if x == 3:
                            temp = choice.split(" ")[x]
                            continue
                        temp = temp + " " + choice.split(" ")[x]
                    append_block(choice.split(" ")[2].casefold(), choice.split(" ")[1].casefold(), temp)
                    # append_block("c", "/b", input())
                except IndexError:
                    print("Invalid Command")

            case "/exit":
                exit(0)

            case _:
                print("Invalid Command")


menu()
