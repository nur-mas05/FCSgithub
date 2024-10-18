class Item:
    def __init__(self, barcode, name, price):
        self.barcode = barcode
        self.name = name
        self.price = price

inventory = {
    "001": Item("001", "Apple", 0.5),
    "002": Item("002", "Banana", 0.3),
    "003": Item("003", "Cherry", 0.2)
}
def start_receipt():
    items_purchased = []
    total_amount = 0.0

    while True:
        barcode = input("Enter item barcode: ")
        quantity = int(input("Enter quantity: "))

        if barcode in inventory:
            item = inventory[barcode]
            cost = item.price * quantity
            items_purchased.append((item.name, quantity, item.price, cost))
            total_amount += cost
        else:
            print("Item not found. Please try again.")

        add_more = input("Would you like to add another item? (yes/no): ").strip().lower()
        if add_more != 'yes':
            break

    print_receipt(items_purchased, total_amount)

def print_receipt(items_purchased, total_amount):
    print("\n--- Receipt ---")
    for name, quantity, price, cost in items_purchased:
        print(f"{name} (Qty: {quantity}, Price: ${price:.2f}) - Total: ${cost:.2f}")
    print(f"Total Amount: ${total_amount:.2f}\n")

def main():
    while True:
        start_new_receipt = input("Would you like to start a new receipt? (yes/no): ").strip().lower()
        if start_new_receipt == 'yes':
            start_receipt()
        else:
            print("Exiting the system.")
            break

if __name__ == "__main__":
    main()
