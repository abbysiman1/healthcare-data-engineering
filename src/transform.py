import pandas as pd
from extract import extract_data


def transform_data():
    """Clean and prepare patient and encounter data."""

    patients, encounters = extract_data()

    print("Data transformation started!")
    print("--------------------------------")

    # Convert date columns to datetime
    patients["BIRTHDATE"] = pd.to_datetime(patients["BIRTHDATE"])
    patients["DEATHDATE"] = pd.to_datetime(patients["DEATHDATE"])

    encounters["START"] = pd.to_datetime(encounters["START"])
    encounters["STOP"] = pd.to_datetime(encounters["STOP"])

    print("\nUPDATED DATE COLUMN TYPES")
    print("-------------------------")

    print(patients[["BIRTHDATE", "DEATHDATE"]].dtypes)
    print(encounters[["START", "STOP"]].dtypes)

    # Remove columns that contain no data
    patients = patients.drop(columns=["SUFFIX"])

    print("\nUPDATED PATIENT COLUMNS")
    print("-----------------------")
    print(patients.columns.tolist())

    # Check for completely duplicated records
    print("\nDUPLICATE ROW CHECK")
    print("-------------------")

    print("Duplicate patient rows:", patients.duplicated().sum())
    print("Duplicate encounter rows:", encounters.duplicated().sum())

    # Calculate encounter duration in hours
    encounters["DURATION_HOURS"] = (
        encounters["STOP"] - encounters["START"]
    ).dt.total_seconds() / 3600

    print("\nENCOUNTER DURATION")
    print("------------------")
    print(encounters["DURATION_HOURS"].describe())

    print("\n10 LONGEST ENCOUNTERS")
    print("---------------------")

    print(
        encounters.nlargest(10, "DURATION_HOURS")[
            ["Id", "PATIENT", "START", "STOP", "DURATION_HOURS"]
        ]
    )

    longest_encounter = encounters.loc[
        encounters["DURATION_HOURS"].idxmax()
    ]

    print("\nLONGEST ENCOUNTER DETAILS")
    print("-------------------------")
    print(longest_encounter[
        ["Id", "PATIENT", "START", "STOP", "ENCOUNTERCLASS", "DESCRIPTION", "DURATION_HOURS"]
    ].to_string())

    # Check for negative encounter durations
    negative_durations = encounters[
        encounters["DURATION_HOURS"] < 0
    ]

    print("\nNEGATIVE ENCOUNTER DURATIONS")
    print("----------------------------")
    print("Number of negative durations:", len(negative_durations))
    
    print("\nMISSING VALUES AFTER TRANSFORMATION")
    print("-----------------------------------")

    print("Patient missing values:")
    print(patients.isnull().sum())

    print("\nEncounter missing values:")
    print(encounters.isnull().sum())

    print("\nTRANSFORMATION SUMMARY")
    print("----------------------")
    print(f"Patients: {len(patients):,}")
    print(f"Encounters: {len(encounters):,}")
    print(f"Patient columns: {len(patients.columns)}")
    print(f"Encounter columns: {len(encounters.columns)}")
    
    return patients, encounters


if __name__ == "__main__":
    patients, encounters = transform_data()