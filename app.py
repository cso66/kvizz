import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Kvíz Dashboard", layout="wide", height=800)

st.markdown("""
# 🖥️ Kvíz vizualizációk
**Interaktív dashboard – kattints a navigációra!**
""")

# Sidebar menü az index.html szerkezetével
menu = st.sidebar.selectbox("Válassz ábrát:", [
    "Sunburst", "Tablázatos graf", "Sankey 2025", "Sankey 2024",
    "Radar 2025", "Radar 2024", "Animáció lassítva", "Chord diagram", "Heatmap 2025"
])

# BASE URL a te GitHub Pages oldaladra
base_url = "https://cso66.github.io/kvizz/"

if menu == "Sunburst":
    components.iframe(f"{base_url}3sunburst_diagram.html", height=800, scrolling=True)
elif menu == "Tablázatos graf":
    components.iframe(f"{base_url}tabla_graf.html", height=800, scrolling=True)
elif menu == "Sankey 2025":
    components.iframe(f"{base_url}sankey2025_3.html", height=600, scrolling=True)
elif menu == "Sankey 2024":
    components.iframe(f"{base_url}sankey2024_.html", height=600, scrolling=True)
elif menu == "Radar 2025":
    components.iframe(f"{base_url}radar_2025.html", height=600, scrolling=True)
elif menu == "Radar 2024":
    components.iframe(f"{base_url}radar_2024.html", height=600, scrolling=True)
elif menu == "Animáció lassítva":
    components.iframe(f"{base_url}animacio_lassitva.html", height=800, scrolling=True)
elif menu == "Chord diagram":
    components.iframe(f"{base_url}chord_diagram.html", height=600, scrolling=True)
elif menu == "Heatmap 2025":
    components.iframe(f"{base_url}heat_2025.html", height=600, scrolling=True)

# Alul link a teljes oldaladra
st.markdown("---")
st.markdown("[👉 Teljes dashboard GitHub Pages-en](https://cso66.github.io/kvizz/)")
