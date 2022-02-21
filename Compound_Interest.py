#Compound Interest Calculation


#Formula to calculate compound interest annually is given by: 
#A = P(1 + R/100)^t 
#Compound Interest = A – P 
#Where, 
#A is amount 
#P is principle amount 
#R is the rate and 
#T is the time span

def Compound_Interest(p,t,r):
    A=p*pow((1+r/100),t)
    Comp_Int=A-p
    return Comp_Int

p=float(input("Enter initial principal amount : "))
t=float(input("Enter the time span : "))
r=float(input("Enter interest rate : "))

CI=Compound_Interest(p,t,r)
print("Compound_Interest is = ",CI)

