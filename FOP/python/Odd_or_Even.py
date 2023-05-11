def odd_or_even(number):
    if (number&1==1):
        return "Odd";
    return "Even";

#User input -> number
number = int(input("Enter number: "));
print("The given number is {}".format(odd_or_even(number)));
