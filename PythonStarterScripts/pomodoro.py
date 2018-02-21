import datetime, time, os

#Functions here

def RestTimer():
    print "Rest time! 5 minutes."
    time.sleep(4)
    print "Rest time done!"
    print "Starting another Pomodoro..."
    StartTimer()

#def Delete():
#def PrintLog():
#def NewItem():


def StartTimer():

    pomodoro = 0

    print "Starting Pomodoro timer, 25 minutes. Ctrl-C to cancel out."

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
print "L = Check log file."
print "S = Start timer. "
print ""
check = raw_input("What opton would you like to pick? ")

if check == "S" :
    StartTimer()
