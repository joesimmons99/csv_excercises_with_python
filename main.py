import pandas as pd
import numpy as np
import glob

# import all files as one dataframe
files = glob.glob('*.csv')

# print(files) 

## Create a dataframe for each file in the directory
df_list = [] # create an empty list

for f in files: # loop through each file
    csv = pd.read_csv(f) # read the file
    df_list.append(csv) # append the dataframe to the list

sales = pd.concat(df_list) # concatenate all dataframes

## print the concatenated dataframe
# print (sales) 

## print the column types
print(sales.dtypes)

## convert the 'date' column to datetime data type
sales['date'] = pd.to_datetime(sales['date'])
print(sales.dtypes) # confirm the data type of the 'date' column has changed

# # print the 'order' column
# print(sales['order'])

# remove the '#' character from the 'order' column
sales['order'] = sales['order'].str.replace('#', '')
# print(sales['order']) # confirm the '#' character has been removed
