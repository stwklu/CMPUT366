# Quick script to help with calculating answers for written questions

qn = 0
alpha = 0.5
n = 1

while(True):
    print("n = " + str(n))
    reward = int(input("Reward? "))
    qnplusone = qn + alpha * (reward - qn)

    print("qn+1 = " + str(qnplusone))
    print("")

    n = n+1
    qn = qnplusone