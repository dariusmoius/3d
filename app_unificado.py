import numpy as np
import plotly.graph_objects as go
import streamlit as st

# Configuración del entorno web de la aplicación
st.set_page_config(page_title="Motor Unificado QAST + HDC-CBC", layout="wide")
st.title("🌌 Motor Operativo Unificado: Q.A.S.T. / HDC-CBC")
st.markdown("### Emergencia del Tensor de Vacío desde Primeros Principios Variacionales")

# Barra lateral interactiva para parámetros de control físico
st.sidebar.header("Parámetros del Sustrato Cuántico")
H0_base = st.sidebar.slider("H0 Base Cosmológica (Planck)", 65.0, 70.0, 67.4, step=0.1)
V_rot = st.sidebar.slider("Velocidad de Acoplamiento (Gaia) [km/s]", 200.0, 300.0, 240.0, step=10.0)
z_decay = st.sidebar.slider("Límite de la Burbuja Local (z_decay)", 0.005, 0.03, 0.01, step=0.001)

# Generación de la matriz bidimensional de datos observacionales
z_space = np.linspace(0, 0.05, 100)
v_space = np.linspace(0, 1000, 100)
Z, V = np.meshgrid(z_space, v_space)

# Computación del acoplamiento reológico condicionado
actividad = (np.abs(V) / V_rot) * 100
friccion_emergente = np.tanh(actividad / 100) * np.exp(-Z / z_decay)
H0_surface = H0_base + 5.6 * friccion_emergente

# Renderizado de la Devolución 3D con Plotly
fig = go.Figure(data=[go.Surface(
    z=H0_surface, x=Z, y=V, 
    colorscale='Plasma',
    colorbar=dict(title='H0 (km/s/Mpc)')
)])

fig.update_layout(
    scene=dict(
        xaxis_title='Redshift (z)',
        yaxis_title='Velocidad Peculiar (km/s)',
        zaxis_title='H0 Efectivo',
        xaxis=dict(backgroundcolor="rgb(15, 15, 25)", gridcolor="gray", showbackground=True),
        yaxis=dict(backgroundcolor="rgb(15, 15, 25)", gridcolor="gray", showbackground=True),
        zaxis=dict(backgroundcolor="rgb(15, 15, 25)", gridcolor="gray", showbackground=True)
    ),
    template='plotly_dark',
    width=1000,
    height=750,
    margin=dict(l=0, r=0, b=0, t=30)
)

# Proyección en la interfaz de Streamlit
st.plotly_chart(fig, use_container_width=True)
