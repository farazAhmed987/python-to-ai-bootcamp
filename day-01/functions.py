def greet(name="Student"):
    print(f"Hello, {name}!")
greet("Akif")
greet()


def introduce(name, age):
    print(f"My name is {name}, and I am {age}.")
introduce(age=20, name="Akif")


// my part

def calculate_discount(price, discount=10):
    final_price = price - (price * discount / 100)
    return round(final_price, 2)


price = 2500
discounted_price = calculate_discount(price, 15)

print("Original Price:", price)
print("Discounted Price:", discounted_price)
print("Default Discount Price:", calculate_discount(price))
