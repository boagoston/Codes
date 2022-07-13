# Caio Beraldi Ribeiro - 11683



from table import Table



TableLin = Table(10, "lin")
TableLin.sortedInsert(44, 9)
TableLin.sortedInsert(32, 2)
TableLin.sortedInsert(3, 8)
TableLin.sortedInsert(15, 7)
TableLin.sortedInsert(26, 6)
TableLin.sortedInsert(9, 3)
TableLin.sortedInsert(42, 5)
TableLin.sortedInsert(14, 1)
TableLin.sortedInsert(1, 10)
TableLin.sortedInsert(7, 4)
# TableLin.delete(26)
# print(TableLin)
# TableLin.destroy()
print(TableLin)
TableLin.binarySearch(3)
TableLin.linearRecursionSearch(0, 5)
