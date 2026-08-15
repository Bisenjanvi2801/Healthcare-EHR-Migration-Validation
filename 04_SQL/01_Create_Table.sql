CREATE DATABASE wellmed_ehr_migration;

USE wellmed_ehr_migration;

-- ===========================
-- Departments
-- ===========================

CREATE TABLE departments (
    Department_ID VARCHAR(10) PRIMARY KEY,
    Department_Name VARCHAR(100) NOT NULL
);

-- ===========================
-- Providers
-- ===========================

CREATE TABLE providers (
    Provider_ID VARCHAR(10) PRIMARY KEY,
    Provider_Name VARCHAR(100) NOT NULL,
    Specialty VARCHAR(100),
    Phone VARCHAR(15),
    Email VARCHAR(100),
    Experience_Years INT,
    Department_ID VARCHAR(10),
    Status VARCHAR(20),

    FOREIGN KEY (Department_ID)
        REFERENCES departments(Department_ID)
);

-- ===========================
-- Patients
-- ===========================

CREATE TABLE patients (
    Patient_ID VARCHAR(10) PRIMARY KEY,
    MRN VARCHAR(15) UNIQUE,
    First_Name VARCHAR(50),
    Last_Name VARCHAR(50),
    Gender VARCHAR(10),
    Date_of_Birth DATE,
    Age INT,
    Phone VARCHAR(15),
    Email VARCHAR(100),
    Address VARCHAR(255),
    City VARCHAR(50),
    State VARCHAR(50),
    ZIP_Code VARCHAR(10),
    Insurance_Provider VARCHAR(50),
    Blood_Group VARCHAR(10),
    Status VARCHAR(20)
);

-- ===========================
-- Appointments
-- ===========================

CREATE TABLE appointments (
    Appointment_ID VARCHAR(10) PRIMARY KEY,
    Patient_ID VARCHAR(10),
    Provider_ID VARCHAR(10),
    Department_ID VARCHAR(10),
    Appointment_Date DATE,
    Appointment_Time TIME,
    Appointment_Type VARCHAR(50),
    Status VARCHAR(30),

    FOREIGN KEY (Patient_ID)
        REFERENCES patients(Patient_ID),

    FOREIGN KEY (Provider_ID)
        REFERENCES providers(Provider_ID),

    FOREIGN KEY (Department_ID)
        REFERENCES departments(Department_ID)
);

-- ===========================
-- Encounters
-- ===========================

CREATE TABLE encounters (
    Encounter_ID VARCHAR(10) PRIMARY KEY,
    MRN VARCHAR(15),
    Patient_ID VARCHAR(10),
    Provider_ID VARCHAR(10),
    Encounter_Date DATE,
    Diagnosis_Code VARCHAR(20),
    Procedure_Code VARCHAR(20),
    Visit_Reason VARCHAR(100),
    Discharge_Status VARCHAR(50),

    FOREIGN KEY (Patient_ID)
        REFERENCES patients(Patient_ID),

    FOREIGN KEY (Provider_ID)
        REFERENCES providers(Provider_ID)
);

-- ===========================
-- Diagnoses
-- ===========================

CREATE TABLE diagnoses (
    Diagnosis_ID VARCHAR(10) PRIMARY KEY,
    Encounter_ID VARCHAR(10),
    Diagnosis_Code VARCHAR(20),
    Diagnosis_Name VARCHAR(100),
    Diagnosis_Type VARCHAR(30),
    Diagnosis_Status VARCHAR(20),

    FOREIGN KEY (Encounter_ID)
        REFERENCES encounters(Encounter_ID)
);

-- ===========================
-- Medications
-- ===========================

CREATE TABLE medications (
    Medication_ID VARCHAR(10) PRIMARY KEY,
    Encounter_ID VARCHAR(10),
    Medication_Name VARCHAR(100),
    Dosage VARCHAR(50),
    Frequency VARCHAR(50),
    Route VARCHAR(30),
    Start_Date DATE,
    End_Date DATE,

    FOREIGN KEY (Encounter_ID)
        REFERENCES encounters(Encounter_ID)
);

-- ===========================
-- Allergies
-- ===========================

CREATE TABLE allergies (
    Allergy_ID VARCHAR(10) PRIMARY KEY,
    Encounter_ID VARCHAR(10),
    Allergy_Name VARCHAR(100),
    Severity VARCHAR(30),
    Reaction VARCHAR(100),
    Status VARCHAR(20),

    FOREIGN KEY (Encounter_ID)
        REFERENCES encounters(Encounter_ID)
);

SHOW TABLES;