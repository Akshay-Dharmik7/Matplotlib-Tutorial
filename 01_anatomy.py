import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]
sales = [100, 120, 150, 130]

fig, ax = plt.subplots(figsize=(8, 5))

ax.plot(months, sales, marker='o', label='Sales')

ax.set_title("Monthly Sales Report")
ax.set_xlabel("Months")
ax.set_ylabel("Sales")
ax.grid(True)
ax.legend()

plt.show()