
import pandas as pd
import numpy as np
import re
from dateutil import parser

INPUT = "fit_trackr_data.csv"
OUTPUT = "fit_trackr_data_cleaned.csv"

print("Loading", INPUT)
df = pd.read_csv(INPUT, encoding='utf-8', low_memory=False)
print("Initial rows:", len(df))

# standardize column names
df.columns = [c.strip() for c in df.columns]

# parse datetime columns if exista
for col in ['timestamp','datetime','date','time']:
    if col in df.columns:
        try:
            df[col+'_parsed'] = pd.to_datetime(df[col], errors='coerce')
        except:
            df[col+'_parsed'] = pd.to_datetime(df[col].astype(str), errors='coerce')

# parse duration -> minute
if 'Duration' in df.columns:
    durations = []
    for x in df['Duration']:
        if pd.isna(x):
            durations.append(np.nan)
            continue
        s = str(x).strip().lower()
        # HH:MM
        m = re.match(r'^(\d+):(\d{1,2})(?::\d{1,2})?$', s)
        if m:
            durations.append(int(m.group(1))*60 + int(m.group(2)))
            continue
        # 1h 20m
        m_h = re.findall(r'(\d+)\s*h', s)
        h = int(m_h[0]) if m_h else 0
        m_m = re.findall(r'(\d+)\s*m', s)
        mnt = int(m_m[0]) if m_m else 0
        if h or mnt:
            durations.append(h*60 + mnt)
            continue
        # number only
        m_n = re.search(r'(\d+(\.\d+)?)', s)
        if m_n:
            durations.append(float(m_n.group(1)))
        else:
            durations.append(np.nan)
    df['Duration_min'] = durations

# parse calories -> numeric
if 'Calories' in df.columns:
    calories_num = []
    for x in df['Calories']:
        if pd.isna(x):
            calories_num.append(np.nan)
            continue
        s = str(x).lower().replace(',', '.')
        m = re.search(r'(\d+(\.\d+)?)', s)
        if m:
            calories_num.append(float(m.group(1)))
        else:
            calories_num.append(np.nan)
    df['Calories_num'] = calories_num

# standardize activity
activity_map = {'walk':'Walking','walking':'Walking','run':'Running','running':'Running',
                'bike':'Cycling','cycling':'Cycling','yoga':'Yoga','strength':'Strength Training',
                'gym':'Strength Training','hike':'Hiking','swim':'Swimming','swimming':'Swimming'}

activity_std = []
if 'Activity' in df.columns:
    for x in df['Activity']:
        if pd.isna(x):
            activity_std.append(np.nan)
            continue
        s = str(x).strip().lower()
        if s in activity_map:
            activity_std.append(activity_map[s])
        else:
            matched = False
            for k,v in activity_map.items():
                if s.startswith(k):
                    activity_std.append(v)
                    matched = True
                    break
            if not matched:
                activity_std.append(str(x).strip().title())
    df['Activity_std'] = activity_std

# standardize Mood
mood_map = {'happy':'Happy','sad':'Sad','neutral':'Neutral','energetic':'Energetic',
            'tired':'Tired','stressed':'Stressed','relaxed':'Relaxed'}

mood_std = []
if 'Mood' in df.columns:
    for x in df['Mood']:
        if pd.isna(x):
            mood_std.append(np.nan)
            continue
        s = str(x).strip().lower()
        if s in mood_map:
            mood_std.append(mood_map[s])
        else:
            matched = False
            for k,v in mood_map.items():
                if k in s:
                    mood_std.append(v)
                    matched = True
                    break
            if not matched:
                mood_std.append(str(x).strip().title())
    df['Mood_std'] = mood_std

# age numeric
if 'Age' in df.columns:
    df['Age_num'] = pd.to_numeric(df['Age'], errors='coerce')

# remove duplicates
before = len(df)
df = df.drop_duplicates()
print(f"Removed duplicates: {before - len(df)}")

# drop rows missing essential info
required = []
if 'Activity_std' in df.columns: required.append('Activity_std')
if 'Duration_min' in df.columns: required.append('Duration_min')

before = len(df)
df = df.dropna(subset=required)
print(f"Dropped rows missing required {required}: {before - len(df)}")

# reset index
df = df.reset_index(drop=True)

# save
df.to_csv(OUTPUT, index=False, encoding='utf-8')
print("Saved cleaned data to", OUTPUT)
print("Final rows:", len(df))
