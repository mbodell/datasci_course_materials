import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: dna identifier
    # value: dna pairs
    key = record[0]
    value = record[1]
    w = value[:-10]
    mr.emit_intermediate(w, 1)

def reducer(key, list_of_values):
    # key: snipped dna pairs
    # value: number of times it occurs
    mr.emit(key)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
