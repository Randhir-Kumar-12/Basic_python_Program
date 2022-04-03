from cgi import print_arguments


p_amout=int(input("Enter principle amount:"))
rate_of_interest=float(input("Enter rate of interest:"))
time=int(input("Enter time (in year):"))

simple_interest=(p_amout*rate_of_interest*time)/100
print("Simple interest:", simple_interest)

