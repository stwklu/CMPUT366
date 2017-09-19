# Quick script to help with calculating answers for written questions

qn = 0
alpha = 1.0
n = 1

while(True):
    print("n = " + str(n))
    reward = float(input("Reward? "))
    qnplusone = qn + alpha * (reward - qn)

    print("qn+1 = " + str(qnplusone))
    print("")

    n = n+1
    qn = qnplusone