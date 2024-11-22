# read mode
'''file = open("exp4.txt",mode = "r")
print(file.read())
file.close()'''
# write Mode
'''file = open("exp4.txt",mode = "w")
file.write(input("enter the Text : "))
file.close()'''
# read and write mode
'''file = open("exp4.txt",mode = "r+")
print(file.read())
file.write(input("enter text: "))
file.close()'''
# write and read mode
'''file =open("exp4.txt",mode = "w+")
file.write(input("enter text: "))
file.seek(0)
print(file.read())
file.close()'''
#append
file = open("exp4.txt",mode = "a")
file.write(input("enter text: "))
file.close()

