
# Vehicle Number Plate
vehicle_no = "MH12AB4589"

# Extract parts
state_code = vehicle_no[:2]
district_code = vehicle_no[2:4]
series = vehicle_no[4:6]
vehicle_number = vehicle_no[6:]

# Count letters and digits
letters = sum(ch.isalpha() for ch in vehicle_no)
digits = sum(ch.isdigit() for ch in vehicle_no)

# Validate number plate format
is_valid = (
    len(vehicle_no) == 10 and
    vehicle_no[:2].isalpha() and
    vehicle_no[2:4].isdigit() and
    vehicle_no[4:6].isalpha() and
    vehicle_no[6:].isdigit()
)

# Display results
print("Vehicle Number:", vehicle_no)
print("State Code:", state_code)
print("District Code:", district_code)
print("Series:", series)
print("Vehicle Number:", vehicle_number)

print("\nTotal Letters:", letters)
print("Total Digits:", digits)

if is_valid:
    print("\nVehicle Number Status: Valid")
else:
    print("\nVehicle Number Status: Invalid")