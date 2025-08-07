#Design a program that determines the award a person competing will receive.
#Have user input the time for their triathlon.
time = int(input("Please enter your time for the triathlon."))

#Program the first qualifying criteria using if. 
#I chose the and operator because both conditions must be met to be given the award.
if(time>=0) and (time<=100):
    print("Provincial Colors")

#Program five minutes off from the qualifying time.
elif(time>=101) and (time<=105):
    print("Provincial Half Colours")

#Program  10 minutes off from the qualifying time.
elif(time>=106) and (time<=110):
    print("Provincial Scroll")

#Program more than 10 minutes off from the qualifying time.
elif (time>=111):
    print("No Award")