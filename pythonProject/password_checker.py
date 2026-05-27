a=input("Password:")
b=input("Confirm Password:")
flag1=0
if a.isalnum() and b.isalnum():
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                flag1 += 1
            else:
                break
    flag1 = flag1 / len(a)
    if flag1 == len(a) and flag1 == len(b):
        print("Same password")
    else:
        print("Please enter same password")
else:
    print("Password must contain number")