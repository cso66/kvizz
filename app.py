import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Kvíz Dashboard", layout="wide")

st.markdown("# 🖥️ Kvíz vizualizációk")

base_url = "https://cso66.github.io/kvizz/"

# EREDETI MÉRETEKKEL: 5 TAB
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🌞 Sunburst (820px)", "🔗 Sankey-k (600px)", "📊 Radar-ok (600px)", "🎬 Animáció (820px)", "🔥 Heat + Chord + Tabla"
])

with tab1:
    st.markdown("### Sunburst diagram")
    components.iframe(f"{base_url}3sunburst_diagram.html", height=820)  # eredeti column méret

with tab2:
    st.markdown("### Sankey diagramok")
    col1, col2 = st.columns(2)
    with col1: components.iframe(f"{base_url}sankey2025_3.html", height=900)
    with col2: components.iframe(f"{base_url}sankey2024_.html", height=900)

with tab3:
    st.markdown("### Radar diagramok")
    col1, col2 = st.columns(2)
    with col1: components.iframe(f"{base_url}radar_2025.html", height=600)
    with col2: components.iframe(f"{base_url}radar_2024.html", height=600)

with tab4:
    st.markdown("### Animáció lassítva")
    components.iframe(f"{base_url}animacio_lassitva.html", height=800)

with tab5:
    st.markdown("### Heatmap 2025 + Chord diagram")
    col1, col2 = st.columns(2)
    with col1: components.iframe(f"{base_url}heat_2025.html", height=600)
    with col2: components.iframe(f"{base_url}chord_diagram.html", height=600)
    st.markdown("**Tablázatos graf:**")
    components.iframe(f"{base_url}tabla_graf.html", height=500)

st.markdown("---")
st.markdown("[👉 Teljes eredeti verzió](https://cso66.github.io/kvizz/) | ✨ Streamlit + Plotly")
