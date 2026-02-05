import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Kvíz Dashboard", layout="wide")

st.markdown("# 🖥️ Kvíz vizualizációk")

base_url = "https://cso66.github.io/kvizz/"

# TABOK A TETEJÉN – mint az eredeti index.html!
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Sunburst & Sankey", "Radar chartok", "Animáció & Chord", "Heatmap", "Összes"
])

with tab1:
    col1, col2 = st.columns(2)
    with col1: components.iframe(f"{base_url}3sunburst_diagram.html", height=500)
    with col2: components.iframe(f"{base_url}sankey2025_3.html", height=500)
    st.markdown("---")
    components.iframe(f"{base_url}sankey2024_.html", height=500)

with tab2:
    col1, col2 = st.columns(2)
    with col1: components.iframe(f"{base_url}radar_2025.html", height=500)
    with col2: components.iframe(f"{base_url}radar_2024.html", height=500)

with tab3:
    components.iframe(f"{base_url}animacio_lassitva.html", height=600)
    st.markdown("---")
    components.iframe(f"{base_url}chord_diagram.html", height=500)

with tab4:
    components.iframe(f"{base_url}heat_2025.html", height=600)
    st.markdown("---")
    components.iframe(f"{base_url}tabla_graf.html", height=600)

with tab5:
    st.markdown("**Teljes GitHub Pages:** [cso66.github.io/kvizz/](https://cso66.github.io/kvizz/)")

st.markdown("---")
st.caption("✨ Powered by Streamlit + Plotly")
