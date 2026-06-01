marks = {
    "Santosh": 100,
    "Ram": 34,
    "Rohan": 57
}

print(type(marks), marks["Santosh"])

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Rohan": 60})
print(marks)