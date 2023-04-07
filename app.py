import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import helper
st.set_page_config(page_title="My Streamlit App", page_icon=":sunglasses:", layout="wide", initial_sidebar_state="expanded")

#st.title('Carwale')
df = pd.read_csv('carwale_cleaned2.csv')
st.sidebar.title('Pre-Owned Cars')
option = st.sidebar.selectbox('Select One', ['Overall Analysis', 'Car_brand','Find car'])
def load_car_analysis():
    st.title('Car Analysis')
    col1, col2= st.columns(2)

    with col1:
        st.subheader('Top 10 Companies')
        fig, ax = plt.subplots()
        com=df['company'].value_counts().head(10)
        ax.bar(com.index, com.values)
        plt.xticks(rotation=90)
        st.pyplot(fig)
    with col2:
        st.subheader('Fuel Type Distribution')
        fig, ax = plt.subplots()
        com = df['fuel'].value_counts().head(3)
        ax.pie(com,labels=com.index, autopct="%0.01f%%")
        st.pyplot(fig)
    col3, col4 = st.columns(2)
    with col3:
        st.subheader('Tag Count')
        fig, ax = plt.subplots()
        x,y=helper.fetch_tag_details(df)
        ax.bar(x,y)
        plt.xticks(rotation=90)
        st.pyplot(fig)
    with col4:
        st.subheader('YoY growth in Prices')
        fig, ax = plt.subplots()
        year=df.groupby('year').mean()['price']
        ax.plot(year)
        st.pyplot(fig)
    col5, col6 = st.columns(2)
    with col5:
        st.subheader('Top 10 Cities')
        x,y= helper.fetch_year_details(df)
        fig, ax = plt.subplots()
        ax.bar(x,y)
        plt.xticks(rotation=90)
        st.pyplot(fig)
    with col6:
        st.subheader('Top 10 Cars')
        x,y= helper.fetch_most_cars(df)
        fig, ax = plt.subplots()
        ax.bar(x,y)
        plt.xticks(rotation=90)
        st.pyplot(fig)




def load_car_details(Car_brand):
    st.title(Car_brand)
    col1, col2, col3= st.columns(3)
    with col1:
        st.subheader('Number of Cars')
        num=df[df['company'] == Car_brand].shape[0]
        st.subheader(num)
    with col2:
        st.subheader('Average price')
        num_avg=round(df[df['company'] == Car_brand]['price'].mean(),2)
        st.subheader(num_avg)
    with col3:
        st.subheader('Petrol Cars')
        temp = df[df['company'] == Car_brand]
        num_petrol=temp[temp['fuel']=='Petrol'].shape[0]
        st.subheader(num_petrol)


    col4, col5, col6 = st.columns(3)
    with col4:
        st.subheader('Diesel Cars')
        temp = df[df['company'] == Car_brand]
        num_diesel = temp[temp['fuel'] == 'Diesel'].shape[0]
        st.subheader(num_diesel)

    with col5:
        st.subheader('Min Price')
        x, y = helper.fetch_min_max(df, Car_brand)
        st.subheader(y)

    with col6:
        st.subheader('Max Price')
        x, y = helper.fetch_min_max(df, Car_brand)
        st.subheader(x)

    col7, col8 = st.columns(2)
    with col7:
        st.subheader('Avalability in City')
        x,y=helper.fetch_city_cars(df,Car_brand)
        fig, ax = plt.subplots()
        ax.bar(x, y)
        plt.xticks(rotation=90)
        st.pyplot(fig)

    with col8:
        st.subheader('Car Model Year')
        x,y=helper.fetch_year_cars(df,Car_brand)
        fig, ax = plt.subplots()
        ax.bar(x, y)
        plt.xticks(rotation=90)
        st.pyplot(fig)



if option == 'Overall Analysis':
    btn = st.sidebar.button('Find Car Analysis')
    if btn:
        load_car_analysis()

elif option == 'Car_brand':
    abc = st.sidebar.selectbox('select Car Brand', sorted(df['company'].unique().tolist()))
    btn1 = st.sidebar.button('Find Car Analysis')
    if btn1:
        load_car_details(abc)

elif option== 'Find car':
    col1, col2, col3 = st.columns(3)
    brands = sorted(df['company'].unique().tolist())
    citys = sorted(df['city'].unique().tolist())
    fuels = sorted(df['fuel'].unique().tolist())
    years = sorted(df['year'].unique().tolist())
    with col1:
        brand = st.selectbox('Select Brand', brands)

    with col2:
        city = st.selectbox('Select City', citys)

    with col3:
        fuel = st.selectbox('Select Fuel type', fuels)

    data = helper.fetch_find(brand, fuel, city, df)
    if data.empty:
        st.subheader('No results Found')
    else:
        st.dataframe(data)
        col5,col6 = st.columns(2)
        with col5:
            st.subheader('Car-Model Distribution')
            x, y = helper.fetch_car_num(df,brand,city,fuel)
            fig, ax = plt.subplots()
            ax.bar(x, y)
            plt.xticks(rotation=90)
            st.pyplot(fig)
        with col6:
            st.subheader('Year-wise distribution')
            x, y = helper.fetch_year_num(df,brand,city,fuel)
            fig, ax = plt.subplots()
            ax.bar(x, y)
            plt.xticks(rotation=90)
            st.pyplot(fig)



else:
    st.title('give Overview of project')
