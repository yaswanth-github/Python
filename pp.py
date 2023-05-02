import random

# list of assets
assets = ["stock1", "stock2", "stock3", "bond1", "bond2", "real estate"]

# total portfolio value
portfolio_value = 1000000

# create an empty dictionary to store the allocation for each asset
allocation = {}

# randomly select a set of assets and allocate a percentage of the total portfolio value to each asset
for asset in random.sample(assets, k=3):
    allocation[asset] = round(random.uniform(0, 1), 2)

# calculate the allocation for each asset
for asset in allocation:
    allocation[asset] = round(allocation[asset] * portfolio_value, 2)

print(allocation)
