heart_rate = {
    "P101": 72,
    "P102": 105,
    "P103": 88,
    "P104": 120,
    "P105": 65,
    "P106": 98,
    "P107": 110,
    "P108": 70,
    "P109": 85,
    "P110": 130
}

# 1. Critical patients (heart rate > 100)
critical_patients = [patient for patient, rate in heart_rate.items() if rate > 100]

# 2. Highest and lowest heart rate
highest_patient = max(heart_rate, key=heart_rate.get)
lowest_patient = min(heart_rate, key=heart_rate.get)

# 3. Average heart rate
average_rate = sum(heart_rate.values()) / len(heart_rate)

# 4. Count stable patients (60–100 bpm)
stable_count = sum(1 for rate in heart_rate.values() if 60 <= rate <= 100)

# Display results
print("Critical Patients:")
for patient in critical_patients:
    print(patient)

print("\nHighest Heart Rate:")
print(f"{highest_patient} ({heart_rate[highest_patient]} bpm)")

print("\nLowest Heart Rate:")
print(f"{lowest_patient} ({heart_rate[lowest_patient]} bpm)")

print(f"\nAverage Heart Rate: {average_rate:.1f} bpm")

print(f"\nStable Patients: {stable_count}")
