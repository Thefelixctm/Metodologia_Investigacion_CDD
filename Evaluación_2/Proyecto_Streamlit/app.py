import streamlit as st
import pandas as pd
import plotly.express as px
from common import *

page_config("Inicio | Burnout académico", "🎓")

render_header(
    "Predicción y modelado del burnout académico en estudiantes universitarios",
    "Revisión sistemática de literatura mediante técnicas de Ciencia de Datos"
)

c1, c2 = st.columns([2, 1])
with c1:
    st.markdown(f"""
    **Integrante:** {AUTHOR}  
    **Curso:** {COURSE}  
    **Universidad:** {UNIVERSITY}  
    **Correo:** {EMAIL}  
    **Fecha:** {DATE}
    """)
    st.markdown(
        """
        Esta aplicación comunica los contenidos principales del manuscrito: problema de investigación,
        metodología PRISMA, artículos incluidos, resultados, metodologías de Ciencia de Datos,
        discusión, vacíos de investigación, declaración de uso de IA y material suplementario.
        """
    )
with c2:
    st.image(ASSET_DIR / "prisma_final.png", caption="Flujo PRISMA final", use_container_width=True)

st.subheader("Problema de investigación")
st.markdown(
    """
    El burnout académico en estudiantes universitarios se asocia con agotamiento emocional,
    desenganche, bajo bienestar psicológico, rendimiento académico y permanencia estudiantil.
    El problema central es que muchas instituciones detectan este fenómeno cuando sus efectos ya
    son visibles. Desde la Ciencia de Datos, es posible analizar patrones de riesgo y diseñar
    mecanismos de detección temprana basados en variables psicológicas, académicas, conductuales
    e institucionales.
    """
)

col1, col2, col3, col4 = st.columns(4)
with col1: metric_card("Registros identificados", "1.020")
with col2: metric_card("Registros cribados", "898")
with col3: metric_card("Informes evaluados", "122")
with col4: metric_card("Estudios incluidos", "6")

st.subheader("Pregunta de investigación")
st.info(
    "¿Qué técnicas de Ciencia de Datos se han utilizado para predecir o modelar el burnout académico "
    "en estudiantes universitarios y qué vacíos metodológicos permanecen en la literatura?"
)

st.subheader("Preguntas específicas")
q1, q2 = st.columns(2)
with q1:
    card("Tipos de datos", "¿Qué datos psicológicos, académicos, conductuales e institucionales se utilizan?")
    card("Métodos", "¿Qué algoritmos, modelos o técnicas analíticas aparecen con mayor frecuencia?")
with q2:
    card("Métricas", "¿Qué procedimientos de evaluación reportan los estudios incluidos?")
    card("Limitaciones", "¿Qué problemas afectan la reproducibilidad, validez externa y aplicabilidad?")

st.subheader("Área OCDE y ODS")
col_a, col_b = st.columns([1, 2])
with col_a:
    st.markdown("**Área OCDE sugerida:** Ciencias Sociales")
    st.markdown("**Subárea:** Educación, Psicología y Ciencia de Datos aplicada")
with col_b:
    ods = load_csv("ods.csv")
    for _, row in ods.iterrows():
        st.markdown(f"<span class='tag'>{row['ods']}: {row['nombre']}</span>", unsafe_allow_html=True)
    st.dataframe(ods, use_container_width=True, hide_index=True)

st.subheader("Navegación sugerida")
st.markdown(
    """
    Usa el menú lateral para revisar las páginas: **Metodología**, **Estudios incluidos**,
    **Resultados**, **Discusión y vacíos**, **ODS**, y **IA + material suplementario**.
    """
)
