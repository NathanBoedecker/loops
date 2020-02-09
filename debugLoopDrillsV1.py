'''
The following functions have problems that keep them from
completing the task that they have to do.

All the problems are either Logical or Syntactical errors with LOOPS.
Focus on the loops and find the problems with the LOOPS.

The number of errors are as follows:
counting: 4
fruits: 3
checkStudents: 4
printGrades: 2
'''

'''
This function uses a while loop to print out every number from
1 to 100.
'''
def counting():
    x = 0
    while(x <= 100):
        print(x)
        x = x + 1
    print("DONE")
    return 

counting()

'''
This function takes a list of fruits and prints out each fruit in the list using
a for loop.
'''
fruit = ["apple", "pear", "peach", "watermelon", "tomato"]
for x in fruit:
    print(x)
    print("DONE")






'''
This function takes an input of a 2D list. In the first dimension, it's a string 
list of the student names. In the second dimension, it's a boolean list of 
whether or not the student is failing.
The function then goes through the list and prints whether or not the student is 
passing and or not. If the student is passing, it prints "[NAME] is passing." If
the student is failing, it prints "[NAME] is failing."
'''
def checkStudents(studentList):
    x = 0
    while(len(studentList[0])):
        if("Michael"):
            print("Michael is passing.")
        if("Patrice"):
            print("Patrice is passing")
        if("Amaya"):
            print("Amaya is passing")
        else:
            print("William is failing.")
        break
    print("DONE")
    return 

listOfStudents = [["Michael", "Patrice", "Amaya", "William"], [True, True, True, False]]


'''
This function takes a list of grades and then prints each of the grades out with
a for loop.
'''
def printGrades(studentList):
    for x in listOfStudents:
        print(x)
        print("DONE")
 

listOfStudents = [66, 24, 12, 45, 100, 100, 100]
printGrades(listOfStudents)
        