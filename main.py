import sys
from lib import *
from rich import print as rprint

def main():

    try:
        # Get parsed arguments from the args module
        args = parse_args()
        
        # Use the parsed arguments
        day = args.day
        as_example = args.example
        
        if day is not None:
          
          # Run single day
          rprint(f"DAY {day} | ", end="")
          DAY_FUNCTIONS[day](as_example)
          
        else:
          
          # Run all days if no specific day is specified
          for day in DAY_FUNCTIONS:
            rprint(f"DAY {day} | ", end="")
            DAY_FUNCTIONS[day](as_example)
        
        return 0
      
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())