import argparse
from itertools import repeat


def merge(*args):
    " Produce an iterable of sorted numbers from iterables passed as arguments "

    iterators = [iter(it) for it in args]
    remaining_iterators_num = len(iterators)
    if not remaining_iterators_num:
        return
    checked_values = []
    while True:
        for i, it in enumerate(iterators):
            try:
                value = next(it)
                if value is not None:
                    checked_values.append(value)
                    if i >= remaining_iterators_num - 1:

                        checked_values.sort()
                        min_value = checked_values.pop(0)
                        yield min_value
            except StopIteration:
                remaining_iterators_num -= 1

                iterators[i] = repeat(None)
                if not remaining_iterators_num:
                    if len(checked_values) > 0:

                        for val in sorted(checked_values):
                            yield val
                    return


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    merge(args)