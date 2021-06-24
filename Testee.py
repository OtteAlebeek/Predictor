import streamlit as st
import pandas as pd
import numpy as np
import pickle
import gunicorn

HousePrice = pickle.load(open('Downloads/PredictNN.pkl', 'rb'))

st.write("""
# House Price Prediction Australia App

In this Application you can find out what the price of your house is right now. 

There are 6 filters where you have to filter on to see what the price of your house is.

The filters you can filter on are:

- Rooms
	- You have to filter on the amount of rooms in your house. The minimum amount of rooms is 0 and the maximum is 10
- Type
	- You have to filter on the type of your house
		- 1 = Normale House
		- 2 = Unit
		- 3 = Townhouse
- Distance
	- You have to filter on the distance to the nearest station. The distance is in meters.
- Bedrooms
	- You have to filter on the amount of bedrooms in your house. The minimum bedroom is 0 and the maximum bedrooms are 9.
- Landsize
	- You have to filter on the size of your land at the house. The landsize is in m^2.
- BuildingArea
	- You have to filter on the size of yout building area at the house. The BuildingArea is in m^2.
- Year
	- You have to filter on the year the house is build. It goes from 1830 to 2018.

Fill in the filters and see what the price of your house is.
""")

def user_input_features():
	Rooms = st.text_input("Fill in the amount of rooms", 0)
	Type = st.text_input("Fill in the type of your house", 0)
	Distance = st.text_input("Fill in the distance to nearest station (m)", 0)
	Bedroom2 = st.text_input("Fill in the amount of bedrooms in your house", 0)
	Landsize = st.text_input("Fill in the landsize (m^2)", 0)
	BuildingArea = st.text_input("Fill in the BuildingArea (m^2)", 0)
	YearBuilt = st.text_input("Fill in the year the house is built", 0)
	data = {'Rooms' : Rooms,
			'Type': Type,
			'Distance': Distance,
			'Bedrooms': Bedroom2,
			'Landsize': Landsize,
			'BuildingArea': BuildingArea,
			'YearBuilt': YearBuilt}
	features = pd.DataFrame(data, index=['Values'])
	return features

df = user_input_features()
st.write(df)

if st.button('Submit to see your predict house value'):
	HousePrice_load = HousePrice.predict(df)
	data = {'HousePrice load': HousePrice_load}
	features = pd.DataFrame(data, index=['Values $'])
	st.write(features)