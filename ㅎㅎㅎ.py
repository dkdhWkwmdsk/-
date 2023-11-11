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
st.metric(label="온도",value="10°C",delta="1.2°C)
st.metric(label="삼성전하",value="61,000원",delta="-1200원"
