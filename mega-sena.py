import operator
num = {i: 0 for i in range(1,61)}
for bet in open("bets.txt", "r"):
    for i in bet.split("-"):
        num[int(i)]+=1
num = sorted(num.items(), key=operator.itemgetter(1), reverse=True)
print sorted([num[i][0] for i in range(0,9)])
