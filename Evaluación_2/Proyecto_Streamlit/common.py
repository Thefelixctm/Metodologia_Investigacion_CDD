from pathlib import Path
import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
ASSET_DIR = ROOT / "assets"

APP_TITLE = "Predicción y modelado del burnout académico"
AUTHOR = "Felipe Martínez González"
COURSE = "Metodología de la Investigación en Ciencia de Datos"
UNIVERSITY = "Universidad Tecnológica Metropolitana"
EMAIL = "fmartinezgo@utem.cl"
DATE = "06 de mayo de 2026"

PRIMARY = "#2563eb"
SECONDARY = "#0f172a"
MUTED = "#64748b"
BG = "#f8fafc"


def load_csv(name: str) -> pd.DataFrame:
    path = DATA_DIR / name
    if not path.exists():
        return pd.DataFrame()
    return pd.read_csv(path)


def page_config(title: str, icon: str = "📊"):
    st.set_page_config(page_title=title, page_icon=icon, layout="wide")
    inject_css()


def inject_css():
    st.markdown(
        """
        <style>
        .block-container {padding-top: 1.2rem; padding-bottom: 2rem;}
        h1, h2, h3 {color: #0f172a;}
        .hm-card {
            background: white;
            border: 1px solid #e2e8f0;
            border-radius: 18px;
            padding: 1rem 1.1rem;
            box-shadow: 0 1px 2px rgba(15, 23, 42, 0.06);
            min-height: 105px;
        }
        .hm-card h3 {margin-top: 0; margin-bottom: .35rem; font-size: 1.05rem;}
        .hm-card p {color: #334155; margin-bottom: 0;}
        .metric-card {
            background: linear-gradient(180deg,#ffffff,#f8fafc);
            border: 1px solid #dbeafe;
            border-radius: 18px;
            padding: 1rem;
            text-align: center;
        }
        .metric-card .num {font-size: 2rem; font-weight: 800; color: #1d4ed8;}
        .metric-card .label {font-size: .85rem; color: #475569;}
        .tag {
            display:inline-block; padding:.25rem .55rem; border-radius:999px;
            background:#eff6ff; color:#1d4ed8; border:1px solid #bfdbfe;
            font-size:.82rem; margin:.15rem .2rem .15rem 0;
        }
        .warn-box {
            background:#fff7ed; border:1px solid #fed7aa; border-radius:14px; padding:1rem;
        }
        .ok-box {
            background:#ecfdf5; border:1px solid #bbf7d0; border-radius:14px; padding:1rem;
        }
        .small {font-size:.9rem;color:#475569;}
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_header(title: str, subtitle: str = ""):
    st.title(title)
    if subtitle:
        st.caption(subtitle)
    st.divider()


def card(title: str, body: str):
    st.markdown(f"""
    <div class='hm-card'>
      <h3>{title}</h3>
      <p>{body}</p>
    </div>
    """, unsafe_allow_html=True)


def metric_card(label: str, value: str):
    st.markdown(f"""
    <div class='metric-card'>
      <div class='num'>{value}</div>
      <div class='label'>{label}</div>
    </div>
    """, unsafe_allow_html=True)


def download_file(path: Path, label: str, mime: str):
    if path.exists():
        st.download_button(label, data=path.read_bytes(), file_name=path.name, mime=mime)
    else:
        st.info(f"No se encontró el archivo: {path.name}")
