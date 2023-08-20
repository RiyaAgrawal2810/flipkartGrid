import streamlit as st

import pickle
import pandas as pd
from PIL import Image
import urllib.request
# from flask import Flask, render_template_string
st.set_page_config(
    layout="wide",
    page_icon=None,
    initial_sidebar_state="collapsed",
    menu_items={
        "Get help": None,       # This will remove the "Get help" item
        "Report a bug": None,   # This will remove the "Report a bug" item
        "About": None           # This will remove the "About" item
    }
)


def im(h):
    urllib.request.urlretrieve(h, 'image.jpg')
    img = Image.open('image.jpg')
    return img
    # display(Image(url=h))


def recommend(item):
    print(item)
    print(products['title'] == item)
    d = (products['title'] == item)
    prod_idx = products[d].index[0]
    distances = similarity[prod_idx]
    prod_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:50]

    recommended_product = []
    recommended_product_posters = []

    for i in prod_list:
        im(products.iloc[i[0]].images)
        recommended_product.append(products.iloc[i[0]].title)
        recommended_product_posters.append(im(products.iloc[i[0]].images))
    return recommended_product, recommended_product_posters


similarity = pickle.load(open('similarity.pkl', 'rb'))

# st.title('Product Recommendation System')


def custom_css(css_string: str):
    """Inject custom CSS into the Streamlit app."""
    st.markdown(f"<style>{css_string}</style>", unsafe_allow_html=True)


# Adjust the height of the Streamlit header bar
custom_css("""
    .reportview-container .main .block-container {
        margin-top: -20px;
    }
    header .toolbar {
        height: 10px; 
        line-height: 10px;
    }
    header .toolbar img {
        height: 10px;
    }
""")
st.markdown("""
<style>
    div[role="listbox"] {
        width: 540px !important;
    }
    div.row-widget.stWidget {
        padding: 0 !important;
        margin: 0 !important;
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

products_dict = pickle.load(open('product_dict.pkl', 'rb'))
products = pd.DataFrame(products_dict)
selected_product_name = st.selectbox('', products['title'].values)


if st.button('Recommend'):
    names, posters = recommend(selected_product_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])

    col11, col21, col31, col41, col51 = st.columns(5)
    with col11:
        st.text(names[5])
        st.image(posters[5])
    with col21:
        st.text(names[6])
        st.image(posters[6])
    with col31:
        st.text(names[7])
        st.image(posters[7])
    with col41:
        st.text(names[8])
        st.image(posters[8])
    with col51:
        st.text(names[9])
        st.image(posters[9])

    col112, col212, col312, col412, col512 = st.columns(5)
    with col112:
        st.text(names[10])
        st.image(posters[10])
    with col212:
        st.text(names[11])
        st.image(posters[11])
    with col312:
        st.text(names[12])
        st.image(posters[12])
    with col412:
        st.text(names[13])
        st.image(posters[13])
    with col512:
        st.text(names[14])
        st.image(posters[14])

    col113, col213, col313, col413, col513 = st.columns(5)
    with col113:
        st.text(names[15])
        st.image(posters[15])
    with col213:
        st.text(names[16])
        st.image(posters[16])
    with col313:
        st.text(names[17])
        st.image(posters[17])
    with col413:
        st.text(names[18])
        st.image(posters[18])
    with col513:
        st.text(names[19])
        st.image(posters[19])

    col114, col214, col314, col414, col514 = st.columns(5)
    with col114:
        st.text(names[20])
        st.image(posters[20])
    with col214:
        st.text(names[21])
        st.image(posters[21])
    with col314:
        st.text(names[22])
        st.image(posters[22])
    with col414:
        st.text(names[23])
        st.image(posters[23])
    with col514:
        st.text(names[24])
        st.image(posters[24])

    col115, col215, col315, col415, col515 = st.columns(5)
    with col115:
        st.text(names[25])
        st.image(posters[25])
    with col215:
        st.text(names[26])
        st.image(posters[26])
    with col315:
        st.text(names[27])
        st.image(posters[27])
    with col415:
        st.text(names[28])
        st.image(posters[28])
    with col515:
        st.text(names[29])
        st.image(posters[29])

    col116, col216, col316, col416, col516 = st.columns(5)
    with col116:
        st.text(names[30])
        st.image(posters[30])
    with col216:
        st.text(names[32])
        st.image(posters[32])
    with col316:
        st.text(names[33])
        st.image(posters[33])
    with col416:
        st.text(names[34])
        st.image(posters[34])
    with col516:
        st.text(names[35])
        st.image(posters[35])

    col117, col217, col317, col417, col517 = st.columns(5)
    with col117:
        st.text(names[40])
        st.image(posters[40])
    with col217:
        st.text(names[36])
        st.image(posters[36])
    with col317:
        st.text(names[37])
        st.image(posters[37])
    with col417:
        st.text(names[38])
        st.image(posters[38])
    with col517:
        st.text(names[39])
        st.image(posters[39])
