import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Kvíz Dashboard", layout="wide")

st.markdown("# 🖥️ Kvíz vizualizációk")

# SIDEBAR MENÜ – EZ KELL!
menu = st.sidebar.selectbox("Válassz ábrát:", [
    "Sunburst", "Tablázatos graf", "Sankey 2025", "Sankey 2024",
    "Radar 2025", "Radar 2024", "Animáció lassítva", "Chord diagram", "Heatmap 2025"
])

base_url = "https://cso66.github.io/kvizz/"

if menu == "Sunburst":
    components.iframe(f"{base_url}3sunburst_diagram.html", height=800)
elif menu == "Tablázatos graf":
    components.iframe(f"{base_url}tabla_graf.html", height=800)
elif menu == "Sankey 2025":
    components.iframe(f"{base_url}sankey2025_3.html", height=600)
elif menu == "Sankey 2024":
    components.iframe(f"{base_url}sankey2024_.html", height=600)
elif menu == "Radar 2025":
    components.iframe(f"{base_url}radar_2025.html", height=600)
elif menu == "Radar 2024":
    components.iframe(f"{base_url}radar_2024.html", height=600)
elif menu == "Animáció lassítva":
    components.iframe(f"{base_url}animacio_lassitva.html", height=800)
elif menu == "Chord diagram":
    components.iframe(f"{base_url}chord_diagram.html", height=600)
elif menu == "Heatmap 2025":
    components.iframe(f"{base_url}heat_2025.html", height=600)

st.markdown("---")
st.markdown("[👉 Teljes GitHub Pages verzió](https://cso66.github.io/kvizz/)")
