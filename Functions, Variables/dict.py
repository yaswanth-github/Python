students={
    "BH1":"yaswanth",
    "BH2":"jaswanth",
    "BH3":"pranay",
    "BH4":"pavan"
    }
print("")
print(students)
print("")

for student in students:
    print(student, students[student], sep=" - ")

print("")
lpu=[
    {"name":"yaswanth","hostal":"BH4","bed":None},
    {"name":"jaswanth","hostal":"BH4","bed":"C"},
    {"name":"pranay","hostal":"BH4","bed":None},
    {"name":"pavan","hostal":"BH4","bed":None}
]

print(lpu)
print("")

for i in lpu:
    print(i["name"],i["hostal"],i["bed"], sep=" - ")
print("")

