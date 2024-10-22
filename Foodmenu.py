menu = {
    'Pizza': 280,
    'samosa': 20,
    'chai': 10,
    'pav bhaji': 50,
    'dahi bada': 90,
    'chaumeen': 70,
    'Chhole-kulchhe': 150
}

print("-----------SWAGAT-----------\n Welcome nhi karoge hamra...🧐")
for item, price in menu.items():
    print(f"{item} : {price}")

total_order = 0

item_1 = input("Kya khaoge/pioge babua? ")
if item_1 in menu:
    total_order += menu[item_1]
    print(f"Ordered item {item_1} added....!")

else:
    print(f"Sorry, {item_1} is not available yet!")

another_item = input("Apko kuchh aur chahiye? (Ha/Na): ")
if another_item.lower() == "ha":
    item_2 = input("Enter the name of 2nd item: ")
    if item_2 in menu:
        total_order += menu[item_2]
        print(f"Ordered item {item_2} added....!")
    else:
        print(f"Sorry, {item_2} is not available!")
else:
    print("Order finalized.")

print(f"Total kharcha = {total_order}")
