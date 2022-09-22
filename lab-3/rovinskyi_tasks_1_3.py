# Task 1

products = [ 
    ['apple', 12], ['banana', 38.5], ['bread', 20.3], 
    ['potato', 40], ['cucumber', 18.2], ['tomato', 10]
]

sum_of_purchase = 0.0

print("Welcome to our shop!\nHere is the assortment:")
for product in products:
    for info in product:
        print(info, end = ' ')
    print('UAH/kg')

chosen_product = input("Please enter the product name (enough - to stop): ").lower()
purchase = []
while chosen_product != 'enough':
    previous_sum = sum_of_purchase
    for product in products:
        if chosen_product in product:
            quantity_flag = False
            while quantity_flag == False:
                try:
                    quantity = float(input("Please enter the quantity in kilos: "))
                    if quantity <= 0.0:
                        print("Product quantity should be a positive number!")
                        continue
                    quantity_flag = True
                except ValueError:
                    print("Product quantity should be a positive number!")
            partial_sum = product[1] * quantity
            sum_of_purchase += partial_sum
            purchase.append((chosen_product, quantity, partial_sum))
  
    if previous_sum == sum_of_purchase:
        print("This product is not for sale! Choose something else!")
  
    chosen_product = input("Please enter the product name (enough - to stop): ").lower()

if sum_of_purchase != 0.0:
    print("Here is your purchase: ")
    print("------------------------")
    for item, amount, sum in purchase:
        print(f'{item} x {amount} = {sum}')
    print("------------------------")
    print(f"To pay: {sum_of_purchase} UAH")
    print("Have a nice day!")

# Task 2

grade_book = { 
    "Doroshenko": [5, 4, 4, 5, 4], "Pavliv": [3, 4, 5, 4], "Kapush": [3, 3, 2], 
    "Ugrynia": [5, 4, 3, 2, 1], "Koropetskyi": [2, 2, 3, 3, 3, 1], 
    "Pavliuk": [5, 5, 4, 5], "Bodnar": [2, 1, 2]
}
zaborgovanist = 0
for student, marks in grade_book.items():
    average = sum(marks) / len(marks)
    if average < 3:
        zaborgovanist += 1
  
    print(f"{student}'s {average = }")

zalik = { student: sum(marks) / len(marks) for student, marks in grade_book.items() }
print(f"{zaborgovanist = }")
print(zalik)

# Task 3

group = [
    {"surname": "Shevchenko", "name": "Petro", "marks": [5, 2, 5]},
    {"surname": "Kolomiets", "name": "Mariia", "marks": [4, 3, 4, 5]},
    {"surname": "Kril", "name": "Oleksandr", "marks": [4, 3, 3, 4, 3]},
    {"surname": "Ivantsiv", "name": "Tetyana", "marks": [3, 4]},
    {"surname": "Korop", "name": "Vasyl", "marks": [5, 5, 5, 4, 4, 4]}
]
print(group[0]["name"], group[0]["surname"], group[0]["marks"])
for i in group:
    print(i["surname"].ljust(12),i["name"].ljust(10),i["marks"])

for student in group:
    average = sum(student["marks"]) / len(student["marks"])
    print(f"{student['surname']}'s {average = }")

zalik = { s["surname"]:sum(s["marks"]) / len(s["marks"]) for s in group }
print(zalik)
surnames = [ student["surname"] for student in group ]
print(surnames)
print(f'Total average = {(sum(list(zalik.values())) / len(zalik))}')