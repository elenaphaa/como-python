import streamlit as st

st.header("Moje aplikace")
st.header ("Vítej v programu")
choice = st.selectbox("Co chcete počítat?", ["čtverec", "obdélník", "kvádr", "krychle"])
if choice == "čtverec":
    strana_ctverce = st.number_input("Zadej stranu čtverce v cm: ", min_value=1)
    st.text(f"Obsah čtverce je {strana_ctverce**2} a obvod čtverce je {strana_ctverce*4}")
elif choice == "obdélník":
    strana_1 = st.number_input("Zadejte první stranu obdélníku v cm: ", min_value=1)
    strana_2 = st.number_input("Zadejte druhou stranu obdélníku v cm: ", min_value=1)
    obsah_obdelniku = strana_1 * strana_2
    obvod_obdelniku = 2*(strana_1 + strana_2)
    st.text(f"Obsah obdélníku je {obsah_obdelniku} a obvod obdélníku je {obvod_obdelniku}")
elif choice == "kvádr":
    strana_a = st.number_input("Zadejte první stranu kvádru v cm: ", min_value=1)
    strana_b = st.number_input("Zadejte druhou stranu kvádru v cm: ", min_value=1)
    strana_c = st.number_input("Zadejte třetí stranu v cm: ", min_value=1)
    objem_kvadru = strana_a * strana_b * strana_c
    plocha_kvadru = 2*(strana_a * strana_b + strana_a * strana_c + strana_b * strana_c)
    st.text(f"Objem kvádru je {objem_kvadru}, plocha kvádru je {plocha_kvadru} součet hran je {4*(strana_a + strana_b + strana_c) }")
elif choice == "krychle":
    strana_A = st.number_input("Zadejte stranu krychle v cm ", min_value=1)
    plocha_krychle = 6*(strana_A**2)
    objem_krychle = (strana_A**3)
    st.text(f"Objem krychle je {objem_krychle} a obvod krychle je {plocha_krychle} součet hran je {4*(strana_A)}")

