# this function determines the validitiy of a given takuzu square
# author: Cohen Robinson
# created: 29/5/18
# edited:

from collections import defaultdict as dd
from class_takuzu import Takuzu_Square

def valid_takuzu(takuzu_list):
    """Determines if a given takuzu_list is valid (or not)."""
    takuzu_list = Takuzu_Square(takuzu_list)
    rows_columns = (takuzu_list.rows, takuzu_list.columns)

    # calculates number of occurances in row and column
    for lists_rc in rows_columns:
        for list_rc in lists_rc:
            rc_occur = dd(int)
            for square in list_rc:
                if square is not None:
                    rc_occur[square] += 1
            if len(set(rc_occur.values())) != 1:
                return False
    # determines if there is more than two consectutive occurances
    for lists_rc in rows_columns:
        for list_rc in lists_rc:
            for n in range(takuzu_list.length):
                square = list_rc[n]
                if takuzu_list.length - n > 2:
                    if list_rc[n] == list_rc[n+1] and list_rc[n] == list_rc[n+2]:
                        return False
    return True


if __name__ =="__main__":

    test_cases = [(False, [[1, 0, None, None],
                          [1, None, 0, 1],
                          [0, 1, 0, None],
                          [None, 1, 1, 0]]),
                  (True, [[0, 1, 0, 1],
                          [1, 0, 1, 0],
                          [1, 1, 0, 0],
                          [0, 0, 1, 1]])]
    n = 1
    for test in test_cases:
        result = valid_takuzu(test[1])
        if result == test[0]:
            outcome = "passed!"
        else:
            outcome = "failed!"
        print("for test_case {} valid_takuzu {}".format(n, outcome))
        print("the output was: {}\n".format(result))
        n += 1
