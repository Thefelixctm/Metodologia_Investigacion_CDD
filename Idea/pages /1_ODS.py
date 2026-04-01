import streamlit as st

st.set_page_config(page_title="Alineación con ODS", page_icon="🌍")

st.title("Alineación con los ODS 🌍")
st.write("Esta investigación contribuye directamente a los Objetivos de Desarrollo Sostenible de la ONU:")

# Usando columnas para mostrar los ODS de forma visual
col1, col2 = st.columns(2)

with col1:
    st.info("### ODS 3: Salud y Bienestar")
    st.write("Promueve el bienestar psicológico y la detección temprana de trastornos emocionales en universitarios.")

    st.success("### ODS 4: Educación de Calidad")
    st.write("Busca reducir la deserción y mejorar el rendimiento académico mediante el apoyo basado en datos.")

with col2:
    st.warning("### ODS 9: Innovación")
    st.write("Aplica Machine Learning y ciencia de datos avanzada para resolver problemas sociales complejos.")

st.markdown("---")
st.markdown("#### Metas Específicas")
st.table({
    "ODS": ["3. Salud", "4. Educación", "9. Innovación"],
    "Meta": ["3.4 (Salud Mental)", "4.4 (Competencias Técnicas)", "9.5 (Investigación Científica)"]
})

if st.button("Volver a la Idea Principal"):
    st.switch_page("app.py")
