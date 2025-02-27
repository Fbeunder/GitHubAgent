"""
Utilities module voor Stan de GitHub Agent applicatie.

Deze module bevat algemene hulpfuncties voor de applicatie,
zoals het afhandelen van klikgebeurtenissen en de sessiestate beheren.
"""

import streamlit as st
from quotes import get_random_quote, get_next_quote


def initialize_session_state():
    """
    Initialiseert de Streamlit session state variabelen die nodig zijn
    voor de applicatie als ze nog niet bestaan.
    
    Returns:
        None
    """
    if 'current_quote' not in st.session_state:
        st.session_state.current_quote = get_random_quote()
    
    if 'quote_index' not in st.session_state:
        st.session_state.quote_index = 0
    
    if 'click_count' not in st.session_state:
        st.session_state.click_count = 0
    
    # Voorkom reset van session state bij hot reload
    if 'initialized' not in st.session_state:
        st.session_state.initialized = True


def handle_click_event():
    """
    Verwerkt een klikgebeurtenis op de robot. Werkt de huidige quote bij,
    verhoogt de klik teller en past indien nodig andere UI elementen aan.
    
    Returns:
        None: Updates de session state direct.
    """
    try:
        # Verhoog de klik teller
        st.session_state.click_count += 1
        
        # Haal de volgende quote op
        new_quote, new_index = get_next_quote(st.session_state.quote_index)
        st.session_state.current_quote = new_quote
        st.session_state.quote_index = new_index
        
        # Success message voor debugging (kan later verwijderd worden)
        # st.success("Klikgebeurtenis succesvol verwerkt!")
    except Exception as e:
        # Voorkom dat de applicatie crasht bij een fout
        st.error(f"Er is een fout opgetreden: {str(e)}")
        # Bij een fout, gebruik fallback quote
        st.session_state.current_quote = "Oeps, een bug! Maar geen zorgen, ik vind bugs leuker dan mensen!"
