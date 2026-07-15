import matplotlib.pyplot as plt
products = ["Laptop","Phone","Tablet","Watch"]
sales = [120,180,90,150]
plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
plt.bar(products, sales, color="green")
plt.title("Product Sales")
plt.xlabel("Products")
plt.ylabel("Units Sold")
plt.grid(axis="y")
plt.subplot(1,2,2)
plt.hist(sales, bins=4, color="orange")
plt.title("Sales Distribution")
plt.xlabel("Units Sold")
plt.ylabel("Frequency")
plt.grid()
plt.tight_layout()
plt.show()