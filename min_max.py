# Author: Mahtab Zilaie
# Date: October 8 2019
# Description:asks the user how many integers they would
# like to enter then prompt the user to enter that many integers
# then display the largest and smallest of those numbers

min = 0
max = 0
user_value = int(input('How many integers would you like to enter?'))
print(user_value)
print("Please enter", user_value, "integers.")

for len in range(user_value):
    numbs =int(input())

    if len ==0:
        max = numbs
        min = numbs
    elif(numbs<min):
        min = numbs
    elif (numbs>max):
        max=numbs
print("min:", min)
print("max:", max)