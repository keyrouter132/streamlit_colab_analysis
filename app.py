import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



# Load CSV files from GitHub URL
car_df = pd.read_csv("https://raw.githubusercontent.com/keyrouter132/streamlit_colab_analysis/main/cleaned_car_details_df.csv")
price_df = pd.read_csv("https://raw.githubusercontent.com/keyrouter132/streamlit_colab_analysis/main/cleaned_price_cardetails_df.csv")


# Load datasets
st.title("Car Sales Analysis Dashboard")

@st.cache_data
def load_data():
    car_df = pd.read_csv("cleaned_car_details_df.csv")
    price_df = pd.read_csv("cleaned_price_cardetails_df.csv")
    merged_df = pd.merge(car_df, price_df, on='Car_ID', how='inner')
    merged_df["Car_Age"] = 2024 - merged_df["Year"]
    return car_df, price_df, merged_df

car_df, price_df, merged_df = load_data()

# Display Data
st.write("### Car Details Dataset")
st.dataframe(car_df.head())

# 1. Most Common Car Brands
st.write("### Most Common Car Brands")
top_brands = car_df['Brand'].value_counts().head(5)
st.bar_chart(top_brands)

# 2. Brand and Transmission Types
st.write("### Transmission Types by Brand")
brand_transmission_df = car_df.groupby("Brand")["Transmission"].unique().reset_index()
st.dataframe(brand_transmission_df)

# 3. Top Locations with Most Cars Listed
st.write("### Locations with Most Cars Listed")
top_locations = car_df['Location'].value_counts().head(10)
fig, ax = plt.subplots()
sns.barplot(x=top_locations.index, y=top_locations.values, palette='cividis', ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)

# 4. Count of Cars by Fuel Type
st.write("### Count of Cars by Fuel Type")
fuel_counts = merged_df["Fuel_Type"].value_counts()
st.bar_chart(fuel_counts)

# 5. Engine Size vs. Average Price
st.write("### Engine Size vs. Average Price")
fig, ax = plt.subplots()
sns.barplot(x="Engine_cc", y="Price_USD", data=merged_df, palette='cividis', ax=ax)
st.pyplot(fig)

# 6. Depreciation: Average Price of Cars by Age
st.write("### Depreciation: Average Price of Cars by Age")
fig, ax = plt.subplots()
sns.lineplot(x="Car_Age", y="Price_USD", data=merged_df, marker="o", color="green", ax=ax)
st.pyplot(fig)

# 7. Number of Cars Sold Each Year
st.write("### Number of Cars Sold Each Year")
yearly_sales = car_df["Year"].value_counts().reset_index()
yearly_sales.columns = ["Year", "Number of Listings"]
fig, ax = plt.subplots()
sns.barplot(x="Year", y="Number of Listings", data=yearly_sales, palette='cividis', ax=ax)
st.pyplot(fig)

st.write("### Done! 🚀")
