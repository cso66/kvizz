import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Kvíz Dashboard", layout="wide")

st.markdown("# 🖥️ Kvíz vizualizációk")

base_url = "https://cso66.github.io/kvizz/"

# 5 TAB a pontos elrendezéssel
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🌞 Sunburst", "🔗 Sankey-k", "📊 Radar-ok", "🎬 Animáció (2025/2)", "🔥 Heatmap + Chord (2025/2)"
])

with tab1:
    st.markdown("### Sunburst diagram")
    components.iframe(f"{base_url}3sunburst_diagram.html", height=800)

with tab2:
    st.markdown("### Sankey diagramok")
    col1, col2 = st.columns(2)
    with col1: components.iframe(f"{base_url}sankey2024_.html", height=600)
    with col2: components.iframe(f"{base_url}sankey2025_3.html", height=600)

with tab3:
    st.markdown("### Radar diagramok")
    col1, col2 = st.columns(2)
    with col1: components.iframe(f"{base_url}radar_2024.html", height=600)
    with col2: components.iframe(f"{base_url}radar_2025.html", height=600)
        
with tab4:
    st.markdown("### 🎬 Animáció 2025/2")
    components.html(f"""
    <div style='width: 100%; display: flex; justify-content: center; align-items: center; padding: 20px;'>
        <iframe src='{base_url}animacio_lassitva.html' 
                width='95%' height='1000' style='border: none; box-shadow: 0 4px 8px rgba(0,0,0,0.1);'>
        </iframe>
    </div>
    """, height=1050)

with tab5:
    st.markdown("### Heatmap 2025 + Chord diagram")
    col1, col2 = st.columns(2)
    with col1: components.iframe(f"{base_url}heat_2025.html", height=600)
    with col2: components.iframe(f"{base_url}chord_diagram.html", height=600)
    st.markdown("**Pontok:**")
    components.iframe(f"{base_url}tabla_graf.html", height=800)

st.markdown("---")
st.markdown("[👉 Teljes eredeti verzió](https://cso66.github.io/kvizz/) | ✨ Streamlit + Plotly")
