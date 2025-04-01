#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 30 23:12:46 2025

@author: haojiacheng
"""

import random
import string

def generate_booking_code(existing_codes=set()):
    """
    Generates a random 8-character booking code using uppercase letters and digits.
    Ensures uniqueness by checking against existing_codes.
    """
    while True:
        # Generate an 8-character code mixing letters and numbers.
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        # If it's a new addition, welcome it into the existing collection and acknowledge its presence.
        if code not in existing_codes:
            existing_codes.add(code)
            return code
