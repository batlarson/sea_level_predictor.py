# 🌊 Sea Level Predictor

This project is part of the **Data Analysis with Python** certification on freeCodeCamp.  
It analyzes sea level rise data and uses linear regression to project future sea levels until the year 2050.

---

## 🧠 Project Description

The goal of this project is to perform simple linear regression using historical data from the **EPA (Environmental Protection Agency)**.  
The analysis visualizes both the long-term and modern trends of global sea level rise.

Two lines of best fit are plotted:
1. **1880–2018:** Long-term trend based on all available data.
2. **2000–2018:** Recent trend showing accelerated sea level rise.

---

## 📈 What the Program Does

- Reads the EPA sea level dataset (`epa-sea-level.csv`).
- Creates a **scatter plot** of the measured data.
- Calculates and plots two **lines of best fit**:
  - One using all data.
  - One using data from 2000 onwards.
- Projects sea level rise up to the year **2050**.
- Saves the final chart as `sea_level_plot.png`.

---

## 🧰 Technologies Used

- Python 3  
- Pandas  
- Matplotlib  
- SciPy (for linear regression)

---

## 📂 Files in This Repository

| File | Description |
|------|--------------|
| `main.py` | Main Python script that generates the plot. |
| `README.md` | Project documentation (this file). |
| `requirements.txt` | Python dependencies. |
| `.gitignore` | Files and folders ignored by Git. |
| `sea_level_plot.png` | Output plot image. |

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR-USERNAME/sea-level-predictor.git
   cd sea-level-predictor
