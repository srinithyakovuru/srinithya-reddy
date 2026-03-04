
def Student_Grade_System(name,n1,n2,n3):
    average = (n1 + n2 + n3) / 3
    average =int(average*100)/100
    if average >= 40:
        Status = "Pass"
    else:
        Status = "fail"
    return f"Average grade: {average}, Status: {Status}"