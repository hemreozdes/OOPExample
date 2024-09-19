from models.product import Product

class ProductHelper:
    @staticmethod
    def createItemFromText(file_path: str) -> list:
        products = []
        with open(file_path, 'r') as file:
            for line in file:
                name, price, quantity = line.strip().split(',')
                product = Product(
                    name=name,
                    price=float(price),
                    quantity=int(quantity)
                )
                products.append(product)
        return products
    @staticmethod
    def getTotalBalance(products: list) -> float:
        total = sum([product.getTotalPrice() for product in products])
        totalWithTax = total * 1.20
        return totalWithTax