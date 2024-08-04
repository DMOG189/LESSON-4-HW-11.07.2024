# LESSON 4 EX 8

# DO WHILE LOOP


# input 3 numbers in a loop a, b, c
# until a * 2 + b > c-1

# code
# while
# code

a: int
b: int
c: int = 0
while True:
    a = float(input("enter a:"));
    b = float(input("enter b:"));
    c = float(input("enter c:"));
    print(f"a: {a} b: {b} c: {c}");
    if a * 2 + b <= c-1:
        break

print("finish")


# END