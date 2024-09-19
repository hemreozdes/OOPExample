from helpers.productHelper import ProductHelper

products = ProductHelper.createItemFromText('products.txt')
totalBalance = ProductHelper.getTotalBalance(products)

print(f"Total balance with tax: {totalBalance:.2f} USD")