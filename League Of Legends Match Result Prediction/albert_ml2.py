

import streamlit as st
import pickle
import pandas as pd

with open("full_pipe.pkl", "rb") as f:
    pipeline = pickle.load(f)

df=pd.read_csv('LOLmatch.csv')

st.title("WIn/Lose  Predictor for League of Legends")
st.write("Created by Albertus Magnus")

columns =  ['d_spell','f_spell','role',
            'assists','dmg_obj','dmg_bd','dmg_tr','deaths',
            'gold','kda','kills','level','time_cc','dmg_tot',
            'dmg_tkn','tot_cs','tr_kills','vision']

# ============= INPUT =============

d_spell = st.number_input("d_spell")
f_spell = st.number_input("f_spell")
role = st.selectbox("role", df['role'].unique())
assists = st.number_input("assists")
dmg_obj = st.number_input("dmg_obj")
dmg_bd = st.number_input("dmg_bd")
dmg_tr = st.number_input("dmg_tr")
deaths = st.number_input("deaths")
gold = st.number_input("gold")
kda = st.number_input("kda")
kills = st.number_input("kills")
level = st.number_input("level")
time_cc = st.number_input("time_cc")
dmg_tot = st.number_input("dmg_tot")
dmg_tkn = st.number_input("dmg_tkn")
tot_cs = st.number_input("tot_cs")
tr_kills = st.number_input("tr_kills")
vision = st.number_input("vision")



new_data = [d_spell,f_spell,role,
            assists,dmg_obj,dmg_bd,dmg_tr,deaths,
            gold,kda,kills,level,time_cc,dmg_tot,
            dmg_tkn,tot_cs,tr_kills,vision]
new_data = pd.DataFrame([new_data], columns=columns)
res = pipeline.predict(new_data)
press = st.button('PREDICTION')
if press:
    st.write(f'WIN/LOSE : {res[0]}')
