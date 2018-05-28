# contains constants for takuzu function
# author: Cohen Robinson
# created: 29/5/18
# edited:

class Takuzu_Square(object):
    """docstring for Takuzu_Square."""
    def __init__(self, takuzu_list):
        super(Takuzu_Square, self).__init__()
        self.rows = takuzu_list
        self.length = len(takuzu_list)
        self.columns = [takuzu_list[i][j] for i in range(self.length) for j in range(self.length)]

xzy = Takuzu_Square([[1,2], [3, 4]])
print(xzy.rows)
