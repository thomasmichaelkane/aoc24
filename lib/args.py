#!/usr/bin/env python3
"""
Command line argument parsing module.

This module handles parsing and validating command line arguments
"""

import argparse

NUMBER_OF_DAYS_ATTEMPTED = 20

def validate_day(value):
    """Validate that the day is between 1 and last day attempted if provided.
    
    Args:
        day: The day number to validate, or None
        
    Returns:
        int or None: The validated day or None
        
    Raises:
        argparse.ArgumentTypeError: If the day is out of range
    """
    if day is None:
        return None
        
    try:
        day = int(day)
        if not 1 <= day <= NUMBER_OF_DAYS_ATTEMPTED:
            raise argparse.ArgumentTypeError(
                f"The day number to run was {day}, the max is {NUMBER_OF_DAYS_ATTEMPTED}."
            )
        return day
    except ValueError:
        raise argparse.ArgumentTypeError(f"Argument '{day}' must be an integer")


def parse_args():
    """Parse and validate command line arguments.

    Returns:
        argparse.Namespace: The parsed command line arguments.
    """
    parser = argparse.ArgumentParser(
        description="Process command line arguments following best practices.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    # Add optional integer argument (1-19)
    parser.add_argument(
        "-d", "--day",
        type=int,
        default=None,
        help="An optional integer between 1 and last day attempted."
    )

    # Add optional flag for as_example
    parser.add_argument(
        "-e", "--example",
        action="store_true",
        default=False,
        help="Set this flag to change to run on example inputs."
    )

    # Parse the arguments
    args = parser.parse_args()

    return args


if __name__ == "__main__":
    # Testing the module directly
    args = parse_args()
    print(f"Parsed arguments: day={args.day}, as_example={args.example}")