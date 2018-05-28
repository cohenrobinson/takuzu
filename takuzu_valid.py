# this function determines the validitiy of a given takuzu square
# author: Cohen Robinson
# created: 29/5/18
# edited:

from collections import defaultdict as dd
from common import *

def valid_takuzu(takuzu_list):
    """Determines if a given takuzu_list is valid (or not)."""
    takuzu_list = Takuzu_Square(takuzu_list)
    rows = takuzu_list.rows
    columns = takuzu_list.columns
    row_occur = dd(int)
    column_occur = dd(int)

    # calculates number of occurances in row and
    print(rows)
    for row in rows:
        for square in row:
            row_occur[square] += 1
    print(columns)
    for column in columns:
        for square in column:
            column_occur += 1

    pass



if __name__ =="__main__":

    test_cases = [(True, [[1, 0, None, None],
                          [1, None, 0, 1],
                          [0, 1, 0, None],
                          [None, 1, 1, 0]])]
    n = 1
    for test in test_cases:
        result = valid_takuzu(test[1])
        if result == test[0]:
            outcome = "passed!"
        else:
            outcome = "failed!"
        print("for test_case {} valid_takuzu {} \n".format(n, outcome))
        print("The output was {}".format(result))
