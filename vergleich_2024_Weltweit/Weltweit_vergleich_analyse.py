# Bibliotheken importieren
from google.colab import files                      # Für Datei-Upload im Browser
import pandas as pd                                 # Für Tabellenverarbeitung
import matplotlib.pyplot as plt                     # Für Diagramme
from IPython.display import display                 # Zum Anzeigen von Tabellen

# Benutzer wird aufgefordert, drei Dateien hochzuladen
print(" Bitte lade die CSV-Dateien für Deutschland, USA und Indien hoch (Reihenfolge egal)...")
uploaded = files.upload()                           # Öffnet Dialog zum Hochladen
dateien = list(uploaded.keys())                     # Holt Dateinamen

# Automatische Zuordnung der Dateien zu Ländern basierend auf Inhalt
dateipfade = {}
for pfad in dateien:
    with open(pfad, encoding='utf-8') as f:
        first_line = f.readline()
        if "Deutschland" in first_line:
            dateipfade["Deutschland"] = pfad
        elif "USA" in first_line:
            dateipfade["USA"] = pfad
        elif "Indien" in first_line or "India" in first_line:
            dateipfade["Indien"] = pfad

# Sicherstellen, dass alle drei Länder erkannt wurden
if len(dateipfade) != 3:
    raise ValueError(" Nicht alle Länder erkannt. Bitte lade genau drei gültige CSV-Dateien hoch.")

# Farben für Diagrammlinien pro Land
farben = {
    "Deutschland": "steelblue",
    "USA": "tomato",
    "Indien": "seagreen"
}

# Monatsnamen für x-Achse
monate = ["Jan", "Feb", "Mär", "Apr", "Mai", "Jun",
          "Jul", "Aug", "Sep", "Okt", "Nov", "Dez"]

# Zeilenindex für jedes Produkt (Deutschland & USA)
standard_index = {
    "Brot und Brötchen": 9,
    "Rind- und Kalbfleisch": 11,
    "Vollmilch": 17
}

# Abweichende Zeilenindexe für Indien
indien_index = {
    "Brot und Brötchen": 4,
    "Rind- und Kalbfleisch": 6,
    "Vollmilch": 12
}

# Dateien einlesen (Indien braucht skiprows=5)
datenframes = {}
for land, pfad in dateipfade.items():
    if land == "Indien":
        datenframes[land] = pd.read_csv(pfad, skiprows=5)
    else:
        datenframes[land] = pd.read_csv(pfad)

# Diagramm für jedes Produkt erstellen
for produkt in standard_index.keys():
    plt.figure(figsize=(12, 6))        # Diagrammgröße
    tabelle = {}                       # Zum Speichern der Werte in einer Tabelle

    for land, df in datenframes.items():
        # Korrekte Zeile für das Produkt bestimmen
        index = indien_index[produkt] if land == "Indien" else standard_index[produkt]

        # Werte für Jan–Dez aus Spalten 3–14 (Index 2:14)
        werte = df.iloc[index, 2:14].astype(float).values

        # 🔁 Normierung: Juni = 100 → Index 5 ist Juni
        werte = werte / werte[5] * 100

        # Linie ins Diagramm zeichnen
        plt.plot(monate, werte, marker="o", label=land,
                 color=farben[land], linewidth=2)

        # Werte für die spätere Tabelle speichern
        tabelle[land] = werte

    # Diagramm beschriften
    plt.title(f" Verbraucherpreisindex 2024 – {produkt} (Basis: Juni = 100)")
    plt.xlabel("Monat")
    plt.ylabel("Indexwert (Juni = 100)")
    plt.grid(True)

    # Horizontale Referenzlinie bei 100 (Basislinie)
    plt.axhline(100, color="gray", linestyle="--", linewidth=1, label="Basis: Juni = 100")

    # Legende und Anzeige
    plt.legend()
    plt.tight_layout()
    plt.show()

    # Tabelle der Indexwerte anzeigen
    df_tabelle = pd.DataFrame(tabelle, index=monate)
    display(df_tabelle.round(2))  # Auf 2 Nachkommastellen runden
