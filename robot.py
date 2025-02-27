"""
Robot module voor Stan de GitHub Agent applicatie.

Deze module bevat de functionaliteit voor het weergeven van de robot visualisatie
en het verwerken van klikinteracties.
"""

import streamlit as st
from config import ROBOT_SVG


def display_robot() -> bool:
    """
    Geeft de robot weer als een interactief component in de Streamlit interface.
    De robot is klikbaar en heeft een SVG afbeelding zoals gedefinieerd in config.py.
    
    Returns:
        bool: True als er op de robot is geklikt, anders False.
    """
    # Centreer de robot horizontaal en voeg wat padding toe
    col1, col2, col3 = st.columns([1, 2, 1])
    
    clicked = False
    
    with col2:
        # Maak een div met centrale uitlijning en een hover effect
        css_styles = """
        <style>
        .robot-container {
            display: flex;
            justify-content: center;
            cursor: pointer;
            transition: transform 0.3s ease;
            width: 100%;
            max-width: 300px;
            margin: 0 auto;
            position: relative;
        }
        .robot-container:hover {
            transform: scale(1.05);
        }
        .robot-container:active {
            transform: scale(0.95);
        }
        /* Media queries voor verschillende schermgroottes */
        @media (max-width: 768px) {
            .robot-container {
                max-width: 200px;
            }
        }
        @media (max-width: 480px) {
            .robot-container {
                max-width: 150px;
            }
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
                if (window.parent && window.parent.Streamlit) {{
                    window.parent.Streamlit.setComponentValue(data);
                }}
            }});
        </script>
        """
        
        # Render de HTML met de robot en script
        click_data = st.components.v1.html(robot_html, height=280)
        
        # Controleer of er een klik event is
        if click_data and isinstance(click_data, dict) and click_data.get('event') == 'robot_clicked':
            clicked = True
    
    return clicked
