from datetime import datetime

with open("test.tex", "a") as myfile:
    dateTimeObj = datetime.now()
    myfile.write(str(dateTimeObj))