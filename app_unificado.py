import numpy as np
import plotly.graph_objects as go

# 1. Definición del mallado de datos (Grid espacial y cinemático)
# x: Desplazamiento al rojo (z) que cubre la burbuja local y su vecindad (0 a 0.05)
# y: Velocidad peculiar corregida en km/s (0 a 1000 km/s)
z = np.linspace(0, 0.05, 100)

v_pec = np. espacio de línea ( 0, 1000, 100 )
Z, V = np. cuadrícula de malla ( z, v_pec )

# 2. Parámetros físicos reales de la Teoría QAST
V_rot = 240.0       # Escala de acoplamiento cinemático de la misión Gaia (km/s)
z_decay = 0.01      # Parámetro de decadencia dinámica de la burbuja local (~30 Mpc)
H0_baseline = 67.4  # Valor base cosmológico de la colaboración Planck

# 3. Cálculo del Factor de Actividad (A) y modulación de la métrica
actividad = ( np. abs ( V ) / V_rot ) * 100
# El término exponencial modela el efecto de pantalla del vacío
H0_superficie = H0_línea base + 2,3 * np. log10 ( 1 + actividad ) * np. exp ( -Z/z_decay )

# 4. Diseño del Gráfico con Devolución 3D Interactiva
fig = ir. Figura ( datos= [ ir. Superficie (
    z=superficie_H0,
    x=Z,
    y=V,
    escala de colores = 'Viridis' ,
    barra de color = dict ( título = 'H0 Aparente (km/s/Mpc)' )
) ] )

# 5. Configuración de los ejes y entorno visual (Estilo Dark/Académico)
fig. actualizar_diseño (
    title= 'Superficie de Solución QAST: H0 vs. Redshift y Velocidad Peculiar' ,
    escena = diccionario (
        xaxis_title= 'Desplazamiento al rojo (z)' ,
        yaxis_title= 'Velocidad Peculiar v_pec (km/s)' ,
        zaxis_title= 'H0 (km/s/Mpc)' ,
        xaxis=dict(backgroundcolor="rgb(20, 24, 35)", gridcolor="gray", showbackground=True),
        yaxis=dict(backgroundcolor="rgb(20, 24, 35)", gridcolor="gray", showbackground=True),
        zaxis=dict(backgroundcolor="rgb(20, 24, 35)", gridcolor="gray", showbackground=True, range=[65, 75])
    ),
    template='plotly_dark',
    margin=dict(l=0, r=0, b=0, t=50),
    width=900,
    height=700
)

# Para ejecutar localmente en tu entorno de desarrollo o integrarlo a Streamlit:
# fig.show()
