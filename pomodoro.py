from time import sleep

#Configure inputs
work_length = float(input("How long will your work time be? (minutes): "))
sBreak_length = float(input("How long will your short break be? (minutes): "))
lBreak_length = float(input("How long will your long break be? (minutes): "))
numBreaks = int(input("How many short breaks do you need?: "))

#Variable used to track time elapsed
secs = 1

#Variable used to track number of short breaks
breakCounter = 0

#Bool used to track if work or break period. True = Work, False = Break
w_or_b = True

#Bool used to track if short or long break should occur. True = Short, False = Long
s_or_l = True


print("Begin work period\n")
while True:
    if w_or_b:
        # If the time elapsed = work period length change to break period and reset timer
        if secs / 60  == work_length :
            w_or_b = False
            secs = 1

            # Check if specified number of small breaks has occured, and if so execute a long rbeak and reset number of short breaks to 0
            if breakCounter == numBreaks:
                s_or_l = False
                breakCounter = 0
                print("Begin long break period\n")
            else:
                breakCounter += 1
                print("Begin short break period\n")
    else:
            # If time elapsed = the specified break period length change to work period and reset timer 
            if (secs / 60 == sBreak_length and s_or_l) or (secs / 60 == lBreak_length and not s_or_l):
                w_or_b = True
                s_or_l = True
                print("Begin work period\n")
                secs = 1
    sleep(1)
    secs += 1
    print(secs)

# TODO
# - Implement CLI graphics
# - Play sound when timer is done each period
# - Implement datetime instead of current `sleep(1)` method


