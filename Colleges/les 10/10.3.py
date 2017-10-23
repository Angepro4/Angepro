def doe1():
 y = 7
 x = 0
 return y
def doe2():
 global x
 x = doe1()
 x += 1
doe2()
print(x)
