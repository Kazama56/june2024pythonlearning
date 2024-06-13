# List is a mutable datatype in Python
# List is a sequence of heterogenous data separated by comma and enclosed within big brackets

# Creating non-empty list
a = [1, 2]
b = ["a", "e", "i", "o"]
v = [1, 2, "a", "Hello", [1, 2], {1, 2}, 2.2]

# Creating empty lists
x = []
print(x)
y = list()


# Accessing elements of list
# List elements can be accessed using indexing and slicing

# indexing
vowels = ["a", "e", "i", "o", "u"]

print(vowels[4]) #u
print(vowels[0]) #a
print(vowels[2]) #i
#print(vowels[10]) #indexerror

print(vowels[-1]) #u
print(vowels[-4]) #e
#print(vowels[-10]) #indexerror


# slicing
data = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

print(data[2:8]) # c d e f g h 
print(data[:7]) # abcdefg
print(data[0:9]) #abcdefghi
print(data[6:]) #ghij
print(data[7:3]) #emptylist
print(data[-8:-3]) #cdefg
print(data[-4: -2]) #gh
print(data[2:-3]) #cdefg
print(data[-9:9]) #bcdefghi
print(data[2:9:2]) #cegi