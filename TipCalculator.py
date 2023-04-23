#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

#Assigning variable 'bill' amount as a float data type.
#Printing string showing the amount of the bill while converting the int datatype into a string data type.
bill = float(150.00)
print("The bill is " + str(bill) + ".")

#Assigning variable 'num_of_people' as the amount of people the bill must be split between as an integer data
#Printing string showing the amount of people the bill people while converting the interger data type into a string data type. 
num_of_people = int(5)
print("That bill is being split by " + str(num_of_people) + " people.")

#Assigning variable 'tip_percentage' as the amount of tip percentage amount as a float datatype.
#Printing string showing the tip percentage, the decimal number that it's being multiplied by and converting float data type into a string data type. 
tip_percentage = float(1.12)
print("The tip percentage is 12%, so we are multiplying by " + str(tip_percentage) + ".")

#Assigning variable result to the bill being divided by the amount of people and multiplaying by the tip percentage in decimal form.
#Assigning variable rounded_result which is rounded off by the second decimal point. 
result = (bill/num_of_people) * tip_percentage
rounded_result = round((bill/num_of_people) * tip_percentage, 2)

#Printing the rounded_result variable.
print(rounded_result)

#Printing the entire result of using f string. 
print(f"The bill is {bill} and that bill is being divided by {num_of_people}. Since the tip percent is 12%, we are dividing by {tip_percentage}. The result is {result} which is rounded {rounded_result}.")