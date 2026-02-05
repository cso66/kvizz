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
    st.markdown("### 🎬 Animáció lassítva")
    components.html(f"""
    <div style="width: 100%; height: 800px; overflow: auto; padding: 10px;">
        <iframe src="{base_url}animacio_lassitva.html" 
                style="width: 100%; height: 1250px; border: none; border-radius: 12px; 
                       box-shadow: 0 8px 24px rgba(0,0,0,0.15);"
                frameborder="0" scrolling="auto">
        </iframe>
    </div>
    """, height=1350)

with tab5:
    col1, col2 = st.columns(2)
    with col1: components.iframe(f"{base_url}heat_2025.html", height=600)
    with col2: components.iframe(f"{base_url}chord_diagram.html", height=600)

with tab6:
    st.markdown("### 🏠 ÖSSZES – eredeti elrendezés")
    
    # 1. Column: Sunburst (820px)
    st.markdown("**Sunburst diagram**")
    components.iframe(f"{base_url}3sunburst_diagram.html", height=820)
    
    # 2. Column: Tabla graf (820px)
    st.markdown("**Tablázatos graf**")
    components.iframe(f"{base_url}tabla_graf.html", height=820)
    
    # 3. Row1: Sankey-k (600px, 2 oszlop)
    st.markdown("**Sankey diagramok**")
    col1, col2 = st.columns(2)
    with col1: components.iframe(f"{base_url}sankey2025_3.html", height=600)
    with col2: components.iframe(f"{base_url}sankey2024_.html


st.markdown("---")
st.markdown("[👉 Eredeti GitHub Pages](https://cso66.github.io/kvizz/) | ✨ Streamlit Dashboard")
