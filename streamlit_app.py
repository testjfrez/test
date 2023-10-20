import streamlit as st

import pandas as pd

# Crear un DataFrame simple
df = pd.DataFrame({
    'Mensaje': ['¡Hola mundo!']
})

# Mostrar el DataFrame
st.dataframe(df)
