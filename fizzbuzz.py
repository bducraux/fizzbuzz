"""
Fizzbuzz Rules:

- Numbers divisible by three say fizz.
- Numbers divisible by five say buzz.
- Numbers divisible by three and five say fizzbuzz.
- Any other number say the number itself
"""


def get_fizzbuzz(_multiples: dict, exact_number=0, **kwargs):
    """
    :param _multiples: dictionary that contains the multiples and the answer that need to be said on that case
    :param exact_number: optional parameter that will return the answer for this specific number
    :param kwargs: min_range and max_range to be played
    :return: return the answer for the game
    """

    if type(_multiples) is not dict:
        print("Need to pass one dictionary with the multiples")
        return False

    if exact_number != 0:
        min_range = int(exact_number)
        max_range = int(exact_number)+1
    else:
        min_range = kwargs.get('min_range') if 'min_range' in kwargs else 1
        max_range = kwargs.get('max_range') if 'max_range' in kwargs else min_range+1

    _return = ""
    for i in range(min_range, max_range):
        output = ''
        for multiple in _multiples:
            if i%multiple == 0:
                output += _multiples[multiple]
        if output == '':
            output = str(i)
        _return += output

    return _return

if __name__ == '__main__':
    multiples = {3:'Fizz', 5:'Buzz'}
    result = get_fizzbuzz(multiples, 2)

    print(result)
