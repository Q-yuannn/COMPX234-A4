import sys
def main():
     if len(sys.argv) != 2:
        print("Please input valid command")
        return
     # if the command is valid
     port = int(sys.argv[1])
