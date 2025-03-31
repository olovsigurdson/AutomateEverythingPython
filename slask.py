import time
import datetime

string = "20/01/2020"

element = datetime.datetime.strptime(string, "%d/%m/%Y")

timestamp = time.mktime(element.timetuple())

#print(timestamp)

dict = {"Olov": 50}
print(dict["Olov"])
print(dict.get("Olov"))