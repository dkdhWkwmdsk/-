import  streamlit as st
import pandas as pd
import numpy as np
st.title("하하하하핳ㅎ하")
st.write("HELLO **world**!")
dataframe=pd.DataFrame({
  'first column':[1,2,3,4],
  'second column':[10,20,30,40],
})

st.dataframe(dataframe, use_container_width=False)

st.table(dataframe)
st.metric(label="온도",value="10°C",delta="1.2°C")
st.metric(label="삼성전하",value="61,000원",delta="-1200원")
col1, col2, col3 = st.columns(3)
col1.metric(label="달러USD",value="1,228원",delta="-2.00원")
col2.metric(label="일본JPY(100엔",value="958.63원",delta="-7.44원")
col3.metric(label="유럽연랍EUR",value+"1,335.82원",delta="11.44원")

tab1, tab2 = st.tabs(["Cat","Dog"])
with tab1:
  st.header("A cat")
  st.image("https://startic.streamlit.fo/examples/cat.jpg",width=200)
  with tab2:
  st.header("A dog")
  st.image("https://startic.streamlit.fo/examples/dog.jpg",width=200)
