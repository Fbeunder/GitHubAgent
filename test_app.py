"""
Test script voor Stan de GitHub Agent applicatie.

Dit script test de verschillende componenten en functionaliteiten
van de applicatie om ervoor te zorgen dat alles correct werkt.
"""

import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Voeg het project pad toe aan sys.path om te kunnen importeren
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Imports van de applicatie modules
from quotes import get_random_quote, get_next_quote
from config import ROBOT_QUOTES, APP_TITLE, ROBOT_SVG


class TestGitHubAgent(unittest.TestCase):
    """
    Test class voor het testen van de GitHub Agent applicatie componenten.
    """
    
    def test_quotes_functionality(self):
        """Test de quotes module functionaliteit."""
        # Test of get_random_quote een string teruggeeft
        random_quote = get_random_quote()
        self.assertIsInstance(random_quote, str)
        self.assertTrue(random_quote in ROBOT_QUOTES)
        
        # Test get_next_quote functionaliteit
        for i in range(len(ROBOT_QUOTES)):
            next_quote, next_index = get_next_quote(i)
            # Controleer of de index correct wordt verhoogd of gereset
            expected_index = (i + 1) % len(ROBOT_QUOTES)
            self.assertEqual(next_index, expected_index)
            # Controleer of de juiste quote wordt teruggegeven
            self.assertEqual(next_quote, ROBOT_QUOTES[expected_index])
    
    def test_config_values(self):
        """Test of de configuratiewaarden correct zijn ingesteld."""
        # Controleer of de titel is ingesteld
        self.assertIsInstance(APP_TITLE, str)
        self.assertTrue(len(APP_TITLE) > 0)
        
        # Controleer of de robot SVG is ingesteld
        self.assertIsInstance(ROBOT_SVG, str)
        self.assertTrue("<svg" in ROBOT_SVG)
        
        # Controleer of er voldoende quotes zijn
        self.assertTrue(len(ROBOT_QUOTES) >= 5)
        for quote in ROBOT_QUOTES:
            self.assertIsInstance(quote, str)
    
    @patch('streamlit.components.v1.html')
    @patch('streamlit.columns')
    def test_robot_display(self, mock_columns, mock_html):
        """Test de robot display functionaliteit."""
        # Setup mock voor columns
        mock_col = MagicMock()
        mock_columns.return_value = [MagicMock(), mock_col, MagicMock()]
        
        # Mock voor html component
        mock_html.return_value = {'event': 'robot_clicked'}
        
        # Import hier om de mocks correct toe te passen
        from robot import display_robot
        
        # Test de robot display functie
        result = display_robot()
        
        # Controleer of de functie True teruggeeft bij klik event
        self.assertTrue(result)
        
        # Controleer of de mock functies zijn aangeroepen
        mock_columns.assert_called_once()
        mock_html.assert_called_once()
    
    @patch('streamlit.session_state', {})
    def test_session_state_initialization(self):
        """Test of de session state correct wordt geïnitialiseerd."""
        # Import hier om de mock correct toe te passen
        from utils import initialize_session_state
        
        # Test de initialize functie
        initialize_session_state()
        
        # Controleer of de session state keys correct zijn ingesteld
        import streamlit as st
        self.assertIn('current_quote', st.session_state)
        self.assertIn('quote_index', st.session_state)
        self.assertIn('click_count', st.session_state)
        self.assertIn('initialized', st.session_state)
        
        # Controleer of de waarden correct zijn geïnitialiseerd
        self.assertIsInstance(st.session_state.current_quote, str)
        self.assertEqual(st.session_state.quote_index, 0)
        self.assertEqual(st.session_state.click_count, 0)
        self.assertTrue(st.session_state.initialized)


if __name__ == "__main__":
    unittest.main()
