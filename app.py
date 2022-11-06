import streamlit as st
import requests

def getAllBookstore():
	url = 'https://cloud.culture.tw/frontsite/trans/emapOpenDataAction.do?method=exportEmapJson&typeId=M' # 在這裡輸入目標 url
	headers = {"accept": "application/json"}
	response = requests.get(url, headers=headers)
	# 將 response 轉換成 json 格式
	# 回傳值

def app():
	st.header('特色書店地圖')
	st.metric('Total bookstore', 118)
	county = st.selectbox('請選擇縣市', ['A', 'B', 'C'])
	district = st.multiselect('請選擇區域', ['a', 'b', 'c', 'd'])
    
if __name__ == '__main__':
    app()

     #python -m streamlit run app.py
     #python -m streamlit run app.py
     #streamlit run app.py