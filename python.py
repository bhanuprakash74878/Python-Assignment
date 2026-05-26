#Question 1:

Name = input("Enter your First Name :")
City = input("Enter your current city :")
Language = input("Enter your Favourite Programming Language :")
print(f"Iam {Name}.I live in {City} and I love coding in {Language}!")

#Question 2 :

num1 = int(input("Enter First Number :"))
num2 = int(input("Enter second number :"))
Result = num1 + num2
print(f"The total sum is : {Result}")

#Queston number 3 :

Name = input("Enter the name of the Product :")
Price_of_sinle_unit = float(input("Enter the Price if a single unit : $"))
Quantity = int(input("Enter the total quatity bought :"))
Subtotal = Price_of_sinle_unit * Quantity
Additional_Tax = 0.18 * Subtotal
rounded_tax = round(Additional_Tax, 2)
Grand_Total = Subtotal + Additional_Tax
rounded_Grand_Total = round(Grand_Total, 2)
print(f" Subtotal : ${Subtotal} \n Tax amount added : ${rounded_tax}\n Grand Total : ${rounded_Grand_Total}")

#Question number 4 :

Distance = float(input("Enter the Total Distance travelled in kilometers :"))
Time = float(input("Enter the Total time taken in hours :"))
Average_Speed = Distance / Time
rounded_speed = round(Average_Speed, 2)
print(f"The Average Speed is : {rounded_speed} km/hr")

#Question number 5 :

Bill_Amount = float(input("The Total Restaurant's bill is : $"))
People = int(input("Total number of people splitting the bill are :"))
Individual_amount = Bill_Amount / People
rounded_amount = round(Individual_amount, 2)
print(f"Each person need to pay : ${rounded_amount}")
#Here,we cannot use number 0.When we place 0 in the formula provided in line# 30,we get undefined value.
#It is because,any value divided by 0 will give infinity,which is undefined.3

#Question number 6 :

Savings = float(input("Enter Your Current Total Savings : $"))
rounded_Savings = round(Savings, 2)
House_rent = float(input("Enter Your House rent : $"))
Food_expenses = float(input("Enter Your Food Expenses : $"))
Electricity = float(input("Enter Your Monthly Electricity cost : $"))
Internet = float(input("Enter Your Monthly Internet cost : $"))
Total_Monthly_Expenses = House_rent + Food_expenses + Electricity + Internet
rounded_expenses = round(Total_Monthly_Expenses, 2)
Emergency_Buffer = 0.01 * Savings
rounded_Buffer = round(Emergency_Buffer, 2)
Usable_Savings = Savings - Emergency_Buffer
rounded_savings = round(Usable_Savings, 2)
Remaining_Runway_Months = Usable_Savings / rounded_expenses
rounded_runway_months = round(Remaining_Runway_Months, 2)
print(f" Your Savings = ${rounded_Savings} \n Emergency buffer = ${rounded_Buffer} \n Total Usable Savings = ${rounded_savings} \n Your Total Monthly Expenses = ${rounded_expenses} \n Total remaining Runway months = {rounded_runway_months}")

#Question number 7 :

Name = input("Enter The Product Name :")
print("Enter Your Package Dimensions Below :")
Length = float(input("Enter Length in centimetres : "))
Breadth = float(input("Enter Breadthvin centimetres :"))
Height = float(input("Enter Heigth in centimetres:"))
Weight = float(input("Enter the Weight of the Package in kilograms :"))
Volume = Length * Breadth * Height
Volumetric_Weight = Volume / 5000
Base_charge = Weight * 15.00
Subcharge = Volumetric_Weight * 0.05
Total_amount = Base_charge + Subcharge
rounded_amount = round(Total_amount, 2)
print(f" Name of the product is : {Name}\n Total Weight of the product : {Weight}\n Total Volumetric Weight : {Volumetric_Weight}\n Base charge = ${Base_charge}\n Subcharge = ${Subcharge}\n Total Amount = ${rounded_amount}")
print("NOTE:")
print("Base Price per physical kilogram is $15.00 and subcharge per cubic centimeter occupied is $0.05 ")

#Question number 8 :

Name = input("Enter Your Name :")
Gender = input("Enter Your Gender :")
Age = int(input("Enter Your Age :"))
Weight = float(input("Enter Your Weight in kilograms :"))
Height = float(input("Enter Your Height in centimeters :"))
BMI = Weight / Height / Height
Final_BMI = BMI * 10000
rounded_BMI = round(Final_BMI, 2)
print(rounded_BMI)
Water_Intake =  Weight * 0.033
rounded_water_intake = round(Water_Intake, 2)
print("Your Personal Biometric Diagnostic Matrix :")
print(f" Name : {Name}\n Gender : {Gender}\n Weight : {Weight}\n Height : {Height}\n BMI = {rounded_BMI}\n Daily Water intake Target in Litres : {rounded_water_intake} ")