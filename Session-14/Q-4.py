orders = {}

def add_order(order_id, restaurant, items, total):

    orders.setdefault(order_id, {
        "Restaurant" : restaurant,
        "Items" : items,
        "Total" : total
    })
def update_total(order_id, new_total):

    if order_id in orders:
        orders[order_id]["total"] = new_total
    else :
        print("Order not found")

add_order(
    101,
    "Dominos",
    ["Pizza", "Garlic Bread"],
    450
)

add_order(
    102,
    "Swiggy Restaurant",
    ["Burger", "Fries"],
    300
)

update_total(101,500)

print(orders)