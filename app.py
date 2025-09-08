import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache_data
def load_data(path="vehicles_us.csv"):
    return pd.read_csv(path)

df = load_data()

st.title("Panel de control — Anuncios de coches")
st.header("Resumen y filtros")
st.write(f"Dataset cargado: **{df.shape[0]}** filas y **{df.shape[1]}** columnas.")

# Checkbox para ver datos crudos
if st.checkbox("Mostrar primeras 10 filas del dataset"):
    st.write(df.head(10))

# Encabezado 2
st.header("Visualizaciones seaborn")

# Botón para histogramas (genera 2 histogramas)
if st.button("Construir histogramas"):
    st.write("Creando histogramas...")
    # Histograma odometer
    if "odometer" in df.columns:
        fig1, ax = plt.subplots()
        sns.histplot(df["odometer"], bins=50, kde=False, ax=ax)
        ax.set_title("Histograma: odometer")
        st.pyplot(fig1)


    # Histograma price
    if "price" in df.columns:
        fig2, ax = plt.subplots()
        sns.histplot(df["price"], bins=50, kde=False, ax=ax)
        ax.set_title("Histograma:price")
        st.pyplot(fig2)

# Botón para scatterplots (genera 2 scatterplots)
if st.button("Construir gráficos de dispersión"):
    st.write("Creando gráficos de dispersión...")
    # Scatter odometer vs price
    if "odometer" in df.columns and "price" in df.columns:
        fig3, ax = plt.subplots()
        sns.scatterplot(data=df, x="odometer", y= "price", ax=ax)
        ax.set_title("Odometer vs Price")
        st.pyplot(fig3)

    # Scatter model_year vs price
    if "model_year" in df.columns and "price" in df.columns:
        fig4, ax = plt.subplots()
        sns.scatterplot(data=df, x="model_year", y="price", ax=ax)
        ax.set_title("Model Year vs Price")
        st.pyplot(fig4)

# Un segundo encabezado extra para cumplir con "al menos dos encabezados"
st.header("Análisis adicional")
st.write("Usa los botones anteriores para construir las visualizaciones.")
        

            
                
            
        




        
