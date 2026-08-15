CREATE DATABASE welmed_ehr_target;

USE welmed_ehr_target;

CREATE TABLE patients LIKE wellmed_ehr_migration.patients;
CREATE TABLE departments LIKE wellmed_ehr_migration.departments;
CREATE TABLE providers LIKE wellmed_ehr_migration.providers;
CREATE TABLE appointments LIKE wellmed_ehr_migration.appointments;
CREATE TABLE encounters LIKE wellmed_ehr_migration.encounters;
CREATE TABLE diagnoses LIKE wellmed_ehr_migration.diagnoses;
CREATE TABLE medications LIKE wellmed_ehr_migration.medications;
CREATE TABLE allergies LIKE wellmed_ehr_migration.allergies;

SHOW TABLES;