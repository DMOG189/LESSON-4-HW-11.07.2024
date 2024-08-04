# LESON 4 EX 7 LOOP TARGIL 3


# LOOP TARGIL
# input product prices from the user, float
# until the total price exceed 1000
# print the avg price of the products
# print how many products you have purchased
# print how muvh beyond 1000 you reached
# i.e. 1900 then print:
# "you went 900 beyond 1000"

# START

price: int = 0;
total: int = 0;
count: int = 0;

while total <= 1000:
    price = float(input("enter a product price:"));
    total = total + price;
    count = count + 1;
diff: float = total - 1_000;
print(f"\n You bought {count} products looks heavy");
print(f"\n You exceed the 1,000 by {diff}");

# END

# enter a product price:50
# enter a product price:50
# enter a product price:50
# enter a product price:40
# enter a product price:4
# enter a product price:5743
#
#  You bought 6 products looks heavy
#
#  You exceed the 1,000 by 4937.0