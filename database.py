# print("This is the database.py module")
# print("It's name is {}".format(__name__))

# import blood_calculator2
# from blood_calculator2 import hdl_analysis
from blood_calculator2 import HDL_Driver

answer = blood_calculator2.hdl_analysis(55)
print("The answer of 55 HDL is {}".format(answer))

answer2 = blood_calculator2.ldl_analysis(200)
