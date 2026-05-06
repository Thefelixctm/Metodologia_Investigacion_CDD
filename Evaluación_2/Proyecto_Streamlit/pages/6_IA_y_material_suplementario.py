import streamlit as st
from common import *

page_config("IA y material suplementario", "🤖")
render_header("Declaración de IA y material suplementario", "Transparencia, trazabilidad y descargas")

st.subheader("Uso declarado de inteligencia artificial")
st.markdown(
    """
    En esta revisión se utilizaron herramientas de IA como apoyo auxiliar. Gemini fue utilizado únicamente
    en la formulación inicial del problema. ChatGPT fue utilizado para apoyar búsqueda y criterios,
    extracción de datos, síntesis de evidencia, redacción y tablas. La IA no reemplazó la revisión humana.
    """
)

ia = load_csv("uso_ia.csv")
st.dataframe(ia, use_container_width=True, hide_index=True)

st.subheader("Verificación humana")
st.markdown(
    """
    La selección final de artículos, la recuperación de textos completos, la interpretación de resultados y la
    validación de la información fueron realizadas manualmente. La información generada con IA fue contrastada
    con los artículos incluidos, la base filtrada, el diagrama PRISMA y la matriz de extracción.
    """
)

st.subheader("Material suplementario descargable")
files = [
    ("01_articulos_identificados_y_seleccionados.xlsx", "Artículos identificados y seleccionados"),
    ("02_matriz_extraccion_datos_6_estudios.xlsx", "Matriz completa de extracción de datos"),
    ("03_criterios_inclusion_exclusion_aplicados.xlsx", "Criterios de inclusión y exclusión aplicados"),
    ("04_prompts_principales_utilizados_con_IA.xlsx", "Prompts principales utilizados con IA"),
    ("05_tabla_uso_IA_verificacion_humana.xlsx", "Tabla de uso de IA y verificación humana"),
    ("06_registro_articulos_excluidos_texto_completo.xlsx", "Registro de artículos excluidos en texto completo"),
    ("manuscrito_revision_sistematica.pdf", "Manuscrito final PDF"),
]
for fname, label in files:
    path = DATA_DIR / fname
    ext = path.suffix.lower()
    mime = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" if ext == ".xlsx" else "application/pdf"
    download_file(path, f"Descargar: {label}", mime)

st.subheader("Referencias principales")
st.markdown(
    """
    - Alluri et al. (2026). *Fairness-aware K-means clustering in digital mental health for higher education students*.  
    - Cuevas Caravaca et al. (2025). *Academic burnout and emotional exhaustion among university students*.  
    - Mudło-Głagolska & Larionow (2025). *Passion for studying and its relationships with academic burnout and mental health*.  
    - Bojorque et al. (2025). *Stress Factors in Higher Education: A Data Analysis Case*.  
    - Rodrigues Matos et al. (2024). *Relationships between Student Burnout, Mental Health, Study Habits and Sleep*.  
    - Rodríguez Muñoz & Antino (2021). *El uso del teléfono móvil en clase y su efecto sobre el engagement académico y el agotamiento*.  
    - Page et al. (2021). *The PRISMA 2020 statement*.  
    """
)
