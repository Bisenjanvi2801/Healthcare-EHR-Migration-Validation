from faker import Faker
import pandas as pd
import random
import os


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
# PROVIDER SPECIALTIES
# ---------------------------------------------------------

specialties = [
    "Cardiology",
    "Neurology",
    "Orthopedics",
    "Pediatrics",
    "Dermatology",
    "Radiology",
    "Emergency",
    "ENT",
    "Urology",
    "General Medicine",
    "Oncology",
    "Gynecology"
]


# ---------------------------------------------------------
# GENERATE PROVIDERS
# ---------------------------------------------------------

providers = []

for i in range(1, 501):

    providers.append({
        "Provider_ID": f"PROV{i:04}",
        "Provider_Name": fake.name(),
        "Specialty": random.choice(specialties),
        "Phone": fake.msisdn()[:10],
        "Email": fake.email(),
        "Experience_Years": random.randint(1, 35),
        "Department_ID": f"DEPT{random.randint(1, 20):03}",
        "Status": random.choice(["Active", "Inactive"])
    })


# ---------------------------------------------------------
# CREATE DATAFRAME
# ---------------------------------------------------------

df = pd.DataFrame(providers)


# ---------------------------------------------------------
# SAVE OUTPUT
# ---------------------------------------------------------

output_file = os.path.join(
    SOURCE_PATH,
    "Providers_Source.xlsx"
)

df.to_excel(output_file, index=False)


# ---------------------------------------------------------
# OUTPUT MESSAGE
# ---------------------------------------------------------

print("=" * 50)
print("Providers file generated successfully!")
print(f"Total Records : {len(df)}")
print(f"Output File   : {output_file}")
print("=" * 50)