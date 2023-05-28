import streamlit as st
import pandas as pd
import plotly_express as px

df = pd.read_csv('vehicles_us.csv')
df['manufacturer'] = df['model'].apply(lambda x: x.split()[0])

# For model_year
df['model_year'] = df.groupby('model')['model_year'].transform(lambda x: x.fillna(x.median()))

# For cylinders
df['cylinders'] = df.groupby('model')['cylinders'].transform(lambda x: x.fillna(x.median()))

# For odometer
df['odometer'] = df.groupby(['model_year', 'model'])['odometer'].transform(lambda x: x.fillna(x.mean()))

# For paint_color
df['paint_color'] = df['paint_color'].fillna('no info')

# For is_4wd
data['is_4wd'] = data['is_4wd'].fillna(0)


# create a text header above the dataframe
st.header('Data viewer') 
# display the dataframe with streamlit
st.dataframe(df)

st.header('Vehicle types by manufacturer')
# create a plotly histogram figure
fig = px.histogram(df, x='manufacturer', color='type')
# display the figure with streamlit
st.write(fig)

st.header('Histogram of `condition` vs `model_year`')
fig = px.histogram(df, x='model_year', color='condition')
st.write(fig)

st.header('`Scatter of model_year` vs `odometer`')
fig = px.scatter(df, x='model_year', y='odometer')
# Display the plot
st.plotly_chart(fig)