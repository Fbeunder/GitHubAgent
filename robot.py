"""
Robot module voor Stan de GitHub Agent applicatie.

Deze module bevat de functionaliteit voor het weergeven van de robot visualisatie
en het verwerken van klikinteracties.
"""

import streamlit as st
from config import ROBOT_SVG


def display_robot() -> None:
    """
    Geeft de robot weer als een interactief component in de Streamlit interface.
    De robot is klikbaar en heeft een SVG afbeelding zoals gedefinieerd in config.py.
    
    Returns:
        None: Deze functie wijzigt direct de Streamlit UI.
    """
    # Centreer de robot horizontaal en voeg wat padding toe
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # Maak een div met centrale uitlijning en een hover effect
        css_styles = """
        <style>
        .robot-container {
            display: flex;
            justify-content: center;
            cursor: pointer;
            transition: transform 0.3s ease;
        }
        .robot-container:hover {
            transform: scale(1.05);
        }
        </style>
        """
        
        # Combineer de CSS en de robot SVG in een klikbare container
        robot_html = f"""
        {css_styles}
        <div class="robot-container" id="robot-clickable">
            {ROBOT_SVG}
        </div>
        <script>
            const robot = document.getElementById('robot-clickable');
            robot.addEventListener('click', function() {{
                // Stuur een event naar Streamlit om de klik te detecteren
                const data = {{event: 'robot_clicked'}};
                // Gebruik de Streamlit JS API om het event door te geven
                if (window.parent.Streamlit) {{
                    window.parent.Streamlit.setComponentValue(data);
                }}
            }});
        </script>
        """
        
        # Render de HTML met de robot en script
        st.components.v1.html(robot_html, height=280)
