# Quick script to help with calculating answers for written questions

qn = 0
n = 1.0

while(True):
    alpha = float(1/n)
    print("n = " + str(n))

    reward = float(input("Reward? "))
    qnplusone = qn + alpha * (reward - qn)

    print("qn+1 = " + str(float(qnplusone)))
    print("")

    n = float(n+1)
    qn = qnplusone