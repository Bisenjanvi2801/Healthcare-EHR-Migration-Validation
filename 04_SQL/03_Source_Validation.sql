USE wellmed_ehr_migration;

-- ============================================
-- SOURCE DATA VALIDATION
-- WellMed EHR Migration Project
-- ============================================

-- ============================================
-- 1. Record Count Validation
-- ============================================

SELECT COUNT(*) AS Patients FROM patients;
SELECT COUNT(*) AS Providers FROM providers;
SELECT COUNT(*) AS Departments FROM departments;
SELECT COUNT(*) AS Appointments FROM appointments;
SELECT COUNT(*) AS Encounters FROM encounters;
SELECT COUNT(*) AS Diagnoses FROM diagnoses;
SELECT COUNT(*) AS Medications FROM medications;
SELECT COUNT(*) AS Allergies FROM allergies;


-- ============================================
-- 2. Duplicate Primary Key Check
-- ============================================

SELECT Patient_ID, COUNT(*)
FROM patients
GROUP BY Patient_ID
HAVING COUNT(*) > 1;

SELECT Provider_ID, COUNT(*)
FROM providers
GROUP BY Provider_ID
HAVING COUNT(*) > 1;

SELECT Department_ID, COUNT(*)
FROM departments
GROUP BY Department_ID
HAVING COUNT(*) > 1;

SELECT Appointment_ID, COUNT(*)
FROM appointments
GROUP BY Appointment_ID
HAVING COUNT(*) > 1;

SELECT Encounter_ID, COUNT(*)
FROM encounters
GROUP BY Encounter_ID
HAVING COUNT(*) > 1;

SELECT Diagnosis_ID, COUNT(*)
FROM diagnoses
GROUP BY Diagnosis_ID
HAVING COUNT(*) > 1;

SELECT Medication_ID, COUNT(*)
FROM medications
GROUP BY Medication_ID
HAVING COUNT(*) > 1;

SELECT Allergy_ID, COUNT(*)
FROM allergies
GROUP BY Allergy_ID
HAVING COUNT(*) > 1;


-- ============================================
-- 3. NULL Value Check
-- ============================================

SELECT *
FROM patients
WHERE Patient_ID IS NULL;

SELECT *
FROM providers
WHERE Provider_ID IS NULL;

SELECT *
FROM departments
WHERE Department_ID IS NULL;

SELECT *
FROM appointments
WHERE Appointment_ID IS NULL;

SELECT *
FROM encounters
WHERE Encounter_ID IS NULL;

SELECT *
FROM diagnoses
WHERE Diagnosis_ID IS NULL;

SELECT *
FROM medications
WHERE Medication_ID IS NULL;

SELECT *
FROM allergies
WHERE Allergy_ID IS NULL;


-- ============================================
-- 4. Referential Integrity Validation
-- ============================================

SELECT COUNT(*) AS Invalid_Appointments
FROM appointments a
LEFT JOIN patients p
ON a.Patient_ID = p.Patient_ID
WHERE p.Patient_ID IS NULL;


SELECT COUNT(*) AS Invalid_Encounters
FROM encounters e
LEFT JOIN appointments a
ON e.Appointment_ID = a.Appointment_ID
WHERE a.Appointment_ID IS NULL;


SELECT COUNT(*) AS Invalid_Diagnoses
FROM diagnoses d
LEFT JOIN encounters e
ON d.Encounter_ID = e.Encounter_ID
WHERE e.Encounter_ID IS NULL;


SELECT COUNT(*) AS Invalid_Medications
FROM medications m
LEFT JOIN encounters e
ON m.Encounter_ID = e.Encounter_ID
WHERE e.Encounter_ID IS NULL;


SELECT COUNT(*) AS Invalid_Allergies
FROM allergies a
LEFT JOIN encounters e
ON a.Encounter_ID = e.Encounter_ID
WHERE e.Encounter_ID IS NULL;


-- ============================================
-- Validation Completed
-- ============================================

SELECT 'Source Data Validation Completed Successfully' AS Status;