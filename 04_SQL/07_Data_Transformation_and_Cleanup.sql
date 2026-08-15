-- ============================================
-- 07_Data_Transformation_and_Cleanup.sql
-- Data Quality Checks & Cleanup
-- ============================================

USE welmed_ehr_target;

-- 1. Check duplicate Patient IDs
SELECT Patient_ID, COUNT(*) AS Duplicate_Count
FROM patients
GROUP BY Patient_ID
HAVING COUNT(*) > 1;

-- 2. Check duplicate MRNs
SELECT MRN, COUNT(*) AS Duplicate_Count
FROM patients
GROUP BY MRN
HAVING COUNT(*) > 1;

-- 3. Check patients with missing email
SELECT COUNT(*) AS Missing_Email
FROM patients
WHERE Email IS NULL OR Email = '';

-- 4. Check patients with missing phone
SELECT COUNT(*) AS Missing_Phone
FROM patients
WHERE Phone IS NULL OR Phone = '';

-- 5. Check inactive providers
SELECT COUNT(*) AS Inactive_Providers
FROM providers
WHERE Status = 'Inactive';

-- 6. Appointment status distribution
SELECT Status, COUNT(*) AS Total
FROM appointments
GROUP BY Status;

-- 7. Encounter discharge status
SELECT Discharge_Status, COUNT(*) AS Total
FROM encounters
GROUP BY Discharge_Status;

-- 8. Diagnosis type distribution
SELECT Diagnosis_Type, COUNT(*) AS Total
FROM diagnoses
GROUP BY Diagnosis_Type;

-- 9. Medication route distribution
SELECT Route, COUNT(*) AS Total
FROM medications
GROUP BY Route;

-- 10. Allergy severity distribution
SELECT Severity, COUNT(*) AS Total
FROM allergies
GROUP BY Severity;