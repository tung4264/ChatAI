import math
iN = input()
count = 1
lstLastNum = [0, 1, 4, 5, 6, 9]
lstRusult = []
def last_digit(num):
    num_str = str(num)
    last_digit_unsigned = int(num_str[-1])
    return -last_digit_unsigned if (num < 0) else last_digit_unsigned
for i in range(int(iN)):    
    if last_digit(i) in lstLastNum and math.modf(math.sqrt(i))[0] == 0:
        j=2
        while j <= math.sqrt(i):
            if (i/j).is_integer:
                # lstRusult.append("("+str(j)+","+str(int(i/j))+");")
                count+=2
            j = j+1
            
print(count)