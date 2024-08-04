# HOMEWORK LESSON 4 TARGIL 4

# START

# EX 1
# for loop ex
# print the numbers from 10 to 20
# 10 11 12 13 14 15 16 17 18 19 20

for i in range(20, 9, -1):
    print(i);

# 20
# 19
# 18
# 17
# 16
# 15
# 14
# 13
# 12
# 11
# 10

# EX 2
# now print from 10 to 20
# in skips of 2

for i in range(20, 9, -2):
    print(i);

# 20
# 18
# 16
# 14
# 12
# 10

# EX 3
# now input a step from user
# print the range from user

step = int(input("Please enter the step value: "));

for i in range(20, 9, -step):
    print(i);

# Please enter the step value: 3
# 20
# 17
# 14
# 11

# EX 4
# input a start and finish point and a step
# print accordingly

start = int(input("Please enter the starting number: "));
end = int(input("Please enter the ending number: "));
step = int(input("Please enter the step value: "));

if start > end:
    for i in range(start, end - 1, -step):
        print(i);
else:
    for i in range(start, end + 1, step):
        print(i);

# Please enter the starting number: 30
# Please enter the ending number: 20
# Please enter the step value: 3
# 30
# 27
# 24
# 21


# END