import pypickle
import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder

data=pypickle.load('test.pkl')


st.title('CHURN PREDICTION')
user_id=st.number_input('Clients user id')
region=st.text_input('Clients location')
tenure=st.number_input('Clients duration in months ')
montant= st.number_input('Clients top up amount?')
frequence_rech=st.number_input('The number of times the client refilled')
revenue=st.number_input('Monthly income of the client')
arpu_segment=st.number_input('Clients income over 90days/3')
frequence=st.number('The number of times the client has made an income')
data_volume=st.number_input('The number of connections')
on_net=st.number_input('Client inter expresso call')
orange=st.number_input('Clients call to Orange')
tigo=st.number_input('Clients call to Tigo')
zone1=st.number_input('Clients call to Zone1')
zone2=st.number_input('Clients call to Zone2')
mrg=st.radio('MRG:', ('Yes','No'))
if mrg == 'Yes':
    mrg = st.text_input('Yes')
elif (mrg == 'No'):
    # take gender input in text
     mrg= st.text_input('No')

regularity=st.number_input('The number of times the client is active for 90days')
top_pack=st.number_input('Client most active pack')
freq_top_pack=st.number_input('The number of times Client has activated the top packages')


#encoder=['user_id','region', 'tenure','montant','frequence_rech','revenue',
          #'arpu_segment','frequence','data_volume','on_net','orange','tigo'.'zone1','zone2','mrg','regularity','top_pack','freq_top_pack']


x=pd.DataFrame({
    'user_id': [user_id],
    'region': [region],
    'tenure': [tenure],
    'montant': [montant],
    'frequence_rech': [frequence_rech],
    'revenue': [revenue],
    'arpu_segment': [arpu_segment],
    'frequence': [frequence],
    'data_volume': [data_volume],
    'on_net': [on_net],
    'orange':[orange],
    'tigo': [tigo],
    'zone1':[zone1],
    'zone2':[zone2],
    'mrg':[mrg],
    'regularity':[regularity],
    'top_pack':[top_pack],
    'freq_top_pack':[freq_top_pack]
)}

encoder= LabelEncoder()

#Label Encoder to convert categorical columns into numerical features passing in a lambda function
def object_to_int(dataframe_series):
    if dataframe_series.dtype=='object':
        dataframe_series = LabelEncoder().fit_transform(dataframe_series)
    return dataframe_series

df_merges = x.apply(lambda x: object_to_int(x))
df_merges.head()

if (st.button('Predict Client churn probability')):
    predict= data.predict(df_merges)
    if predict== 1:
        st.write('yes')
    else:
        st.write('No')