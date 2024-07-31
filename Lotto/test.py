import csv
myarr = [[10.3,11.2,10.7],[13.4,12.6,12.7],[12.56,14.21,11.33]]
with open("myarray.csv", "wb") as f:
	writer = csv.writer(f)
	writer.writerows(myarr)