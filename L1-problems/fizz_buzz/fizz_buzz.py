import typing as tp


def get_fizz_buzz(n: int) -> tp.List[tp.Union[int, str]]:
    """
    If value divided by 3 - "Fizz",
       value divided by 5 - "Buzz",
       value divided by 15 -  "FizzBuzz",
    else - value.
    :param n: size of sequence
    :return: list of values.
    """
    return [
        "FizzBuzz" if x % 15 == 0
        else "Fizz" if x % 3 == 0
        else "Buzz" if x % 5 == 0
        else x for x in range(1, n+1)
    ]
