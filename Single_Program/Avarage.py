#কতগুলো সংখ্যা ইনপুট নিয়ে গড় নির্ণয়

num = [0,1,2,3]

num[0] = int(input("Please enter 1st number : "))
num[1] = int(input("Please enter 2st number : "))
num[2] = int(input("Please enter 3rd number : "))
num[3] = int(input("Please enter 4st number : "))

avarage = (
   (num[0]+
    num[1]+
    num[2]+
    num[3])/4
    )
print("Avarage value is = ",avarage)
