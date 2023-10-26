# Write a program to produce some basic 
# statistics on sales. Ask user how many
# invoices were issued today, then repeat 
# and ask the amount of each invoice. In the
# end display the maximum and minimum value, 
# the total value, and the average.

n = int(input("Give number of invoices: "))
min = float('inf')
max = 0
sum = 0

for i in range(n):
    amount = float(input("Give amount: "))
    sum = sum + amount
    if amount > max:
        max = amount
    if amount < min:
        min = amount

print("MAX:", max)
print("MIN:", min)
print("TOTAL:", sum)
print("AVG:", sum/n)
