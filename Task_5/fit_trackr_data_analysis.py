

import pandas as pd
import numpy as np

CLEANED = "fit_trackr_data_cleaned.csv"
OUTTXT = "analysis_results.txt" # pentru raport docx

df = pd.read_csv(CLEANED, low_memory=False)

out = []

# 1) Durata medie
if 'Duration_min' in df.columns:
    durations = df['Duration_min'].dropna().astype(float)
    mean_duration = durations.mean()
    out.append(f"1) Durata medie a activității (minute): {mean_duration:.2f}")
else:
    out.append("1) Nu există coloana 'Duration_min'.")

# 2) Activitate cea mai frecventă
if 'Activity_std' in df.columns:
    mode_activity = df['Activity_std'].mode()
    mode_activity_val = mode_activity.iloc[0] if not mode_activity.empty else "N/A"
    out.append(f"2) Activitatea cea mai frecventă: {mode_activity_val}")
else:
    out.append("2) Nu există coloana 'Activity_std'.")

# 3) Mood cea mai frecventă
if 'Mood_std' in df.columns:
    mode_mood = df['Mood_std'].mode()
    mode_mood_val = mode_mood.iloc[0] if not mode_mood.empty else "N/A"
    out.append(f"3) Starea de spirit cea mai frecventă: {mode_mood_val}")
else:
    out.append("3) Nu există coloana 'Mood_std'.")

# 4) Variația calorii per activitate
if 'Calories_num' in df.columns and 'Activity_std' in df.columns:
    grouped = df.groupby('Activity_std')['Calories_num'].agg(['count','mean','std']).sort_values('count', ascending=False)
    out.append("4) Variatia calorii (per Activity):\n" + grouped.to_string())
else:
    out.append("4) Nu se poate calcula std pe Calories per Activity.")

# 5) Age: IQR
if 'Age_num' in df.columns:
    ages = df['Age_num'].dropna().astype(float)
    q1 = ages.quantile(0.25)
    q2 = ages.quantile(0.5)
    q3 = ages.quantile(0.75)
    iqr = q3 - q1
    out.append(f"5) Age: Q1={q1:.2f}, Median(Q2)={q2:.2f}, Q3={q3:.2f}, IQR={iqr:.2f}")
    out.append("   Interpretare: IQR măsoară dispersia centrală a vârstelor utilizatorilor.")
else:
    out.append("5) Nu există coloana 'Age_num' pentru calcul IQR.")

# Salvare rezultate
with open(OUTTXT,'w', encoding='utf-8') as f:
    f.write("\n\n".join(out))

print("\n\n".join(out))
print("\nRezultatele au fost salvate în", OUTTXT)