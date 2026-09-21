prices = np.array([10, 25, 8, 40, 15], dtype=float)

#1
new_prices = (prices * 0.1) + prices

#2
new_prices = prices - 2

#3
new_prices = prices * 2

#4
check_prices = prices > 20

#5
new_prices = prices[check_prices]
