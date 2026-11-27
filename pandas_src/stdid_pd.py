import pandas as pd

users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]

orders = [
    {"id": 1, "user_id": 1, "price": 1000},
    {"id": 2, "user_id": 2, "price": 500},
    {"id": 3, "user_id": 1, "price": 200}
]

users_df = pd.DataFrame(users)
orders_df = pd.DataFrame(orders)

merged_df = pd.merge(users_df, orders_df, left_on="id", right_on="user_id")

grouped_sorted_df = (
    merged_df.groupby("name")
    .agg(
        total_price=("price", "sum"),
        order_count=("id_y", "count")
    )
    .sort_values(by="total_price", ascending=False)
)

highest_total_price_user = grouped_sorted_df.iloc[0]

if __name__ == "__main__":
    print("Users DataFrame:")
    print(users_df)
    print("\nOrders DataFrame:")
    print(orders_df)
    print()
    print(merged_df)
    print()
    print(grouped_sorted_df)
    print()
    print(highest_total_price_user)
