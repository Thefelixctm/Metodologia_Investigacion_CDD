import streamlit as st
from common import *

page_config("ODS", "🌐")
render_header("Alineación con ODS", "Relación del proyecto con Objetivos de Desarrollo Sostenible")

st.markdown("Esta investigación contribuye directamente a tres ODS principales.")

ods = load_csv("ods.csv")
col1, col2 = st.columns(2)
for i, row in ods.iterrows():
    target = col1 if i < 2 else col2
    with target:
        if row['ods'] == 'ODS 3':
            st.info(f"### {row['ods']}: {row['nombre']}\n{row['descripcion']}\n\n**{row['meta']}**")
        elif row['ods'] == 'ODS 4':
            st.success(f"### {row['ods']}: {row['nombre']}\n{row['descripcion']}\n\n**{row['meta']}**")
        else:
            st.warning(f"### {row['ods']}: {row['nombre']}\n{row['descripcion']}\n\n**{row['meta']}**")

st.markdown("---")
st.subheader("Resumen de metas específicas")
st.dataframe(ods, use_container_width=True, hide_index=True)

if st.button("Volver al inicio"):
    st.switch_page("app.py")
