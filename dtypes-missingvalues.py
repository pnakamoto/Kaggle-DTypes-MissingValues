import pandas as pd

reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

from learntools.core import binder; binder.bind(globals())
from learntools.pandas.data_types_and_missing_data import *
print("Setup complete.")

# Your code here
dtype = reviews.points.dtype
print(dtype)

# Check your answer
q1.check()

point_strings = reviews.points.astype(str)
print(point_strings)
# Check your answer
q2.check()

missing_price_reviews = reviews[reviews.price.isnull()]
n_missing_prices = len(missing_price_reviews)

# Cute alternative solution: if we sum a boolean series, True is treated as 1 and False as 0
#n_missing_prices = reviews.price.isnull().sum()
# or equivalently:
#n_missing_prices = pd.isnull(reviews.price).sum()

# Check your answer
q3.check()

reviews_per_region = reviews.region_1.fillna('Unknown').value_counts().sort_values(ascending=False)
print(reviews_per_region)
# Check your answer
q4.check()
