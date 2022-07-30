nu1 = float(input("Enter the number 1 :"))
nu2 = float(input("Enter the number 2 :"))
nu3 = float(input("Enter the number 3 :"))


if ( nu1 >= nu2 >= nu3 ):
    largest = nu1
    print("the largest number 1 is :",nu1 )
elif ( nu2 >= nu1) and (nu2 >= nu3 ):
    largest = nu2
    print("the largest number 2 is :",nu2 )
else:
    largest = nu3
    print("the largest number 3 is :",nu3 )
