#Question number 1.1 :

amount = float(input("Enter the total Bill Amount in rupees : ₹"))
participants = int(input("Enter total number of people sharing the bill :"))
surcharge = amount * 0.018
rounded_charge = round(surcharge, 2)
total_amount = amount + rounded_charge
amount_per_head = total_amount / participants
rounded_amount = round(amount_per_head, 2)
print(f"  Your Bill : \n Bill amount : ₹{amount}\n Surcharge = ₹{rounded_charge}\n Total Bill Amount = ₹{total_amount}\n Amount needed to pay per head = ₹{rounded_amount}")

#Question number 1.2 :

radius = float(input("Enter the Radius of the Circle in centimeters :"))
Circumference = 2 * 3.1415926535 * radius
rounded_Circumference = round(Circumference, 2)
Area = 3.1415926535 * radius * radius
rounded_area = round(Area, 2)
if radius > 0:
  print(f" Results : \n Circumference = {rounded_Circumference} cm\n Area = {rounded_area} cm\u00b2 ")
else:
  print("Error Detected in value of Radius")

#Question number 2.1 :

print("Welcome To My Calculator Model!!")
print("NOTE : \n 1)In case of power,1st number is base and 2nd number is power \n 2)Incase of root,1st number is number and 2nd number is nth root ")
operator = input("Enter Your operation : (+,-,/,*,power,root)")
num1 = float(input("Enter Your First Number ="))
num2 = float(input("Enter Your Second Number ="))
if operator == '+':
    print(f"Result = {num1 + num2}")
elif operator == '-':
    print(f"Result = {num1 - num2}")
elif operator == '/':
    if num2 == 0:
        print("Result = Error:Cannot divide by zero!")
    else:
        print(f"Result = {num1 / num2}")
elif operator == '*':
    print(f"Result = {num1 * num2}")
elif operator == 'power':
    power = num1 ** num2
    print(f"Result = {power}")
elif operator == 'root':
    if num2 == 0:
        print("Result = Error:Root cannot be zero!")
    else:
        root = num1 ** (1/num2)
        print(f"Result = {root}")
else:
    print("Your Operation in Invalid")
print("Thanks For Letting me Help you,with Your Calculation!!")
Rating = int(input("Could You Please Give me a Rating out of 5? :"))
if 0 <= Rating <= 2:
    print("Sorry for That!! I will definitely Improve Much Better")
elif 3<= Rating <= 4:
    print("Thanks For Your Feedback!! I will try to still Improve more ")
elif Rating == 5:
   print("Thank You So much!! You Made me Feel Confident in my Model")
else:
   print("Invalid Rating")
print("OK Then! Feel Free to visit my Model Some other time")

#Question number 2.2 :

marks = int(input("Enter Your Marks ="))
if 80 <= marks <= 89:
    print(f" Result :\n Marks = {marks}\n Grade = B\n Congracts!!")
elif 70 <= marks <= 79:
    print(f"Results :\n Marks = {marks}\n Grade = C\n Congracts!!")
elif 100 <= marks <= 90:
    print(f" Result :\n Marks = {marks}\n Grade = A\n Heartly Congracts upon your success!!")
elif 60 <= marks <= 69:
    print(f" Result :\n Marks = {marks}\n Grade = D\n You Are a bit closer to your Success!!")
elif 0 <= marks <= 59:
    print(f" Result :\n Marks = {marks}\n Grade = F\n Not let the Marks demotivate You!!")
else:
    print("OUT OF THE BOUNDS:Data parameter deviation detected.")

#Question number 3.1 :

print("NOTE :\n k or K = kilograms, l or L = pounds")
units = input("Enter units of the weight needed to be converted :")
value_input = input("Enter the weight value :")
try:
    value = float(value_input)
    if units == 'k' or units == 'K':
        pounds = value * 2.204622
        print(f" Result :\n {value_input} kg = {pounds} lbs")
    elif units == 'l' or units == 'L':
        kg = value /  2.204622
        print(f"Result :\n {value_input} lbs = {kg} kg")
    else:
        print("Type Mismatch: Invalid unit signature code mapped to data stream.")
except:
    print("Type Mismatch: Invalid unit signature code mapped to data stream.")
    
#Question number 3.2 :

print("NOTE :\n C or c = Celsius, F or f = Fahrenheit,K or k = Kelvins")
source_units = input("Enter the source temperature units : (k,K,f,F,c,C)")
temperature = float(input("Enter the temperature "))
destination_units = input("Enter the destination temperature units : (k,K,f,F,c,C)")
if source_units == 'C' or source_units == 'c':
    if destination_units == 'C' or destination_units == 'c':
        celcius = temperature
        print(f" Result :\n {temperature} C = {temperature} C ")
    elif destination_units == 'K' or destination_units == 'k':
        kelvin = temperature + 273.15
        print(f" Result :\n {temperature} C = {kelvin} K")
    elif destination_units == 'F' or destination_units == 'f':
        fahrenheit = (temperature * 9/5) + 32
        print(f" Result :\n {temperature} C = {fahrenheit} F")
elif source_units == 'F' or source_units == 'f':
    if destination_units == 'F' or 'f':
        fahrenheit = temperature
        print(f" Result :\n {temperature} F = {fahrenheit} F")
    elif destination_units == 'C' or destination_units == 'c':
        celcius = (temperature - 32)* 5/9
        print(f" Result :\n {temperature} F = {celcius} C")
    elif destination_units == 'K' or destination_units == 'k':
        kelvin = (temperature - 32) * 5/9 + 273.15
        print(f" Result :\n {temperature} F = {kelvin} K")
elif source_units == 'K' or source_units == 'k':
    if destination_units == 'K' or destination_units == 'k':
        kelvin = temperature
        print(f" Result :\n {temperature} K = {kelvin}")
    elif destination_units == 'C' or 'c':
        celcius = temperature - 273.15
        print(f" Result :\n {temperature} K = {celcius}")
    elif destination_units == 'F' or 'f':
        fahrenheit = (temperature - 273.15)*9/5 + 32
        print(f" Result :\n {temperature} K = {fahrenheit}")
else:
    print("SYS_ERR: Invalid Scale Permutation Vector.")
    print("SYS_ERR: Invalid Scale Permutation Vector.")
