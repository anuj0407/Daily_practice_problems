'''
Task: Given a dictionary of products and their prices, create a new dictionary where:
Items costing more than $100 get a 10% discount.
Items costing $100 or less get a 5% discount.
'''

prices = {"Laptop": 1200, "Mouse": 20, "Monitor": 200, "HDMI": 10}
print("Original Prices : ",prices)
#Prices after discount
new_prices = {k:((v-(v*10/100)) if v>100 else (v-(v*5/100))) for k,v in prices.items()}
print("Discounted Prices : ",new_prices)
