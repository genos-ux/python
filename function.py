def calculate_discount(price,discount_percent):
    if(discount_percent >= 0.2):
        return price * discount_percent

    return price

print(calculate_discount(1000,0.1))

