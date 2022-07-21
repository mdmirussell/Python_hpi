# n সংখ্যক সংখ্যার যোগফল

from tkinter import N


num = int(input("Enter a Number : "))

if num<0:
    print("Please Input positive number ..")
else:
    sum = 0
    while(num>0):
        # print(num)
        sum += num
        num -= 1
print("The sum is = ",sum)