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

print(oldest_name,oldest)


for k,v in familia_ruiz.items():
    if v[1]< lightest:
        lightest = v[1]
        lightest_name = k

print(lightest_name,lightest)

for k,v in familia_ruiz.items():
    if v[1]> heaviest:
        heaviest = v[1]
        heaviest_name = k

print(heaviest_name,heaviest)
