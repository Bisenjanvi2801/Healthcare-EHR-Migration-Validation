-- ============================================
-- 06_Post_Migration_Validation.sql
-- Validate Source vs Target Data
-- ============================================

-- Source Database
USE wellmed_ehr_migration;

SELECT 'Departments' AS Table_Name, COUNT(*) AS Source_Count FROM departments
UNION ALL
SELECT 'Providers', COUNT(*) FROM providers
UNION ALL
SELECT 'Patients', COUNT(*) FROM patients
UNION ALL
SELECT 'Appointments', COUNT(*) FROM appointments
UNION ALL
SELECT 'Encounters', COUNT(*) FROM encounters
UNION ALL
SELECT 'Diagnoses', COUNT(*) FROM diagnoses
UNION ALL
SELECT 'Medications', COUNT(*) FROM medications
UNION ALL
SELECT 'Allergies', COUNT(*) FROM allergies;

-- Target Database
USE welmed_ehr_target;

SELECT 'Departments' AS Table_Name, COUNT(*) AS Target_Count FROM departments
UNION ALL
SELECT 'Providers', COUNT(*) FROM providers
UNION ALL
SELECT 'Patients', COUNT(*) FROM patients
UNION ALL
SELECT 'Appointments', COUNT(*) FROM appointments
UNION ALL
SELECT 'Encounters', COUNT(*) FROM encounters
UNION ALL
SELECT 'Diagnoses', COUNT(*) FROM diagnoses
UNION ALL
SELECT 'Medications', COUNT(*) FROM medications
UNION ALL
SELECT 'Allergies', COUNT(*) FROM allergies;

-- Check for Missing Patients
SELECT COUNT(*) AS Missing_Patients
FROM wellmed_ehr_migration.patients s
LEFT JOIN welmed_ehr_target.patients t
ON s.Patient_ID = t.Patient_ID
WHERE t.Patient_ID IS NULL;

-- Check for Missing Providers
SELECT COUNT(*) AS Missing_Providers
FROM wellmed_ehr_migration.providers s
LEFT JOIN welmed_ehr_target.providers t
ON s.Provider_ID = t.Provider_ID
WHERE t.Provider_ID IS NULL;

-- Check for Missing Departments
SELECT COUNT(*) AS Missing_Departments
FROM wellmed_ehr_migration.departments s
LEFT JOIN welmed_ehr_target.departments t
ON s.Department_ID = t.Department_ID
WHERE t.Department_ID IS NULL;

-- Check for Missing Encounters
SELECT COUNT(*) AS Missing_Encounters
FROM wellmed_ehr_migration.encounters s
LEFT JOIN welmed_ehr_target.encounters t
ON s.Encounter_ID = t.Encounter_ID
WHERE t.Encounter_ID IS NULL;