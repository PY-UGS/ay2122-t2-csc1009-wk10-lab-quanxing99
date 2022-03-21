# 3A Print out module name when pass in module code
def printModuleName(moduleCode):
    switch = {
        "CSC1006": "Mathematics 2",
        "CSC1007": "Operating System",
        "CSC1008": "Data Structures and Algorithms",
        "CSC1009": "Object-Oriented Programming",
        "CSC1010": "Computer Networks",
    }

    return switch.get(moduleCode, "nothing")


moduleCode = input("Please enter the module code: ")

print("Module Name: ", printModuleName(moduleCode))


# 3B Print out odd numbers in descending order starting from 102 to 66
for i in range(102, 66, -1):
    if i % 2 != 0:
        print(i, end=" ")
