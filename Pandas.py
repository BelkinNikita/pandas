import pandas as pd
# Using of Pandas as pd is a recommended convention for data manipulation in Python

import pyarrow as pa
import pyarrow.parquet as pq 
# Using of PyArrow as pa is a recommended convention for data manipulation in Python


# Series and DataFrame
s = pd.Series([1, 2, 3, 4, 5],  index=['a','b','c','d','e']) # each index has its own label
df = pd.DataFrame({ 
    "A": [1, 2, 3, 4, 4, 4],
    "B": [5, 6, 7, 8, 8, 8],
    "C": ["foo", "bar", "baz", "qux", "qux", "qux"] }, index=['a','b','c','d','d','d']) # Its like a dictionary, but with index operations. Each column - a single object(row)
print("Series:\n", s) # pandas array
print("DataFrame:\n", df) # pandas dictionary

# Selection
print("Head:\n", df.head(2))                       # first n rows
print("Tail:\n", df.tail(2))                       # last n rows
print("Shape:", df.shape)                          # num: rows, columns
print("Columns:", df.columns)                      # Column labels
print("Index:", df.index)                          # Row labels
print("Select column A:\n", df["A"])               # indexes of an all array and their value
print("Select multiple columns:\n", df[["A","B"]]) # val of two cols
print("Select row by index:\n", df.iloc[1])        # selects an obhect
print("Select row by label:\n", df.loc['c'])       # Label-based selection
print("Select subset:\n", df.iloc[0:2, [0,2]])     # slicing
print("Value counts of C:\n", df["C"].value_counts()) # Counts all values
print("Unique values of C:", df["C"].unique())        # returns all unique values

# Modifying 
df["D"] = df["A"] + df["B"]                        # new col
df["C"] = df["C"].str.upper()                      # mod col
print("Modified DataFrame:\n", df)
print("Drop column B:\n", df.drop("B", axis=1))    # axis=1 means col
print("Drop row 0:\n", df.drop('a', axis=0))       # axis=0 means row
print("Sort by column A:\n", df.sort_values("A"))  # Sort by single col
print("Sort by column B descending:\n", df.sort_values("B", ascending=False)) # sorts bottom -> top
grouped = df.groupby("C")                          # groups by id
print("Group by C and sum:\n", grouped.sum())      # sums all identical ids
print("Apply lambda on column A:\n", df["A"].apply(lambda x: x*2)) # lambda


# NaN
df_nan = pd.DataFrame({
    "A": [1, None, 3, None],
    "B": [4, 5, None, 7] })                        # deletes value 
print("Original with NaNs:\n", df_nan)             # creates NaN values
print("Drop rows with NaN:\n", df_nan.dropna())    # deletes rows with NaN
print("Fill NaN with 0:\n", df_nan.fillna(0))      # fill NaN as "0"

# Math
print("Describe:\n", df.describe())      # returns all stat operations
print("Mean of A:", df["A"].mean())      # Mean
print("Sum of B:", df["B"].sum())        # Sum
print("Max of D:", df["D"].max())        # Max
print("Min of D:", df["D"].min())        # Min


# Filter
print("Filter rows where A>2:\n", df[df["A"]>2])   # simple comparing
print("Filter with multiple conditions:\n", df[(df["A"]>1) & (df["B"]<8)]) # comparing with AND

# Merging and joining
df1 = pd.DataFrame({"key":["A","B","C"], "val1":[1,2,3]}) # key = col; saves col, if col includes val
df2 = pd.DataFrame({"key":["A","B","D"], "val2":[4,5,6]})
print("Merge on key:\n", pd.merge(df1, df2))              # merges cols

# Concatenation
df3 = pd.DataFrame({"A":[10,20], "B":[30,40]})                      # creates DataFrame with two rows
df4 = pd.DataFrame({"A":[50,60], "B":[70,80]})
print("Concatenate vertically:\n", pd.concat([df3, df4]))           # add vals as add cols
print("Concatenate horizontally:\n", pd.concat([df3, df4], axis=1)) # add vals as add rows

# Save / Load
df.to_csv('DataFrame.csv', index=False) # False doesn't save indexes
print("save/read.csv:\n", pd.read_csv('DataFrame.csv'))
df.to_pickle('DataFrame.pkl')
print("save/read.pkl:\n", pd.read_pickle('DataFrame.pkl'))
df.to_parquet('DataFrame.parquet')
print("save/read.parquet:\n", pd.read_parquet('DataFrame.parquet'))
