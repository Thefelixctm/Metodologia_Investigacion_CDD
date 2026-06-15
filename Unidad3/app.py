import streamlit as st
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "articulos.csv"

st.set_page_config(
    page_title="Unidad 3 | Burnout académico y Ciencia de Datos",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    .main-title {
        font-size: 2.1rem;
        font-weight: 800;
        line-height: 1.15;
        margin-bottom: 0.3rem;
    }
    .subtitle {
        font-size: 1rem;
        color: #555;
        margin-bottom: 1.2rem;
    }
    .card {
        border: 1px solid rgba(49, 51, 63, 0.18);
        border-radius: 14px;
        padding: 1rem 1.1rem;
        background: rgba(250, 250, 250, 0.72);
        margin-bottom: 0.85rem;
    }
    .card h3 {
        margin-top: 0;
        margin-bottom: 0.35rem;
        font-size: 1.05rem;
    }
    .small {
        font-size: 0.9rem;
        color: #555;
    }
    .question-box {
        border-left: 6px solid #4b5563;
        background: rgba(243, 244, 246, 0.95);
        border-radius: 10px;
        padding: 1.1rem 1.2rem;
        font-size: 1.1rem;
        font-weight: 650;
        margin-bottom: 1rem;
    }
    .flow-card {
        min-height: 118px;
        border: 1px solid rgba(49, 51, 63, 0.16);
        border-radius: 14px;
        padding: 0.9rem;
        background: rgba(250,250,250,0.78);
    }
    .flow-title {
        font-weight: 800;
        margin-bottom: 0.35rem;
    }
    .metric-note {
        font-size: 0.85rem;
        color: #666;
        margin-top: -0.6rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def load_articles() -> pd.DataFrame:
    if DATA_PATH.exists():
        try:
            # Intentamos leer con UTF-8 estándar
            return pd.read_csv(DATA_PATH, sep=";", encoding="utf-8")
        except Exception:
            try:
                # Si falla, intentamos con latin-1 (muy común para archivos generados en Excel/Windows)
                return pd.read_csv(DATA_PATH, encoding="latin-1")
            except Exception as e:
                # Si sigue fallando por la estructura interna del CSV, mostramos una alerta
                st.sidebar.error(f"Error al parsear el CSV: {e}")
                
    # Fallback: Datos de respaldo idénticos a tu diseño original
    return pd.DataFrame(
        [
            {
                "Estudio": "Cuevas Caravaca et al.",
                "Año": 2025,
                "Tipo de evidencia": "Directa sobre burnout académico",
                "Población/datos": "789 universitarios",
                "Método principal": "Regresión lineal múltiple",
                "Aporte al planteamiento": "Identifica ejercicio físico como posible factor protector.",
                "Limitación o brecha": "Diseño transversal; no ML supervisado.",
            }
        ]
    )


def card(title: str, body: str):
    st.markdown(
        f"""
        <div class="card">
            <h3>{title}</h3>
            <div>{body}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def flow_card(title: str, body: str):
    st.markdown(
        f"""
        <div class="flow-card">
            <div class="flow-title">{title}</div>
            <div class="small">{body}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


articles = load_articles()

SECTIONS = [
    "Portada",
    "Problema",
    "Estado del arte",
    "Pregunta e hipótesis",
    "Objetivos",
    "Evidencia bibliográfica",
    "Coherencia del planteamiento",
    "Uso de IA",
    "Checklist rúbrica",
]

with st.sidebar:
    st.title("Unidad 3")
    st.caption("Hipótesis y objetivos de investigación")
    section = st.radio("Navegación", SECTIONS, index=0)
    st.divider()
    st.metric("Estudios finales", "6")
    st.metric("Bases consultadas", "2")
    st.metric("Registros iniciales", "1.020")
    st.caption("WoS + Scopus | Síntesis narrativa y comparativa")

if section == "Portada":
    st.markdown(
        '<div class="main-title">Modelamiento predictivo explicable del riesgo de burnout académico en estudiantes universitarios mediante técnicas de Ciencia de Datos</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="subtitle">Felipe Martínez González · Metodología de la Investigación en Ciencia de Datos · UTEM</div>',
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        card("Área OCDE", "Ciencias de la Educación, con enfoque metodológico en Ciencia de Datos e Inteligencia Artificial.")
    with col2:
        card("ODS vinculados", "ODS 3: Salud y bienestar · ODS 4: Educación de calidad · ODS 10: Reducción de desigualdades.")
    with col3:
        card("Producto", "App de presentación interactiva conectada con el informe escrito de la Unidad 3.")

    st.subheader("Propósito de la investigación")
    st.write(
        "La investigación busca transformar la revisión sistemática previa en un planteamiento investigable, "
        "centrado en una pregunta, una hipótesis y objetivos coherentes sobre el uso de Ciencia de Datos para "
        "modelar el riesgo de burnout académico."
    )

    st.info(
        "Idea central: el burnout académico no debe modelarse desde una sola dimensión. Un enfoque útil requiere "
        "integrar variables psicológicas, académicas y conductuales, con criterios de explicabilidad, reproducibilidad y equidad."
    )

elif section == "Problema":
    st.header("Problema de investigación")
    st.write(
        "El burnout académico es relevante en educación superior porque se asocia con agotamiento emocional, "
        "desenganche, bajo bienestar psicológico, menor rendimiento académico e intención de abandono."
    )

    col1, col2 = st.columns(2)
    with col1:
        card(
            "Fenómeno central",
            "Burnout académico entendido como agotamiento asociado al rol de estudiante, acompañado de cinismo, desenganche o baja eficacia académica.",
        )
        card(
            "Contexto",
            "Educación superior, donde los estudiantes enfrentan presión por desempeño, adaptación universitaria, carga académica, uso intensivo de tecnología y condiciones institucionales variables.",
        )
    with col2:
        card(
            "Problema para Ciencia de Datos",
            "La literatura muestra factores asociados, pero aún existen pocos modelos predictivos supervisados, validados, explicables y reproducibles para detección temprana.",
        )
        card(
            "Relevancia aplicada",
            "Un sistema de alerta temprana podría apoyar intervenciones preventivas, siempre que el modelo sea interpretable, ético y sensible al contexto universitario.",
        )

    st.subheader("Formulación sintética")
    st.warning(
        "El problema no es solo la existencia del burnout académico, sino la dificultad de traducirlo en modelos "
        "de Ciencia de Datos aplicables, explicables y útiles para la prevención en educación superior."
    )

elif section == "Estado del arte":
    st.header("Resumen del estado del arte")
    tab1, tab2, tab3, tab4 = st.tabs(["Fundamentos", "Avances", "Brechas", "Síntesis crítica"])

    with tab1:
        st.subheader("Conceptos y variables principales")
        st.write(
            "El burnout académico suele operacionalizarse mediante dimensiones como agotamiento emocional, "
            "cinismo o desenganche, y baja eficacia académica. Instrumentos como MBI-SS y OLBI permiten medir "
            "el fenómeno con escalas psicométricas."
        )
        st.write(
            "La literatura reciente también considera variables relacionadas: cansancio emocional, engagement académico, "
            "bienestar, ansiedad, depresión, sueño, hábitos de estudio, actividad física, uso del smartphone y factores sociodemográficos."
        )
        st.write(
            "Los métodos identificados incluyen regresión, análisis multinivel, modelos de ecuaciones estructurales, "
            "análisis de redes, clustering y minería de datos institucional."
        )

    with tab2:
        st.subheader("Avances identificados")
        st.markdown(
            """
            - La regresión permite relacionar dimensiones del burnout con cansancio emocional.
            - El análisis multinivel permite observar fluctuaciones diarias de agotamiento y engagement.
            - SEM longitudinal permite evaluar relaciones temporales entre pasión por estudiar, bienestar y burnout.
            - El análisis de redes permite identificar variables centrales dentro de sistemas psicológicos complejos.
            - El clustering con restricciones de equidad permite segmentar perfiles de salud mental reduciendo disparidades.
            - La minería de datos institucional permite detectar anomalías en registros académicos y condiciones del sistema.
            """
        )

    with tab3:
        st.subheader("Brechas metodológicas")
        st.markdown(
            """
            1. Evidencia heterogénea en población, instrumentos, técnicas y métricas.
            2. Predominio de estudios explicativos o exploratorios, no de modelos predictivos supervisados robustos.
            3. Falta de validación externa y reproducibilidad mediante datos o código disponible.
            4. Evidencia parcialmente indirecta: algunos estudios abordan salud mental, sueño, tecnología o analítica institucional, pero no burnout como variable objetivo central.
            5. Escasa integración de explicabilidad y equidad algorítmica en propuestas de detección temprana.
            """
        )

    with tab4:
        st.subheader("Síntesis crítica")
        st.success(
            "La literatura permite identificar factores asociados al burnout académico, pero todavía no consolida "
            "un marco predictivo supervisado, explicable y reproducible. La brecha central es integrar variables "
            "psicológicas, académicas y conductuales en una estructura de modelamiento útil para educación superior."
        )
        st.dataframe(
            articles[["Estudio", "Tipo de evidencia", "Método principal", "Limitación o brecha"]],
            use_container_width=True,
            hide_index=True,
        )

elif section == "Pregunta e hipótesis":
    st.header("Pregunta de investigación e hipótesis")

    st.subheader("Pregunta de investigación")
    st.markdown(
        """
        <div class="question-box">
        ¿En qué medida la integración de variables psicológicas, académicas y conductuales permite modelar de forma explicable el riesgo de burnout académico en estudiantes universitarios mediante técnicas de Ciencia de Datos?
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("Hipótesis")
    st.write(
        "Se hipotetiza que la integración de variables psicológicas, académicas y conductuales permitirá construir "
        "un modelo más útil y explicable para identificar riesgo de burnout académico en estudiantes universitarios "
        "que los enfoques basados en una sola dimensión de datos."
    )
    st.write(
        "Esta hipótesis se fundamenta en que la literatura reciente muestra que el burnout académico no depende "
        "de un único factor, sino de la interacción entre agotamiento, desenganche, bienestar psicológico, hábitos "
        "de estudio, sueño, uso de tecnología, actividad física y condiciones institucionales."
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        card("Variable / fenómeno central", "Riesgo de burnout académico en estudiantes universitarios.")
    with col2:
        card("Condición esperada", "Integración de variables psicológicas, académicas y conductuales.")
    with col3:
        card("Resultado esperado", "Modelo más explicable y útil para detección temprana que enfoques unidimensionales.")

elif section == "Objetivos":
    st.header("Objetivos de investigación")

    st.subheader("Objetivo general")
    st.info(
        "Evaluar el potencial de un modelo predictivo explicable para identificar riesgo de burnout académico "
        "en estudiantes universitarios mediante la integración de variables psicológicas, académicas y conductuales "
        "reportadas en la literatura reciente."
    )

    st.subheader("Objetivos específicos")
    objetivos = [
        "Identificar las variables psicológicas, académicas y conductuales más relevantes asociadas al burnout académico en estudiantes universitarios según la evidencia revisada.",
        "Caracterizar los enfoques metodológicos utilizados en la literatura reciente para analizar, modelar o predecir burnout académico y fenómenos relacionados.",
        "Comparar las principales brechas metodológicas de los estudios revisados, considerando tipo de datos, técnicas utilizadas, métricas reportadas, reproducibilidad y validación.",
        "Proponer una estructura preliminar de modelamiento predictivo explicable orientada a la detección temprana del riesgo de burnout académico en educación superior.",
    ]
    for i, obj in enumerate(objetivos, start=1):
        card(f"Objetivo específico {i}", obj)

elif section == "Evidencia bibliográfica":
    st.header("Evidencia bibliográfica")
    st.write("La tabla resume los seis estudios finales y distingue evidencia directa, complementaria e institucional.")

    tipos = ["Todos"] + sorted(articles["Tipo de evidencia"].unique().tolist())
    tipo_sel = st.selectbox("Filtrar por tipo de evidencia", tipos)
    filtered = articles.copy()
    if tipo_sel != "Todos":
        filtered = filtered[filtered["Tipo de evidencia"] == tipo_sel]

    st.dataframe(filtered, use_container_width=True, hide_index=True)

    st.subheader("Detalle por estudio")
    selected = st.selectbox("Selecciona un estudio", articles["Estudio"].tolist())
    row = articles[articles["Estudio"] == selected].iloc[0]

    col1, col2 = st.columns(2)
    with col1:
        card("Método principal", row["Método principal"])
        card("Población / datos", row["Población/datos"])
    with col2:
        card("Aporte", row["Aporte al planteamiento"])
        card("Limitación o brecha", row["Limitación o brecha"])

    st.subheader("Referencias clave")
    st.markdown(
        """
        - Alluri et al. (2026). *Fairness-aware K-means clustering in digital mental health for higher education students*.
        - Bojorque et al. (2025). *Stress factors in higher education: A data analysis case*.
        - Cuevas Caravaca et al. (2025). *Academic burnout and emotional exhaustion among university students*.
        - Mudło-Głagolska y Larionow (2025). *Passion for studying and its relationships with academic burnout and mental health*.
        - Rodrigues Matos et al. (2024). *Relações entre burnout estudantil, saúde mental, hábitos de estudo e sono*.
        - Rodríguez Muñoz y Antino (2021). *El uso del teléfono móvil en clase y su efecto sobre el engagement académico y el agotamiento*.
        """
    )

elif section == "Coherencia del planteamiento":
    st.header("Coherencia del planteamiento")
    st.write("La investigación se sostiene en una secuencia lógica: problema → brecha → pregunta → hipótesis → objetivos.")

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        flow_card("1. Problema", "Burnout académico asociado a agotamiento, desenganche, bajo bienestar y riesgo de abandono.")
    with col2:
        flow_card("2. Brecha", "Faltan modelos predictivos supervisados, explicables, reproducibles y validados externamente.")
    with col3:
        flow_card("3. Pregunta", "¿La integración de variables permite modelar explicablemente el riesgo?")
    with col4:
        flow_card("4. Hipótesis", "La integración multidimensional será más útil que enfoques basados en una sola dimensión.")
    with col5:
        flow_card("5. Objetivos", "Identificar variables, caracterizar métodos, comparar brechas y proponer estructura de modelamiento.")

    st.subheader("Relación entre variables")
    st.markdown(
        """
        **Variables psicológicas:** agotamiento, desenganche, bienestar, ansiedad, depresión, engagement.  
        **Variables académicas:** rendimiento, carga académica, asistencia, avance curricular, reprobaciones.  
        **Variables conductuales:** sueño, tiempo de estudio, uso de smartphone, actividad física, participación social.  
        **Salida esperada:** riesgo de burnout académico o perfil de estudiante en riesgo.
        """
    )

    st.info(
        "La coherencia central es que la pregunta y la hipótesis emergen directamente de la brecha: "
        "la literatura identifica factores, pero no consolida un modelo predictivo explicable e integrado."
    )

elif section == "Uso de IA":
    st.header("Declaración de uso de inteligencia artificial")
    st.write(
        "Se utilizaron herramientas de IA como apoyo metodológico y de redacción. La interpretación final, "
        "selección de estudios y validación del contenido fueron revisadas manualmente."
    )

    ia_data = pd.DataFrame(
        [
            {
                "Herramienta": "Gemini",
                "Uso específico": "Exploración inicial de posibles enfoques de investigación.",
                "Verificación humana": "El tema final fue ajustado según la asignatura, la evidencia disponible y la revisión sistemática previa.",
            },
            {
                "Herramienta": "ChatGPT",
                "Uso específico": "Apoyo en síntesis, redacción académica, organización del planteamiento y construcción de la app Streamlit.",
                "Verificación humana": "Los contenidos fueron contrastados con el informe previo, los estudios finales seleccionados y la rúbrica de la Unidad 3.",
            },
        ]
    )
    st.dataframe(ia_data, use_container_width=True, hide_index=True)

    st.warning(
        "La IA no reemplazó la lectura crítica ni la decisión metodológica. Funcionó como apoyo auxiliar para organizar, resumir y presentar el trabajo."
    )

elif section == "Checklist rúbrica":
    st.header("Checklist de cumplimiento de la rúbrica")
    checklist = pd.DataFrame(
        [
            ["Portada", "Título, estudiante, asignatura, área OCDE y ODS", "Cumple"],
            ["Problema", "Explicación breve del problema de investigación", "Cumple"],
            ["Estado del arte", "Fundamentos, avances y brechas en formato visual", "Cumple"],
            ["Pregunta", "Pregunta principal destacada", "Cumple"],
            ["Hipótesis", "Hipótesis formulada y justificada", "Cumple"],
            ["Objetivo general", "Objetivo central destacado", "Cumple"],
            ["Objetivos específicos", "Lista ordenada y evaluable", "Cumple"],
            ["Evidencia bibliográfica", "Tabla breve de artículos principales", "Cumple"],
            ["Coherencia", "Relación problema-brecha-pregunta-hipótesis-objetivos", "Cumple"],
            ["Declaración de IA", "Herramientas, propósito y verificación humana", "Cumple"],
            ["Reproducibilidad", "app.py, requirements.txt, data/articulos.csv y README.md", "Cumple"],
        ],
        columns=["Sección", "Requisito", "Estado"],
    )
    st.dataframe(checklist, use_container_width=True, hide_index=True)

    st.success(
        "La app está diseñada como presentación interactiva, no como copia plana del informe. Usa navegación, tabs, cards, tabla filtrable y síntesis visual."
    )

st.divider()
st.caption("Unidad 3 · Hipótesis y objetivos de investigación · Metodología de la Investigación en Ciencia de Datos")
