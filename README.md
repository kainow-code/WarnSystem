
![Logo](https://cdn.leonardo.ai/users/448575ec-2432-4881-8c84-d8f925a25b2f/generations/e372e812-2fa0-4018-9dc2-140de711785a/Default_A_futuristic_neonlit_banner_with_a_bold_red_font_displ_0.jpg)


# Warn System

Ein leistungsstarkes Warnsystem für Discord-Server, das es Moderatoren ermöglicht, Benutzer zu verwalten, Warnungen zu protokollieren und automatische Strafen festzulegen. Dieses System nutzt `py-cord` und `aiosqlite` zur Verwaltung von Warnungen und Strafen innerhalb einer SQLite-Datenbank.




### Funktionen

- **Benutzer warnen**: Moderatoren können Benutzer warnen, wobei die Warnung in einer Datenbank gespeichert wird.
- **Automatische Strafen**: Automatische Strafen wie Kick, Ban oder Mute können basierend auf der Anzahl der Warnungen eines Benutzers festgelegt werden.
- **Warnungen anzeigen**: Zeigt eine Liste aller Warnungen eines bestimmten Benutzers oder aller Benutzer an.
- **Warnungen löschen**: Löschen von Warnungen basierend auf ihrer ID.
- **Strafen verwalten**: Setzen, anzeigen und löschen von Strafen, die bei einer bestimmten Anzahl von Warnungen ausgelöst werden.
- **Seitenweise Navigation**: Anzeige langer Listen von Warnungen in einem paginierten Format im Discord-Chat.

### Voraussetzungen

- `Python` 3.12
- `py-cord` Bibliothek
- `aiosqlite` Bibliothek
### Installation


1. Klone das Repository:

   ```bash
   git clone https://github.com/kainow-code/WarnSystem
   cd warnsystem-bot
   ```

2. Installiere die benötigten Bibliotheken:

   ```bash
   pip install py-cord aiosqlite
   ```

3. Erstelle eine `.env` Datei und füge deinen Discord-Bot-Token hinzu:

   ```bash
   TOKEN=your-bot-token-here
   ```

4. Starte den Bot:

   ```bash
   python main.py
   ```
### Befehle

- `/warn <user> <reason>` - Warnt einen Benutzer mit einem angegebenen Grund.
- `/warnings <user>` - Zeigt alle Warnungen für einen Benutzer an.
- `/delwarn <warn_id>` - Löscht eine spezifische Warnung.
- `/allwarnings` - Zeigt alle Warnungen aller Benutzer an.
- `/set_punishment <warn_count> <punishment_type> [duration]` - Setzt eine Strafe für eine bestimmte Anzahl von Warnungen.
- `/show_punishments` - Zeigt alle festgelegten Strafen an.
- `/del_punishments` - Löscht alle festgelegten Strafen.
## Authors

- [@kainow-code](https://github.com/kainow-code)

