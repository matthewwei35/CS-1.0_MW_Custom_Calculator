#-----------------------
#Water Calculator
#Created by Matthew Wei
#-----------------------

#This is the header
print("~~~~~ Welcome to the Water Calculator! ~~~~~")

#Takes user input and stores that value into the variable named weight
weight = int(input("How much do you weigh in Pounds? "))
#Takes user input and stores that value into the variable named exercise_time
exercise_time = int(input("What's your average for Minutes of Daily exercise? "))

#Multiply your weight by 2/3 to determine how much water to drink daily in ounces
#Add 0.4 ounces to the total for every minute you workout daily, ex: 30 min * 0.4 = 12 ounces
#Prints out the result of the operands weight and exercise_time
print(">>> It is recommended that you drink", int((weight * 0.66666667) + (exercise_time * 0.4)),"ounces of water daily. <<<")