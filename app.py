import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="AeroSustain", layout="wide")
st.title("🌍 AeroSustain – Sostenibilidad y Cumplimiento Normativo con IA")

# Introducción
st.markdown("""
### ¿Qué es AeroSustain?
AeroSustain es una plataforma inteligente para gestionar la sostenibilidad ambiental y el cumplimiento de normativas europeas en aviación. Ayuda a prevenir sanciones, optimiza el uso de combustibles sostenibles y mejora la reputación corporativa.
""")

# Simulación de Datos Operativos
st.header("🛫 Datos de Consumo y Emisiones")
data = {
    'Vuelo': ['MAD → FRA'],
    'Combustible usado (kg)': [7100],
    'SAF utilizado (%)': [8],
    'CO₂ emitido (kg)': [22000],
    'Tankering detectado': [True],
    'Días sin reporte medioambiental': [3]
}
df = pd.DataFrame(data)
st.dataframe(df)

# Módulo de IA
st.header("🧠 Análisis Predictivo y Riesgos")
st.markdown("""
La IA analiza estos indicadores para predecir:
- Riesgo de sanción regulatoria
- Cumplimiento de normativa europea (UE 2023/2405)
- Pérdidas reputacionales por prácticas no sostenibles
""")

predict = {
    'Riesgo de sanción (%)': [74.2],
    'Multa estimada (€)': [125000],
    'Impacto reputacional estimado': ['Moderado-alto'],
    'Recomendación': ['Incrementar SAF a mínimo 12% y eliminar tankering']
}
st.subheader("📋 Resultados del Análisis")
st.table(pd.DataFrame(predict))

# KPIs Ambientales
st.header("📊 Monitor de KPIs Medioambientales")
k1, k2, k3 = st.columns(3)
k1.metric("🌱 SAF utilizado", "8%", "⇩ por debajo del mínimo")
k2.metric("🚫 Tankering", "Detectado", "⚠️ Riesgo")
k3.metric("📆 Días sin reporte", "3 días", "↑")

# Footer
st.markdown("""
---
Aplicación demo desarrollada con [Streamlit](https://streamlit.io/) | Repositorio: [GitHub - AeroSustain](https://github.com/jftamames/aerosustain-demo)
""")
