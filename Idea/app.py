import streamlit as st

st.set_page_config(
    page_title="Idea de Investigación - Salud Mental",
    page_icon="🧠",
    layout="centered"
)

# -----------------------
# IMAGEN INICIAL
# -----------------------
st.markdown("""
<div style="display:flex; justify-content:center;">
    <img src="https://assets.isu.pub/document-structure/240323220837-72cbe6a2ff108e4b792e485cad9848c2/v1/e7f3fb74941cb95df5bb8bbfe2ec105e.jpeg"
         style="width:100%; max-height:750px; object-fit:cover; border-radius:10px;">
</div>
""", unsafe_allow_html=True)

st.markdown("## Idea")
st.write(
    "Predicción del riesgo de burnout académico en estudiantes universitarios "
    "mediante técnicas de ciencia de datos."
)

st.markdown("## Fundamento o Motivación")
st.write(
    "La salud mental estudiantil es un tema cada vez más relevante en educación "
    "superior debido al aumento del estrés, la sobrecarga académica y el agotamiento "
    "emocional. El burnout académico afecta tanto el bienestar psicológico como el "
    "desempeño de los estudiantes, por lo que resulta pertinente estudiarlo desde "
    "una perspectiva basada en datos."
)

st.markdown("## Descripción del Problema")
st.write(
    "Muchas instituciones detectan el burnout académico cuando sus efectos ya son "
    "evidentes, como bajo rendimiento, ausentismo, desmotivación o abandono. "
    "El problema es la falta de mecanismos tempranos para identificar a estudiantes "
    "en riesgo. Desde la ciencia de datos, variables como carga académica, horas "
    "de sueño, asistencia, uso de plataformas virtuales y encuestas de bienestar "
    "podrían utilizarse para construir modelos predictivos."
)

st.markdown("## Relevancia")
st.write(
    "Esta investigación es relevante para la ciencia de datos porque permite aplicar "
    "análisis predictivo y detección de patrones sobre datos educacionales y de "
    "bienestar. Además, podría apoyar decisiones institucionales orientadas a la "
    "prevención, la intervención temprana y la mejora de la permanencia estudiantil."
)

st.markdown("## Palabras clave")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### Iniciales")
    st.markdown(
        """
        - Salud mental estudiantil  
        - Estudiantes universitarios  
        - Predicción  
        - Aprendizaje automático  
        - Factores de riesgo  
        - Bienestar psicológico  
        - Burnout académico
        """
    )

with col2:
    st.markdown("### Expansión con IA")
    st.markdown(
        """
        - student mental health  
        - college student mental health  
        - university students  
        - psychological wellbeing  
        - academic burnout  
        - student burnout  
        - academic stress  
        - emotional exhaustion  
        - predictive modeling  
        - machine learning  
        - educational data mining  
        - early detection  
        - MBI-SS
        """
    )

with col3:
    st.markdown("### Selección final")
    st.markdown(
        """
        - academic burnout  
        - student mental health  
        - higher education  
        - machine learning  
        - predictive modeling  
        - risk factors  
        - academic stress  
        - early detection
        """
    )

with st.expander("Prompt usado con IA"):
    st.code(
        'Expande estas palabras clave para una investigación en ciencia de datos '
        'sobre predicción de burnout académico en estudiantes universitarios. '
        'Incluye sinónimos, términos técnicos, variantes usadas en papers y '
        'conceptos relacionados.',
        language="text"
    )

st.markdown("---")
st.caption("Aplicación simple en Streamlit para presentar la idea de investigación.")
