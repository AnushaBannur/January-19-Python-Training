#Simple Interest Calculation

def Simple_Interest(p,t,r):
    Sim_Int=(p*t*r)/100
    return Sim_Int

p=float(input("Enter principal amount: "))
t=float(input("Enter time: "))
r=float(input("Enter rate: "))     

SI=Simple_Interest(p,t,r)
print("Simple Interest is = ",SI)


