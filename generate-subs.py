import csv
import random

f = open("/tmp/subs.csv", "w+")
w = csv.writer(f)
w.writerow(["email", "name", "status", "attributes"])

for n in range(0, 100000):
	w.writerow([
		"user%d@mail.com" % (n,),
		"First%d Last%d" % (n, n),
		"enabled",
		"{\"age\": %d, \"city\": \"Bangalore\"}" % (random.randint(20,70),)
	])
