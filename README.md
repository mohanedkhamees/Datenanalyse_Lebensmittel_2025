
# 📊 Datenanalyse 2025 – Lebensmittelpreise & Gehälter

📊 Dieses Projekt wurde im Rahmen einer Seminararbeit an der HTW Berlin erstellt. Es umfasst die Analyse von Gehältern und Lebensmittelpreisen in Deutschland (2015–2024) sowie einen internationalen Vergleich mit Indien und den USA für das Jahr 2024.

---

## 📁 Projektstruktur

```
Datenanalyse_Lebensmittel_2025/
├── deutschland_gehälter/
│   ├── daten/
│   ├── output/
│   └── gehalt_analyse.py
├── deutschland_preise_2015_2024/
│   ├── daten/
│   ├── output/
│   └── De_preise_analyse.py
├── vergleich_2024_d/
│   ├── daten/
│   ├── output/
│   └── Weltweit_vergleich_analyse.py
```

---

## 🇩🇪 1. Gehälter in Deutschland (`deutschland_gehälter/`)

- **Datenquelle:** © Statistisches Bundesamt (Destatis), 2025
- **Letzter Stand:** 12.06.2025 / 01:34:18
- **Inhalt:** Analyse der durchschnittlichen Gehälter in Deutschland über mehrere Jahre hinweg.
- **Dateien:**
  - `daten/gehalt_daten.csv` – Originaldaten
  - `gehalt_analyse.py` – Python-Skript zur Auswertung
  - `output/gehalt_plot.png` – Visualisierung
  - `output/jahresdurchschnitt.png` – Berechnete Jahresmittel

---

## 🍞🥩🥛 2. Lebensmittelpreise Deutschland 2015–2024 (`deutschland_preise_2015_2024/`)

- **Datenquelle:** © Statistisches Bundesamt (Destatis), 2025
- **Letzter Stand:** 12.06.2025 / 01:34:18
- **Produkte:** Brot, Fleisch, Milch
- **Zeitraum:** 2015 bis 2024
- **Dateien:**
  - `daten/De_Lebensmittel.csv` – Preisindizes
  - `De_preise_analyse.py` – Analyse- und Visualisierungsskript
  - `output/De_Lebensmittel.png` – Vergleichsdiagramm pro Produkt
  - `output/mittelwerte.png` – Durchschnittswerte je Jahr

---

## 🌍 3. Internationaler Vergleich 2024 (`vergleich_2024_d/`)

- **Länder:** Deutschland 🇩🇪, Indien 🇮🇳, USA 🇺🇸
- **Produkte:** Fleisch, Brot, Milch
- **Jahr:** 2024
- **Dateien:**
  - `daten/Deutschland(2024).csv`,`India(2024).csv`,`USA(2024).csv` – Preisdaten pro Land
  - `Weltweit_vergleich_analyse.py` – Vergleichsanalyse und Visualisierung
  - `output/Brot_plot.png` – Vergleichsdiagramm für Brot
  - `output/Fleisch_plot.png` – Vergleichsdiagramm für Fleisch
  - `output/Milch_plot.png` – Vergleichsdiagramm für Milch
  - `output/Brot_2024_werte.png` – Vergleichstabelle für Brot
  - `output/Fleisch_2024_werte.png` – Vergleichstabelle für Fleisch
  - `output/Milch_2024_werte.png` – Vergleichstabelle für Milch

---

## 🛠️ Technologien

- `Python 3.x`
- `pandas`
- `matplotlib`
- `Jupyter / Google Colab`

---

## 📚 Quellen

### 🇩🇪 Deutschland

- © Statistisches Bundesamt (Destatis), 2025  
  Stand: 12.06.2025 / 01:34:18  
  - **Gehälter in Deutschland**
  - **Lebensmittelpreise Deutschland 2015–2024**
  - **Daten für internationalen Vergleich (Deutschland, 2024)**

---

### 🇮🇳 Indien

Quelle: CEICdata.com  
Stand: 09.06.2025  
- CEICdata.com. (2025, 26. März).  
  **India Consumer Price Index: Food and Beverages: Meat and Fish**  
  https://www.ceicdata.com/en/india/consumer-price-index-2012100/consumer-price-index-food-and-beverages-meat-and-fish

- CEICdata.com. (2025, 26. März).  
  **India Consumer Price Index: Food and Beverages: Milk and Milk Product**  
  https://www.ceicdata.com/en/india/consumer-price-index-2012100/consumer-price-index-food-and-beverages-milk-and-milk-product

- CEICdata.com. (2025, 26. März).  
  **India Consumer Price Index: Food and Beverages: Bread for Bakery**  
  _(kein direkter Link verfügbar)_

---

### 🇺🇸 USA

- © Federal Reserve Economic Data (FRED), 2025  
  Stand: 13.06.2025  
  - **Lebensmittelpreise USA 2024**

---

## 📬 Kontakt

Erstellt von **Mohaned Khamees**  
📧 mohanedkhamess@gmail.com
