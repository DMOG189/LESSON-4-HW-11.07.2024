# LLESON 4 EX 6 LOOP TARGIL 2


# input grades until got -1
# calculate avg.

# START

grade: int = 0;
sum: int = 0;
count: int = 0;
grade = int(input("Enter Grade:"));

while grade >= 0 and grade <= 100:
    sum = sum + grade;
    count = count + 1;
    grade = int(input("Enter Grade:"));
    # jump to top
avg: float = sum / count
print(f"\nthe average is: {avg}");

# END