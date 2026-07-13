# Entrega final - Burnout académico

Aplicación interactiva en Streamlit para comunicar la propuesta final de investigación:

**Contribución predictiva de variables psicológicas, académicas y conductuales al burnout académico en estudiantes universitarios mediante modelos explicables de Ciencia de Datos.**

## Estructura

- `app.py`: aplicación principal.
- `requirements.txt`: dependencias.
- `logo_utem.jpg`: logo utilizado en la barra lateral.
- `data/articulos.csv`: matriz de evidencia bibliográfica.
- `data/variables_propuestas.csv`: diccionario preliminar del dataset futuro.
- `data/objetivos_metodos.csv`: trazabilidad entre objetivos y metodología.

## Ejecución local

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

Linux/macOS:

```bash
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Alcance

La app comunica una **propuesta de investigación**. Los gráficos y tablas describen el diseño previsto; no representan resultados empíricos ya obtenidos.

