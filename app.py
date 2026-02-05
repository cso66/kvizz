import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Kvíz Dashboard", layout="wide")

st.markdown("# 🖥️ Kvíz vizualizációk")

base_url = "https://cso66.github.io/kvizz/"

# 6 TAB – utolsó az ÖSSZES!
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🌞 Sunburst", "🔗 Sankey-k", "📊 Radar-ok", "🎬 Animáció", "🔥 Heat + Chord", "🏠 ÖSSZES"
])

with tab1:
    components.iframe(f"{base_url}3sunburst_diagram.html", height=800)

with tab2:
    col1, col2 = st.columns(2)
    with col1: components.iframe(f"{base_url}sankey2025_3.html", height=600)
    with col2: components.iframe(f"{base_url}sankey2024_.html", height=600)

with tab3:
    col1, col2 = st.columns(2)
    with col1: components.iframe(f"{base_url}radar_2025.html", height=600)
    with col2: components.iframe(f"{base_url}radar_2024.html", height=600)

with tab4:
    components.iframe(f"{base_url}animacio_lassitva.html", height=1000)

with tab5:
    col1, col2 = st.columns(2)
    with col1: components.iframe(f"{base_url}heat_2025.html", height=600)
    with col2: components.iframe(f"{base_url}chord_diagram.html", height=600)

# TAB6: PONT OSAN AZ EREDETI INDEX.HTM ELRENDZÉSE!
with tab6:
    st.markdown("### 🏠 Minden egy helyen – eredeti layout")
    
    # Első: Sunburst (column)
    st.markdown("**Sunburst:**")
    components.iframe(f"{base_url}3sunburst_diagram.html", height=700)
    
    # Második: Tablázatos (column)
    st.markdown("**Tablázatos graf:**")
    components.iframe(f"{base_url}tabla_graf.html", height=700)
    
    # Sor1: 2 Sankey (row)
    st.markdown("**Sankey diagramok:**")
    col1, col2 = st.columns(2)
    with col1: components.iframe(f"{base_url}sankey2025_3.html", height=500)
    with col2: components.iframe(f"{base_url}sankey2024_.html", height=500)
    
    # Sor2: 2 Radar (row)
    st.markdown("**Radar diagramok:**")
    col1, col2 = st.columns(2)
    with col1: components.iframe(f"{base_url}radar_2025.html", height=500)
    with col2: components.iframe(f"{base_url}radar_2024.html", height=500)
    
    # Oszlop: Animáció
    st.markdown("**Animáció:**")
    components.iframe(f"{base_url}animacio_lassitva.html", height=700)
    
    # Sor3: Chord + Heat
    st.markdown("**Chord + Heatmap:**")
    col1, col2 = st.columns(2)
    with col1: components.iframe(f"{base_url}chord_diagram.html", height=500)
    with col2: components.iframe(f"{base_url}heat_2025.html", height=500)

st.markdown("---")
st.markdown("[👉 Eredeti GitHub Pages](https://cso66.github.io/kvizz/) | ✨ Streamlit Dashboard")
