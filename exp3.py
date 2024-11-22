'''text handling'''
## string methods
# capitalize
text ="hi, welcome to python Lab"
x = text.capitalize()
print(x)
#casefold
text ="Hi, welcome to python Lab"
x = text.casefold()
print(x)
#center
text ="CSE"
x = text.center(15)
print(x)
#count
text ="hi, welcome to python Lab. let's start to code in python"
x = text.count('python')
print(x)
#endswith
text ="hi, welcome to python Lab"
x = text.endswith('hi')
y = text.endswith("Lab")
print(x)
print(y)
#expandtable
text ="PYTHON"
x = text.expandtabs(5)
text ="P\tY\tT\tH\tO\tN"
y = text.expandtabs(5)
print(x)
print(y)
#find
text ="namste,welcome to SIH"
x = text.find("vanakam")
y = text.find("SIH")
print(x)
print(y)
#index
text ="namste,welcome to SIH"
x = text.index("to")
print(x)
#is alpha num
text ="SIH1644"
text1 = "555*SIH"
x = text.isalnum()
y = text1.isalnum()
print(x)
print(y)
#is digit
text ="1245"
text1 = "sih1644"
x = text.isdigit()
y = text1.isdigit()
print(x)
print(y)
#is lower
text ="namste,welcome to SIH"
text1 ="namste,welcome to sih"
x = text.islower()
y = text1.islower()
print(x)
print(y)
#is upper
text ="NAMSTE,WELCOME TO SIH"
text1 ="namste,welcome to sih"
x = text.isupper()
y = text1.isupper()
print(x)
print(y)
#join
text =(" namste "," hi "," vanakam")
x ="#".join(text)
print(x)
# is titles
text ="namste,welcome to SIH"
text1 = "Namte , Welcome To Sih"
x = text.istitle()
y = text1.istitle()
print(x)
print(y)
#lower
text = " NAMTE , WELCOME TO SIH"
x = text.lower()
print(x)
#upper
text = "Namte , Welcome To Sih"
x = text.upper()
print(x)
## strip
text = "hello"
x = text.strip()
print("hi ",x," vanakam")
#lstrip
text = "hello"
x = text.lstrip()
print("hi ",x," vanakam")
#rstrip
text = "hello"
x = text.rstrip()
print("hi ",x," vanakam")
#replace
text = "welcome to SIH"
x = text.replace("SIH","PYTHON LAB")
print(x)
#partition
text = "welcome to SIH"
x = text.partition('to')
print(x)
#swap case
text = "Welcome To SIH"
x = text.swapcase()
print(x)