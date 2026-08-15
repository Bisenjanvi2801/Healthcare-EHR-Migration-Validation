-- ============================================
-- 05_Data_Migration.sql
-- Migrate Data from Source to Target
-- ============================================

USE welmed_ehr_target;

-- 1. Departments
INSERT INTO departments
SELECT * FROM wellmed_ehr_migration.departments;

-- 2. Providers
INSERT INTO providers
SELECT * FROM wellmed_ehr_migration.providers;

-- 3. Patients
INSERT INTO patients
SELECT * FROM wellmed_ehr_migration.patients;

-- 4. Appointments
INSERT INTO appointments
SELECT * FROM wellmed_ehr_migration.appointments;

-- 5. Encounters
INSERT INTO encounters
SELECT * FROM wellmed_ehr_migration.encounters;

-- 6. Diagnoses
INSERT INTO diagnoses
SELECT * FROM wellmed_ehr_migration.diagnoses;

-- 7. Medications
INSERT INTO medications
SELECT * FROM wellmed_ehr_migration.medications;

-- 8. Allergies
INSERT INTO allergies
SELECT * FROM wellmed_ehr_migration.allergies;

-- Verify migrated data
SELECT 'Departments' AS Table_Name, COUNT(*) AS Records FROM departments
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