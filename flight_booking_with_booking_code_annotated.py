
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 14:19:27 2025

@author: haojiacheng
"""

# Import required libraries for generating random booking codes
import random
import string

# Apache Airlines Seat Booking System (Extended Version with Booking Code)
# Each seat can have values:
# "F" - Free seat
# "R" - Reserved (replaced with booking code)
# "X" - Aisle
# "S" - Storage

# Define the number of seat rows and columns in the airplane layout
rows = 5
columns = 6
# 2D list representing the seat map: F = Free, X = Aisle, S = Storage
seat_map = [
    ["F", "F", "F", "X", "F", "F"],
    ["F", "F", "F", "X", "S", "S"],
    ["F", "F", "F", "X", "S", "S"],
    ["F", "F", "F", "X", "F", "F"],
    ["F", "F", "F", "X", "F", "F"]
]

# Store seat info and booking code: (row, col) → (name, booking_code)
# Dictionary to store seat bookings with (row, col) as key
passenger_records = {}
# Set to track used booking codes and ensure uniqueness
existing_codes = set()

# Function to generate a unique 8-character booking code
# Function to generate a unique 8-character booking code
def generate_booking_code():
    while True:
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        if code not in existing_codes:
# Set to track used booking codes and ensure uniqueness
            existing_codes.add(code)
            return code

# Display the current seating arrangement with seat statuses
def show_seat_map():
    print("\n--- Current Seat Map ---")
    for i, row in enumerate(seat_map):
        row_display = []
        for j, seat in enumerate(row):
            row_display.append(f"{seat}")
        print(f"Row {i+1}: {' '.join(row_display)}")
    print("------------------------")

# Prompt user for seat row and column, with validation
def get_seat_input():
    try:
        row = int(input("Enter row number (1-5): ")) - 1
        col = int(input("Enter seat column (0-5): "))
        if 0 <= row < rows and 0 <= col < columns:
            return row, col
        else:
            print("Invalid seat location.")
            return None
    except:
        print("Invalid input.")
        return None

# Check whether a specific seat is available or already booked
def check_availability():
    print("\nCheck Seat Availability")
    seat = get_seat_input()
    if seat:
        row, col = seat
        status = seat_map[row][col]
        if status == "F":
            print(" Seat is available.")
        elif status not in ["F", "X", "S"]:
            print(f"Seat is already booked. Code: {status}")
        else:
            print(" This seat is not bookable (X or S).")

# Book a seat: generate booking code and assign to a passenger
def book_seat():
    print("\nBook a Seat")
    seat = get_seat_input()
    if seat:
        row, col = seat
        if seat_map[row][col] == "F":
            passenger_name = input("Enter passenger name: ")
            # Generate a booking code and store it
            booking_code = generate_booking_code()
            seat_map[row][col] = booking_code
# Dictionary to store seat bookings with (row, col) as key
            passenger_records[(row, col)] = (passenger_name, booking_code)
            print(f"Seat booked successfully. Booking code: {booking_code}")
        elif seat_map[row][col] not in ["X", "S"]:
            print("Seat is already booked.")
        else:
            print("⚠️ Cannot book this seat (X or S).")

# Cancel an existing seat booking and free the seat
def free_seat():
    print("\nFree a Seat")
    seat = get_seat_input()
    if seat:
        row, col = seat
        if seat_map[row][col] not in ["F", "X", "S"]:
            code = seat_map[row][col]
            seat_map[row][col] = "F"
# Dictionary to store seat bookings with (row, col) as key
            passenger_records.pop((row, col), None)
# Set to track used booking codes and ensure uniqueness
            existing_codes.discard(code)
            print(f"Booking {code} cancelled.")
        else:
            print("⚠️ This seat is not currently booked.")

# Search for seats booked by a specific passenger name
def search_by_name():
    print("\nSearch Booked Seats by Passenger Name")
    name = input("Enter passenger name to search: ")
    found = False
    for (row, col), (pname, code) in passenger_records.items():
        if pname.lower() == name.lower():
            print(f"Passenger {name} has booking {code} at Row {row+1}, Seat {col}")
            found = True
    if not found:
        print("No bookings found for this passenger.")

# Main program loop to interact with the user via menu
def main():
    while True:
        print("""
Apache Airlines Booking System
1. Check availability of seat
2. Book a seat
3. Free a seat
4. Show booking status
5. Search by passenger name
6. Exit program
""")
        choice = input("Enter your choice (1-6): ")
        if choice == "1":
            check_availability()
        elif choice == "2":
            book_seat()
        elif choice == "3":
            free_seat()
        elif choice == "4":
            show_seat_map()
        elif choice == "5":
            search_by_name()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# Entry point of the program
main()
