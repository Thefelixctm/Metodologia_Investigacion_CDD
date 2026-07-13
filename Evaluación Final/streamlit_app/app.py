from __future__ import annotations

from pathlib import Path
from typing import Iterable

import pandas as pd
import plotly.express as px
import streamlit as st
from graphviz import Digraph

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
LOGO_PATH = BASE_DIR / "logo_utem.jpg"
ARTICLES_PATH = DATA_DIR / "articulos.csv"
VARIABLES_PATH = DATA_DIR / "variables_propuestas.csv"
OBJECTIVES_PATH = DATA_DIR / "objetivos_metodos.csv"

st.set_page_config(
    page_title="Entrega final | Burnout académico explicable",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    :root {
        --ink: #172033;
        --muted: #5d6778;
        --line: rgba(23, 32, 51, 0.14);
        --surface: rgba(248, 250, 252, 0.90);
        --accent: #006d77;
        --accent-soft: rgba(0, 109, 119, 0.09);
        --warning-soft: rgba(196, 124, 0, 0.10);
    }
    .block-container {padding-top: 1.8rem; padding-bottom: 3rem; max-width: 1450px;}
    .hero {
        padding: 1.5rem 1.6rem;
        border: 1px solid var(--line);
        border-radius: 22px;
        background: linear-gradient(135deg, rgba(0,109,119,.11), rgba(255,255,255,.92));
        margin-bottom: 1.2rem;
    }
    .hero h1 {font-size: 2.25rem; line-height: 1.13; margin: 0 0 .6rem 0; color: var(--ink);}
    .hero p {font-size: 1rem; color: var(--muted); margin: 0;}
    .card {
        border: 1px solid var(--line);
        border-radius: 16px;
        padding: 1rem 1.05rem;
        background: var(--surface);
        min-height: 128px;
        margin-bottom: .85rem;
    }
    .card h3 {font-size: 1.02rem; margin: 0 0 .45rem 0; color: var(--ink);}
    .card p {margin: 0; color: var(--muted); line-height: 1.48;}
    .statement {
        border-left: 6px solid var(--accent);
        background: var(--accent-soft);
        border-radius: 12px;
        padding: 1rem 1.1rem;
        font-size: 1.07rem;
        font-weight: 650;
        color: var(--ink);
        margin: .7rem 0 1rem 0;
    }
    .warning-box {
        border-left: 6px solid #c47c00;
        background: var(--warning-soft);
        border-radius: 12px;
        padding: .95rem 1.05rem;
        color: var(--ink);
        margin: .7rem 0;
    }
    .eyebrow {text-transform: uppercase; letter-spacing: .09em; font-size: .72rem; font-weight: 800; color: var(--accent);}
    .small-note {font-size: .88rem; color: var(--muted);}
    .step {
        border: 1px solid var(--line);
        border-radius: 15px;
        padding: .85rem;
        background: rgba(255,255,255,.78);
        min-height: 140px;
    }
    .step-number {
        display: inline-block; width: 1.8rem; height: 1.8rem; line-height: 1.8rem;
        text-align: center; border-radius: 999px; background: var(--accent); color: white;
        font-weight: 800; margin-bottom: .45rem;
    }
    [data-testid="stSidebar"] {border-right: 1px solid var(--line);}
    div[data-testid="stMetric"] {border: 1px solid var(--line); padding: .75rem; border-radius: 14px; background: var(--surface);}
    </style>
    """,
    unsafe_allow_html=True,
)

SECTIONS = [
    "Portada",
    "Problema y brecha",
    "Pregunta, hipótesis y objetivos",
    "Diseño metodológico",
    "Dataset propuesto",
    "Modelos y explicabilidad",
    "Evaluación y estabilidad",
    "Resultados, alcance y ética",
    "Coherencia del proyecto",
    "Evidencia bibliográfica",
    "Uso de IA",
]


def read_csv(path: Path, fallback: Iterable[dict] | None = None) -> pd.DataFrame:
    try:
        return pd.read_csv(path)
    except Exception as exc:
        st.warning(f"No fue posible cargar {path.name}: {exc}")
        return pd.DataFrame(list(fallback or []))


def card(title: str, body: str) -> None:
    st.markdown(
        f'<div class="card"><h3>{title}</h3><p>{body}</p></div>',
        unsafe_allow_html=True,
    )


def statement(text: str) -> None:
    st.markdown(f'<div class="statement">{text}</div>', unsafe_allow_html=True)


def warning_box(text: str) -> None:
    st.markdown(f'<div class="warning-box">{text}</div>', unsafe_allow_html=True)


def methodology_graph() -> Digraph:
    graph = Digraph()
    graph.attr(rankdir="LR", bgcolor="transparent", pad="0.2", nodesep="0.35", ranksep="0.45")
    graph.attr("node", shape="box", style="rounded,filled", fontname="Arial", fontsize="10", color="#8ca3a7", fillcolor="#f7fafb", margin="0.14")
    graph.attr("edge", color="#006d77", penwidth="1.5", arrowsize="0.7")
    nodes = [
        ("A", "Diseño del\ncuestionario"),
        ("B", "Piloto y\nconsentimiento"),
        ("C", "Recolección\nprospectiva"),
        ("D", "Anonimización y\ncontrol de calidad"),
        ("E", "Preprocesamiento\ndentro de validación"),
        ("F", "Elastic Net\ny XGBoost"),
        ("G", "SHAP, permutación\ny ablación"),
        ("H", "Estabilidad,\ninterpretación y ética"),
    ]
    for key, label in nodes:
        graph.node(key, label)
    for left, right in zip([n[0] for n in nodes[:-1]], [n[0] for n in nodes[1:]]):
        graph.edge(left, right)
    return graph


articles = read_csv(ARTICLES_PATH)
variables = read_csv(VARIABLES_PATH)
objectives = read_csv(OBJECTIVES_PATH)

with st.sidebar:
    if LOGO_PATH.exists():
        st.image(str(LOGO_PATH), width="stretch")
    st.markdown("### Entrega 4")
    st.caption("Formulación final del proyecto de investigación")
    section = st.radio("Navegación", SECTIONS, index=0)
    st.divider()
    st.caption("Felipe Martínez González")
    st.caption("Metodología de la Investigación en Ciencia de Datos")

if section == "Portada":
    st.markdown(
        """
        <div class="hero">
          <div class="eyebrow">Propuesta de investigación · Ciencia de Datos</div>
          <h1>Contribución predictiva de variables psicológicas, académicas y conductuales al burnout académico en estudiantes universitarios</h1>
          <p>Modelos explicables, dataset prospectivo y evaluación de estabilidad de las contribuciones.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric("Tipo de estudio", "Predictivo", help="Observacional, cuantitativo y prospectivo")
    with c2:
        st.metric("Unidad de análisis", "Estudiante", help="Estudiantes de pregrado participantes")
    with c3:
        st.metric("Modelos", "2", help="Elastic Net y XGBoost")
    with c4:
        st.metric("Dimensiones", "3", help="Psicológica, académica y conductual")

    statement(
        "El eje del proyecto no es determinar solamente qué algoritmo obtiene mejores métricas, sino identificar qué variables aportan información predictiva, en qué dirección lo hacen y qué tan estables son esas conclusiones."
    )

    col1, col2 = st.columns([1.3, 1])
    with col1:
        st.subheader("Propósito")
        st.write(
            "Diseñar una investigación reproducible que permita construir un dataset futuro, validar modelos predictivos y analizar la contribución de variables asociadas al burnout académico sin atribuir causalidad ni realizar diagnósticos clínicos."
        )
        st.subheader("Palabras clave")
        st.markdown("`burnout académico` · `explicabilidad` · `predicción` · `estudiantes universitarios` · `Ciencia de Datos`")
    with col2:
        card("Contexto", "Educación superior y bienestar estudiantil, con aplicación metodológica de aprendizaje automático explicable.")
        card("Alcance", "Propuesta de investigación. No se presentan resultados empíricos ni se afirma que las variables causen burnout.")

elif section == "Problema y brecha":
    st.header("Problema, antecedentes y brecha")
    st.write(
        "El burnout académico se relaciona con agotamiento, desenganche y deterioro del bienestar estudiantil. La literatura identifica múltiples factores asociados, pero suele analizarlos de forma fragmentada o mediante enfoques principalmente explicativos."
    )

    c1, c2, c3 = st.columns(3)
    with c1:
        card("Problema sustantivo", "El fenómeno es multidimensional y puede afectar bienestar, engagement, desempeño y permanencia universitaria.")
    with c2:
        card("Problema analítico", "Una métrica predictiva aislada no permite saber qué variables utiliza el modelo ni si sus explicaciones son robustas.")
    with c3:
        card("Problema aplicado", "Una alerta temprana no debería operar como caja negra ni sustituir una evaluación profesional.")

    st.subheader("Brecha de investigación")
    statement(
        "Existe una integración limitada entre modelamiento predictivo, comparación de grupos de variables, explicabilidad y evaluación de la estabilidad de las interpretaciones en estudios de burnout académico."
    )

    tab1, tab2, tab3 = st.tabs(["Qué se conoce", "Qué falta", "Aporte propuesto"])
    with tab1:
        st.markdown(
            """
            - Se han descrito asociaciones con estrés, sueño, engagement, actividad física, carga académica y uso de tecnología.
            - Se han empleado regresión, análisis multinivel, ecuaciones estructurales, redes, clustering y minería de datos institucional.
            - Existen instrumentos psicométricos para operacionalizar el burnout académico.
            """
        )
    with tab2:
        st.markdown(
            """
            - Comparar los tres grupos de variables dentro de un mismo diseño.
            - Evaluar cuánto se deteriora el modelo al retirar una dimensión completa.
            - Contrastar la importancia mediante métodos complementarios.
            - Medir si los rankings de variables se mantienen entre modelos y particiones.
            """
        )
    with tab3:
        st.markdown(
            """
            - Dataset prospectivo documentado.
            - Comparación entre un modelo lineal regularizado y uno no lineal.
            - Explicaciones globales y locales.
            - Análisis de ablación y estabilidad.
            - Discusión explícita de límites causales y éticos.
            """
        )

elif section == "Pregunta, hipótesis y objetivos":
    st.header("Pregunta, hipótesis y objetivos")
    st.subheader("Pregunta de investigación")
    statement(
        "¿Qué variables psicológicas, académicas y conductuales presentan una mayor contribución predictiva al nivel de burnout académico en estudiantes de pregrado, y qué tan estables son dichas contribuciones entre un modelo Elastic Net y un modelo XGBoost?"
    )

    st.subheader("Hipótesis de investigación")
    st.info(
        "Las variables psicológicas y conductuales presentarán una contribución predictiva mayor y más estable que las variables académicas consideradas de manera aislada. Además, el modelo que integre las tres dimensiones presentará menor error predictivo que los modelos construidos con una sola dimensión."
    )
    st.caption("La hipótesis se refiere a contribución predictiva, no a causalidad.")

    st.subheader("Objetivo general")
    st.success(
        "Analizar la contribución predictiva de variables psicológicas, académicas y conductuales al nivel de burnout académico en estudiantes de pregrado mediante modelos explicables de Ciencia de Datos."
    )

    st.subheader("Objetivos específicos")
    goals = [
        ("OE1", "Diseñar y construir un dataset prospectivo que integre una medición validada de burnout con variables psicológicas, académicas, conductuales y de control."),
        ("OE2", "Desarrollar y evaluar modelos Elastic Net y XGBoost para estimar el nivel de burnout académico."),
        ("OE3", "Estimar e interpretar la magnitud y dirección de las contribuciones mediante coeficientes estandarizados, SHAP e importancia por permutación."),
        ("OE4", "Comparar la contribución de los grupos de variables mediante ablación y evaluar la estabilidad de las variables más relevantes entre modelos y particiones."),
    ]
    cols = st.columns(2)
    for idx, (code, text) in enumerate(goals):
        with cols[idx % 2]:
            card(code, text)

elif section == "Diseño metodológico":
    st.header("Diseño metodológico")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        card("Enfoque", "Cuantitativo y computacional.")
    with c2:
        card("Diseño", "Observacional, prospectivo y transversal.")
    with c3:
        card("Alcance", "Predictivo, comparativo y explicable.")
    with c4:
        card("Población", "Estudiantes de pregrado de la institución definida para la ejecución.")

    st.subheader("Pipeline")
    st.graphviz_chart(methodology_graph(), width="stretch")

    st.subheader("Trazabilidad entre objetivos y métodos")
    st.dataframe(objectives, width="stretch", hide_index=True)
    st.download_button(
        "Descargar matriz metodológica",
        objectives.to_csv(index=False).encode("utf-8"),
        file_name="objetivos_metodos.csv",
        mime="text/csv",
    )

    st.subheader("Etapas")
    stages = [
        ("1", "Instrumentos", "Selección de escala de burnout y medidas predictoras con evidencia de validez y autorización de uso."),
        ("2", "Piloto", "Revisión de comprensión, duración, consistencia y funcionamiento del formulario."),
        ("3", "Recolección", "Consentimiento informado, participación voluntaria y captura prospectiva."),
        ("4", "Calidad", "Anonimización, duplicados, faltantes, rangos y documentación de exclusiones."),
        ("5", "Modelamiento", "Pipelines de preprocesamiento, ajuste y evaluación sin fuga de información."),
        ("6", "Explicación", "Coeficientes, SHAP, permutación, ablación y estabilidad entre folds."),
    ]
    row1 = st.columns(3)
    row2 = st.columns(3)
    for i, (num, title, text) in enumerate(stages):
        target = row1[i] if i < 3 else row2[i - 3]
        with target:
            st.markdown(
                f'<div class="step"><div class="step-number">{num}</div><strong>{title}</strong><div class="small-note">{text}</div></div>',
                unsafe_allow_html=True,
            )

elif section == "Dataset propuesto":
    st.header("Dataset prospectivo propuesto")
    statement(
        "La base se construirá en una etapa futura mediante una encuesta digital anónima. Cada fila representará a un estudiante y cada columna una variable definida previamente en el protocolo."
    )

    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Muestra inicial esperada", "300-400", help="El tamaño definitivo requerirá justificación formal antes de ejecutar el estudio")
    with c2:
        st.metric("Unidad de análisis", "1 estudiante")
    with c3:
        st.metric("Momento de medición", "1 corte", help="Diseño transversal")

    dims = variables[variables["Dimensión"] != "Variable objetivo"]["Dimensión"].value_counts().reset_index()
    dims.columns = ["Dimensión", "Número de variables"]
    fig = px.bar(
        dims,
        x="Dimensión",
        y="Número de variables",
        text="Número de variables",
        title="Cobertura prevista del diccionario de datos",
    )
    fig.update_layout(showlegend=False, margin=dict(l=20, r=20, t=55, b=20), height=360)
    st.plotly_chart(fig, width="stretch")
    st.caption("El gráfico representa el diseño preliminar del dataset; no corresponde a resultados observados.")

    st.subheader("Diccionario preliminar")
    selected_dims = st.multiselect(
        "Filtrar dimensiones",
        options=variables["Dimensión"].dropna().unique().tolist(),
        default=variables["Dimensión"].dropna().unique().tolist(),
    )
    shown = variables[variables["Dimensión"].isin(selected_dims)]
    st.dataframe(shown, width="stretch", hide_index=True)
    st.download_button(
        "Descargar diccionario preliminar",
        shown.to_csv(index=False).encode("utf-8"),
        file_name="variables_propuestas.csv",
        mime="text/csv",
    )

    st.subheader("Criterios de selección")
    c1, c2 = st.columns(2)
    with c1:
        card("Inclusión", "Matrícula vigente; consentimiento; pertenencia a la población definida; respuesta suficiente del instrumento principal.")
        card("Calidad", "Controles de rango, duplicados, patrones inverosímiles y reglas de faltantes definidas antes del análisis.")
    with c2:
        card("Exclusión", "Sin consentimiento; registro duplicado; cuestionario insuficiente; población fuera del alcance definido.")
        card("Fuga de información", "Los ítems o dimensiones usados para construir el outcome no se incorporarán como predictores del mismo outcome.")

    warning_box(
        "El instrumento definitivo debe contar con evidencia de validez para estudiantes, reglas de puntuación claras y autorización de uso. No se inventarán puntos de corte."
    )

elif section == "Modelos y explicabilidad":
    st.header("Modelos y estrategia de explicabilidad")
    tab1, tab2, tab3, tab4 = st.tabs(["Elastic Net", "XGBoost", "Métodos explicativos", "Ablación"])

    with tab1:
        st.subheader("Elastic Net como baseline interpretable")
        st.write(
            "Combina penalización L1 y L2. Es útil cuando existen predictores correlacionados y permite analizar el signo y la magnitud de coeficientes estandarizados."
        )
        card("Pregunta que responde", "¿Qué variables mantienen una asociación predictiva lineal al controlar simultáneamente las demás?")
        card("Precaución", "Un coeficiente no representa un efecto causal y su interpretación depende de la escala, regularización y colinealidad.")

    with tab2:
        st.subheader("XGBoost como contraste no lineal")
        st.write(
            "Permite representar relaciones no lineales e interacciones entre variables. Se utilizará como contraste frente al modelo lineal regularizado, no como garantía automática de mejor desempeño."
        )
        card("Pregunta que responde", "¿Aparecen patrones predictivos que un modelo lineal no captura adecuadamente?")
        card("Precaución", "Su mayor complejidad exige validación rigurosa y métodos de explicación post hoc.")

    with tab3:
        methods = pd.DataFrame(
            [
                ["Coeficientes estandarizados", "Dirección y magnitud lineal", "Elastic Net", "Sensibles a escala, regularización y correlación"],
                ["SHAP", "Contribución global y local", "Principalmente XGBoost", "Explica el modelo, no la realidad causal"],
                ["Importancia por permutación", "Pérdida de desempeño al alterar una variable", "Ambos", "Puede distorsionarse con predictores correlacionados"],
                ["Ablación por grupos", "Aporte incremental de una dimensión", "Ambos", "La comparación depende de la estrategia de validación"],
            ],
            columns=["Método", "Qué informa", "Aplicación", "Limitación principal"],
        )
        st.dataframe(methods, width="stretch", hide_index=True)

    with tab4:
        st.subheader("Comparaciones previstas")
        models = pd.DataFrame(
            {
                "Configuración": [
                    "Todas las dimensiones",
                    "Solo psicológicas",
                    "Solo académicas",
                    "Solo conductuales",
                    "Sin psicológicas",
                    "Sin académicas",
                    "Sin conductuales",
                ],
                "Finalidad": [
                    "Referencia integrada",
                    "Capacidad independiente",
                    "Capacidad independiente",
                    "Capacidad independiente",
                    "Contribución incremental psicológica",
                    "Contribución incremental académica",
                    "Contribución incremental conductual",
                ],
            }
        )
        st.dataframe(models, width="stretch", hide_index=True)
        st.caption("No se asignan métricas hipotéticas. Los cambios se estimarán únicamente después de ejecutar el estudio.")

elif section == "Evaluación y estabilidad":
    st.header("Evaluación predictiva y estabilidad")
    st.subheader("Estrategia de validación")
    statement(
        "Todo el preprocesamiento, la selección de hiperparámetros y el entrenamiento se realizarán dentro de la validación para evitar fuga de información."
    )

    c1, c2 = st.columns(2)
    with c1:
        card("Validación propuesta", "Validación cruzada anidada de cinco folds, repetida cuando el tamaño muestral lo permita.")
        card("Métricas principales", "MAE, RMSE y R² para un outcome continuo. Se reportarán medias, dispersión e intervalos.")
    with c2:
        card("Análisis secundario", "Clasificación de riesgo solo si existen puntos de corte validados; entonces se usarán ROC-AUC, PR-AUC, sensibilidad, precisión, F1 y calibración.")
        card("Comparación", "Elastic Net frente a XGBoost y modelo integrado frente a configuraciones parciales o ablacionadas.")

    st.subheader("Cómo se evaluará la estabilidad")
    stability = pd.DataFrame(
        [
            ["Ranking medio", "Posición promedio de cada variable entre folds"],
            ["Frecuencia top-5", "Número de particiones en que aparece entre las cinco principales"],
            ["Dirección predominante", "Consistencia del signo o dirección de la contribución"],
            ["Dispersión", "Variabilidad de coeficientes, SHAP o importancia por permutación"],
            ["Concordancia entre métodos", "Coincidencia entre Elastic Net, SHAP y permutación"],
            ["Correlación de rankings", "Semejanza de ordenamientos entre folds o modelos"],
        ],
        columns=["Indicador", "Interpretación"],
    )
    st.dataframe(stability, width="stretch", hide_index=True)

    warning_box(
        "Un modelo con desempeño insuficiente no justifica interpretaciones fuertes. Primero se verifica capacidad predictiva; después se analizan las variables."
    )

elif section == "Resultados, alcance y ética":
    st.header("Resultados esperados, alcance, limitaciones y ética")
    st.subheader("Resultados esperados")
    st.markdown(
        """
        - Dataset prospectivo documentado, con diccionario de datos y criterios de calidad.
        - Estimación comparativa del desempeño de Elastic Net y XGBoost.
        - Identificación de variables y dimensiones con contribución predictiva consistente.
        - Evaluación de estabilidad y concordancia entre métodos explicativos.
        - Pipeline reproducible para futuras investigaciones universitarias.
        """
    )
    st.caption("No se anticipan valores numéricos ni se afirma de antemano qué variable será la más importante.")

    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Alcance")
        card("Contribución metodológica", "Integra predicción, explicabilidad, ablación y estabilidad en un mismo diseño.")
        card("Contribución aplicada", "Puede orientar futuras líneas de prevención y levantamiento de información, sin automatizar decisiones académicas.")
        card("Generalización", "Inicialmente limitada a la población e institución efectivamente muestreadas.")
    with c2:
        st.subheader("Limitaciones")
        card("Diseño transversal", "No permite establecer causalidad ni secuencia temporal.")
        card("Autorreporte", "Puede contener sesgo de recuerdo, deseabilidad social y error de medición.")
        card("Muestra", "Tamaño, autoselección y representación por subgrupos pueden afectar estabilidad y equidad.")

    st.subheader("Consideraciones éticas")
    ethics = [
        "Consentimiento informado y participación voluntaria.",
        "Anonimización y exclusión de identificadores directos.",
        "Almacenamiento seguro y acceso restringido.",
        "Aprobación institucional antes de recolectar datos sensibles.",
        "Prohibición de usar el modelo como diagnóstico clínico o mecanismo sancionatorio.",
        "Evaluación de desempeño y errores por subgrupos cuando el tamaño muestral lo permita.",
    ]
    for item in ethics:
        st.checkbox(item, value=True, disabled=True)

elif section == "Coherencia del proyecto":
    st.header("Coherencia interna")
    st.write("La propuesta debe poder leerse como una cadena lógica y verificable.")
    cols = st.columns(6)
    sequence = [
        ("1", "Problema", "Factores múltiples y modelos poco interpretables."),
        ("2", "Brecha", "Falta integración entre predicción, explicabilidad y estabilidad."),
        ("3", "Pregunta", "Qué variables contribuyen y con qué estabilidad."),
        ("4", "Hipótesis", "Psicológicas y conductuales aportarán más; integración reducirá error."),
        ("5", "Objetivos", "Dataset, modelos, explicación y ablación."),
        ("6", "Métodos", "Encuesta, validación, Elastic Net, XGBoost, SHAP y estabilidad."),
    ]
    for col, (num, title, text) in zip(cols, sequence):
        with col:
            st.markdown(
                f'<div class="step"><div class="step-number">{num}</div><strong>{title}</strong><div class="small-note">{text}</div></div>',
                unsafe_allow_html=True,
            )

    st.subheader("Matriz de verificación")
    checks = pd.DataFrame(
        [
            ["Pregunta respondible con datos", "Sí", "Variables y outcome definidos en un dataset prospectivo"],
            ["Hipótesis contrastable", "Sí", "Métricas, ablación y estabilidad permiten evaluarla"],
            ["Objetivos evaluables", "Sí", "Cada objetivo tiene procedimientos y resultados esperados"],
            ["Metodología alineada", "Sí", "Los métodos corresponden directamente a OE1-OE4"],
            ["Lenguaje no causal", "Sí", "Se usa contribución predictiva y asociación"],
            ["Resultados no inventados", "Sí", "La app diferencia diseño previsto de evidencia observada"],
        ],
        columns=["Criterio", "Estado", "Justificación"],
    )
    st.dataframe(checks, width="stretch", hide_index=True)

elif section == "Evidencia bibliográfica":
    st.header("Evidencia bibliográfica")
    st.write("Matriz resumida de los estudios utilizados para fundamentar variables, métodos previos y brechas.")
    if articles.empty:
        st.info("No hay datos bibliográficos disponibles.")
    else:
        filters = ["Todos"] + sorted(articles["Tipo de evidencia"].dropna().unique().tolist())
        selected = st.selectbox("Tipo de evidencia", filters)
        filtered = articles if selected == "Todos" else articles[articles["Tipo de evidencia"] == selected]
        st.dataframe(filtered, width="stretch", hide_index=True)

        study = st.selectbox("Detalle de estudio", filtered["Estudio"].tolist())
        row = filtered[filtered["Estudio"] == study].iloc[0]
        c1, c2 = st.columns(2)
        with c1:
            card("Población o datos", str(row["Población/datos"]))
            card("Método principal", str(row["Método principal"]))
        with c2:
            card("Aporte", str(row["Aporte al planteamiento"]))
            card("Limitación", str(row["Limitación o brecha"]))

    st.subheader("Referencias metodológicas añadidas")
    st.markdown(
        """
        - Zou y Hastie (2005): Elastic Net.
        - Chen y Guestrin (2016): XGBoost.
        - Lundberg y Lee (2017): SHAP.
        - Fisher, Rudin y Dominici (2019): importancia y dependencia del modelo respecto de las variables.
        """
    )

elif section == "Uso de IA":
    st.header("Declaración de uso de inteligencia artificial")
    st.write(
        "Se utilizó inteligencia artificial como apoyo para reformular el planteamiento, revisar la coherencia metodológica, estructurar el informe en LaTeX y desarrollar la aplicación Streamlit."
    )

    ia = pd.DataFrame(
        [
            {
                "Herramienta": "ChatGPT",
                "Modelo": "GPT-5.6 Thinking",
                "Fecha": "11 de julio de 2026",
                "Propósito": "Revisión metodológica; redacción; diseño de pipeline; generación y depuración de LaTeX y Streamlit.",
                "Verificación humana": "Contraste con la rúbrica, el informe previo y las referencias; revisión manual de afirmaciones, código y estructura.",
            }
        ]
    )
    st.dataframe(ia, width="stretch", hide_index=True)

    st.subheader("Prompt principal sintetizado")
    st.code(
        "Actúa como experto en metodología de investigación en Ciencia de Datos. Reformula el proyecto sobre burnout académico para centrarlo en la contribución predictiva de variables psicológicas, académicas y conductuales. Alinea problema, brecha, pregunta, hipótesis, objetivos y metodología con la rúbrica final. No inventes resultados ni atribuyas causalidad. Genera un informe en LaTeX y una app Streamlit ejecutable.",
        language=None,
    )

    warning_box(
        "Antes de entregar, el estudiante debe añadir el modelo y la fecha exactos de cualquier otra herramienta de IA utilizada en etapas previas, si ese contenido se mantiene en la versión final."
    )
    st.write(
        "El estudiante revisó la propuesta, seleccionó las decisiones metodológicas finales y asume responsabilidad académica completa por el contenido entregado."
    )

st.divider()
st.caption("Entrega 4 · Metodología de la Investigación en Ciencia de Datos · UTEM · Propuesta sin resultados empíricos")
