import csv
import matplotlib.pyplot as plt

# Read the Data from CSV File
fruits = []
retail_prices = []

with open('Fruit Prices 2020.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  #Skip the header row
    for row in csv_reader:
        fruits.append(row[0])
        retail_prices.append(float(row[2]))  #Assuming retail price is in column index 2

#Create the Bar Chart
plt.bar(fruits,retail_prices)

#Customize the Chart
plt.title("Retail Price Comparison of All Fruits")
plt.xlabel("All Fruits")
plt.ylabel("Retail Price in Dollars ($)")
plt.xticks(rotation=45, ha = 'right')  #Rotate x-axis labels for better visibility
plt.subplots_adjust(bottom=0.3) #Display the Chart
plt.show()
