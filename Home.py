import streamlit as st
import pandas


def app_data(title, desc, url, image):
    st.header(title)
    st.write(desc)
    img_path = f'images/{image}'
    st.image(img_path, width=300)
    link = f"[Source code]({url})"
    st.markdown(link)


st.set_page_config(layout="wide")

col1, col2 = st.columns(2)
with col1:
    st.image('naruto.jpg', width=350)

with col2:
    st.title('Ha Tran Van')
    content = """
    I am Ha Tran Van. I am 20 years old. I am a Python Developer, programmer, 
    a students as Economic University, major: E-commerce. I want to become a Professor Python Developer
    and Data Analytics.I really like working with data. I built some project.
    """
    st.info(content)

content2 = """This section includes all projects that i built from now on, in down below,
 you can see the link and some descriptions"""
st.text(content2)

col3, empty_col, col4 = st.columns([45, 10, 45])
# get data from csv file
df = pandas.read_csv('data.csv', sep=';')

for index, row in df.iterrows():
    if index % 2 == 0:
        with col3:
            app_data(row['title'], row['description'], row['url'], row['image'])
    else:
        with col4:
            app_data(row['title'], row['description'], row['url'], row['image'])

