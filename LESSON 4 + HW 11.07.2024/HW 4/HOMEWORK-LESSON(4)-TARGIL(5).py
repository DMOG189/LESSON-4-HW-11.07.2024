# HOMEWORK LESSON 4 TARGIL 5

# while loop ex
# while loop for general python studies

# START

iq_list_before = []

while True:
    iq = int(input("Please enter an IQ value before studies (Enter a value < 30 or > 300 to stop): "));
    if iq < 30 or iq > 300:
        break
    iq_list_before.append(iq);

if len(iq_list_before) > 0:
    average_iq_before = sum(iq_list_before) / len(iq_list_before);
    print(f"The average IQ of the group before studies is: {average_iq_before:.2f}");
else:
    print("No valid IQ values were entered before studies.");
    average_iq_before = 0

print("After one year of Python studies, the group's programming skills have significantly improved!");

iq_list_after = []

while True:
    iq = int(input("Please enter an IQ value after studies (Enter a value < 30 or > 300 to stop): "));
    if iq < 30 or iq > 300:
        break
    iq_list_after.append(iq);

if len(iq_list_after) > 0:
    average_iq_after = sum(iq_list_after) / len(iq_list_after);
    print(f"The average IQ of the group after studies is: {average_iq_after:.2f}");
else:
    print("No valid IQ values were entered after studies.");
    average_iq_after = 0

if average_iq_before > 0 and average_iq_after > 0:
    increase_in_average_iq = average_iq_after - average_iq_before
    print(f"The average IQ increased by: {increase_in_average_iq:.2f}");
else:
    print("Unable to calculate the increase in average IQ due to lack of valid values.");

# END



# Please enter an IQ value before studies (Enter a value < 30 or > 300 to stop): 50
# Please enter an IQ value before studies (Enter a value < 30 or > 300 to stop): 60
# Please enter an IQ value before studies (Enter a value < 30 or > 300 to stop): 80
# Please enter an IQ value before studies (Enter a value < 30 or > 300 to stop): 90
# Please enter an IQ value before studies (Enter a value < 30 or > 300 to stop): 100
# Please enter an IQ value before studies (Enter a value < 30 or > 300 to stop): 100
# Please enter an IQ value before studies (Enter a value < 30 or > 300 to stop): 120
# Please enter an IQ value before studies (Enter a value < 30 or > 300 to stop): 300
# Please enter an IQ value before studies (Enter a value < 30 or > 300 to stop): 350
# The average IQ of the group before studies is: 112.50
# After one year of Python studies, the group's programming skills have significantly improved!
# Please enter an IQ value after studies (Enter a value < 30 or > 300 to stop): 120
# Please enter an IQ value after studies (Enter a value < 30 or > 300 to stop): 130
# Please enter an IQ value after studies (Enter a value < 30 or > 300 to stop): 130
# Please enter an IQ value after studies (Enter a value < 30 or > 300 to stop): 210
# Please enter an IQ value after studies (Enter a value < 30 or > 300 to stop): 120
# Please enter an IQ value after studies (Enter a value < 30 or > 300 to stop): 20
# The average IQ of the group after studies is: 142.00
# The average IQ increased by: 29.50