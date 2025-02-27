# Stan de GitHub Agent

Een interactieve Streamlit-applicatie die een robot weergeeft waarop gebruikers kunnen klikken om grappige uitspraken te zien over wat een GitHub Agent allemaal kan doen.

## Projectbeschrijving

Stan de GitHub Agent is een eenvoudige, vermakelijke interface die laat zien wat de mogelijkheden van een GitHub Agent zijn op een humoristische wijze. Klik op Stan de robot om te ontdekken wat een GitHub Agent allemaal kan doen!

## Installatie

### Vereisten

- Python 3.8 of hoger
- Streamlit 1.15.0 of hoger

### Stappen

1. Clone de repository:
   ```
   git clone https://github.com/Fbeunder/GitHubAgent.git
   cd GitHubAgent
   ```

2. Installeer de benodigde packages:
   ```
   pip install -r requirements.txt
   ```

## Gebruik

1. Start de applicatie:
   ```
   streamlit run app.py
   ```

2. Open je browser en navigeer naar de URL die in de terminal wordt weergegeven (meestal http://localhost:8501).

3. Klik op Stan de robot om verschillende grappige uitspraken te zien over wat een GitHub Agent allemaal kan doen!

## Projectstructuur

- `app.py`: Hoofdapplicatie en Streamlit interface
- `robot.py`: Module voor robotvisualisatie en interactie
- `quotes.py`: Module voor het beheren van grappige uitspraken
- `utils.py`: Algemene hulpfuncties
- `config.py`: Configuratie-instellingen met constanten
- `test_app.py`: Unittest script voor het testen van de applicatie

## Testen

Voer de unit tests uit om de functionaliteit te verifiëren:

```
python -m unittest test_app.py
```

## Bijdragen

Bijdragen aan dit project zijn welkom! Je kunt bijdragen door:

1. Een fork te maken van het project
2. Een nieuwe branch te maken voor je functie (`git checkout -b feature/geweldige-functie`)
3. Je wijzigingen te committen (`git commit -m 'Voeg geweldige functie toe'`)
4. De branch te pushen (`git push origin feature/geweldige-functie`)
5. Een Pull Request te openen

## Licentie

Dit project is gelicenseerd onder de MIT-licentie. Zie het LICENSE-bestand voor details.
