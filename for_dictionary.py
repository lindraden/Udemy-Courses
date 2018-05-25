student = {
    "male": ["Anthony", "Dom", "Andre", "Michael", "Nathan"],
    "female": ["Grace", "Sarah", "Amelia", "Christine"]
}

for key in student.keys():
    for name in student[key]:
        if "a" in name:
            print(name)
