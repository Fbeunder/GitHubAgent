"""
Configuratie module voor Stan de GitHub Agent applicatie.

Deze module bevat constanten en configuratievariabelen die in de hele applicatie worden gebruikt.
"""

# App configuratie
APP_TITLE = "Stan de GitHub Agent"
APP_DESCRIPTION = "Klik op Stan om te ontdekken wat een GitHub Agent allemaal kan doen!"

# Robot visualisatie
ROBOT_SVG = """
<svg width="200" height="240" xmlns="http://www.w3.org/2000/svg">
    <!-- Hoofd -->
    <rect x="50" y="20" width="100" height="80" rx="10" fill="#3498db" stroke="#2980b9" stroke-width="2"/>
    
    <!-- Ogen -->
    <circle cx="75" cy="50" r="15" fill="white" stroke="#2c3e50" stroke-width="2"/>
    <circle cx="125" cy="50" r="15" fill="white" stroke="#2c3e50" stroke-width="2"/>
    <circle cx="75" cy="50" r="7" fill="#2c3e50"/>
    <circle cx="125" cy="50" r="7" fill="#2c3e50"/>
    
    <!-- Mond -->
    <rect x="70" y="80" width="60" height="10" rx="5" fill="#2c3e50"/>
    
    <!-- Antenne -->
    <line x1="100" y1="20" x2="100" y2="0" stroke="#2c3e50" stroke-width="3"/>
    <circle cx="100" cy="0" r="5" fill="#e74c3c"/>
    
    <!-- Lichaam -->
    <rect x="60" y="100" width="80" height="100" rx="5" fill="#3498db" stroke="#2980b9" stroke-width="2"/>
    
    <!-- Knop 1 -->
    <circle cx="100" cy="120" r="8" fill="#e74c3c" stroke="#c0392b" stroke-width="1"/>
    
    <!-- Knop 2 -->
    <circle cx="100" cy="145" r="8" fill="#f1c40f" stroke="#f39c12" stroke-width="1"/>
    
    <!-- Knop 3 -->
    <circle cx="100" cy="170" r="8" fill="#2ecc71" stroke="#27ae60" stroke-width="1"/>
    
    <!-- Armen -->
    <rect x="20" y="120" width="40" height="10" rx="5" fill="#3498db" stroke="#2980b9" stroke-width="2"/>
    <rect x="140" y="120" width="40" height="10" rx="5" fill="#3498db" stroke="#2980b9" stroke-width="2"/>
    
    <!-- Benen -->
    <rect x="70" y="200" width="15" height="30" rx="5" fill="#3498db" stroke="#2980b9" stroke-width="2"/>
    <rect x="115" y="200" width="15" height="30" rx="5" fill="#3498db" stroke="#2980b9" stroke-width="2"/>
</svg>
"""

# Grappige uitspraken over wat een GitHub Agent allemaal kan doen
ROBOT_QUOTES = [
    "Ik kan commits maken terwijl jij koffie drinkt!",
    "Pull requests? Ik keur ze goed voordat je ze zelfs hebt ingediend!",
    "Bugs vind ik sneller dan jij ze kunt maken!",
    "Ik kan je codebase refactoren terwijl jij een YouTube video kijkt!",
    "Mijn merge conflicts lossen zichzelf op!",
    "Ik schrijf tests die bugs vinden voordat je ze schrijft!",
    "Ik kan 24/7 je GitHub repository monitoren, zonder koffie!",
    "Code review? Ik lees je gedachten en weet al wat je gaat committen!",
    "Mijn CI/CD pipeline is zo snel dat je denkt dat ik tijdreizen kan!",
    "Issue tracking? Ik weet welke bugs je morgen gaat maken!",
    "Branches? Ik kan door de git-boom klimmen als een echte aap!",
    "GitHub Actions? Ik was al bezig voordat je op de knop drukte!",
    "Ik kan je hele applicatie documenteren terwijl jij een meeting hebt!",
    "Semantische versioning? Ik kan de toekomst van je codebase voorspellen!",
    "Ik deployde al naar productie voordat je klaar was met typen!"
]
