import streamlit as st
import plotly.express as px
from common import *

page_config("Estudios incluidos", "📚")
render_header("Artículos incluidos y related work", "Los 6 estudios que forman la síntesis final")

estudios = load_csv("estudios_incluidos.csv")
if estudios.empty:
    st.warning("No se encontró la tabla de estudios incluidos.")
else:
    filtro = st.text_input("Filtrar por autor, título, método o aporte")
    df = estudios.copy()
    if filtro:
        mask = df.apply(lambda col: col.astype(str).str.contains(filtro, case=False, na=False)).any(axis=1)
        df = df[mask]
    st.dataframe(df, use_container_width=True, hide_index=True)

    st.subheader("Exploración por método principal")
    method_terms = {
        "Clustering": "clustering|K-means",
        "Regresión": "regresión|regression",
        "SEM / longitudinal": "SEM|longitudinal",
        "Redes": "red|network",
        "Minería de datos / EDA": "Minería|exploratorio|EDA",
        "Multinivel / diario": "multinivel|diario",
    }
    counts = []
    for name, pat in method_terms.items():
        counts.append([name, int(estudios["metodo_principal"].str.contains(pat, case=False, regex=True).sum())])
    chart_df = pd.DataFrame(counts, columns=["método", "n"])
    fig = px.bar(chart_df, x="método", y="n", text="n", title="Métodos identificados en los estudios incluidos")
    fig.update_layout(yaxis_title="Número de estudios", xaxis_title="Método", height=420)
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Lectura crítica rápida")
col1, col2, col3 = st.columns(3)
with col1:
    card("Más cercano a Ciencia de Datos", "Alluri et al. (2026): clustering justo, equidad algorítmica e inferencia causal.")
with col2:
    card("Evidencia directa sobre burnout", "Cuevas Caravaca et al. (2025) y Mudło-Głagolska & Larionow (2025).")
with col3:
    card("Evidencia complementaria", "Bojorque et al. y Rodrigues Matos et al. amplían el análisis hacia estrés, hábitos y datos institucionales.")

st.subheader("Material relacionado")
st.markdown(
    """
    La revisión combina evidencia directa sobre burnout académico con evidencia complementaria sobre salud mental,
    hábitos de estudio, uso de tecnología y analítica institucional. Esto se justifica por la baja disponibilidad de
    estudios que combinen simultáneamente burnout académico, población universitaria y modelos predictivos avanzados.
    """
)
