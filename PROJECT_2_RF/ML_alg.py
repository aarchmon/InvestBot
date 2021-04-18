# Import statements
import pandas as pd
import numpy as np

# Create a Pandas DataFrame containing closing prices for stock FNTK
fntk_df = pd.DataFrame(
    {"close": [30.05, 30.36, 30.22, 30.52, 30.45, 31.85, 30.47, 30.60, 30.21, 31.30]}
)

# Review the DataFrame
fntk_df

# Set the index as datetime objects starting from 2019-09-09, but only for business days
fntk_df.index = pd.bdate_range(start='2019-09-09', periods=10)

# Review the DataFrame
fntk_df


# Initialize trade_type column to track buys and sells
fntk_df["trade_type"] = np.nan

# Initialize variable to hold previous day's trading price
# Set the initial value of the previous_price to 0
previous_price = 0

# Loop through the Pandas DataFrame and initiate a trade at each iteration
for index, row in fntk_df.iterrows():

    # buy if the previous_price is 0, in other words, buy on the first day
    if previous_price == 0:
        fntk_df.loc[index, "trade_type"] = "buy"

    # buy if the current day's price is less than the previous day's price
    elif row["close"] < previous_price:
        fntk_df.loc[index, "trade_type"] = "buy"

    # sell if the current day's price is greater than the previous day's price
    elif row["close"] > previous_price:
        fntk_df.loc[index, "trade_type"] = "sell"

    # hold if the current day's price is equal to the previous day's price
    else:
        fntk_df.loc[index, "trade_type"] = "hold"

    # update the previous_price to the current row's price
    previous_price = row["close"]

    # if the index is the last index of the DataFrame, sell
    if index == fntk_df.index[-1]:
        fntk_df.loc[index, "trade_type"] = "sell"
# Review the DataFrame
fntk_df


# Initialize trade_type column to track buys and sells
fntk_df["trade_type"] = np.nan

# Initialize a cost/proceeds column for recording trade metrics
fntk_df["cost/proceeds"] = np.nan

# Initialize share size and accumulated shares
share_size = 100
accumulated_shares = 0

# Initialize variable to hold previous price
previous_price = 0

# Loop through the Pandas DataFrame and initiate a trade at each iteration
for index, row in fntk_df.iterrows():

    # buy if the previous_price is 0, in other words, buy on the first day
    if previous_price == 0:
        fntk_df.loc[index, "trade_type"] = "buy"

        # calculate the cost of the trade by multiplying the current day's price
        # by the share_size, or number of shares purchased
        fntk_df.loc[index, "cost/proceeds"] = -(row["close"] * share_size)

        # add the number of shares purchased to the accumulated shares
        accumulated_shares += share_size

    # buy if the current day's price is less than the previous day's price
    elif row["close"] < previous_price:
        fntk_df.loc[index, "trade_type"] = "buy"

        # calculate the cost of the trade by multiplying the current day's price
        # by the share_size, or number of shares purchased
        fntk_df.loc[index, "cost/proceeds"] = -(row["close"] * share_size)

        # add the number of shares purchased to the accumulated shares
        accumulated_shares += share_size

    # hold if the current day's price is greater than the previous day's price
    elif row["close"] > previous_price:
        fntk_df.loc[index, "trade_type"] = "hold"

    # hold if the current day's price is equal to the previous day's price
    else:
        fntk_df.loc[index, "trade_type"] = "hold"

    # update the previous_price to the current row's price
    previous_price = row["close"]

    # if the index is the last index of the DataFrame, sell
    if index == fntk_df.index[-1]:
        fntk_df.loc[index, "trade_type"] = "sell"

        # calculate the proceeds by multiplying the last day's price by the accumulated shares
        fntk_df.loc[index, "cost/proceeds"] = row["close"] * accumulated_shares

# Review the DataFrame
fntk_df