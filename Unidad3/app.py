import streamlit as st
import pandas as pd
import os
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

#  Resolver ruta absoluta del logo usando el directorio base del script
LOGO_PATH = BASE_DIR / "logo_utem.jpg"

# 2. Definir las secciones de navegación de la app
SECTIONS = [
    "Portada",
    "Problema",
    "Estado del arte",
    "Pregunta e hipótesis",
    "Objetivos",
    "Uso de IA",
]

#  Construir la barra lateral completa en un único bloque unificado
with st.sidebar:
    # Renderizar el logo de la UTEM si físicamente existe en el repositorio
    if LOGO_PATH.exists():
        try:
            st.image(str(LOGO_PATH), use_container_width=True)
        except Exception as e:
            st.markdown("### UTEM")
            st.caption("Error al cargar imagen local")
    else:
        # Fallback si el archivo no está en el repositorio de GitHub
        try:
            st.image("https://via.placeholder.com/200x100.png?text=UTEM", use_container_width=True)
        except Exception:
            st.markdown("### UTEM")

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

with st.sidebar:
    st.title("Unidad 3")
    st.caption("Hipótesis y objetivos de investigación")
    section = st.radio("Navegación", SECTIONS, index=0)
    st.divider()

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

st.divider()
st.caption("Unidad 3 · Hipótesis y objetivos de investigación · Metodología de la Investigación en Ciencia de Datos")
