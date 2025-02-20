import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
st.title("Car Sales Analysis Dashboard")

# Load CSV files
@st.cache_data
def load_data():
    car_details = pd.read_csv("cleaned_car_details_df.csv")
    price_details = pd.read_csv("cleaned_price_cardetails_df.csv")
    return car_details, price_details

car_df, price_df = load_data()

# Display Data
st.write("### Car Details Dataset")
st.dataframe(car_df.head())

st.write("### Price Details Dataset")
st.dataframe(price_df.head())

# Most Common Car Brands
st.write("### Most Common Car Brands")
top_brands = car_df['Brand'].value_counts().head(5)
st.bar_chart(top_brands)

# Average Price by Car Brand
st.write("### Average Price by Car Brand")
avg_price = price_df.groupby("Brand")["Price_USD"].mean().sort_values(ascending=False)
st.bar_chart(avg_price)

# Correlation Between Car Age and Price
st.write("### Correlation: Car Age vs Price")
merged_df = pd.merge(car_df, price_df, on='Car_ID', how='inner')
merged_df["Car_Age"] = 2024 - merged_df["Year"]

fig, ax = plt.subplots()
sns.scatterplot(x=merged_df["Car_Age"], y=merged_df["Price_USD"], ax=ax)
plt.xlabel("Car Age")
plt.ylabel("Price (USD)")
st.pyplot(fig)

# Transmission Type Analysis
st.write("### Transmission Type Distribution")
transmission_counts = merged_df["Transmission"].value_counts()
st.bar_chart(transmission_counts)

# Price Trends Over Years
st.write("### Price Trends Over Years")
price_trends = merged_df.groupby("Year")["Price_USD"].mean()
st.line_chart(price_trends)

st.write("### Depreciation: Average Price of Cars by Age")
age_price = merged_df.groupby("Car_Age")["Price_USD"].mean()
st.line_chart(age_price)

st.write("### Done! 🚀")
