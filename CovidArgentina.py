# Importar las bibliotecas necesarias
import pandas as pd
import plotly.express as px
import json
import streamlit as st
from PIL import Image

# Configurar la página de Streamlit
st.set_page_config(page_title="Covid 19 en Argentina", page_icon=" 🌎", layout="wide")

# Crear dos columnas en el diseño de la aplicación
with st.container():
    text_column, image_column = st.columns((3, 2))
    
    # Columna de la imagen
    with image_column:
        # Cargar y mostrar la imagen
        image = Image.open("img/vacuna.jpg")
        st.image(image, use_column_width=True)

# Columna de texto
with text_column:
    # Títulos y bienvenida
    st.write("##")
    st.write("##")
    st.write("##")
    st.markdown("<h1 style='text-align: center; color: #A385FF;'>COVID-19 Insights Argentina: Análisis Integral y Visualización Geoespacial</h1>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center;'>Bienvenido a COVID-19 Insights Argentina, una plataforma interactiva que ofrece un análisis detallado y una visualización completa de la evolución de la pandemia de COVID-19 en las provincias de Argentina.</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center;'>A través de gráficos, mapas y tablas informativas, esta aplicación busca proporcionar una comprensión profunda de la situación epidemiológica en el país.</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center;'>Con el objetivo de brindar una experiencia visual enriquecedora, hemos diseñado una interfaz intuitiva para explorar los datos de COVID-19 en Argentina. ¡Explora y mantente informado!</h5>", unsafe_allow_html=True)

# Cargar el GeoJSON de las Provincias de Argentina
with open('ProvinciasArgentina.geojson') as f:
    geojson_data = json.load(f)

# Cargar los datos de casos desde el archivo CSV
df = pd.read_csv('Casos.CSV', encoding='utf-8')

# Separador visual
st.write("---")
st.write("##")

# Crear un contenedor para organizar el diseño
with st.container():
    # Dividir el contenedor en cuatro columnas para estadísticas clave
    columna_Casos, columna_Muertes, columna_Letalidad, columna_Incidencia = st.columns(4)

    # En la primera columna, mostrar el total de casos
    with columna_Casos:
        st.markdown("""
            <div style='background-color: #A385FF; padding: 0px; border-radius: 10px;'>
                <h3 style='text-align: center;color: white;'>Total de Casos</h3>
                <h2 style='text-align: center;color: white;'>11,275,224</h2>
            </div>
        """, unsafe_allow_html=True)

    # En la segunda columna, mostrar el total de muertes
    with columna_Muertes:
        st.markdown("""
            <div style='background-color: #A385FF; padding: 0px; border-radius: 10px;'>
                <h3 style='text-align: center;color: white;'>Total de Muertos</h3>
                <h2 style='text-align: center;color: white;'>130,463</h2>
            </div>
        """, unsafe_allow_html=True)
    
    # En la tercera columna, mostrar la tasa de letalidad
    with columna_Letalidad:
        st.markdown("""
            <div style='background-color: #A385FF; padding: 0px; border-radius: 10px;'>
                <h3 style='text-align: center;color: white;'>Tasa de Letalidad</h3>
                <h2 style='text-align: center;color: white;'>1.16%</h2>
            </div>
        """, unsafe_allow_html=True)
    
    # En la cuarta columna, mostrar la tasa de incidencia
    with columna_Incidencia:
        st.markdown("""
            <div style='background-color: #A385FF; padding: 0px; border-radius: 10px;'>
                <h3 style="text-align: center; color: white;">Tasa de Incidencia</h3>
                <h2 style='text-align: center; color: white;'>22.225,4</h2>
            </div>
        """, unsafe_allow_html=True)


# Separador visual
st.write("---")

# Título y descripción del análisis geoespacial
st.markdown("<h1 style='text-align: center;'>Análisis Geoespacial de Casos de COVID-19 en Provincias</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Explora una visualización detallada que muestra la distribución de casos de COVID-19 en diferentes provincias. Esta aplicación interactiva ofrece un mapa coroplético que destaca la intensidad de casos, junto con una tabla ordenable y estilizada para examinar los datos en detalle. Obtén perspectivas sobre las variaciones y tendencias regionales con esta completa herramienta de análisis geoespacial.</p>", unsafe_allow_html=True)

# Expandir la sección de la tabla de clientes y regiones
with st.expander("Tabla de Clientes y Regiones"):
    # Ordenar el DataFrame por la columna 'Casos' de mayor a menor
    df_sorted = df.sort_values(by='Casos', ascending=False)

    # Aplicar estilos al DataFrame ordenado
    styled_df = df_sorted.style \
        .set_properties(**{'text-align': 'center', 'font-size': '12px'}) \
        .format({'Casos': '{:,.0f}','Tasa de incidencia': '{:,.0f}','Muertes': '{:,.0f}','Letalidad': '{:,.2f}'}) \
        .set_table_styles([
            {'selector': 'th', 'props': [('background-color', '#A385FF'), ('color', 'white'), ('font-size', '12px'), ('border', '1px solid #000000')]},
            {'selector': 'td', 'props': [('border', '1px solid #000000'), ('color', '0039A3')]},
            {'selector': 'tr:hover', 'props': [('background-color', '#A385FF'), ('color', 'A385FF')]},  # Cambiado el color de hover
            {'selector': 'tr:nth-child(even)', 'props': [('background-color', '#A385FF'), ('color',  'white')]},
            {'selector': 'tr:nth-child(even)', 'props': [('background-color', '#A385FF')]},
            {'selector': 'td:hover', 'props': [('background-color', '#7547FF'), ('color', 'white')]}
        ])

    # Mostrar la tabla estilizada con Streamlit
    st.table(styled_df)

# Separadores visuales para dar espacio antes de mostrar el mapa
st.write("##")
st.write("##")

# Crear un contenedor para organizar el diseño
with st.container():
    # Crear el mapa con Plotly Express
    fig = px.choropleth_mapbox(
        df,
        geojson=geojson_data,
        locations='Provincias',
        featureidkey="properties.nombre",
        color='Casos',
        color_continuous_scale="purples",
        mapbox_style="carto-positron",
        zoom=3,
        center={"lat": -39, "lon": -64},
        hover_name='Provincias',
        hover_data={'Casos': True, 'Muertes': True, 'Tasa de incidencia': True, 'Letalidad': True, 'Provincias': False},
    )

    # Actualizar el hovertemplate para incluir información sobre muertes
    fig.update_traces(hovertemplate='<b>%{hovertext}</b><br>Casos: %{z:,.0f}<br>Muertes: %{customdata[1]:,.0f}<br>Tasa de incidencia: %{customdata[2]:,.0f}<br>Letalidad: %{customdata[3]:,.2f}')

    # Configuraciones adicionales del mapa
    fig.update_geos(showcountries=True, showcoastlines=True, showland=True, fitbounds="locations", visible=False)
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0}, height=680)

    # Mostrar el mapa en Streamlit
    st.plotly_chart(fig, use_container_width=True)


# Separadores visuales para dar espacio antes de mostrar la visualización
st.write("##")
st.write("##")

# Crear un contenedor para organizar el diseño
with st.container():
    # Título y descripción de la visualización de casos y fallecimientos
    st.markdown("<h1 style='text-align: center;'>Visualización de Casos y Fallecimientos de COVID-19 por Provincia en Argentina</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Este código presenta una visualización clara y ordenada de las estadísticas de COVID-19 en diferentes provincias de Argentina. Dos gráficos de barras muestran la evolución de casos y fallecimientos, respectivamente, presentando la información de manera ascendente para una fácil comparación.</p>", unsafe_allow_html=True)
    st.write("##")

    # Dividir el contenedor en dos columnas para la tabla y el texto
    tabla_column, text_column = st.columns(2)

    # En la primera columna (tabla), mostrar el gráfico de barras de casos
    with tabla_column:
        df_sorted = df.sort_values(by='Casos', ascending=True)

        # Crear el gráfico de barras con Plotly Express para casos
        fig = px.bar(
            df_sorted,
            x='Provincias',
            y='Casos',
            color='Casos',
            color_continuous_scale='algae',
            title='Casos de COVID-19 en Argentina',
            labels={'Casos': 'Número de Casos'},
            text='Casos',  
        )

        # Configuraciones específicas del gráfico de casos
        fig.update_traces(
            textfont_size=12, 
            textangle=0, 
            textposition="outside", 
            cliponaxis=False,
            textfont_color='black', 
            texttemplate='%{y:,.0f}', 
            marker_color='#6633FF', 
            marker_line_color='#6633FF'
        )

        fig.update_traces(
            hovertemplate='<b>%{y}</b><br>Número de Casos: %{y:,.0f}<br>',
        )

        # Ajustar el diseño del gráfico de casos
        fig.update_layout(
            xaxis_title='Número de Casos',
            yaxis_title='Provincias',
            width=600,
            height=680,
            margin=dict(l=50, r=50, t=50, b=50),
            bargap=0.2,
        )

        # Mostrar el gráfico de casos en Streamlit
        st.plotly_chart(fig, use_container_width=True)

    # En la segunda columna (texto), mostrar el gráfico de barras de muertes
    with text_column:
        data_sorted = df.sort_values(by='Muertes', ascending=True)

        # Crear el gráfico de barras con Plotly Express para muertes
        fig = px.bar(
            data_sorted,
            x='Provincias',
            y='Muertes',
            color='Muertes',
            color_continuous_scale='algae',
            title='Muertes de COVID-19 en Argentina',
            labels={'Muertes': 'Número de Muertes'},
            text='Muertes',  
        )

        # Configuraciones específicas del gráfico de muertes
        fig.update_traces(
            textfont_size=12, 
            textangle=0, 
            textposition="outside", 
            cliponaxis=False,
            textfont_color='black', 
            texttemplate='%{y:,.0f}',  
            marker_color='#6633FF', 
            marker_line_color='#6633FF'
        )

        fig.update_traces(
            hovertemplate='<b>%{y}</b><br>Número de Muertes: %{y:,.0f}<br>',
        )

        # Ajustar el diseño del gráfico de muertes
        fig.update_layout(
            xaxis_title='Número de Muertes',
            yaxis_title='Provincias',
            width=600,
            height=680,
            margin=dict(l=50, r=50, t=50, b=50),
            bargap=0.2,
        )

        # Mostrar el gráfico de muertes en Streamlit
        st.plotly_chart(fig, use_container_width=True)

# Separadores visuales para dar espacio antes de mostrar el gráfico
st.write("##")
st.write("##")

# Crear un contenedor para organizar el diseño
with st.container():       
    # Título y descripción de la evolución temporal de casos y muertes
    st.markdown("<h1 style='text-align: center;'>Evolución Temporal de Casos y Muertes por COVID-19 en Argentina</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Representación visual de la evolución temporal de los casos y muertes por COVID-19 en Argentina. Se trata de un gráfico de líneas interactivo que facilita la exploración de la progresión de la enfermedad a lo largo del tiempo. En el eje x se presentan las fechas, mientras que en el eje y se representa el número de casos y muertes. Este enfoque proporciona una visión clara y detallada de cómo la situación ha evolucionado en el país.</p>", unsafe_allow_html=True)
   
    # Cargar datos para la evolución temporal desde un archivo CSV
    data = pd.read_csv('tiempo.csv', encoding='utf-8')
    df_melted = data.melt(id_vars=['Tipo'], var_name='Fecha', value_name='Cantidad')

    # Asignar colores personalizados
    color_map = {'Casos': '#A385FF', 'Muertes': '#6633FF'}
    
    # Crear un gráfico lineal con Plotly Express
    fig = px.line(df_melted, x='Fecha', y='Cantidad', color='Tipo', markers=True, title='Casos y Muertes a lo largo del tiempo',
                labels={'Cantidad': 'Cantidad Total', 'Fecha': 'Fecha', 'Tipo': 'Tipo'},
                color_discrete_map=color_map)  

    # Personalizar el diseño y la estética del gráfico
    fig.update_layout(
        xaxis_title_font=dict(size=14, color='Black'),
        yaxis_title_font=dict(size=14, color='Black'),
        title_font=dict(size=20, color='black'), 
        font=dict(family="Arial, sans-serif", size=12, color="black"),
        legend=dict(title=dict(text='Casos y Fallecimientos', font=dict(size=12))),
    )

    # Personalizar las trazas
    fig.update_traces(
        line=dict(width=2),  
        hovertemplate='%{y}',  
        hoverinfo='y+y',  
    )

    # Mostrar el gráfico en Streamlit
    st.plotly_chart(fig, use_container_width=True)

# Separadores visuales para dar espacio antes de mostrar los gráficos
st.write("##")
st.write("##")

# Crear un contenedor para organizar el diseño
with st.container():
    # Título y descripción de la tasa de incidencia y letalidad
    st.markdown("<h1 style='text-align: center;'>Tasa de Incidencia y Letalidad del COVID-19 por Provincia en Argentina</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Visualizaciones informativas sobre la Tasa de Incidencia y la Letalidad del COVID-19 en diferentes provincias de Argentina. Dos gráficos circulares (pie charts) ofrecen una perspectiva clara y concisa de la distribución de estas métricas esenciales. El primer gráfico destaca la provincia con la mayor Tasa de Incidencia, mientras que el segundo identifica la provincia con la mayor Letalidad.</p>", unsafe_allow_html=True)
    st.write("##")

    # Dividir el contenedor en dos columnas para los gráficos
    tabla_column, text_column = st.columns(2)

    # En la primera columna (izquierda), mostrar el gráfico de tasa de incidencia
    with text_column:
        # Crear el gráfico circular (pie chart) con Plotly Express para tasa de incidencia
        fig = px.pie(
            df,
            values='Tasa de incidencia',
            names='Provincias',
            color_discrete_sequence=px.colors.sequential.Purples,
            title='Provincia con Más Tasa de Incidencia de COVID-19 en Argentina',
            hover_data=['Tasa de incidencia'],
            labels={'Tasa de incidencia': 'Número de Tasa de Incidencia'},
            hole=0.5,
        )

        # Configuraciones específicas del gráfico de tasa de incidencia
        fig.update_traces(textposition='inside', textinfo='percent+label')

        # Ajustar el diseño del gráfico de tasa de incidencia
        fig.update_layout(
            width=800,
            height=500,
            margin=dict(t=40, b=60),
            showlegend=True,
            legend=dict(x=1, y=0.5),
        )

        # Personalizar la paleta de colores
        fig.update_traces(marker=dict(line=dict(color='#ffffff', width=1)))

        # Personalizar el cuadro emergente al pasar el mouse
        fig.update_traces(
            hovertemplate='<b>%{label}</b><br>Tasa de Incidencia: %{percent}<br>',
        )

        # Mostrar el gráfico de tasa de incidencia en Streamlit
        st.plotly_chart(fig, use_container_width=True)

    # En la segunda columna (derecha), mostrar el gráfico de letalidad
    with tabla_column:
        # Crear el gráfico circular (pie chart) con Plotly Express para letalidad
        fig = px.pie(
            df,
            values='Letalidad',
            names='Provincias',
            color_discrete_sequence=px.colors.sequential.Purples,
            title='Provincia con Más Letalidad de COVID-19 en Argentina',
            hover_data=['Letalidad'],
            labels={'Letalidad': 'Número de Letalidad'},
            hole=0.5,
        )

        # Configuraciones específicas del gráfico de letalidad
        fig.update_traces(textposition='inside', textinfo='percent+label')

        # Ajustar el diseño del gráfico de letalidad
        fig.update_layout(
            width=800,
            height=500,
            margin=dict(t=40, b=60),
            legend=dict(x=1, y=0.5),
        )

        # Personalizar la paleta de colores
        fig.update_traces(marker=dict(line=dict(color='#ffffff', width=1)))

        # Personalizar el cuadro emergente al pasar el mouse
        fig.update_traces(
            hovertemplate='<b>%{label}</b><br>Letalidad: %{percent}<br>')

        # Mostrar el gráfico de letalidad en Streamlit
        st.plotly_chart(fig, use_container_width=True)


# Separadores visuales para dar espacio antes de mostrar el gráfico
st.write("##")
st.write("##")

# Crear un contenedor para organizar el diseño
with st.container():
    # Título y descripción de la relación entre tasa de incidencia y letalidad
    st.markdown("<h1 style='text-align: center;'>Relación entre Tasa de Incidencia y Letalidad por Provincia en Argentina</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>La visualización presenta un gráfico de dispersión que analiza la relación entre la Tasa de Incidencia y la Letalidad por provincia en Argentina. Cada punto en el gráfico representa una provincia, donde el eje x representa la Tasa de Incidencia y el eje y representa la Letalidad. El tamaño de los marcadores indica la magnitud de la relación entre estas dos métricas críticas.</p>", unsafe_allow_html=True)

    # Crear el gráfico de dispersión con Plotly Express
    fig = px.scatter(df, x="Tasa de incidencia", y="Letalidad", text="Provincias",
                    labels={"Tasa de incidencia": "Número de Tasa de Incidencia", "Letalidad": "Número de Letalidad"},
                    hover_name="Provincias", color_discrete_sequence=["#A385FF"], size_max=50)

    # Personalizar el diseño y estilo del gráfico
    fig.update_traces(marker=dict(size=12, line=dict(width=2, color='DarkSlateGray')),
                    textposition='top center', textfont_size=9)

    fig.update_layout(
                    xaxis_title='Número de Tasa de Incidencia',
                    yaxis_title='Número de Letalidad',
                    showlegend=False)

    # Personalizar la información que aparece al pasar el mouse sobre los puntos
    fig.update_traces(hovertemplate='<b>%{hovertext}</b><br>Tasa de Incidencia: %{x:,.0f}<br>Letalidad: %{y:,.2f}')

    # Mostrar el gráfico en Streamlit
    st.plotly_chart(fig, use_container_width=True)

