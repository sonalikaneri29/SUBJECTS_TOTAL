marks={}

x=int(input("enter num:"))
marks.update({"English": x})

x=int(input("enter num:"))
marks.update({"Hindi": x})

x=int(input("enter num:"))
marks.update({"Maths": x})

x=int(input("enter num:"))
marks.update({"Science": x})

x=int(input("enter num:"))
marks.update({"Social Science": x})

x=int(input("enter num:"))
marks.update({"Sanskrit": x})


total = sum(marks.values())

print("total marks:",total)
