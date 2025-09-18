w=float(input("enter your weight in kg:"))
h=float(input("enter your height in meters:"))
bmi=w/(h*h)
print("your bmi is:",bmi)
if bmi<14.5:
  print("your are less weight.")
elif bmi<20.9:
  print("your are strong.")
elif bmi<25.5:
  print("your are healthy.")
elif bmi<30.0:
  print("your are over age.")

else:
  print("you are obese")