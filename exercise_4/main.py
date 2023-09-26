name = input('Enter your name:')
hours = input("Enter Hours:")
rate = input("Enter Rate:")

try:
    float_hour = float(hours)
    float_rate = float(rate)
except:
    print("Error, please enter numeric input")
    quit()

print(float_hour , float_rate)
if float_hour > 40:
    reg = float_rate * float_hour
    otp = (float_hour - 40.0) * (float_rate * 0.5)
    total = reg + otp
else:
    total = float_hour * float_rate
print("Hello",name, "Here's Your Pay:",total)