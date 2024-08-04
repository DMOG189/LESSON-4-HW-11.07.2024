# LESSON 4 EX 9

# FOR LOOP
# range

# x: int = 1;
# while x < 20 # condition tested before entering first cycle
#    print(x, end=" ");
#    x = x + 1;
#    # --

# START

for i in range (1, 11):
    print(i, end=" ");

total: int = 0
for i in range(1, 11):
    price: int = int(input("enter price:"));
    total = total + price
    if total > 1000:
        break


# for each loop

for c in "Hello":
    print(c, end_=_",");
print()

for i in range(1, 20, 2):
    print(i, end_=_",");
print()

for i in range(20, 1, -1):
    print(i, end_=_",");
print()

for i in range(1, 20, 1):
    print(i, end_=_",");
print()

# END