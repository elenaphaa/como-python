import streamlit as st
import pandas as pd
import numpy as np

st.title("Výpočet čistých mezd k výplatě")
st.header("Mzdová kalkulačka")

st.markdown('Streamlit is **_really_ cool**.')

castka_1 = st.number_input("Zadejte vaší hrubou mzdu: ", min_value=1)

deti_1 = st.number_input("Zadejte počet dětí: ", min_value=0, max_value=30)
st.text(f"Děti: {deti_1}")

if deti_1 == 0:
    st.text(f"Sleva: {deti_1}")
elif deti_1 == 1:
    sleva_1 = 1267
    st.text(f"Sleva: {sleva_1}")
elif deti_1 == 2:
    sleva_2 = 1267 + 1860
    st.text(f"Sleva: {sleva_2}")
elif deti_1 == 3:
    sleva_3 = 1267 + 1860 + 2320
    st.text(f"Sleva: {sleva_3}")
else:
    sleva_atd = (1267 + 1860 + 2320) + (deti_1 - 3) * 2320
    st.text(f"Sleva: {sleva_atd}")








   