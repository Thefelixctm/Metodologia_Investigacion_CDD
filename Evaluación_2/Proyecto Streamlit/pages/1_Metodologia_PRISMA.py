import streamlit as st
import plotly.express as px
from common import *

page_config("Metodología y PRISMA", "🔎")
render_header("Metodología y flujo PRISMA", "Búsqueda, criterios, selección y trazabilidad")

st.subheader("Estrategia de búsqueda")
st.markdown(
    """
    **Bases consultadas:** Web of Science y Scopus.  
    **Fecha de búsqueda:** 24 de abril de 2026.  
    **Periodo:** 2021 a 2026.  
    **Ajuste aplicado:** en Web of Science se seleccionaron papers en español para reducir el volumen de registros.
    """
)

st.code(
    '(Academic burnout OR Student mental health OR Higher education) AND\n'
    '(Academic stress OR Risk factors) AND\n'
    '(Machine learning OR Predictive modeling OR Early detection)',
    language="text"
)

st.subheader("Criterios de inclusión y exclusión")
criterios = [
    ["Inclusión", "Artículos revisados por pares", "Asegura calidad científica mínima"],
    ["Inclusión", "Estudios sobre burnout académico, agotamiento académico o burnout estudiantil", "Asegura pertinencia temática"],
    ["Inclusión", "Estudios en estudiantes universitarios o educación superior", "Mantiene coherencia con la población objetivo"],
    ["Inclusión", "Estudios con métodos cuantitativos, computacionales o de Ciencia de Datos", "Permite analizar técnicas de modelado o predicción"],
    ["Inclusión", "Estudios con resumen, metadatos o texto completo disponible", "Permite evaluar pertinencia metodológica"],
    ["Exclusión", "Registros duplicados", "Evita sobrecontar evidencia"],
    ["Exclusión", "Estudios sin relación directa con burnout académico", "Reduce ruido temático"],
    ["Exclusión", "Estudios solo sobre salud mental general sin vínculo con burnout", "Evita desviar el alcance"],
    ["Exclusión", "Población no universitaria sin aporte metodológico relevante", "Mantiene coherencia poblacional"],
    ["Exclusión", "Documentos sin análisis estadístico, computacional o predictivo", "No aportan al enfoque de Ciencia de Datos"],
    ["Exclusión", "Texto completo no recuperado", "No permite evaluación adecuada"],
]
import pandas as pd
criterios_df = pd.DataFrame(criterios, columns=["Tipo", "Criterio", "Justificación"])
st.dataframe(criterios_df, use_container_width=True, hide_index=True)

st.subheader("Diagrama PRISMA")
col1, col2 = st.columns([1.2, 1])
with col1:
    st.image(ASSET_DIR / "prisma_final.png", use_container_width=True)
with col2:
    prisma = load_csv("prisma_counts.csv")
    fig = px.bar(prisma, x="etapa", y="n", text="n", title="Conteos del proceso PRISMA")
    fig.update_layout(xaxis_title="Etapa", yaxis_title="Cantidad", xaxis_tickangle=-35, height=520)
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Evaluación y síntesis de evidencia")
st.markdown(
    """
    La evaluación se realizó mediante síntesis narrativa y comparativa. No se aplicó metaanálisis por la
    heterogeneidad de poblaciones, instrumentos, diseños, variables y métricas. Los estudios se compararon
    por tipo de población, variable asociada al burnout, tipo de dato, método de análisis, resultados y limitaciones.
    ChatGPT fue usado como apoyo para ordenar la síntesis, pero la interpretación final fue revisada manualmente.
    """
)
