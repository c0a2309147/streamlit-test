from distutils.core import setup, Extension

setup(name = 'calModule', version = '1.0.0',  \
   ext_modules = [Extension('calModule', ['cal_py.c'])])


import calModule
import streamlit as st

kekka = (calModule.cal(1234,224,123,456))


st.title("りんか") # タイトル
st.header(kekka) # ヘッダー
 
