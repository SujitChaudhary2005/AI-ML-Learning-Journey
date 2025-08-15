import os
from preprocessing import preprocess_titanic
import pandas as pd

# ====== 1. SETUP PATHS ======
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # mini_project folder
DATA_DIR = os.path.join(BASE_DIR, "Project_data")
INPUT_FILE = os.path.join(DATA_DIR, "train.csv")
CLEANED_FILE = os.path.join(DATA_DIR, "titanic_cleaned.csv")
SURVIVAL_RATES_FILE = os.path.join(DATA_DIR, "survival_rates.csv")
TOP_CABINS_COUNT_FILE = os.path.join(DATA_DIR, "top_cabins_by_survivors.csv")
TOP_CABINS_RATE_FILE = os.path.join(DATA_DIR, "top_cabins_by_survival_rate.csv")

# ====== 2. CHECK INPUT FILE ======
if not os.path.exists(INPUT_FILE):
    raise FileNotFoundError(f"Cannot find train.csv at {INPUT_FILE}")

# ====== 3. LOAD AND PREPROCESS DATA ======
print("Loading dataset...")
df = preprocess_titanic(INPUT_FILE)
print("Dataset loaded and preprocessed successfully!\n")

# ====== 4. SURVIVAL ANALYSIS ======
print("Calculating survival rates by Sex...")
survival_rates = df.groupby("Sex")["Survived"].mean().reset_index()
survival_rates.rename(columns={"Survived": "SurvivalRate"}, inplace=True)
print(survival_rates, "\n")

# Save survival rates
survival_rates.to_csv(SURVIVAL_RATES_FILE, index=False)
print(f"Survival rates saved to: {SURVIVAL_RATES_FILE}\n")

# ====== 5. SAVE CLEANED DATA ======
df.to_csv(CLEANED_FILE, index=False)
print(f"Cleaned dataset saved to: {CLEANED_FILE}\n")

# ====== 6. EXTRA ANALYSIS ======
print("Extra Analysis:")
print("Average Age by Pclass:")
print(df.groupby("Pclass")["Age"].mean(), "\n")

print("Passenger count by Pclass and Sex:")
print(df.groupby(["Pclass", "Sex"])["PassengerId"].count(), "\n")

# ====== 7. CABIN SURVIVAL ANALYSIS ======
print("Top cabins by number of survivors:")
df_cabin = df[df['Cabin'] != "Unknown"]  # exclude unknown cabins
survivors_per_cabin = df_cabin[df_cabin['Survived'] == 1] \
                        .groupby('Cabin')['Survived'] \
                        .count() \
                        .sort_values(ascending=False)
print(survivors_per_cabin.head(10), "\n")

# Save top cabins by survivor count
survivors_per_cabin.to_csv(TOP_CABINS_COUNT_FILE)
print(f"Top cabins by number of survivors saved to: {TOP_CABINS_COUNT_FILE}\n")

print("Top cabins by survival rate:")
survival_rate_cabin = df_cabin.groupby('Cabin')['Survived'].mean() \
                              .sort_values(ascending=False)
print(survival_rate_cabin.head(10), "\n")

# Save top cabins by survival rate
survival_rate_cabin.to_csv(TOP_CABINS_RATE_FILE)
print(f"Top cabins by survival rate saved to: {TOP_CABINS_RATE_FILE}\n")

print("Project Completed Successfully!")
