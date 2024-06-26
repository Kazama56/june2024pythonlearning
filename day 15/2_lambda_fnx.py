students = [
    {"name": "Jon", "age": 15, "address": "KTM"},
    {"name": "Jane", "age": 20, "address": "PKR"},
    {"name": "Alex", "age": 27, "address": "BKT"},
    {"name": "Hary", "age": 10, "address": "LTP"},
    {"name": "Arya", "age": 17, "address": "DHD"},
]
# def get_element(students):
#     return students["age"]
# students.sort(key = get_element)

students.sort(key=lambda student:student["age"])

print(students) 
