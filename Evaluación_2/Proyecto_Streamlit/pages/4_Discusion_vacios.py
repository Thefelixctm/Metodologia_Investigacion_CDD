import streamlit as st
from common import *

page_config("Discusión y vacíos", "🧠")
render_header("Discusión, vacíos y proyección", "Interpretación crítica de la revisión")

st.subheader("Discusión central")
st.markdown(
    """
    Los estudios revisados muestran que el burnout académico no es un fenómeno aislado, sino un sistema
    de variables psicológicas, conductuales, académicas e institucionales. El agotamiento se vincula con
    cansancio emocional, ansiedad, desenganche, menor engagement, bajo bienestar y vulnerabilidad frente
    a factores de estrés. En contraste, el ejercicio físico, la pasión armoniosa, el sueño suficiente y la
    participación social aparecen como factores protectores.
    """
)

st.subheader("Tres grupos metodológicos")
c1, c2, c3 = st.columns(3)
with c1:
    card("Modelos explicativos", "Correlaciones y regresiones. Son interpretables, pero limitados para capturar relaciones complejas.")
with c2:
    card("Modelos temporales", "Diseños longitudinales, multinivel y de diario. Capturan cambios en el tiempo e intraindividuales.")
with c3:
    card("Ciencia de Datos", "Clustering, análisis de redes y minería institucional. Representan perfiles y relaciones multivariadas.")

st.subheader("Vacíos de investigación")
st.markdown(
    """
    1. Pocos estudios integran simultáneamente burnout académico, estudiantes universitarios y modelado predictivo avanzado.  
    2. Baja disponibilidad de datasets abiertos y código reproducible.  
    3. Muestras locales y escasa validación externa.  
    4. Instrumentos de medición heterogéneos.  
    5. Poca integración entre datos psicológicos, académicos, conductuales e institucionales.  
    6. Débil incorporación de equidad algorítmica y gobernanza de datos.  
    """
)

st.subheader("Proyección para un sistema de alerta temprana")
st.markdown(
    """
    Un sistema aplicado debería combinar encuestas validadas, registros académicos, hábitos de sueño,
    carga de estudio, uso de tecnología, engagement y variables sociodemográficas. El modelo debe ser
    explicable, auditable y usado con fines preventivos, no punitivos. En bienestar estudiantil, la precisión
    predictiva no basta: también se requiere consentimiento informado, privacidad, gobernanza de datos y
    revisión humana.
    """
)

st.warning("Riesgo metodológico: un modelo con alta precisión pero baja interpretabilidad puede ser poco útil o incluso riesgoso para decisiones institucionales sobre bienestar estudiantil.")
