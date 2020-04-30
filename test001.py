from fortranformat import FortranRecordWriter
import FENLIN_format

FileName = "fileOutputTest1.txt"
fileOutputTest1 = open(FileName, "w+")
# val1 = [1.0]
# val2 = [0.0, 0.5]
# val1.extend(val2)
# formatOBJ = FENLIN_format.Formatting()
# print(formatOBJ.formatP)
# fileOutputTest1.write(formatOBJ.formatP.write(val1)+'\n')
# fileOutputTest1.write(header_line1.write(val1)+'\n')
print("HELLO")
header_line1 = FortranRecordWriter("3X,F8.3, 3X,F8.3, 3X,F8.3")
val1 = [1.0]
val2 = [0.0, 0.5]
val1.extend(val2)
fileOutputTest1.write(header_line1.write(val1)+'\n')
header_line2 = FortranRecordWriter("'NUM OF ELEMENTS', \
 I5,/,'NUM OF POINTS', I5")
fileOutputTest1.write(header_line2.write([5, 6])+'\n')
header_line3 = FortranRecordWriter("'ELEMENT MESH COLUMN WIDTHS (left to right):'")
fileOutputTest1.write(header_line3.write([])+'\n')




# print("first x: "+str(x))
# # fileOutputTest1.write("first x: "+str(x)+"\n")
# def function1():
#     global x
#     x = x+1
#     print("function1 x: "+str(x))
#     fileOutputTest1.write("function1 x: "+str(x)+"\n")
#     def function2():
#         global x
#         x = x+1
#         print("function2 x: "+str(x))
#         fileOutputTest1.write("function2 x: "+str(x)+"\n")
#     function2()
#     function3()
#     fileOutputTest1.write("last x: "+str(x)+"\n")
#
#
# def function3():
#     global x
#     x = x+1
#     print("function3 x: "+str(x))
#     fileOutputTest1.write("function3 x: "+str(x)+"\n")
#
# function1()
# print("last x: "+str(x))
# fileOutputTest1.close()
#
# print()