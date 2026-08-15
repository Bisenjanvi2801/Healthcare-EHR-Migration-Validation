from faker import Faker
import pandas as pd
import random
import os
from datetime import date


# ---------------------------------------------------------
# INITIALIZATION
# ---------------------------------------------------------

fake = Faker()

random.seed(42)
Faker.seed(42)


# ---------------------------------------------------------
# PROJECT PATH
# ---------------------------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCE_PATH = os.path.join(BASE_DIR, "02_Source_Data")

os.makedirs(SOURCE_PATH, exist_ok=True)


# ---------------------------------------------------------
# LOAD PATIENT DATA
# ---------------------------------------------------------

patients_file = os.path.join(
    SOURCE_PATH,
    "Patients_Source.xlsx"
)

patients = pd.read_excel(patients_file)


# ---------------------------------------------------------
# GENERATE ENCOUNTERS
# ---------------------------------------------------------

encounters = []

for i in range(1, 25001):

    # Select an existing patient
    patient = patients.iloc[
        random.randint(0, len(patients) - 1)
    ]

    encounter = {
        "Encounter_ID": f"ENC{i:05}",

        "MRN": patient["MRN"],

        "Patient_ID": patient["Patient_ID"],

        "Provider_ID": f"PROV{random.randint(1, 500):04}",

        "Encounter_Date": fake.date_between(
            start_date=date(2018, 1, 1),
            end_date=date(2022, 12, 31)
        ),

        "Diagnosis_Code": random.choice([
            "E11.9",
            "I10",
            "J06.9",
            "M54.5",
            "K21.9",
            "N39.0",
            "R51",
            "J45.909"
        ]),

        "Procedure_Code": random.choice([
            "99213",
            "99214",
            "93000",
            "80053",
            "71020",
            "85025"
        ]),

        "Visit_Reason": random.choice([
            "Fever",
            "Cough",
            "Diabetes Follow-up",
            "Hypertension",
            "Annual Checkup",
            "Back Pain",
            "Headache",
            "Routine Consultation"
        ]),

        "Discharge_Status": random.choice([
            "Discharged",
            "Admitted",
            "Referred",
            "Observation"
        ])
    }

    encounters.append(encounter)


# ---------------------------------------------------------
# CREATE DATAFRAME
# ---------------------------------------------------------

df = pd.DataFrame(encounters)


# ---------------------------------------------------------
# SAVE OUTPUT
# ---------------------------------------------------------

output_file = os.path.join(
    SOURCE_PATH,
    "Encounters_Source.xlsx"
)

df.to_excel(
    output_file,
    index=False
)


# ---------------------------------------------------------
# OUTPUT MESSAGE
# ---------------------------------------------------------

print("=" * 50)
print("Encounters file generated successfully!")
print(f"Total Records : {len(df)}")
print(f"Output File   : {output_file}")
print("=" * 50)