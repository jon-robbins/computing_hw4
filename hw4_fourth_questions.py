###############
# Use the data in covid.csv for this exercise
#
# 10) In a separate file, write a piece of code that
# loads the covid.csv file and prints the list of countries
#  and the total average of death/confirmed among those countries
# for those countries that have more than 500, 1000 and 5000
# active cases respectively.
# Follow DRY principles in order to complete this exercise.
#
#
# #

import pandas as pd
import numpy as np

df = pd.read_csv('/Users/jon/Documents/DSDM/github/covid.csv')


# I'm not sure I understand what's being asked here. I thinnk it's asking for two functions: 1. a list of countries,
# and 2. a list of the average of deaths/confirmed cases for four groups of countries: Ones that have
# <=500 cases, ones that have >500<=1000, >1000<=5000, and >5000.

# List of all countries
countries = list(df['Country'])

# total average of death/confirmed among those countries
# for those countries that have more than 500, 1000 and 5000
# active cases respectively.

# first create the categories
df['category'] = np.where(df['Active'] > 5000, '>5000', \
                 np.where(df['Active'] > 1000, '>1000<=5000', \
                 np.where(df['Active'] > 500, '>500', '<=500')))
# Second create the aggregate table
df_summary = df.groupby('category') \
    .agg({'Deaths': 'mean', 'Confirmed': 'mean'}) \
    .rename(columns={'Deaths': 'Average Deaths', 'Confirmed': 'Average Confirmed'})

# I tried making a dict reader that would read and transform the CSV but it ended up being too inefficient. Leaving for posterity.
# from csv import DictReader
# # open file in read mode
# with open("/Users/jon/Documents/DSDM/github/covid.csv", 'r') as f:

#     #convert csv to dict
#     dict_reader = DictReader(f)
#     covid_cases = list(dict_reader)
#     #get all keys but country name to convert values to int
#     keys_to_int = list(covid_cases[0].keys())[1:]
#     for row in covid_cases:
#         for key in keys_to_int:
#             row[key] = int(row[key])


# for row in covid_cases:
#     if row['Active'] > 500:
#         print(row['Country'])
# %%
