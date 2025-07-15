stock_prices = {
    'TCS': 1880,
    'RELIANCE': 2500,
    'INFy': 2730,
    'HDFCBANK': 3400,
    'ITC': 1350
}

portfolio = {}

print("Welcome to the Stock Portfolio Tracker!")
print("Available stocks:", ', '.join(stock_prices.keys()))
print("Enter 'done' when finished.\n")

while True:
    stock = input("Enter stock symbol (e.g., TCS): ").upper()
    if stock == 'DONE':
        break
    if stock not in stock_prices:
        print("Stock not found in our database. Try again.")
        continue
    try:
        quantity = int(input(f"Enter quantity for {stock}: "))
        if quantity < 0:
            print("Quantity can't be negative.")
            continue
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("Please enter a valid number.")

total_value = 0
print("\nYour Portfolio Summary:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = qty * price
    total_value += value
    print(f"{stock}: {qty} shares × ₹{price} = ₹{value}")

print("\nTotal Investment Value:", total_value)

save_choice = input("\nDo you want to save the summary to a file? (yes/no): ").lower()

if save_choice == 'yes':
    filename = "portfolio_summary.csv"
    with open(filename, "w") as file:
        file.write("Stock,Quantity,Price,Value\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = qty * price
            file.write(f"{stock},{qty},{price},{value}\n")
        file.write(f"\nTotal Investment,,,{total_value}")
    print(f"Portfolio saved to '{filename}'")
