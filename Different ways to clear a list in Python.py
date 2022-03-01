#Different ways to clear a list in Python

Li1 = [1,2,3,4,5]

#clear a list using clear() method
print("Li1 before clearing : ", Li1)
Li1.clear()
print("Li after clearing : ", Li1)


Li2 = [1,2,3,4,5,6]

#clear a list using reinitialization
print("Li2 before clearing : ", Li2)
Li2 = []
print("Li after reinitialization : ", Li2)

Li3 = [1,2,3,4,5,6,7]

#clear a list using *= 0 method
print("Li3 before clearing : ", Li3)
Li3 *= 0
print("Li after *= 0 : ", Li3)
