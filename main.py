from pyscript import display, document

def create_order(e):
    # Get customer info
    name = document.getElementById("cust_name").value
    address = document.getElementById("cust_address").value
    contact = document.getElementById("cust_contact").value

    # Menu items (checkbox id : label, price)
    menu = {
        "carbonara": ("Carbonara", 100),
        "garlic": ("Garlic Bread", 50),
        "salad": ("Caesar Salad", 80),
        "icedtea": ("Iced Tea", 40),
        "water": ("Sparkling Water", 30)
    }

    total = 0
    ordered_items = []

    # Check selected items
    for item_id, (label, price) in menu.items():
        checkbox = document.getElementById(item_id)
        if checkbox.checked:
            ordered_items.append(label)
            total += price

    # Build output message
    items_list = ", ".join(ordered_items) if ordered_items else "No items selected"
    order_message = f"""
    Order for: {name}
    Address: {address}
    Contact number: {contact}
    Ordered Items: {items_list}
    Total: ₱ {total:.2f}
    """

    # Clear previous result
    display("", target="output")

    # Show result
    display(order_message, target="output")
