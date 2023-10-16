## The number of person in the family
N = 5

## We get the ages in a list
ages = []
for _ in range(N):
    # Let's not forget the int() to turn the text into a number
    age = int(input())
    ages.append(age) # We add the age to the list

## We count how many people are 15 or more
count = 0
for age in ages:
    if age >= 15:
        count += 1 # We increment by 1

## We display the result
print(count)
