import streamlit as st
import plotly.express as px
from common import *

page_config("Resultados", "📈")
render_header("Resultados principales y visualizaciones", "Variables, métodos y hallazgos sintetizados")

variables = load_csv("variables_metodos.csv")
st.subheader("Síntesis de variables y métodos")
st.dataframe(variables, use_container_width=True, hide_index=True)

st.subheader("Dimensiones analizadas")
if not variables.empty:
    dim_counts = variables.assign(n=1)
    fig = px.bar(dim_counts, x="dimension", y="n", text="dimension", title="Dimensiones integradas en la revisión")
    fig.update_layout(showlegend=False, yaxis_visible=False, xaxis_title="", height=420)
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Factores de riesgo y factores protectores")
risk, prot = st.columns(2)
with risk:
    st.markdown("### Factores de riesgo")
    st.markdown(
        """
        - Agotamiento académico
        - Cinismo y desenganche
        - Ansiedad y síntomas depresivos
        - Menor sueño
        - Mayor tiempo de estudio
        - Uso del smartphone en clase
        - Experiencias de discriminación
        """
    )
with prot:
    st.markdown("### Factores protectores")
    st.markdown(
        """
        - Ejercicio físico
        - Pasión armoniosa por estudiar
        - Sueño suficiente
        - Participación social o cultural
        - Estabilidad financiera
        - Engagement académico
        """
    )

st.subheader("Operacionalización para futuros modelos predictivos")
oper = pd.DataFrame([
    ["Variable objetivo", "Burnout alto; agotamiento; cansancio emocional; perfil at-risk", "Escala o clase", "Definir salida del modelo"],
    ["Psicológico", "Ansiedad; depresión; bienestar; engagement; pasión armoniosa", "Encuesta validada", "Estimar riesgo individual"],
    ["Académico", "Notas; avance curricular; carga académica; asistencia; reprobaciones", "Registro institucional", "Complementar evidencia subjetiva"],
    ["Conductual", "Sueño; horas de estudio; ejercicio; smartphone; participación social", "Encuesta o registro diario", "Detectar factores modificables"],
    ["Sociodemográfico", "Edad; sexo; carrera; nivel socioeconómico; grupo subrepresentado", "Registro o encuesta", "Evaluar equidad y contexto"],
    ["Evaluación", "AUC; F1-score; sensibilidad; especificidad; calibración; explicabilidad", "Métrica de modelo", "Comparar desempeño y utilidad"],
], columns=["Componente", "Ejemplos de variables", "Tipo de dato", "Uso potencial"])
st.dataframe(oper, use_container_width=True, hide_index=True)

st.info("Conclusión operativa: el problema no debe reducirse a un algoritmo específico; requiere combinación de desempeño predictivo, interpretabilidad, privacidad y equidad.")
