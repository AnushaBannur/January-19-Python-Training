#Sum of number digits in List

Li = [12, 13, 114, 55, 67]

print(Li)

res_Li = []

for ele in Li:
    sum1 = 0
    for digit in str(ele):
        sum1 += int(digit)
    res_Li.append(sum1)
print(res_Li)
    
