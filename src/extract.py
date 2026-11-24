
import pandas as pd
from pathlib import Path

# Define project directories
PROJECT_DIR = Path(__file__).resolve().parent.parent
RAW_DATA_DIR = PROJECT_DIR / "data" / "raw"


def extract_data():
    """Extract patient and encounter data from CSV files."""

    patients_path = RAW_DATA_DIR / "patients.csv"
    encounters_path = RAW_DATA_DIR / "encounters.csv"

    # Read CSV files into Pandas DataFrames
    patients = pd.read_csv(patients_path)
    encounters = pd.read_csv(encounters_path)

    print("Data extraction successful!")
    print("--------------------------------")

    print(f"Number of patients: {len(patients):,}")
    print(f"Number of encounters: {len(encounters):,}")

    print("\nPatient data preview:")
    print(patients.head())

    print("\nEncounter data preview:")
    print(encounters.head())

    print("\nPATIENT DATA INFORMATION")
    print("------------------------")
    print(patients.info())

    print("\nMISSING VALUES IN PATIENT DATA")
    print("------------------------------")
    print(patients.isnull().sum())

    print("\nDUPLICATE PATIENT IDS")
    print("---------------------")
    print(patients["Id"].duplicated().sum())

    print("\nENCOUNTER DATA INFORMATION")
    print("--------------------------")
    print(encounters.info())

    print("\nMISSING VALUES IN ENCOUNTER DATA")
    print("--------------------------------")
    print(encounters.isnull().sum())

    print("\nDUPLICATE ENCOUNTER IDS")
    print("-----------------------")
    print(encounters["Id"].duplicated().sum())

    print("\nPATIENT-ENCOUNTER RELATIONSHIP")
    print("------------------------------")

    print("Unique patients in encounter data:")
    print(encounters["PATIENT"].nunique())

    print("\nEncounters per patient:")
    print(encounters["PATIENT"].value_counts().describe())

    print("\nPatients in encounters missing from patient table:")
    print(
        (~encounters["PATIENT"].isin(patients["Id"])).sum()
    )

    return patients, encounters


if __name__ == "__main__":
    patients, encounters = extract_data()
