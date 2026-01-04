# PRINT
print("Data Engineering")
print('Python',3)
print("Hello",1,"Bye",sep=',')
print()

print("Hello 'Santhosh'. How are you ?")
print('Hello \'Santhosh\'. How are you ?')
print()

print('''multi line
string ''')
print("""multi line
string """)
print()

# VARIABLES
first_name="Santhosh"
last_name=" Murugadoss"
print(first_name+last_name)

a,b,c = 10,20,30    # multiple asignments
x = y = z = 5
''' multi line
comment '''
print(a,b,c)
print(x,y,z)

total_sum = 10+20\
            +30+40+50
sum = (10+20
      +30+40+50)
print(total_sum)
print(sum)
print()

# TYPE CASTING
num = "10"
print(type(num))
new_num = int(10)    # explicit
print(type(new_num))

num1 = 10
num2 = 20.5
print(num1+num2)    # implicit
print()

# STRING FORMATTING
s = "Santhosh Murugadoss"
print(s[0:9])
print(s[0:len(s)])
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.replace("sh","z"))
my_list = s.split(" ")
print(my_list)

file = "raw_data.csv"
if file.endswith(".csv"):
    print("CSV File")
if file.startswith("raw"):
    print("Raw File")

statement = "Hello Santhosh. What are you doing. Hey Santhosh I am talking to you"
print(statement.count("Santhosh"))

var1 = "hello"
var2 = "10"
var3 = "10abc"
print(var1.isnumeric())
print(var2.isnumeric())
print(var3.isalnum())
print()

# name = "santhosh"
# age = 22
# greet = f"hello {name}, your age is {age}"
# print(greet)
# print()

# CONDITIONS
x = 10
if x==10:
    print("equal to 10")
elif x<10:
    print("less than 10")
else:
    print("greater than 10")
print()

# LOOPS
table_list = ["Products","Orders","Customers"]
for i in table_list:
    print(i)

x = 1
while (x<=10):
    print(x)
    x = x+1
