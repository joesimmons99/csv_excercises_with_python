import re
import pandas as pd
import numpy as np
import glob
import os

# import all files from the "files" folder as one dataframe
files = glob.glob("files/*.csv")

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

# # remove the '#' character from the 'order' column
sales['order'] = sales['order'].str.replace('#', '')
# print(sales['order']) # confirm the '#' character has been removed

# create a pivot table to show the total sales for each product
total_sales = pd.pivot_table(sales, index='item', values='qty', aggfunc=np.sum)
sales_by_vendor = pd.pivot_table(sales, index=['vendor'], values='qty', aggfunc=np.sum)
sales_by_vendor_and_item = pd.pivot_table(sales, index=['vendor', 'item'], values='qty', aggfunc=np.sum)

# print the pivot table and order by the total sales in descending order
print(total_sales.sort_values(by='qty', ascending=False))
print(sales_by_vendor.sort_values(by='qty', ascending=False))

# write the pivot table to a csv file and order by total sales in descending order and place it in the 'files' folder
# sort the pivot table by total sales in descending order
# if the files below exist, delete them first before writing the new pivot table
total_sales.sort_values(by='qty', ascending=False).to_csv('files/total_sales.csv')
sales_by_vendor.sort_values(by='qty', ascending=False).to_csv('files/sales_by_vendor.csv')
sales_by_vendor_and_item.sort_values(by='qty', ascending=False).to_csv('files/sales_by_vendor_and_item.csv')
