import pandas as pd
import random
import os


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
# DIAGNOSIS MASTER DATA
# ---------------------------------------------------------

diagnosis_master = [
    ("E11.9", "Type 2 Diabetes Mellitus"),
    ("I10", "Essential Hypertension"),
    ("J45.909", "Asthma"),
    ("J06.9", "Upper Respiratory Infection"),
    ("M54.5", "Low Back Pain"),
    ("K21.9", "GERD"),
    ("N39.0", "Urinary Tract Infection"),
    ("R51", "Headache"),
    ("F41.9", "Anxiety Disorder"),
    ("E78.5", "Hyperlipidemia"),
    ("J20.9", "Acute Bronchitis"),
    ("M17.9", "Osteoarthritis"),
    ("E03.9", "Hypothyroidism"),
    ("D64.9", "Anemia"),
    ("J18.9", "Pneumonia")
]


# ---------------------------------------------------------
# GENERATE DIAGNOSES
# ---------------------------------------------------------

records = []

diagnosis_id = 1

for _, row in encounters.iterrows():

    total = random.randint(1, 3)

    for _ in range(total):

        code, name = random.choice(
            diagnosis_master
        )

        records.append({
            "Diagnosis_ID": f"DGN{diagnosis_id:06}",
            "Encounter_ID": row["Encounter_ID"],
            "Diagnosis_Code": code,
            "Diagnosis_Name": name,
            "Diagnosis_Type": random.choice([
                "Primary",
                "Secondary"
            ]),
            "Diagnosis_Status": "Active"
        })

        diagnosis_id += 1


# ---------------------------------------------------------
# CREATE DATAFRAME
# ---------------------------------------------------------

df = pd.DataFrame(records)


# ---------------------------------------------------------
# SAVE OUTPUT
# ---------------------------------------------------------

output_file = os.path.join(
    SOURCE_PATH,
    "Diagnoses_Source.xlsx"
)

df.to_excel(
    output_file,
    index=False
)


# ---------------------------------------------------------
# OUTPUT MESSAGE
# ---------------------------------------------------------

print("=" * 60)
print("Diagnoses Generated Successfully")
print(f"Total Records : {len(df)}")
print(f"Output File   : {output_file}")
print("=" * 60)