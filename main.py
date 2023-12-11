#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# main.py
from car.calliope import Calliope
from car.glissade import Glissade
from car.palindrome import Palindrome
from car.rorschach import Rorschach
from car.thovex import Thovex

def main():
    # Example usage
    calliope_car = Calliope()
    glissade_car = Glissade()
    palindrome_car = Palindrome()
    rorschach_car = Rorschach()
    thovex_car = Thovex()

    # Check if cars need service
    for car in [calliope_car, glissade_car, palindrome_car, rorschach_car, thovex_car]:
        if car.needs_service(mileage=2000, years=2):
            print(f"The {car.__class__.__name__} car needs service.")
        else:
            print(f"The {car.__class__.__name__} car is in good condition.")

if __name__ == "__main__":
    main()
