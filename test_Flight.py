import unittest
from unittest.mock import patch
import string

# Import your main flight booking module
import flight_booking

# Create a test class that inherits from unittest.TestCase
class TestFlightBooking(unittest.TestCase):

    # This function runs before each test
    def setUp(self):
        # Reset the seat map to the default layout
        flight_booking.seat_map = [
            ["F", "F", "F", "X", "F", "F"],
            ["F", "F", "F", "X", "S", "S"],
            ["F", "F", "F", "X", "S", "S"],
            ["F", "F", "F", "X", "F", "F"],
            ["F", "F", "F", "X", "F", "F"]
        ]
        # Clear any existing bookings and codes
        flight_booking.passenger_records.clear()
        flight_booking.existing_codes.clear()

        # Create a new in-memory SQLite database for testing
        flight_booking.conn = flight_booking.sqlite3.connect(":memory:")
        flight_booking.cursor = flight_booking.conn.cursor()
        flight_booking.cursor.execute('''
            CREATE TABLE bookings (
                booking_code TEXT PRIMARY KEY,
                passenger_name TEXT,
                passport_number TEXT,
                row INTEGER,
                col INTEGER
            )
        ''')

    # Test if generate_booking_code returns a valid and unique 8-character code
    def test_generate_unique_booking_code(self):
        codes = set()
        for _ in range(100):
            code = flight_booking.generate_booking_code()
            self.assertEqual(len(code), 8)  # Code must be 8 characters
            self.assertTrue(all(c in string.ascii_uppercase + string.digits for c in code))  # Only A-Z, 0-9
            self.assertNotIn(code, codes)  # Code must be unique
            codes.add(code)

    # Test booking a seat with mocked input (row 1, col 0, Alice)
    @patch('builtins.input', side_effect=["1", "0", "Alice", "A12345678"])
    def test_book_seat(self, mock_input):
        flight_booking.book_seat()

        # Check seat status changed from "F" to booking code
        self.assertNotEqual(flight_booking.seat_map[0][0], "F")

        # Check passenger_records contains the booking
        self.assertIn((0, 0), flight_booking.passenger_records)

        # Check data was saved to the database
        flight_booking.cursor.execute("SELECT * FROM bookings")
        row = flight_booking.cursor.fetchone()
        self.assertIsNotNone(row)
        self.assertEqual(row[1], "Alice")  # passenger_name should be Alice

    # Test canceling a seat reservation
    @patch('builtins.input', side_effect=["1", "0", "Bob", "B12345678"])
    def test_free_seat(self, mock_input):
        # First, book a seat
        flight_booking.book_seat()
        booking_code = flight_booking.seat_map[0][0]

        # Then, cancel the same seat
        with patch('builtins.input', side_effect=["1", "0"]):
            flight_booking.free_seat()

        # Check seat is now free
        self.assertEqual(flight_booking.seat_map[0][0], "F")

        # Check passenger record is removed
        self.assertNotIn((0, 0), flight_booking.passenger_records)

        # Check booking code is removed from used codes
        self.assertNotIn(booking_code, flight_booking.existing_codes)

        # Check database no longer has the booking
        flight_booking.cursor.execute("SELECT * FROM bookings WHERE booking_code=?", (booking_code,))
        self.assertIsNone(flight_booking.cursor.fetchone())

    # Test searching for a passenger by name
    def test_search_by_name(self):
        # Add a fake booking manually
        flight_booking.passenger_records[(0, 0)] = ("Charlie", "CODE1234")

        # Simulate searching by name
        with patch('builtins.input', return_value="Charlie"):
            with patch('builtins.print') as mock_print:
                flight_booking.search_by_name()

                # Check that correct message is printed
                mock_print.assert_any_call("Passenger Charlie has booking CODE1234 at Row 1, Seat 0")

    # Test availability checker when seat is free
    def test_check_availability_free(self):
        with patch('builtins.input', side_effect=["1", "0"]):
            with patch('builtins.print') as mock_print:
                flight_booking.check_availability()
                mock_print.assert_any_call(" Seat is available.")

    # Test availability checker when seat is already booked
    def test_check_availability_booked(self):
        # Pretend a booking code is already assigned to seat (0, 0)
        flight_booking.seat_map[0][0] = "ABCD1234"

        with patch('builtins.input', side_effect=["1", "0"]):
            with patch('builtins.print') as mock_print:
                flight_booking.check_availability()
                mock_print.assert_any_call("Seat is already booked. Code: ABCD1234")

# Run the test suite when this file is executed directly
if __name__ == '__main__':
    unittest.main()