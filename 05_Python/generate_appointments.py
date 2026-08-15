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
# LOAD PROVIDER DATA
# ---------------------------------------------------------

providers_file = os.path.join(
    SOURCE_PATH,
    "Providers_Source.xlsx"
)

providers = pd.read_excel(providers_file)


# ---------------------------------------------------------
# GENERATE APPOINTMENTS
# ---------------------------------------------------------

appointments = []

for i in range(1, 20001):

    # Select an existing provider
    provider = providers.iloc[
        random.randint(0, len(providers) - 1)
    ]

    appointment = {
        "Appointment_ID": f"APT{i:05}",

        "Patient_ID": f"PAT{random.randint(1, 15000):05}",

        "Provider_ID": provider["Provider_ID"],

        "Department_ID": provider["Department_ID"],

        "Appointment_Date": fake.date_between(
            start_date=date(2018, 1, 1),
            end_date=date(2022, 12, 31)
        ),

        "Appointment_Time": fake.time(
            pattern="%H:%M"
        ),

        "Appointment_Type": random.choice([
            "Consultation",
            "Follow-up",
            "Emergency",
            "Annual Checkup",
            "Lab Visit"
        ]),

        "Status": random.choice([
            "Completed",
            "Cancelled",
            "No Show",
            "Scheduled"
        ])
    }

    appointments.append(appointment)


# ---------------------------------------------------------
# CREATE DATAFRAME
# ---------------------------------------------------------

df = pd.DataFrame(appointments)


# ---------------------------------------------------------
# SAVE OUTPUT
# ---------------------------------------------------------

output_file = os.path.join(
    SOURCE_PATH,
    "Appointments_Source.xlsx"
)

df.to_excel(
    output_file,
    index=False
)


# ---------------------------------------------------------
# OUTPUT MESSAGE
# ---------------------------------------------------------

print("=" * 50)
print("Appointments file generated successfully!")
print(f"Total Records : {len(df)}")
print(f"Output File   : {output_file}")
print(f"Output Path   : {output_file}")
print("=" * 50)