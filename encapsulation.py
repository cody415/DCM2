class Computer:
    def __init__(self):
        self.__max_price = 1000   # private attribute

    def sell(self):
        print("Selling Price:", self.__max_price)

    def setmaxprice(self, price):
        self.__max_price = price


# Create object
c = Computer()

# Display initial price
c.sell()

# Try changing the value directly
c.__max_price = 2000   # This won't change the private attribute
c.sell()

# Use setter function to update the value
c.setmaxprice(2000)
c.sell()
