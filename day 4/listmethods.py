a = [(1,12),(4,1),(3,0),(12,10)]
def get_second_element(x):
    return x[1]
a.sort(key=get_second_element)
print(a)
    

a= [(1,2,12),(3,1,14),(1,1),(5,2,0)]
def get_last_element(x):
    return x[-1]
a.sort(key=get_last_element)
print(a)


a= [(1,2,12),(3,1,14),(1,1),(5,2,0)]
def get_last_element(x):
    return x[-1]
a.sort(key=get_last_element, reverse=True)
print(a)