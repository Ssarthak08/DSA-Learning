def greet(name,department,subject="RDBMS"):
    print(f"hey {name}")
    print(f"you are from {department} department")
    print(f"do you know {subject} ")


greet("Sarthak","computer science") # one way is this but we need to know order of the arguments
greet(name="anjor",department="biotech")   # when we don't know order
greet("raghav","sn")  # by default subject is rdbms because we have already mentioned


