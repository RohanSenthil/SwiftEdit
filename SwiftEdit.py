import re
import os

ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))

def main():

    print("")

    print("Welcome to SwiftEdit.py by Rohan Senthil")
    print("----------------------------------------")

    print("")

    print("Editing Modes")
    print("1. Concatenate")
    print("2. Remove")
    print("3. Replace")

    print("")

    while(True):

        mode = input("Select mode: ")

        if mode == '1' or mode == '2' or mode == '3':
            break
        else:
            print("Error: Select mode 1, 2 or 3")

    if mode == '1':

        print("")
        print("Concatenate Sub-Modes")
        print("1. Concatenate at start of...")
        print("2. Concatenate at end of...")
        print("3. Concatenate inbetween...")
        print("")

        while(True):

            subMode1 = input("Select mode: ")

            if subMode1 == '1' or subMode1 == '2' or subMode1 == '3':
                break
            else:
                print("Error: Select sub-mode 1, 2 or 3")
        
        if subMode1 == '1':
            concatenateStart()

        if subMode1 == '2':
            concatenateEnd()
        
        if subMode1 == '3':
            concatenateInbetween()
    
    if mode == '2':
        remove()

    if mode == '3':
        replace()
    
    
def replace():

    print("")

    while(True):

        inputFile = input("File to Edit: ")

        try:
            with open(os.path.join(ROOT_DIR, inputFile), "r") as file:
                file = file.read()
            break
        except:
            print("Error: File cannot be found")
            print("")

    stringToRemove = input("String to replace: ")
    newString = input("Replace string with: ")
    outFile = input("Output File: ")
    print("")

    idx = [m.start() for m in re.finditer(stringToRemove , file)]

    if re.search(stringToRemove , file) is None:
        print("Error: SPECIFIED STRING CANNOT BE FOUND")
        print("")
        return

    for i in range(len(idx)):

        if len(newString) > len(stringToRemove):
            indexToAdd = i * (len(newString) - len(stringToRemove))
            file = file[:(idx[i]+indexToAdd)] + newString + file[(idx[i]+indexToAdd)+len(stringToRemove):]
        elif len(newString) < len(stringToRemove):
            indexToRemove = i * (len(stringToRemove) - len(newString))
            file = file[:(idx[i]-indexToRemove)] + newString + file[(idx[i]-indexToRemove)+len(stringToRemove):]
        else:
            file = file[:idx[i]] + newString + file[idx[i]+len(stringToRemove):]
            

    with open(os.path.join(ROOT_DIR, outFile), "w") as newFile:
        newFile.write(file)

    print("SUCCESS!")
    print("")


def remove():

    print("")

    while(True):

        inputFile = input("File to Edit: ")

        try:
            with open(os.path.join(ROOT_DIR, inputFile), "r") as file:
                file = file.read()
            break
        except:
            print("Error: File cannot be found")
            print("")

    stringToRemove = input("String to remove: ")
    outFile = input("Output File: ")
    print("")

    idx = [m.start() for m in re.finditer(stringToRemove , file)]

    if re.search(stringToRemove , file) is None:
        print("Error: SPECIFIED STRING CANNOT BE FOUND")
        print("")
        return

    for i in range(len(idx)):
        indexToRemove = i*len(stringToRemove)
        file = file[:(idx[i]-indexToRemove)] + file[(idx[i]-indexToRemove)+len(stringToRemove):]

    with open(os.path.join(ROOT_DIR, outFile), "w") as newFile:
        newFile.write(file)

    print("SUCCESS!")
    print("")


def concatenateStart():
    
    print("")

    while(True):

        inputFile = input("File to Edit: ")

        try:
            with open(os.path.join(ROOT_DIR, inputFile), "r") as file:
                file = file.read()
            break
        except:
            print("Error: File cannot be found")
            print("")

    stringToAdd = input("String to concatenate: ")
    placeToAdd = input("Concatenate at the start of: ")
    outFile = input("Output File: ")
    print("")

    idx = [m.start() for m in re.finditer(placeToAdd , file)]

    if re.search(placeToAdd , file) is None:
        print("Error: SPECIFIED STRING CANNOT BE FOUND")
        print("")
        return

    for i in range(len(idx)):
        indexToAdd = i*len(stringToAdd)
        file = file[:(idx[i]+indexToAdd)] + stringToAdd + file[(idx[i]+indexToAdd):]

    with open(os.path.join(ROOT_DIR, outFile), "w") as newFile:
        newFile.write(file)

    print("SUCCESS!")
    print("")

def concatenateEnd():

    print("")

    while(True):

        inputFile = input("File to Edit: ")

        try:
            with open(os.path.join(ROOT_DIR, inputFile), "r") as file:
                file = inputFile.read()
            break
        except:
            print("Error: File cannot be found")
            print("")
        

    stringToAdd = input("String to concatenate: ")
    placeToAdd = input("Concatenate at the end of: ")
    outFile = input("Output File: ")
    print("")

    idx = [m.end() for m in re.finditer(placeToAdd , file)]

    if re.search(placeToAdd , file) is None:
        print("Error: SPECIFIED STRING CANNOT BE FOUND")
        print("")
        return

    for i in range(len(idx)):
        indexToAdd = i*len(stringToAdd)
        file = file[:(idx[i]+indexToAdd)] + stringToAdd + file[(idx[i]+indexToAdd):]

    with open(os.path.join(ROOT_DIR, outFile), "w") as newFile:
        newFile.write(file)
    
    print("SUCCESS!")
    print("")

def concatenateInbetween():

    print("")

    while(True):

        inputFile = input("File to Edit: ")

        try:
            with open(os.path.join(ROOT_DIR, inputFile), "r") as file:
                file = inputFile.read()
            break
        except:
            print("Error: File cannot be found")
            print("")
        

    stringToAdd = input("String to concatenate: ")
    before = input("Specify text before point of concatenation: ")
    after = input("Specify text after point of concatenation: ")
    outFile = input("Output File: ")
    print("")

    letterFrom = len(after)

    placeToAdd = before + after

    idx = [m.end()-letterFrom for m in re.finditer(placeToAdd , file)]

    if re.search(placeToAdd , file) is None:
        print("Error: SPECIFIED STRING CANNOT BE FOUND")
        print("")
        return

    for i in range(len(idx)):
        indexToAdd = i*len(stringToAdd)
        file = file[:(idx[i]+indexToAdd)] + stringToAdd + file[(idx[i]+indexToAdd):]

    with open(os.path.join(ROOT_DIR, outFile), "w") as newFile:
        newFile.write(file)

    print("SUCCESS!")
    print("")


if __name__ == "__main__":
    main()
