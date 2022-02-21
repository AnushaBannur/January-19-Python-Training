#recursion using print statement inside the if condition prints the result every time the tri_recursion function is being called

def tri_recursion_1(k):
  if(k>0):
    result = k+tri_recursion_1(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results of tri_recursion_1")
tri_recursion_1(6)



#recursion using return inside the if condition prints the entire calculation as one result

def tri_recursion_2(k):
  if(k>0):
    result = k+tri_recursion_2(k-1)
    return result
  else:
    return 0
  
res=tri_recursion_2(6)
print("\n\nRecursion Example Results of tri_recursion_2 =",res)

