from .args import parse_args, NUMBER_OF_DAYS_ATTEMPTED

from .day_one import run as day_one_run
from .day_two import run as day_two_run
from .day_three import run as day_three_run
from .day_four import run as day_four_run
from .day_five import run as day_five_run
from .day_six import run as day_six_run
from .day_seven import run as day_seven_run
from .day_eight import run as day_eight_run
from .day_nine import run as day_nine_run
from .day_ten import run as day_ten_run
from .day_eleven import run as day_eleven_run
from .day_twelve import run as day_twelve_run
# from .day_thirteen import run as day_thirteen_run
# from .day_fourteen import run as day_fourteen_run
# from .day_fifteen import run as day_fifteen_run
# from .day_sixteen import run as day_sixteen_run
# from .day_seventeen import run as day_seventeen_run
# from .day_eighteen import run as day_eighteen_run
# from .day_nineteen import run as day_nineteen_run
# from .day_twenty import run as day_twenty_run
# from .day_twentyone import run as day_twentyone_run
# from .day_twentytwo import run as day_twentytwo_run
# from .day_twentythree import run as day_twentythree_run
# from .day_twentyfour import run as day_twentyfour_run
# from .day_twentyfive import run as day_twentyfive_run

# Map day numbers to functions
DAY_FUNCTIONS = {
  1: day_one_run,
  2: day_two_run,
  3: day_three_run,
  4: day_four_run,
  5: day_five_run,
  6: day_six_run,
  7: day_seven_run,
  8: day_eight_run,
  9: day_nine_run,
  10: day_ten_run,
  11: day_eleven_run,
  12: day_twelve_run,
  # 13: day_thirteen_run,
  # 14: day_fourteen_run,
  # 15: day_fifteen_run,
  # 16: day_sixteen_run,
  # 17: day_seventeen_run,
  # 18: day_eighteen_run,
  # 19: day_nineteen_run,
  # 20: day_twenty_run,
  # 21: day_twentyone_run,
  # 22: day_twentytwo_run,
  # 23: day_twentythree_run,
  # 24: day_twentyfour_run,
  # 25: day_twentyfive_run,
}