num = 0
tot = 0.0 
while True:
    sval = input('Enter a number: ')
    if sval == 'done' :
        break 
    try:
        float_value = float(sval)
    except:
        print('Invalid input')
        continue
   # print (float_value)
    num = num + 1 
    tot = tot + float_value

# print('ALL DONE')
print(tot,num,tot/num)