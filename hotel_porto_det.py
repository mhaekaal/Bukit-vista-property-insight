import streamlit as st
import os
from aboutme import aboutme
from bv_project_det import bv_project_det
from closing import closing

#os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'C:\Users\inioc\streamlit-porto\bank-marketing-project-446413-a16e16990932.json'

st.markdown('''<h1 style='text-align:center;font-size:40px;font-weight:bolder;color:#FF4B4B; line-height:2;'>
            Bukit Vista's Property Rental Estimator
         </h1>''', unsafe_allow_html=True)
tab1 = st.tabs(['Bukit Vista Project'])

with tab1:
    bv_project_det()
    st.markdown('         ')
    st.markdown('         ')
    st.markdown('         ')
    st.markdown('         ')
    closing() 
    
