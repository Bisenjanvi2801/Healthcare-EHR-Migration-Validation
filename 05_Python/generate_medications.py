import pandas as pd
import random
import os
from datetime import timedelta


# ---------------------------------------------------------
# INITIALIZATION
# ---------------------------------------------------------

random.seed(42)


# ---------------------------------------------------------
# PROJECT PATH
# ---------------------------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCE_PATH = os.path.join(BASE_DIR, "02_Source_Data")


# ---------------------------------------------------------
# LOAD ENCOUNTER DATA
# ---------------------------------------------------------

encounter_file = os.path.join(
    SOURCE_PATH,
    "Encounters_Source.xlsx"
)

encounters = pd.read_excel(encounter_file)


# ---------------------------------------------------------
# MEDICATION MASTER DATA
# ---------------------------------------------------------

medication_master = [
    ("Metformin", "500 mg"),
    ("Amlodipine", "5 mg"),
    ("Paracetamol", "650 mg"),
    ("Atorvastatin", "20 mg"),
    ("Pantoprazole", "40 mg"),
    ("Amoxicillin", "500 mg"),
    ("Losartan", "50 mg"),
    ("Levothyroxine", "50 mcg"),
    ("Salbutamol", "2 mg"),
    ("Azithromycin", "500 mg"),
    ("Insulin", "10 Units"),
    ("Omeprazole", "20 mg")
]


frequency = [
    "Once Daily",
    "Twice Daily",
    "Three Times Daily",
    "SOS"
]


route = [
    "Oral",
    "IV",
    "IM",
    "Inhalation"
]


# ---------------------------------------------------------
# GENERATE MEDICATIONS
# ---------------------------------------------------------

records = []

medication_id = 1

for _, row in encounters.iterrows():

    total = random.randint(1, 3)

    for _ in range(total):

        medicine, dosage = random.choice(
            medication_master
        )

        start_date = pd.to_datetime(
            row["Encounter_Date"]
        )

        end_date = start_date + timedelta(
            days=random.randint(3, 30)
        )

        records.append({
            "Medication_ID": f"MED{medication_id:06}",
            "Encounter_ID": row["Encounter_ID"],
            "Medication_Name": medicine,
            "Dosage": dosage,
            "Frequency": random.choice(frequency),
            "Route": random.choice(route),
            "Start_Date": start_date.date(),
            "End_Date": end_date.date()
        })

        medication_id += 1


# ---------------------------------------------------------
# CREATE DATAFRAME
# ---------------------------------------------------------

df = pd.DataFrame(records)


# ---------------------------------------------------------
# SAVE OUTPUT
# ---------------------------------------------------------

output_file = os.path.join(
    SOURCE_PATH,
    "Medications_Source.xlsx"
)

df.to_excel(
    output_file,
    index=False
)


# ---------------------------------------------------------
# OUTPUT MESSAGE
# ---------------------------------------------------------

print("=" * 60)
print("Medications Generated Successfully")
print(f"Total Records : {len(df)}")
print(f"Output File   : {output_file}")
print("=" * 60)