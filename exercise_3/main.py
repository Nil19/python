name = input('Enter your name:')
hours = input("Enter Hours:")
rate = input("Enter Rate:")

float_hour = float(hours)
float_rate = float(rate)

# print(float_hour , float_rate)
if float_hour > 40:
    # print("Overtime")
    reg = float_rate * float_hour
    otp = (float_hour - 40.0) * (float_rate * 0.5)
    # print(reg,otp)
    total = reg + otp
else:
    # print("Regular")
    total = float_hour * float_rate
print("Hello",name, "Here's Your Pay:",total)