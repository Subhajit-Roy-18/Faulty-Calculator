# PROBLEM: DESIGN A CALCULATOR WHICH WILL CORRECTLY SOLVE ALL THE PROBLEMS EXCEPT THE FOLLOWING ONES:
#          [I] 45 * 3 = 145
#          [II] 56 + 9 = 67
#          [III] 56 / 6 = 8
#         YOUR PROGRAM SHOULD TAKE THE OPERATOR AND THE TWO NUMBERS AS INPUT FROM THE USER AND THEN RETURN THE RESULT.




print("This is a calculator which will help you to solve mathematical expressions. \n")


print("Which operation do you want to carry out?")

print("For Addition, type 1")
print("For Subtraction, type 2")
print("For Multiplication, type 3")
print("For Division, type 4")

Operator = int(input())

if 4 < Operator or Operator < 1:
    print("Please Check your Input, There's an Error!!")
    exit()


print("\n Now, enter the first number you want to work with.")
N1 = float(input())

print("OK, now you can input the second one.")
N2 = float(input())


if Operator == 1 and N1 == 56 and N2 == 9:
    print(N1, "+", N2, "= 67")

elif Operator == 1:
    print(N1, "+", N2, "=", N1 + N2)


if Operator == 2:
    print(N1, "-", N2, "=", N1 - N2)


if Operator == 3 and N1 == 45 and N2 == 3:
    print(N1, "*", N2, "= 145")

elif Operator == 3:
    print(N1, "*", N2, "=", N1 * N2)


if Operator == 4 and N1 == 56 and N2 == 6:
    print(N1, "/", N2, "= 8")

elif Operator == 4:
    print(N1, "/", N2, "=", N1 / N2)



print("\n Thanks for using the calculator.")
