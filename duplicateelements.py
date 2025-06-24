val = ["India", "Dance", "India", "Dance", "season"]

for i in range(0, len(val)):
    for j in range(i+1, len(val)):
        if (val[i] == val[j]):
            print(val[j])