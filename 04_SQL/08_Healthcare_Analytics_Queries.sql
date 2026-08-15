USE welmed_ehr_target;

-- ==========================================
-- Healthcare Analytics Queries
-- ==========================================

-- 1. Total Patients
SELECT COUNT(*) AS Total_Patients
FROM patients;

-- 2. Total Providers
SELECT COUNT(*) AS Total_Providers
FROM providers;

-- 3. Patients by Gender
SELECT Gender,
COUNT(*) AS Total
FROM patients
GROUP BY Gender;

-- 4. Providers by Specialty
SELECT Specialty,
COUNT(*) AS Total
FROM providers
GROUP BY Specialty
ORDER BY Total DESC;

-- 5. Top 10 Diagnoses
SELECT Diagnosis_Name,
COUNT(*) AS Total
FROM diagnoses
GROUP BY Diagnosis_Name
ORDER BY Total DESC
LIMIT 10;

-- 6. Appointment Status
SELECT Status,
COUNT(*) AS Total
FROM appointments
GROUP BY Status;

-- 7. Discharge Status
SELECT Discharge_Status,
COUNT(*) AS Total
FROM encounters
GROUP BY Discharge_Status;

-- 8. Medication Usage
SELECT Medication_Name,
COUNT(*) AS Total
FROM medications
GROUP BY Medication_Name
ORDER BY Total DESC
LIMIT 10;

-- 9. Allergy Severity
SELECT Severity,
COUNT(*) AS Total
FROM allergies
GROUP BY Severity;

-- 10. Average Patient Age
SELECT ROUND(AVG(Age),2)
AS Average_Age
FROM patients;

-- 11. Oldest Patient
SELECT MAX(Age)
AS Oldest_Patient
FROM patients;

-- 12. Youngest Patient
SELECT MIN(Age)
AS Youngest_Patient
FROM patients;

-- 13. Active Providers
SELECT COUNT(*)
AS Active_Providers
FROM providers
WHERE Status='Active';

-- 14. Inactive Providers
SELECT COUNT(*)
AS Inactive_Providers
FROM providers
WHERE Status='Inactive';

-- 15. Patients by Insurance
SELECT Insurance_Provider,
COUNT(*) AS Total
FROM patients
GROUP BY Insurance_Provider
ORDER BY Total DESC;