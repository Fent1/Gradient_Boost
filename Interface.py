import pandas as pd
import streamlit as st
import pickle


df = pd.read_csv("cleaned_df_withoutY.csv")
st.title("FICO Models/Recommendations")
with open('gb_model.p', 'rb') as f2:
    loaded_model = pickle.load(f2)

st.subheader('Choose the person :red[features] you want to include:')
options = st.multiselect(
    '',
    list(df.columns[1:24]),
    list(df.columns[1:24])
)

st.divider()
predict_dic = dict()
for i in options:
    if i == "MSinceMostRecentDelq":
        value = st.radio("$\mathbf Special$  $\mathbf value?$ ", ('No', '-7 Condition not Met (e.g. No Inquiries, No Delinquencies)', '-8 No Usable/Valid Accounts Trades or Inquiries'), key = 1)
        if value == '-7 Condition not Met (e.g. No Inquiries, No Delinquencies)':
            predict_dic['MSinceMostRecentDelq=-7'] = 1
            predict_dic['MSinceMostRecentDelq'] = df.loc[4, i]
            st.slider('$\mathbf '+ i + '$', int(min(df[i])), int(max(df[i])), disabled=True)
            st.divider()
        elif value == '-8 No Usable/Valid Accounts Trades or Inquiries':
            predict_dic['MSinceMostRecentDelq=-8'] = 1
            predict_dic['MSinceMostRecentDelq'] = df.loc[4, i]
            st.slider('$\mathbf '+ i + '$', int(min(df[i])), int(max(df[i])), disabled=True)
            st.divider()
        else:
            predict_dic['MSinceMostRecentDelq'] = st.slider('$\mathbf '+ i + '$', int(min(df[i])), int(max(df[i])), disabled=False)
            st.divider()
    elif i == "MSinceMostRecentInqexcl7days":
        value = st.radio("$\mathbf Special$  $\mathbf value?$ ", ('No', '-7 Condition not Met (e.g. No Inquiries, No Delinquencies)', '-8 No Usable/Valid Accounts Trades or Inquiries'), key =2)
        if value == '-7 Condition not Met (e.g. No Inquiries, No Delinquencies)':
            predict_dic['MSinceMostRecentInqexcl7days=-7'] = 1
            predict_dic['MSinceMostRecentInqexcl7days'] = df.loc[1, i]
            st.slider('$\mathbf '+ i + '$', int(min(df[i])), int(max(df[i])), disabled= True)
            st.divider()
        elif value == '-8 No Usable/Valid Accounts Trades or Inquiries':
            predict_dic['MSinceMostRecentInqexcl7days=-8'] = 1
            predict_dic['MSinceMostRecentInqexcl7days'] = df.loc[1, i]
            st.slider('$\mathbf '+ i + '$', int(min(df[i])), int(max(df[i])), disabled=True)
            st.divider()
        else:
            predict_dic['MSinceMostRecentInqexcl7days'] = (st.slider('$\mathbf '+ i + '$', int(min(df[i])), int(max(df[i])), disabled=False))
            st.divider()
    elif i == "MSinceOldestTradeOpen":
        value = st.radio("$\mathbf Special$  $\mathbf value?$ ", ('No', '-8 No Usable/Valid Accounts Trades or Inquiries'), key=3)
        if value == '-8 No Usable/Valid Accounts Trades or Inquiries':
            predict_dic['MSinceOldestTradeOpen=-8'] = 1
            predict_dic['MSinceOldestTradeOpen'] = df.loc[1, i]
            st.slider('$\mathbf '+ i + '$', int(min(df[i])), int(max(df[i])), disabled=True)
            st.divider()
        else:
            predict_dic['MSinceOldestTradeOpen'] = (st.slider('$\mathbf '+ i + '$', int(min(df[i])), int(max(df[i])), disabled=False))
            st.divider()
    elif i == "NetFractionRevolvingBurden":
        value = st.radio("$\mathbf Special$  $\mathbf value?$ ", ('No', '-8 No Usable/Valid Accounts Trades or Inquiries'), key=4)
        if value == '-8 No Usable/Valid Accounts Trades or Inquiries':
            predict_dic['NetFractionRevolvingBurden=-8'] = 1
            predict_dic['NetFractionRevolvingBurden'] = df.loc[15, i]
            st.slider('$\mathbf '+ i + '$', int(min(df[i])), int(max(df[i])), disabled=True)
            st.divider()
        else:
            predict_dic['NetFractionRevolvingBurden'] = (st.slider('$\mathbf '+ i + '$', int(min(df[i])), int(max(df[i])), disabled=False))
            st.divider()
    elif i == "NetFractionInstallBurden":
        value = st.radio("$\mathbf Special$  $\mathbf value?$ ", ('No', '-8 No Usable/Valid Accounts Trades or Inquiries'), key=5)
        if value == '-8 No Usable/Valid Accounts Trades or Inquiries':
            predict_dic['NetFractionInstallBurden=-8'] = 1
            predict_dic['NetFractionInstallBurden'] = df.loc[3, i]
            st.slider('$\mathbf '+ i + '$', int(min(df[i])), int(max(df[i])), disabled=True)
            st.divider()
        else:
            predict_dic['NetFractionInstallBurden'] = (st.slider('$\mathbf '+ i + '$', int(min(df[i])), int(max(df[i])), disabled=False))
            st.divider()
    elif i == "NumRevolvingTradesWBalance":
        value = st.radio("$\mathbf Special$  $\mathbf value?$ ", ('No', '-8 No Usable/Valid Accounts Trades or Inquiries'), key=6)
        if value == '-8 No Usable/Valid Accounts Trades or Inquiries':
            predict_dic['NumRevolvingTradesWBalance=-8'] = 1
            predict_dic['NumRevolvingTradesWBalance'] = df.loc[15, i]
            st.slider('$\mathbf '+ i + '$', int(min(df[i])), int(max(df[i])), disabled=True)
            st.divider()
        else:
            predict_dic['NumRevolvingTradesWBalance'] = (st.slider('$\mathbf '+ i + '$', int(min(df[i])), int(max(df[i])), disabled=False))
            st.divider()
    elif i == "NumInstallTradesWBalance":
        value = st.radio("$\mathbf Special$  $\mathbf value?$ ", ('No', '-8 No Usable/Valid Accounts Trades or Inquiries'), key=7)
        if value == '-8 No Usable/Valid Accounts Trades or Inquiries':
            predict_dic['NumInstallTradesWBalance=-8'] = 1
            predict_dic['NumInstallTradesWBalance'] = df.loc[13,i]
            st.slider('$\mathbf '+ i + '$', int(min(df[i])), int(max(df[i])), disabled=True)
            st.divider()
        else:
            predict_dic['NumInstallTradesWBalance'] = (st.slider('$\mathbf '+ i + '$', int(min(df[i])), int(max(df[i])), disabled=False))
            st.divider()
    elif i == "NumBank2NatlTradesWHighUtilization":
        value = st.radio("$\mathbf Special$  $\mathbf value?$ ", ('No', '-8 No Usable/Valid Accounts Trades or Inquiries'), key=8)
        if value == '-8 No Usable/Valid Accounts Trades or Inquiries':
            predict_dic['NumBank2NatlTradesWHighUtilization=-8'] = 1
            st.slider('$\mathbf '+ i + '$', int(min(df[i])), int(max(df[i])), disabled=True)
            predict_dic['NumBank2NatlTradesWHighUtilization'] = df.loc[15, i]
            st.divider()
        else:
            predict_dic['NumBank2NatlTradesWHighUtilization'] = (st.slider('$\mathbf '+ i + '$', int(min(df[i])), int(max(df[i])), disabled=False))
            st.divider()
    elif i == "PercentTradesWBalance":
        value = st.radio("$\mathbf Special$  $\mathbf value?$ ", ('No', '-8 No Usable/Valid Accounts Trades or Inquiries') ,key=9)
        if value == '-8 No Usable/Valid Accounts Trades or Inquiries':
            predict_dic['PercentTradesWBalance=-8'] = 1
            predict_dic['PercentTradesWBalance'] = (st.slider('$\mathbf '+ i + '$', int(min(df[i])), int(max(df[i])), disabled=True))
            st.divider()
        else:
            predict_dic['PercentTradesWBalance'] = (st.slider('$\mathbf '+ i + '$', int(min(df[i])), int(max(df[i])), disabled=False))
            st.divider()
    else:
        predict_dic[i] = (st.slider('$\mathbf '+ i + '$', int(min(df[i])), int(max(df[i]))))
        st.divider()

# Get a list to predict Risk
risk_list = []
for i in df.columns[1:]:
    if i not in predict_dic:
        risk_list.append(0)
    else:
        risk_list.append(predict_dic[i])

# # Get a dataframe to predict Risk
# risk_dic = dict()
# for i in df.columns[1:]:
#     if i not in predict_dic:
#         risk_dic[i] = 0
#     else:
#        risk_dic[i] = predict_dic[i]
# risk_df = pd.DataFrame(risk_dic, index=[0])



prediction = loaded_model.predict([risk_list])[0]
with st.sidebar:
    st.title("Prediction Result")
    if prediction == 1:
        st.markdown('This person is :red[REJECTED]:thumbsdown:, since he/she is classified as a :red[BAD] risk performance. ')
        st.markdown('The features are shown below:')
        st.divider()
        for k, v in predict_dic.items():
            st.text(k + ' is ' + str(v))
        st.divider()
        st.markdown('$Note:$ $Features$  $NOT$  $selected$  $are$ $set$ $to$ $\mathbf 0$ $by$ $default$')
    elif prediction == 0:
        st.markdown('This person is :green[ACCEPTED]:thumbsup:, since he/she is classified as a :green[GOOD] risk performance. ')
        st.markdown('The features are shown below:')
        st.divider()
        for k, v in predict_dic.items():
            st.text(k + ' is ' + str(v))
        st.divider()
        st.markdown('$Note:$ $Features$  $NOT$  $selected$  $are$ $set$ $to$ $\mathbf 0$ $by$ $default$')
    else:
        st.markdown('')

