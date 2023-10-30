import tableprint as tb

# Define constants
FILESYSTEM = []
DIRECTORY = []

# Define the file content
file_a_content = "The Power to Be Your Best."
file_b_content = "This program has performed an illegal operation and will be shut down."
file_c_content = "From tiny ACORNS mighty UNIX trees grow."


def menu():
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
                print("SIZE")

            case "read":
                try:
                    print(choice.split(" ")[1])
                except IndexError:
                    print(choice.split(" ")[0])

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
