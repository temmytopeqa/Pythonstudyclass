x = 1
y = 2.8
z = 1j

print(type(x))
print(type(y))
print(type(z))

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

age = 36
txt = "My name is John, I am "
print(txt)


age = 36
txt = f"My name is John, I am {age}"
print(txt)


price = 59
txt = f"The price is {price} dollars"
print(txt)


price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars"


txt = "We are the so-called \"Vikings\" from the north."

txt = "We are the so-called \"Vikings\" from the north."


txt = 'It\'s alright.'
print(txt)

txt = "This will insert one \\ (backslash)."
print(txt)

txt = "Hello\ntolu\nWorld!"
print(txt)

txt = "Hello\rWorld!"
print(txt)

txt = "Hello\tWorld!"
print(txt)

#This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt)

#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt)

#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt)

txt = "hello, and welcome to my world."

x = txt.capitalize()

print (x)

txt = "python is FUN!"

x = txt.capitalize()

print (x)

txt = "36 is my age."

x = txt.capitalize()

print (x)

txt = "Hello, And Welcome To My World!"

x = txt.casefold()

print(x)

txt = "banana"

x = txt.center(20)

print(x)

txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple")

print(x)

txt = "My name is Ståle"

x = txt.encode()

print(x)

txt = "Hello, welcome to my world."

x = txt.endswith(".")

print(x)

txt = "H\te\tl\tl\to"

x =  txt.expandtabs(2)

print(x)

txt = "Hello, welcome to my world."

x = txt.find("welcome")

print(x)

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

txt = "Company12"

x = txt.isalnum()

print(x)

txt = "Hello, welcome to my world."

x = txt.index("welcome")

print(x)

txt = "CompanyX"

x = txt.isalpha()

print(x)

txt = "My name is Ståle"

print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))

txt = "Company123"

x = txt.isascii()

print(x)

txt = "1234"

x = txt.isdecimal()

print(x)

a = "\u0030" #unicode for 0
b = "\u0047" #unicode for G

print(a.isdecimal())
print(b.isdecimal())

txt = "   "

x = txt.isspace()

print(x)

txt = "   s   "

x = txt.isspace()

print(x)

txt = "Hello, And Welcome To My World!"

x = txt.istitle()

print(x)

a = "HELLO, AND WELCOME TO MY WORLD"
b = "Hello"
c = "22 Names"
d = "This Is %'!?"

print(a.istitle())
print(b.istitle())
print(c.istitle())
print(d.istitle())

txt = "THIS IS NOW!"

x = txt.isupper()

print(x)

a = "Hello World!"
b = "hello 123"
c = "MY NAME IS PETER"

print(a.isupper())
print(b.isupper())
print(c.isupper())

myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)

myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"

x = mySeparator.join(myDict)

print(x)

txt = "banana"

x = txt.ljust(20)

print(x, "is my favorite fruit.")


txt = "banana"

x = txt.ljust(20, "O")

print(x)

txt = "Hello my FRIENDS"

x = txt.lower()

print(x)

txt = "     banana     "

x = txt.lstrip()

print("of all fruits", x, "is my favorite")

txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable))

txt = "Hi Sam!"
x = "mSa"
y = "eJo"
mytable = str.maketrans(x, y)
print(txt.translate(mytable))

txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable))

txt = "Hi Sam!"
x = "mSa"
y = "eJo"
mytable = str.maketrans(x, y)
print(txt.translate(mytable))

txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
mytable = str.maketrans(x, y, z)
print(txt.translate(mytable))

txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
print(str.maketrans(x, y, z))

txt = "I could eat bananas all day"

x = txt.partition("bananas")

txt = "I could eat bananas all day"

x = txt.partition("apples")

print(x)






