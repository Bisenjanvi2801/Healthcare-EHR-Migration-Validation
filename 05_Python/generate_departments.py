import pandas as pd
import os


# ---------------------------------------------------------
# PROJECT PATH
# ---------------------------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCE_PATH = os.path.join(BASE_DIR, "02_Source_Data")

os.makedirs(SOURCE_PATH, exist_ok=True)


# ---------------------------------------------------------
# DEPARTMENT MASTER DATA
# ---------------------------------------------------------

departments = [
    {"Department_ID": "DEPT001", "Department_Name": "Cardiology"},
    {"Department_ID": "DEPT002", "Department_Name": "Neurology"},
    {"Department_ID": "DEPT003", "Department_Name": "Orthopedics"},
    {"Department_ID": "DEPT004", "Department_Name": "Pediatrics"},
    {"Department_ID": "DEPT005", "Department_Name": "Dermatology"},
    {"Department_ID": "DEPT006", "Department_Name": "Oncology"},
    {"Department_ID": "DEPT007", "Department_Name": "Radiology"},
    {"Department_ID": "DEPT008", "Department_Name": "Emergency"},
    {"Department_ID": "DEPT009", "Department_Name": "ENT"},
    {"Department_ID": "DEPT010", "Department_Name": "Urology"},
    {"Department_ID": "DEPT011", "Department_Name": "Ophthalmology"},
    {"Department_ID": "DEPT012", "Department_Name": "Psychiatry"},
    {"Department_ID": "DEPT013", "Department_Name": "Gynecology"},
    {"Department_ID": "DEPT014", "Department_Name": "Nephrology"},
    {"Department_ID": "DEPT015", "Department_Name": "Pulmonology"},
    {"Department_ID": "DEPT016", "Department_Name": "Endocrinology"},
    {"Department_ID": "DEPT017", "Department_Name": "Gastroenterology"},
    {"Department_ID": "DEPT018", "Department_Name": "Pathology"},
    {"Department_ID": "DEPT019", "Department_Name": "Anesthesiology"},
    {"Department_ID": "DEPT020", "Department_Name": "General Medicine"},
]


# ---------------------------------------------------------
# CREATE DATAFRAME
# ---------------------------------------------------------

df = pd.DataFrame(departments)


# ---------------------------------------------------------
# SAVE OUTPUT
# ---------------------------------------------------------

output_file = os.path.join(
    SOURCE_PATH,
    "Departments_Source.xlsx"
)

df.to_excel(output_file, index=False)


# ---------------------------------------------------------
# OUTPUT MESSAGE
# ---------------------------------------------------------

print("=" * 50)
print("Departments file generated successfully!")
print(f"Total Records : {len(df)}")
print(f"Output File   : {output_file}")
print("=" * 50)