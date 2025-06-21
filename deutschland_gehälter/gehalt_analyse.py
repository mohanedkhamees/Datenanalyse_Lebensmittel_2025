# Datei-Upload aus lokalem System (Google Colab)
from google.colab import files
uploaded = files.upload()  # Öffnet Fenster zum Hochladen einer Datei

# Bibliotheken importieren
import pandas as pd                # Für Tabellenverarbeitung
import matplotlib.pyplot as plt    # Für das Zeichnen von Diagrammen

# Dateinamen der hochgeladenen Datei bestimmen
filename = list(uploaded.keys())[0]

# CSV-Datei einlesen – Trennzeichen ist Komma
df_raw = pd.read_csv(filename, encoding="utf-8", delimiter=",")

# Jahre aus Zeile 3 (Index 2), Spalten 3 bis 12 (entspricht 2015–2024)
jahre = df_raw.iloc[2, 2:12].astype(int)  # Umwandeln in Ganzzahlen

# Werte für Entgelt, Bruttolohn und Nettolohn aus den nächsten Zeilen extrahieren
entgelt = df_raw.iloc[3, 2:12].astype(float)   # Arbeitnehmerentgelt (Zeile 4)
brutto = df_raw.iloc[4, 2:12].astype(float)    # Bruttolohn (Zeile 5)
netto = df_raw.iloc[5, 2:12].astype(float)     # Nettolohn (Zeile 6)

# Neuen DataFrame mit den extrahierten Werten erstellen
df_clean = pd.DataFrame({
    "Jahr": jahre,
    "Arbeitnehmerentgelt": entgelt,
    "Bruttolohn": brutto,
    "Nettolohn": netto
})

# Abzüge berechnen = Brutto - Netto
df_clean["Abzüge"] = df_clean["Bruttolohn"] - df_clean["Nettolohn"]

# Werte aus dem Jahr 2020 als Referenzwert (Basis für Index)
# Erklärung siehe unten
wert_2020_netto = df_clean[df_clean["Jahr"] == 2020]["Nettolohn"].values[0]
wert_2020_brutto = df_clean[df_clean["Jahr"] == 2020]["Bruttolohn"].values[0]
wert_2020_abzuege = df_clean[df_clean["Jahr"] == 2020]["Abzüge"].values[0]

# Verbraucherpreisindex berechnen – alles relativ zum Jahr 2020 (=100)
df_clean["Netto_Index"] = df_clean["Nettolohn"] / wert_2020_netto * 100
df_clean["Brutto_Index"] = df_clean["Bruttolohn"] / wert_2020_brutto * 100
df_clean["Abzüge_Index"] = df_clean["Abzüge"] / wert_2020_abzuege * 100

# Diagramm erstellen
plt.figure(figsize=(12, 6))

# Linien für Netto, Brutto, Abzüge
plt.plot(df_clean["Jahr"], df_clean["Netto_Index"], label="Nettolohn (Index)", marker="o")
plt.plot(df_clean["Jahr"], df_clean["Brutto_Index"], label="Bruttolohn (Index)", marker="o")
plt.plot(df_clean["Jahr"], df_clean["Abzüge_Index"], label="Abzüge (Index)", marker="o")

# Referenzlinie bei Index = 100 (Basisjahr)
plt.axhline(100, color="gray", linestyle="--", linewidth=1, label="Basis 2020 = 100")
# Hintergrundfarben für Zeiträume hinzufügen
plt.axvspan(2015, 2020, color='lightblue', alpha=0.2, label="Vor der Krise (2015–2020)")
plt.axvspan(2020, 2022, color='orange', alpha=0.2, label="Corona (2020–2022)")
plt.axvspan(2022, 2023, color='lightcoral', alpha=0.2, label="Ukraine-Krieg (2022–2023)")
plt.axvspan(2023, 2024, color='lightgreen', alpha=0.2, label="Nachwirkungen (2023–2024)")
# Achsenbeschriftung und Anzeige
plt.title("Lohnentwicklung als Verbraucherpreisindex (2020 = 100) in Deutschland")
plt.xlabel("Jahr")
plt.ylabel("Indexwert")
plt.grid(True)
plt.legend()
plt.xticks(df_clean["Jahr"])
plt.tight_layout()
plt.show()

# Tabelle mit Indexwerten anzeigen
from IPython.display import display
df_index = df_clean[["Jahr", "Netto_Index", "Brutto_Index", "Abzüge_Index"]].copy()
df_index = df_index.round(2)  # Werte runden auf 2 Nachkommastellen
display(df_index)

# EXTRAKOMMENTAR (Erklärung für diese Art von Zugriff):

# Beispiel:
# df_clean[df_clean["Jahr"] == 2020]["Nettolohn"].values[0]
#
# → Bedeutet:
# 1. Suche die Zeile, wo "Jahr" = 2020
# 2. Wähle aus dieser Zeile die Spalte "Nettolohn"
# 3. Nutze .values[0], um den konkreten Zahlenwert (float) zu extrahieren
#    (ohne .values[0] bekäme man eine Pandas-Serie, nicht den Wert selbst)
