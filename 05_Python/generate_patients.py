import pandas as pd
from faker import Faker
import random
import os
from datetime import datetime


# ---------------------------------------------------------
# INITIALIZATION
# ---------------------------------------------------------

fake = Faker("en_IN")

random.seed(42)
Faker.seed(42)


# ---------------------------------------------------------
# PROJECT PATH
# ---------------------------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCE_PATH = os.path.join(BASE_DIR, "02_Source_Data")

os.makedirs(SOURCE_PATH, exist_ok=True)


# ---------------------------------------------------------
# PATIENT CONFIGURATION
# ---------------------------------------------------------

TOTAL_PATIENTS = 15000


# ---------------------------------------------------------
# MASTER VALUES
# ---------------------------------------------------------

blood_groups = [
    "A+",
    "A-",
    "B+",
    "B-",
    "AB+",
    "AB-",
    "O+",
    "O-"
]


insurance = [
    "Medicare",
    "Medicaid",
    "Blue Cross",
    "United Health",
    "Aetna",
    "Cigna"
]


genders = [
    "Male",
    "Female"
]


# ---------------------------------------------------------
# GENERATE PATIENTS
# ---------------------------------------------------------

patients = []

for i in range(1, TOTAL_PATIENTS + 1):

    dob = fake.date_between(
        start_date="-80y",
        end_date="-18y"
    )

    age = datetime.now().year - dob.year

    patient = {
        "Patient_ID": f"PAT{i:05}",
        "MRN": f"MRN{i:07}",
        "First_Name": fake.first_name(),
        "Last_Name": fake.last_name(),
        "Gender": random.choice(genders),
        "Date_of_Birth": dob,
        "Age": age,
        "Phone": fake.phone_number(),
        "Email": fake.email(),
        "Address": fake.street_address(),
        "City": fake.city(),
        "State": fake.state(),
        "ZIP_Code": fake.postcode(),
        "Insurance": random.choice(insurance),
        "Blood_Group": random.choice(blood_groups)
    }

    patients.append(patient)


# ---------------------------------------------------------
# CREATE DATAFRAME
# ---------------------------------------------------------

df = pd.DataFrame(patients)


# ---------------------------------------------------------
# SORT BY PATIENT ID
# ---------------------------------------------------------

df = df.sort_values("Patient_ID")


# ---------------------------------------------------------
# SAVE OUTPUT
# ---------------------------------------------------------

output_file = os.path.join(
    SOURCE_PATH,
    "Patients_Source.xlsx"
)

df.to_excel(output_file, index=False)


# ---------------------------------------------------------
# OUTPUT MESSAGE
# ---------------------------------------------------------

print("=" * 50)
print("Patients file generated successfully!")
print(f"Total Records : {len(df)}")
print(f"Output File   : {output_file}")
print("=" * 50)