txt = "I could eat bananas all day"

x = txt.partition("apples")

print(x)

txt = "I like bananas"

x = txt.replace("bananas", "apples")

print(x)

txt = "one one was a race horse, two two was one too."

x = txt.replace("one", "three")

print(x)

txt = "one one was a race horse, two two was one too."

x = txt.replace("one", "three", 2)

print(x)

txt = "Mi casa, su casa."

x = txt.rfind("casa")

print(x)

txt = "Hello, welcome to my world."

x = txt.rfind("e")

print(x)

txt = "Hello, welcome to my world."

x = txt.rfind("e", 5, 10)

print(x)

txt = "Hello, welcome to my world."

print(txt.rfind("q"))
print(txt.rindex("q"))

txt = "Mi casa, su casa."

x = txt.rindex("casa")

print(x)

txt = "Hello, welcome to my world."

x = txt.rindex("e")

print(x)

txt = "Hello, welcome to my world."

x = txt.rindex("e", 5, 10)

print(x)

txt = "Hello, welcome to my world."

print(txt.rfind("q"))
print(txt.rindex("q"))

txt = "banana"

x = txt.rjust(20)

print(x, "is my favorite fruit.")

txt = "banana"

x = txt.rjust(20, "O")

print(x)

txt = "I could eat bananas all day, bananas are my favorite fruit"

x = txt.rpartition("bananas")

print(x)

txt = "I could eat bananas all day, bananas are my favorite fruit"

x = txt.rpartition("apples")

print(x)

txt = "apple, banana, cherry"

x = txt.rsplit(", ")

print(x)

txt = "apple, banana, cherry"

# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.rsplit(", ", 1)

print(x)

txt = "Thank you for the music\nWelcome to the jungle"

x = txt.splitlines()

print(x)

txt = "Thank you for the music\nWelcome to the jungle"

x = txt.splitlines(True)

print(x)

txt = "Thank you for the music\nWelcome to the jungle"

x = txt.splitlines(True)

print(x)

txt = "Hello, welcome to my world."

x = txt.startswith("Hello")

print(x)

txt = "Hi, welcome to my world."

x = txt.startswith(("Hello", "Hi"))

print(x)

txt = "     banana     "

x = txt.strip()

print("of all fruits", x, "is my favorite")

txt = ",,,,,rrttgg.....banana....rrr"

x = txt.strip(",.grt")

print(x)

txt = "Hello My Name Is PETER"

x = txt.swapcase()

print(x)

txt = "Welcome to my world"

x = txt.title()

print(x)

txt = "Welcome to my 2nd world"

x = txt.title()

print(x)

txt = "hello b2b2b2 and 3g3g3g"

x = txt.title()

print(x)

#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))

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
mydict = {109: 101, 83: 74, 97: 111, 111: None, 100: None, 110: None, 103: None, 104: None, 116: None}
print(txt.translate(mydict))

txt = "Hello my friends"

x = txt.upper()

print(x)

txt = "50"

x = txt.zfill(10)

print(x)

a = "hello"
b = "welcome to the jungle"
c = "10.000"

print(a.zfill(10))
print(b.zfill(10))
print(c.zfill(10))

