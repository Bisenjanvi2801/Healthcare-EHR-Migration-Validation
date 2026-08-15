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
# ALLERGY MASTER DATA
# ---------------------------------------------------------

allergy_master = [
    "Penicillin",
    "Sulfa Drugs",
    "Latex",
    "Peanuts",
    "Shellfish",
    "Milk",
    "Egg",
    "Soy",
    "Dust",
    "Pollen",
    "Ibuprofen",
    "Aspirin",
    "Bee Sting",
    "Seafood",
    "Mold"
]


severity = [
    "Mild",
    "Moderate",
    "Severe"
]


reaction = [
    "Skin Rash",
    "Itching",
    "Swelling",
    "Anaphylaxis",
    "Shortness of Breath",
    "Hives",
    "Sneezing"
]


# ---------------------------------------------------------
# GENERATE ALLERGIES
# ---------------------------------------------------------

records = []

allergy_id = 1

for _, row in encounters.iterrows():

    if random.random() < 0.60:

        records.append({
            "Allergy_ID": f"ALG{allergy_id:06}",
            "Encounter_ID": row["Encounter_ID"],
            "Allergy_Name": random.choice(allergy_master),
            "Severity": random.choice(severity),
            "Reaction": random.choice(reaction),
            "Status": "Active"
        })

        allergy_id += 1


# ---------------------------------------------------------
# CREATE DATAFRAME
# ---------------------------------------------------------

df = pd.DataFrame(records)


# ---------------------------------------------------------
# SAVE OUTPUT
# ---------------------------------------------------------

output_file = os.path.join(
    SOURCE_PATH,
    "Allergies_Source.xlsx"
)

df.to_excel(
    output_file,
    index=False
)


# ---------------------------------------------------------
# OUTPUT MESSAGE
# ---------------------------------------------------------

print("=" * 60)
print("Allergies Generated Successfully")
print(f"Total Records : {len(df)}")
print(f"Output File   : {output_file}")
print("=" * 60)