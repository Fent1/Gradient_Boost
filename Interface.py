import pandas as pd
import streamlit as st
import pickle
import os


os.system("pip install sklearn")
df = pd.read_csv("cleaned_df_withoutY.csv")
st.title("Risk of HELOC Prediction")
with open('lr_model.p', 'rb') as f2:
    loaded_model = pickle.load(f2)

options = st.multiselect(
    'Choose the features you want to include:',
    list(df.columns[1:24])
)

st.divider()
predict_dic = dict()
for i in options:
    if i == "MSinceMostRecentDelq":
        value = st.radio("Is it a special value? ", ('No', '-7 Condition not Met (e.g. No Inquiries, No Delinquencies)', '-8 No Usable/Valid Accounts Trades or Inquiries'))
        if value == '-7 Condition not Met (e.g. No Inquiries, No Delinquencies)':
            predict_dic['MSinceMostRecentDelq=-7'] = 1
            predict_dic['MSinceMostRecentDelq'] = df.loc[4, i]
            st.slider(i, int(min(df[i])), int(max(df[i])), disabled=True)
            st.divider()
        elif value == '-8 No Usable/Valid Accounts Trades or Inquiries':
            predict_dic['MSinceMostRecentDelq=-8'] = 1
            predict_dic['MSinceMostRecentDelq'] = df.loc[4, i]
            st.slider(i, int(min(df[i])), int(max(df[i])), disabled=True)
            st.divider()
        else:
            predict_dic['MSinceMostRecentDelq'] = st.slider(i, int(min(df[i])), int(max(df[i])), disabled=False)
            st.divider()
    elif i == "MSinceMostRecentInqexcl7days":
        value = st.radio("Is it a special value? ", ('No', '-7 Condition not Met (e.g. No Inquiries, No Delinquencies)', '-8 No Usable/Valid Accounts Trades or Inquiries'))
        if value == '-7 Condition not Met (e.g. No Inquiries, No Delinquencies)':
            predict_dic['MSinceMostRecentInqexcl7days=-7'] = 1
            predict_dic['MSinceMostRecentInqexcl7days'] = df.loc[1, i]
            st.slider(i, int(min(df[i])), int(max(df[i])), disabled= True)
            st.divider()
        elif value == '-8 No Usable/Valid Accounts Trades or Inquiries':
            predict_dic['MSinceMostRecentInqexcl7days=-8'] = 1
            predict_dic['MSinceMostRecentInqexcl7days'] = df.loc[1, i]
            st.slider(i, int(min(df[i])), int(max(df[i])), disabled=True)
            st.divider()
        else:
            predict_dic['MSinceMostRecentInqexcl7days'] = (st.slider(i, int(min(df[i])), int(max(df[i])), disabled=False))
            st.divider()
    elif i == "MSinceOldestTradeOpen":
        value = st.radio("Is it a special value? ", ('No', '-8 No Usable/Valid Accounts Trades or Inquiries'))
        if value == '-8 No Usable/Valid Accounts Trades or Inquiries':
            predict_dic['MSinceOldestTradeOpen=-8'] = 1
            predict_dic['MSinceOldestTradeOpen'] = df.loc[1, i]
            st.slider(i, int(min(df[i])), int(max(df[i])), disabled=True)
            st.divider()
        else:
            predict_dic['MSinceOldestTradeOpen'] = (st.slider(i, int(min(df[i])), int(max(df[i])), disabled=False))
            st.divider()
    elif i == "NetFractionRevolvingBurden":
        value = st.radio("Is it a special value? ", ('No', '-8 No Usable/Valid Accounts Trades or Inquiries'))
        if value == '-8 No Usable/Valid Accounts Trades or Inquiries':
            predict_dic['NetFractionRevolvingBurden=-8'] = 1
            predict_dic['NetFractionRevolvingBurden'] = df.loc[15, i]
            st.slider(i, int(min(df[i])), int(max(df[i])), disabled=True)
            st.divider()
        else:
            predict_dic['NetFractionRevolvingBurden'] = (st.slider(i, int(min(df[i])), int(max(df[i])), disabled=False))
            st.divider()
    elif i == "NetFractionInstallBurden":
        value = st.radio("Is it a special value? ", ('No', '-8 No Usable/Valid Accounts Trades or Inquiries'))
        if value == '-8 No Usable/Valid Accounts Trades or Inquiries':
            predict_dic['NetFractionInstallBurden=-8'] = 1
            predict_dic['NetFractionInstallBurden'] = df.loc[3, i]
            st.slider(i, int(min(df[i])), int(max(df[i])), disabled=True)
            st.divider()
        else:
            predict_dic['NetFractionInstallBurden'] = (st.slider(i, int(min(df[i])), int(max(df[i])), disabled=False))
            st.divider()
    elif i == "NumRevolvingTradesWBalance":
        value = st.radio("Is it a special value? ", ('No', '-8 No Usable/Valid Accounts Trades or Inquiries'))
        if value == '-8 No Usable/Valid Accounts Trades or Inquiries':
            predict_dic['NumRevolvingTradesWBalance=-8'] = 1
            predict_dic['NumRevolvingTradesWBalance'] = df.loc[15, i]
            st.slider(i, int(min(df[i])), int(max(df[i])), disabled=True)
            st.divider()
        else:
            predict_dic['NumRevolvingTradesWBalance'] = (st.slider(i, int(min(df[i])), int(max(df[i])), disabled=False))
            st.divider()
    elif i == "NumInstallTradesWBalance":
        value = st.radio("Is it a special value? ", ('No', '-8 No Usable/Valid Accounts Trades or Inquiries'))
        if value == '-8 No Usable/Valid Accounts Trades or Inquiries':
            predict_dic['NumInstallTradesWBalance=-8'] = 1
            predict_dic['NumInstallTradesWBalance'] = df.loc[13,i]
            st.slider(i, int(min(df[i])), int(max(df[i])), disabled=True)
            st.divider()
        else:
            predict_dic['NumInstallTradesWBalance'] = (st.slider(i, int(min(df[i])), int(max(df[i])), disabled=False))
            st.divider()
    elif i == "NumBank2NatlTradesWHighUtilization":
        value = st.radio("Is it a special value? ", ('No', '-8 No Usable/Valid Accounts Trades or Inquiries'))
        if value == '-8 No Usable/Valid Accounts Trades or Inquiries':
            predict_dic['NumBank2NatlTradesWHighUtilization=-8'] = 1
            st.slider(i, int(min(df[i])), int(max(df[i])), disabled=True)
            predict_dic['NumBank2NatlTradesWHighUtilization'] = df.loc[15, i]
            st.divider()
        else:
            predict_dic['NumBank2NatlTradesWHighUtilization'] = (st.slider(i, int(min(df[i])), int(max(df[i])), disabled=False))
            st.divider()
    elif i == "PercentTradesWBalance":
        value = st.radio("Is it a special value? ", ('No', '-8 No Usable/Valid Accounts Trades or Inquiries'))
        if value == '-8 No Usable/Valid Accounts Trades or Inquiries':
            predict_dic['PercentTradesWBalance=-8'] = 1
            predict_dic['PercentTradesWBalance'] = (st.slider(i, int(min(df[i])), int(max(df[i])), disabled=True))
            st.divider()
        else:
            predict_dic['PercentTradesWBalance'] = (st.slider(i, int(min(df[i])), int(max(df[i])), disabled=False))
            st.divider()
    else:
        predict_dic[i] = (st.slider(i, int(min(df[i])), int(max(df[i]))))
        st.divider()

# Get a list to predict Risk
risk_list = []
for i in df.columns[1:]:
    if i not in predict_dic:
        risk_list.append(0)
    else:
        risk_list.append(predict_dic[i])

prediction = loaded_model.predict([risk_list])[0]

if prediction == 1:
    st.text('This person is rejected')
else:
    st.text('This person is accepted')
