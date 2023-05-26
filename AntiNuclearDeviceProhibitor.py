class Product:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

class AntiNuclearDeviceProhibitor:
    def __init__(self):
        self.prohibited_keywords = ['nuclear', 'atomic', 'radioactive']

    def is_product_allowed(self, product):
        for keyword in self.prohibited_keywords:
            if keyword in product.name.lower() or keyword in product.description.lower():
                return False
        return True

# Sample usage
if __name__ == "__main__":
    prohibitor = AntiNuclearDeviceProhibitor()

    products = [
        Product('p1', 'Toy Robot', 'A fun and safe toy robot for kids.'),
        Product('p2', 'Atomic Energy Lab Kit', 'Learn about atomic energy with this educational kit.'),
        Product('p3', 'Radioactive Material', 'A sample of radioactive material for educational purposes.'),
    ]

    for product in products:
        if prohibitor.is_product_allowed(product):
            print(f"Product {product.id} ({product.name}) is allowed.")
        else:
            print(f"Product {product.id} ({product.name}) is NOT allowed.")
