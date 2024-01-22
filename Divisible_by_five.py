# Display numbers divisible by 5 from a list

# List
List_of_numbers=[10, 20, 45, 67, 15]
# Divisible by 5
print("Numbers that divisible by 5:")
for numbers in List_of_numbers: 
    if numbers % 5 == 0:
        print( numbers)
    