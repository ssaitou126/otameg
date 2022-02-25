# My practice-1
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.subheader('eqation')

val = st.slider('valiable',1,5,1)

# a = 2
x = np.arange(-3, 3, 0.1)
y = val*x**2+val
  
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title('Title')
# plt.show()
st.pyplot(fig)