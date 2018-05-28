# contains constants for takuzu function
# author: Cohen Robinson
# created: 29/5/18
# edited:

class Takuzu_Square(object):
    """docstring for Takuzu_Square."""
    def __init__(self, takuzu_list):
        super(Takuzu_Square, self).__init__()
        # rows of board
        self.rows = takuzu_list
        # length of board
        self.length = len(takuzu_list)
        columns = []
        for i in range(self.length):
            column = []
            for j in range(self.length):
                column.append(takuzu_list[j][i])
            columns.append(column)
        # columns of board
        self.columns = columns
