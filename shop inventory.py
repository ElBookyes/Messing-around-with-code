Inventory = {"Hoodie":10, "Shirt":7, "Weeb Katana":11, "Special Plushie":5}
print(Inventory)

while True:
    purchase = input("Select item:\n")
    quantity = int(input("Select Quantity of purchase:\n"))

    if purchase not in Inventory:
        print("No such item in store.Please select an available item !")
        continue
    if Inventory[purchase] > 0:
        Inventory[purchase] -= quantity
        print("Purchase was successful !!")
    else:
        print("The selected item is no longer available")
    print(Inventory)
