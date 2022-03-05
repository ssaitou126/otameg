# My practice-1
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import datetime

st.subheader('eqation')

ntoday = datetime.datetime.now()
nstr = ntoday.strftime('%Y-%m-%d  %H:%M:%S')
st.write(f'現在N時刻は{nstr}です')
atoday = datetime.datetime.now(datetime.timezone.utc)
astr = atoday.strftime('%Y-%m-%d  %H:%M:%S')
st.write(f'現在A時刻は{astr}です')
jtoday = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
jstr = jtoday.strftime('%Y-%m-%d  %H:%M:%S')
st.write(f'現在J時刻は{jstr}です')

val = st.slider('valiable',1,5,1)

# a = 2
x = np.arange(-3, 3, 0.1)
y = val*x**2+val
  
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title('Title')
# plt.show()
st.pyplot(fig)