def bounded_avg(nums):
    """Return avg of nums (makes sure nums are 1-100)
    
    >>> bounded_avg([1,2,3])
    2.0

    >>> bounded_avg([1,3,102])
    Traceback (most recent call last):
    TypeError: Outside bounds of 1-100
    """

    for n in nums:
        if n < 1 or n > 100:
            raise TypeError("Outside bounds of 1-100")

    return sum(nums) / len(nums)

def handle_data():
    """Process data from database"""

    # ages = get_ages(from_my_db)
    # ages = [24,25,26,27,26,24]
    ages = [24,125,26,27,26,24]

    try:
        avg = bounded_avg(ages)
        print("Average was", avg)

    except ValueError as exc:
        # exc is exception object -- you can examine it!
        print("Invalid age in list of ages")
    except TypeError as exc:
        print(f"{exc} is TypeError")