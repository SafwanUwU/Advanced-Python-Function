num = int(input("Enter a random number: "))
list = []

for i in range(0, num + 1):
    list.append(i)
print(list)

oddnum = [x for x in list if x % 2 !=0]
print("Odd numbers", oddnum)

fruits = ["apple", "banana", "orange", "jackfruit", "grapes"]
uppercasedfruits = []
for fruit in fruits:
    uppercasedfruits.append(fruit.capitalize())
print(f"The uppercased Fruits: {uppercasedfruits}")
