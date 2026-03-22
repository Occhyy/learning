ShoppingCart = []
PriceGuide = {
    "apple": 1.5,
    "orange": 2.0,
    "banana": 1.0,
    "milk": 3.0,
    "bread": 2.5,
    "eggs": 4.0,
    "cheese": 5.0,
    "chicken": 10.0,
    "beef": 15.0,
    "fish": 12.0,
}
while True:
    item = input("Enter an item to add to your shopping cart (or 'done' to finish): ")
    if item == "done":
        break
    elif item in PriceGuide:
        ShoppingCart.append(item)
        print(f"{item} added to cart.")
    else:
        print(f"{item} is not available in the price guide.")

    total = sum(PriceGuide[item] for item in ShoppingCart)
    print(f"Current total: ${total:.2f}")

    # kolicinski popust
    def calculate_discount(total):
        if total > 20:
            return total * 0.1  # 10% discount
        elif total > 50:
            return total * 0.2  # 20% discount
        else:
            return 0


discount = calculate_discount(total)
final_total = total - discount
print(f"Discount: ${discount:.2f}")
print(f"Final total after discount: ${final_total:.2f}")

print("Thank you for shopping with us!")
