import streamlit as st
from PIL import Image
import pandas as pd 

logo = Image.open('images/logo.jpg')
st.image(logo)
st.subheader('테이크 아웃 메뉴(TAKE-OUT MENU)')
menu = pd.read_excel('menu/menu.xlsx')

select_category = st.selectbox(
    '메뉴종류 선택:',
    ['커피','차','라떼','에이드/소다','디저트']
)

st.header(select_category)
menu_takeout_name = list(menu[menu.테이크아웃 == 'YES'][menu.카테고리==select_category][menu.온도=='HOT']['메뉴명'].values)
menu_takeout_hot = list(menu[menu.테이크아웃 == 'YES'][menu.카테고리==select_category][menu.온도=='HOT']['가격'].values)
menu_takeout_ice = list(menu[menu.테이크아웃 == 'YES'][menu.카테고리==select_category][menu.온도=='ICE']['가격'].values)
if not menu_takeout_name:
    menu_takeout_name = list(menu[menu.테이크아웃 == 'YES'][menu.카테고리==select_category][menu.온도=='ICE']['메뉴명'].values)
    menu_takeout = pd.DataFrame({'메뉴명':menu_takeout_name,
                                 '아이스(ICED)':menu_takeout_ice})
elif not menu_takeout_ice:
    menu_takeout = pd.DataFrame({'메뉴명':menu_takeout_name,
                                 '핫(HOT)':menu_takeout_hot})
        
else:
    menu_takeout = pd.DataFrame({'메뉴명':menu_takeout_name,
                                '핫(HOT)':menu_takeout_hot,
                                '아이스(ICED)':menu_takeout_ice})
st.table(menu_takeout)