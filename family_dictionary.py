familia_ruiz = {'Vicente':[1.80,85,52],'Fabiana':[1.70,65,49],'Victoria':[1.72,60,17],'Lucas':[1.80,75,15]}

oldest = 0
oldest_name = "" 

lightest = 1000
lightest_name = ""

heaviest = 0
heaviest_name = ""

for k,v in familia_ruiz.items():
    if v[2]>oldest:
        oldest = v[2]
        oldest_name = k

print("the oldest is", oldest_name,oldest, "years")


for k,v in familia_ruiz.items():
    if v[1]< lightest:
        lightest = v[1]
        lightest_name = k

print("the lightest is", lightest_name,lightest, "kg")

for k,v in familia_ruiz.items():
    if v[1]> heaviest:
        heaviest = v[1]
        heaviest_name = k

print("the heaviest is ", heaviest_name,heaviest, "kg")
