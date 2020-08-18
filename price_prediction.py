import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

data = pd.read_csv('cars.csv')

# Modifying data to dake all required fields numeric
data['Age'] = 2020 - data['Year']
data['Transmission'] = data['Transmission'].str.replace('Manual', '0',)
data['Transmission'] = data['Transmission'].str.replace('Automatic', '1')
data['Fuel_Type'] = data['Fuel_Type'].str.replace('Petrol', '0')
data['Fuel_Type'] = data['Fuel_Type'].str.replace('Diesel', '1')
data['Fuel_Type'] = data['Fuel_Type'].str.replace('CNG', '2')
data['Seller_Type'] = data['Seller_Type'].str.replace('Dealer', '0')
data['Seller_Type'] = data['Seller_Type'].str.replace('Individual', '1')

# Removing unwanted data
unwanted = ['Car_Name', 'Year']
data.drop(unwanted, axis=1, inplace=True)

y = data['Selling_Price']
X = data.drop('Selling_Price', axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y)

RFreg = RandomForestRegressor(max_features=5, max_depth=8, random_state=0).fit(X_train, y_train)

print('Train Score:', RFreg.score(X_train, y_train))
print('Test Score:', RFreg.score(X_test, y_test))

print('\nPridiction for user defined features:')
p = input('Original Price in Lakhs: ')
kms = input('Kms Driven: ')
fuel = input('Fuel Type (0:Petrol, 1:Diesel, 2:CNG): ')
seller = input('Seller Type (0:Dealer, 1:Individual): ')
trans = input('Transmittion Type (0:Manual, 1:Automatic): ')
own = input('Owners before you: ')
age = input('Age of the car: ')
print('\nValue = %.2f Lakhs'% RFreg.predict([[p, kms, fuel, seller, trans, own, age]]))

