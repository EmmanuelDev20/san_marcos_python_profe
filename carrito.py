class Cart:
  def __init__(self):
    self.items = {}

  def add_item(self, item_name, price, quantity=1):
    if item_name in self.items:
      self.items[item_name]['quantity'] += quantity
    else:
      self.items[item_name] = {'price': price, 'quantity': quantity}

  def remove_item(self, item_name, quantity=None):
    if item_name in self.items:
      if quantity is None or self.items[item_name]['quantity'] <= quantity:
        del self.items[item_name]
      else:
        self.items[item_name]['quantity'] -= quantity

  def calculate_total(self):
    return sum(item['price'] * item['quantity'] for item in self.items.values())

  def show_cart(self):
    if not self.items:
      print("Your cart is empty.")
    else:
      print("Your cart contains:")
      for item_name, details in self.items.items():
        print(f"- {item_name}: ${details['price']} x {details['quantity']}")

  def clear_cart(self):
    self.items.clear()
    print("Your cart has been cleared.")