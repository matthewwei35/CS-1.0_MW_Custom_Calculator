print("Welcome to the Water Calculator!")

weight = int(input("How much do you weigh in Pounds? "))
exercise_time = int(input("What's your average for Minutes of Daily exercise? "))

print("It is recommended that you drink", int((weight * 0.66666667) + (exercise_time * 0.4)),"ounces of water1 daily.")