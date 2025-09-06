# proyecto-7
Proyecto creación  aplicación web. 

# Proyecto 7 - información sobre anuncios de carros

Breve descripción:
App con Streamlit basada en una exploración superficial, el dataset contiene anuncios de carros. Informacón sobre la cual se ejecutaron histogramas y gráficos de dispersión interactivos con Plotly.

Funcionalidad: 
1. Permite ver información general del dataset colo los  nombres de las columnas : price, model_year, model,condition,cylinders, fuel, odometer,transmission,type, paint_color,is_4wd,date_posted y  days_listed
2. Cuenta con la impresion de las primeras 10 filas
3. Tiene dos histogramas
4. Tiene dos graficos de dispersión 


Cómo ejecutar:
1. Activar entorno: `conda activate vehicles_env`
2. Instalar dependencias: `pip install -r requirements.txt`
3. Ejecutar app: `python -m streamlit run app.py`

Estructura del repo:
- README.md
- app.py
- vehicles_us.csv
- requirements.txt
- notebooks/EDA.ipynb

Funcionalidad:
- Visualizaciones: ≥2 histogramas y ≥2 scatterplots
- Botones para construir cada tipo de gráfico
- Checkbox para ver datos crudos