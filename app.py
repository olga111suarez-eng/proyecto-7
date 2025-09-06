import streamlit as st
import pandas as pd
import plotly.express as px

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
st.header("Visualizaciones interactivas")

# Botón para histogramas (genera 2 histogramas)
if st.button("Construir histogramas"):
    st.write("Creando histogramas...")
    # Histograma odometer
    if "odometer" in df.columns:
        fig1 = px.histogram(df, x="odometer", nbins=50, title="Histograma: odometer")
        st.plotly_chart(fig1, use_container_width=True)
    else:
        st.write("No existe la columna 'odometer' en este dataset.")

    # Histograma price
    if "price" in df.columns:
        fig2 = px.histogram(df, x="price", nbins=50, title="Histograma: price")
        st.plotly_chart(fig2, use_container_width=True)
    else:
        st.write("No existe la columna 'price' en este dataset.")

# Botón para scatterplots (genera 2 scatterplots)
if st.button("Construir gráficos de dispersión"):
    st.write("Creando gráficos de dispersión...")
    # Scatter odometer vs price
    if "odometer" in df.columns and "price" in df.columns:
        fig3 = px.scatter(df, x="odometer", y="price", title="Odometer vs Price", trendline="ols")
        st.plotly_chart(fig3, use_container_width=True)
    else:
        st.write("Faltan columnas para Odometer vs Price.")

    # Scatter model_year vs price
    if "model_year" in df.columns and "price" in df.columns:
        fig4 = px.scatter(df, x="model_year", y="price", title="Model Year vs Price")
        st.plotly_chart(fig4, use_container_width=True)
    else:
        st.write("No hay columna 'model_year' para el segundo scatter.")

# Un segundo encabezado extra para cumplir con "al menos dos encabezados"
st.header("Análisis adicional")
st.write("Usa los botones anteriores para construir las visualizaciones. Puedes ampliar la app añadiendo filtros por marca, año, precio, etc.")
        

            
                
            
        




        
