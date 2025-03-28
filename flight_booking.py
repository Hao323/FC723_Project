#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 14:19:27 2025

@author: haojiacheng
"""




# Apache Airlines Seat Booking System (Basic Version)
# This program uses a 2D list to simulate the seat map of a Burak757 airplane.
# Each seat can have the following values:
# "F" - Free seat
# "R" - Reserved/Booked seat
# "X" - Aisle (non-bookable)
# "S" - Storage area (non-bookable)

# Initialize the seat map as a 5x6 grid (rows x columns)
rows = 5
columns = 6
seat_map = [
    ["F", "F", "F", "X", "F", "F"],
    ["F", "F", "F", "X", "S", "S"],
    ["F", "F", "R", "X", "S", "S"],
    ["F", "F", "F", "X", "F", "F"],
    ["F", "F", "F", "X", "F", "F"]
]

# Dictionary to store seat:passenger mapping
passenger_records = {}

# Function to display the current seat map
def show_seat_map():
    print("\n--- Current Seat Map ---")
    for i, row in enumerate(seat_map):
        row_display = []
        for j, seat in enumerate(row):
            row_display.append(f"{seat}")  # Add seat status to display list
        print(f"Row {i+1}: {' '.join(row_display)}")  # Print each row
    print("------------------------")

# Function to get seat input from the user (row and column)
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

# Function to check if a specific seat is available
def check_availability():
    print("\nCheck Seat Availability")
    seat = get_seat_input()
    if seat:
        row, col = seat
        status = seat_map[row][col]
        if status == "F":
            print(" Seat is available.")
        elif status == "R":
            print("Seat is already booked.")
        else:
            print(" This seat is not bookable (X or S).")

# Function to book a seat if it is available
def book_seat():
    print("\nBook a Seat")
    seat = get_seat_input()
    if seat:
        row, col = seat
        if seat_map[row][col] == "F":
            passenger_name = input("Enter passenger name: ")
            seat_map[row][col] = "R"
            passenger_records[(row, col)] = passenger_name
            print(" Seat booked successfully.")
        elif seat_map[row][col] == "R":
            print(" Seat is already booked.")
        else:
            print("Cannot book this seat (X or S).")

# Function to free a seat (cancel a booking)
def free_seat():
    print("\nFree a Seat")
    seat = get_seat_input()
    if seat:
        row, col = seat
        if seat_map[row][col] == "R":
            seat_map[row][col] = "F"
            passenger_records.pop((row, col), None)
            print("Seat booking cancelled.")
        else:
            print("This seat is not currently booked.")

# Function to search seats by passenger name
def search_by_name():
    print("\nSearch Booked Seats by Passenger Name")
    name = input("Enter passenger name to search: ")
    found = False
    for (row, col), pname in passenger_records.items():
        if pname.lower() == name.lower():
            print(f"Passenger {name} has a booking at Row {row+1}, Seat {col}")
            found = True
    if not found:
        print("No bookings found for this passenger.")

# Main program loop
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
            break # Exit the loop and end the program
        else:
            print("Invalid choice. Try again.") # Handle invalid input

# Start the program
main()


