import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Kvíz Dashboard", layout="wide")

st.markdown("# 🖥️ Kvíz vizualizációk")

base_url = "https://cso66.github.io/kvizz/"

# EREDETI MÉRETEKKEL: 5 TAB
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🌞 Sunburst", "🔗 Sankey", "📊 Radar", "🎬 Animáció", "🔥 Heat + Chord + Tabla", "Összes vizu"
])

with tab1:
    st.markdown("### Sunburst diagram")
    components.iframe(f"{base_url}3sunburst_diagram.html", height=1100)  # eredeti column méret

with tab2:
    st.markdown("### Sankey diagramok")
    col1, col2 = st.columns(2)
    with col1: components.iframe(f"{base_url}sankey2025_3.html", height=1100)
    with col2: components.iframe(f"{base_url}sankey2024_.html", height=1100)

with tab3:
    st.markdown("### Radar diagramok")
    col1, col2 = st.columns(2)
    with col1: components.iframe(f"{base_url}radar_2025.html", height=1100)
    with col2: components.iframe(f"{base_url}radar_2024.html", height=1100)

with tab4:
    st.markdown("### Animáció lassítva")
    components.iframe(f"{base_url}animacio_lassitva.html", height=1100)

with tab5:
    st.markdown("### Heatmap 2025 + Chord diagram")
    col1, col2 = st.columns(2)
    with col1: components.iframe(f"{base_url}heat_2025.html", height=600)
    with col2: components.iframe(f"{base_url}chord_diagram.html", height=600)
    st.markdown("**Tablázatos graf:**")
    components.iframe(f"{base_url}tabla_graf.html", height=900)

with tab6:
    st.markdown("### 🏠 Minden egy helyen – eredeti layout")
    
    # Első: Sunburst (column)
    st.markdown("**Sunburst:**")
    components.iframe(f"{base_url}3sunburst_diagram.html", height=1100)
    
    # Második: Tablázatos (column)
    st.markdown("**Tablázatos graf:**")
    components.iframe(f"{base_url}tabla_graf.html", height=1000)
    
    # Sor1: 2 Sankey (row)
    st.markdown("**Sankey diagramok:**")
    col1, col2 = st.columns(2)
    with col1: components.iframe(f"{base_url}sankey2025_3.html", height=1100)
    with col2: components.iframe(f"{base_url}sankey2024_.html", height=1100)
    
    # Sor2: 2 Radar (row)
    st.markdown("**Radar diagramok:**")
    col1, col2 = st.columns(2)
    with col1: components.iframe(f"{base_url}radar_2025.html", height=1100)
    with col2: components.iframe(f"{base_url}radar_2024.html", height=1100)
    
    # Oszlop: Animáció
    st.markdown("**Animáció:**")
    components.iframe(f"{base_url}animacio_lassitva.html", width=3500, height=1100)
    
    # Sor3: Chord + Heat
    st.markdown("**Chord + Heatmap:**")
    col1, col2 = st.columns(2)
    with col1: components.iframe(f"{base_url}chord_diagram.html", height=800)
    with col2: components.iframe(f"{base_url}heat_2025.html", height=800)
        
st.markdown("---")
st.markdown("[👉 Teljes eredeti verzió](https://cso66.github.io/kvizz/) | ✨ Streamlit + Plotly")
