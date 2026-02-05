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
    st.markdown("""
    <style>
    .stApp {{
        background-color: #f5f5f5;
    }}
    .iframe-container {{
        width: 100%;
        padding: 20px;
    }}
    .iframe-column {{
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 30px;
        margin-bottom: 30px;
    }}
    .iframe-column iframe {{
        width: 100%;
        max-width: 1620px;
        height: 820px;
        border: none;
        box-shadow: 0 0 8px rgba(0,0,0,0.1);
    }}
    .iframe-row {{
        display: flex;
        justify-content: space-between;
        gap: 20px;
        margin-bottom: 30px;
    }}
    .iframe-row > div {{
        flex: 1;
    }}
    .iframe-row iframe {{
        width: 100%;
        height: 600px;
        border: none;
        box-shadow: 0 0 8px rgba(0,0,0,0.1);
    }}
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<h1 style="text-align: center;">Kvíz vizualizációk</h1>', unsafe_allow_html=True)
    
    # PONT OSAN AZ EREDETI SORREND!
    st.markdown('<div class="iframe-container">', unsafe_allow_html=True)
    
    # Column1: Sunburst
    st.markdown('<div class="iframe-column">', unsafe_allow_html=True)
    components.iframe("3sunburst_diagram.html", height=820)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Column2: Tabla graf
    st.markdown('<div class="iframe-column">', unsafe_allow_html=True)
    components.iframe("tabla_graf.html", height=820)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Row1: Sankey-k
    st.markdown('<div class="iframe-row">', unsafe_allow_html=True)
    col1, col2 = st.columns([1,1])
    with col1: components.iframe("sankey2025_3.html", height=600)
    with col2: components.iframe("sankey2024_.html", height=600)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Row2: Radar-ok
    st.markdown('<div class="iframe-row">', unsafe_allow_html=True)
    col1, col2 = st.columns([1,1])
    with col1: components.iframe("radar_2025.html", height=600)
    with col2: components.iframe("radar_2024.html", height=600)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Column3: Animáció
    st.markdown('<div class="iframe-column">', unsafe_allow_html=True)
    components.iframe("animacio_lassitva.html", height=820)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Row3: Chord + Heat
    st.markdown('<div class="iframe-row">', unsafe_allow_html=True)
    col1, col2 = st.columns([1,1])
    with col1: components.iframe("chord_diagram.html", height=600)
    with col2: components.iframe("heat_2025.html", height=600)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)


st.markdown("---")
st.markdown("[👉 Eredeti GitHub Pages](https://cso66.github.io/kvizz/) | ✨ Streamlit Dashboard")
