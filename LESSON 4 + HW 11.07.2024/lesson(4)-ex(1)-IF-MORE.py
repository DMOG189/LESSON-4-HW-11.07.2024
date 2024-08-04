# LESSON 4 EX 1

# IF MORE

# 7 BOOM EX
# MORE WAYS TO DO SO


# START


# 1 first option

number = int(input("Enter a number:"));

if number % 7 == 0:
    print("7 boom");
else:
    print("NOT 7 and not boom");


# 2 if not option

if not number % 7 ==0:
    print("NOT 7 and not boom", end=" ");

print("7 boom");


# 3 if not & print f


if not number % 7 ==0:
    print("NOT 7 and not boom", end=" ");

print("NOT 7 and not boom" if not number % 7 == 0 else "" + "7 boom");

print(f"{"NOT 7 and not boom" if not number % 7 == 0 else ""}7 boom");



# END


# question ? YES = everything , NO = 0 , NONE

number1: int = int(input("please enter a number: "));

#begginer

if number1 != 0:
    print("yes")

#pro

if number:
    print("Number different than 0");

#empty

if "":
    print("empty");

#module

if not number1 % 7:
    print("number devided by 7");
 
# module options

print(("NOT " if not number1 % 7 == 0 else "") + "boom");
print(f"{"NOT " if not number1 % 7 == 0 else ""} boom");
print(f"{"NOT " if number1 % 7 else ''} boom");

