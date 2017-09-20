qn = 0
alpha = 1.0
n = 1

target = []
estimate = [0]

while(True):
    entry = raw_input()
    if entry == "end":
        break
    else:
        target.append(int(entry))

for i in range(len(target)):
    estimate.append(estimate[i] + alpha * (target[i] - estimate[i]))

for i in range(len(estimate)):
    print("i = " + str(i+1) + " " + str(estimate[i]))
