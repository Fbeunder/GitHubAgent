"""
Hoofdmodule voor Stan de GitHub Agent applicatie.

Deze module integreert alle componenten van de applicatie en zorgt voor
het opbouwen van de Streamlit user interface.
"""

import streamlit as st
from robot import display_robot
from utils import initialize_session_state, handle_click_event
from config import APP_TITLE, APP_DESCRIPTION


def main():
    """
    Hoofdfunctie die de Streamlit applicatie opbouwt en uitvoert.
    """
    # Pagina configuratie
    st.set_page_config(
        page_title=APP_TITLE,
        page_icon="🤖",
        layout="centered"
    )
    
    # Initialiseer session state
    initialize_session_state()
    
    # Header met titel en beschrijving
    st.title(APP_TITLE)
    st.markdown(f"<p style='text-align: center;'>{APP_DESCRIPTION}</p>", unsafe_allow_html=True)
    
    # Voeg een scheidingslijn toe
    st.divider()
    
    # Toon de robot en vang de klik events op
    robot_clicked = display_robot()
    
    # Verwerk klik events indien nodig
    if robot_clicked:
        handle_click_event()
        st.experimental_rerun()
    
    # Creëer een container voor de quotes met consistente hoogte
    quote_container = st.container(height=120)
    
    # Toon de huidige quote in het midden
    with quote_container:
        # Voeg wat padding en styling toe
        st.markdown(
            f"""
            <div style="text-align: center; padding: 15px; 
                        background-color: #f0f2f6; border-radius: 10px;
                        font-size: 18px; font-weight: bold; margin: 10px 0;">
                "{st.session_state.current_quote}"
            </div>
            """, 
            unsafe_allow_html=True
        )
    
    # Toon een instructie onderaan
    st.markdown(
        "<div style='text-align: center; font-size: 14px; margin-top: 10px;'>"
        "Klik op Stan om meer te ontdekken!"
        "</div>",
        unsafe_allow_html=True
    )
    
    # Toon klik statistieken
    if st.session_state.click_count > 0:
        st.markdown(
            f"""
            <div style='text-align: center; font-size: 12px; margin-top: 20px; color: #888;'>
                Je hebt {st.session_state.click_count} keer op Stan geklikt!
            </div>
            """,
            unsafe_allow_html=True
        )


if __name__ == "__main__":
    main()
