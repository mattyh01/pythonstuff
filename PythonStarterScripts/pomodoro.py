import datetime, time, os

#Functions here

def RestTimer():
    print "Rest time! 5 minutes."
    time.sleep(4)
    print "Rest time done!"
    print "Starting another Pomodoro..."
    StartTimer()

#def Delete():
#How will we delete specific lines?
#def PrintLog():
def NewItem():
    task = raw_input("Input the new task. ")
    #Output task into text ctl file
    openfile = open("current_tasks.txt", 'a')
    openfile.write(task + "\n")
    openfile.close()
    #Careful of overites, need to append

def ListItems():
    openfile = open("current_tasks.txt", 'r')
    taskread = openfile.read()
    print taskread
    openfile.close()


def StartTimer():

    openfile = open("current_tasks.txt", "r")
    taskread = openfile.read().split('\n')
    print taskread
    selected = raw_input("Which task would you like to do?")
    #Print as a list, array?
    print ""

    pomodoro = 0

    print "Starting Pomodoro timer, 25 minutes for task " + selected + ", Ctrl-C to cancel out."

    time.sleep(5) #1500 for real app
    #if cancel out occurs, exit out

    print "Time up!"

    pomodoro = pomodoro + 1

    print pomodoro #Test for if counter works

#Add iteration of Pomodoro (counter)

    restcheck = raw_input("Start Rest Time?")

    if restcheck == "yes" :

        RestTimer()


print "Hello and welcome to the Pomodoro App."
print ""
print "I = New Item of work."
print "D = Delete Item of Work."
print "C = List current tasks"
print "L = Check log file."
print "S = Start timer. "
print ""
check = raw_input("What opton would you like to pick? ")

if check == "S" :
    StartTimer()
elif check == "I":
    NewItem()
elif check == "C":
    ListItems()
