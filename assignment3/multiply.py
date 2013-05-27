import MapReduce
import sys

"""
Matrix multiply in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

# Hard code dimensions.  A is L by M.  B is M by N. Final answer is L by N.
N = 15
L = 15

def mapper(record):
    # key: matrix
    # row: row index
    # col: col index
    # val: value
    key = record[0]
    row = record[1]
    col = record[2]
    val = record[3]
    if (key == "a"):
        for i in range(N):
            mr.emit_intermediate((row, i), record)
    if (key == "b"):
        for i in range(L):
            mr.emit_intermediate((i, col), record)

def reducer(key, list_of_values):
    # key: (i, j)
    # value: list of records
    total = 0
    for record in list_of_values:
        # key: matrix
        # row: row index
        # col: col index
        # val: value
        keyA = record[0]
        row = record[1]
        col = record[2]
        val = record[3]
        if (keyA == "a"):
            for v in list_of_values:
                k = v[0]
                r = v[1]
                c = v[2]
                valB = v[3]
                if (k == "b"):
                    if(col == r):
                        total += val * valB
    if (total != 0):
        mr.emit((key[0],key[1],total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
