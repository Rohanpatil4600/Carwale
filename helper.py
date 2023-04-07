import pandas as pd


def fetch_find(brand, fuel, city, df):
    # df = df[(df['company'] == brand) & (df['year'] == year) & (df['fuel'] == fuel) & (df['city'] == city)]
    df = df[(df['company'] == brand) & (df['city'] == city) & (df['fuel'] == fuel)]
    return df

def fetch_year_details(df):
    x=df.groupby('city').mean()['price'].index.tolist()
    y = df.groupby('city').mean()['price'].values.tolist()
    return x,y

def fetch_most_cars(df):
    x = df['car_name'].value_counts().head(10).index.tolist()
    y = df['car_name'].value_counts().head(10).values.tolist()
    return x,y
def fetch_min_max(df,Car_brand):
    x=df[df['company'] == Car_brand]['price'].max()
    y=df[df['company']==Car_brand]['price'].min()
    return x,y

def fetch_city_cars(df,Car_brand):
    x=df[df['company'] == Car_brand].groupby('city').count()['price'].index.tolist()
    y = df[df['company'] == Car_brand].groupby('city').count()['price'].values.tolist()
    return x,y

def fetch_year_cars(df,Car_brand):
    x=df[df['company'] == Car_brand].groupby('year').count()['price'].index.tolist()
    y = df[df['company'] == Car_brand].groupby('year').count()['price'].values.tolist()
    return x,y

def fetch_car_num(df,brand,city,fuel):
    x=df[(df['company']==brand) & (df['fuel']==fuel) & (df['city']==city)]['car_name'].value_counts().index.tolist()
    y=df[(df['company']==brand) & (df['fuel']==fuel) & (df['city']==city)]['car_name'].value_counts().values.tolist()
    return x,y

def fetch_year_num(df,brand,city,fuel):
    x=df[(df['company']==brand) & (df['fuel']==fuel) & (df['city']==city)]['year'].value_counts().index.tolist()
    y=df[(df['company']==brand) & (df['fuel']==fuel) & (df['city']==city)]['year'].value_counts().values.tolist()
    return x,y

def fetch_tag_details(df):
    x = df.tags.value_counts().index.tolist()[1:]
    y = df.tags.value_counts().values.tolist()[1:]
    return x,y