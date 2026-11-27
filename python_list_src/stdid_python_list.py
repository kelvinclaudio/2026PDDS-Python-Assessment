users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]

orders = [
    {"id": 1, "user_id": 1, "price": 1000},
    {"id": 2, "user_id": 2, "price": 500},
    {"id": 3, "user_id": 1, "price": 200}
]

user_orders = []
for order in orders:
    for user in users:
        if order["user_id"] == user["id"]:
            record = order.copy()
            record["name"] = user["name"]
            user_orders.append(record)

grouped = {}
for record in user_orders:
    name = record["name"]
    if name not in grouped:
        grouped[name] = {"total_price": 0, "order_count": 0}
    grouped[name]["total_price"] += record["price"]
    grouped[name]["order_count"] += 1

sorted_grouped = sorted(grouped.items(), key=lambda item: item[1]["total_price"], reverse=True)

top_name, top_stats = sorted_grouped[0]
highest_total_price_user = {
    "name": top_name,
    "total_price": top_stats["total_price"],
    "order_count": top_stats["order_count"]
}

if __name__ == "__main__":
    print(user_orders)
    print(grouped)
    print(sorted_grouped)
    print(highest_total_price_user)
