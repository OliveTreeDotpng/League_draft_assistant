# LoL Draft Assistant
## 📌 Progress Tracker

### Vecka 1 – 13 till 18 augusti *(EDA & Grundstruktur)*
- [x] Initiera Git-repo och mappstruktur
- [x] Skapa `.gitignore` och README
- [x] Skapa SQLite-databas med schema (`lol_feedback.db`)
- [x] AfterMatch-sida för att logga matchresultat
- [x] EDA-sida bas: filter + winrate per champion
- [x] Export av filtrerad data till CSV
- [ ] Matchup-matris (winrate + antal matcher)
- [ ] Synergiheatmap (roll-par i samma lag)
- [ ] Damage/CC-profiler med varningar
- [ ] Kort EDA-sammanfattning i text
- [ ] Testa alla filter och grafer på större dataset
- [ ] Rensa kod och kommentera inför commit

### Vecka 2 – 19 till 25 augusti *(Vision – Championigenkänning)*
- [ ] Ikonklassificering (CNN på champion icons)
- [ ] Modul för att upptäcka och extrahera champion-rutor i champ select
- [ ] Vision kopplad till Rekommendation-sidan (picks/bans fylls automatiskt)
- [ ] Grad-CAM för vald ikon

### Vecka 3 – 26 augusti till 1 september *(Rekommendation & Utvärdering)*
- [ ] Rekommendationsmotor: win probability per kandidat
- [ ] Lagbalanslogik (engage, tank, damage mix)
- [ ] Utvärdering-sida: ROC, PR, kalibrering
- [ ] Felanalys: drafts där modellen tog mest fel
- [ ] Koppla AfterMatch-feedback till kalibrering

### Vecka 4 – 2 till 3 september *(Polering & Leverans)*
- [ ] README med körinstruktioner och skärmbilder
- [ ] Tooltip/förklaringar i UI
- [ ] Testa hela flödet live
- [ ] Förbered presentation/demofilm
