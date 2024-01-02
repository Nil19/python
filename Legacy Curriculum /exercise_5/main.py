def computepay(hours, rate) :
    print("In computepay", hours, rate)
    if float_hour > 40:
        reg = rate * hours
        otp = (hours - 40.0) * (rate * 0.5)
        pay = reg + otp
    else:
        pay = hours * rate
    # print("returning",pay)
    return pay
    
hours = input("Enter Hours:")
rate = input("Enter Rate:")

float_hour = float(hours)
float_rate = float(rate)

# print(float_hour , float_rate)
total = computepay(float_hour , float_rate)

print("Pay:",total)