#BMI calculator
height=float(input("enter your height in cm"))
weight=float(input("enter your weight in kg"))
BMI=weight/(height/100)**2
print(BMI)
if(BMI<18.5):
    print("underweight")
elif(BMI>=18.5 and BMI<25):
    print("normal")
elif(BMI>=25 and BMI<30):
    print("overweight")
else:
    print("obese")
