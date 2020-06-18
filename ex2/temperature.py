def is_it_summer_yet(limit, temp_day1, temp_day2, temp_day3):
    """a function that says if the temp of the limit is smaller than at least 2 days in the 3 here"""
    if (limit < temp_day1 and limit < temp_day2) or (limit < temp_day1 and limit < temp_day3) or \
            (limit < temp_day2 and limit < temp_day3):
        return True
    return False
