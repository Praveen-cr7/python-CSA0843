n=int(input("enter your age:"))
if n>=18:
    print("the person is eligible")
else:
    eligibility=18-n
    print("you are  allowed to vote after",eligibility,"years")
