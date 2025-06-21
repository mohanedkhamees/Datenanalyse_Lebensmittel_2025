# 1. Datei vom lokalen Gerät hochladen
from google.colab import files
uploaded = files.upload()

# 2. Notwendige Bibliotheken importieren
import pandas as pd                  # Für die Arbeit mit Tabellen
import matplotlib.pyplot as plt      # Für die Erstellung von Diagrammen

# 3. CSV-Datei laden
filename = list(uploaded.keys())[0]  # Den Namen der hochgeladenen Datei ermitteln
df_raw = pd.read_csv(filename, skiprows=5)  # Datei einlesen, Kopfzeilen überspringen

# 4. Relevante Produktzeilen extrahieren
produkte = [
    "Brot und Brötchen",
    "Vollmilch",
    "Rind- und Kalbfleisch",
    "Schweinefleisch",
    "Geflügelfleisch"
]

# Zeilen filtern, die den gewünschten Produkten entsprechen
# Whitespace entfernen und neuen Index setzen
df_filtered = df_raw[df_raw["Unnamed: 0"].str.strip().isin(produkte)].copy()
df_filtered["Produkt"] = df_filtered["Unnamed: 0"].str.strip()
df_filtered = df_filtered.drop(columns=["Unnamed: 0", "Unnamed: 1"])
df_filtered = df_filtered.set_index("Produkt")
df_filtered = df_filtered.apply(pd.to_numeric, errors="coerce")  # Textwerte in Zahlen umwandeln

# 5. Jahreszahlen aus den Spaltennamen extrahieren
def extract_year_fixed(col):
    if "." in col:
        suffix = col.split(".")[1]
        if suffix.isdigit():
            return 2015 + int(suffix)  # z. B. .1 → 2016
    return 2015  # Spalten ohne Punkt gehören zu 2015

# Mapping für Jahreszahlen erzeugen und Durchschnitt pro Jahr berechnen
year_map = {col: extract_year_fixed(col) for col in df_filtered.columns}
df_yearly_avg = df_filtered.groupby(by=year_map, axis=1).mean().T  # Mittelwert pro Jahr

# Index umbenennen für Übersichtlichkeit
df_yearly_avg.index.name = "Jahr"

# Nur Jahre von 2015 bis 2024 behalten
df_yearly_avg = df_yearly_avg[(df_yearly_avg.index >= 2015) & (df_yearly_avg.index <= 2024)]

# 6. Diagramm zeichnen mit Zeitabschnitt-Markierungen
farben = {
    "Brot und Brötchen": "Black",
    "Vollmilch": "steelblue",
    "Rind- und Kalbfleisch": "darkred",
    "Schweinefleisch": "orange",
    "Geflügelfleisch": "green"
}

plt.figure(figsize=(12, 6))  # Größe des Diagramms festlegen

# Jede Produktlinie im Diagramm einzeichnen
for produkt in df_yearly_avg.columns:
    plt.plot(df_yearly_avg.index, df_yearly_avg[produkt], marker='o',
             label=produkt, linewidth=2, color=farben.get(produkt, None))

# Zeitabschnitte farblich markieren
plt.axvspan(2015, 2020, color='lightblue', alpha=0.2, label="Vor der Krise (2015–2020)")
plt.axvspan(2020, 2022, color='moccasin', alpha=0.3, label="Corona (2020–2022)")
plt.axvspan(2022, 2023, color='mistyrose', alpha=0.3, label="Ukraine-Krieg (2022–2023)")
plt.axvspan(2023, 2024, color='honeydew', alpha=0.3, label="Nachwirkungen (2023–2024)")

# Diagramm beschriften
plt.title("Verbraucherpreisindex (2020 = 100) – Brot, Milch, Fleisch (2015–2024) In Deutschland")
plt.xlabel("Jahr")
plt.ylabel("Indexwert")
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.xticks(df_yearly_avg.index)
plt.tight_layout()
plt.show()

# 6b. Tabelle direkt nach dem Diagramm anzeigen lassen – mit 2 Nachkommastellen
from IPython.display import display
print("\n\n👉 Durchschnittlicher Verbraucherpreisindex pro Jahr:\n")
display(df_yearly_avg.round(2))

# 7. Excel-Datei exportieren und zur Verfügung stellen
df_yearly_avg.to_excel("VPI_Lebensmittel_2015_2024.xlsx")
files.download("VPI_Lebensmittel_2015_2024.xlsx")
