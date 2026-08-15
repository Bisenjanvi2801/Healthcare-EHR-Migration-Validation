import subprocess
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

scripts = [
    "generate_departments.py",
    "generate_providers.py",
    "generate_patients.py",
    "generate_appointments.py",
    "generate_encounters.py",
    "generate_diagnoses.py",
    "generate_medications.py",
    "generate_allergies.py"
]

print("=" * 70)
print("      WELLMED EHR MIGRATION - SOURCE DATA GENERATION")
print("=" * 70)

for script in scripts:
    print(f"\nRunning {script}...")
    result = subprocess.run(
        [sys.executable, os.path.join(BASE_DIR, script)]
    )

    if result.returncode == 0:
        print(f"✓ {script} completed successfully.")
    else:
        print(f"✗ Error while running {script}")
        break

print("\n" + "=" * 70)
print("Source Data Generation Completed")
print("=" * 70)
