import statistics
import matplotlib
import numpy as np
import scipy.stats as stats
from scipy.stats import norm
# imported matplotlib i.e pyplot is a plotting library used for 2D graphics in python programming language.
from matplotlib import pyplot as plt
# We have imported all the required libraries

# Row used to divide them in two classes
# Taking all data inti array and further classifying them
# We tried to separate three sample data as AML and ALL for each data we know

x_ALL = [3016,	3424,	7724,	3821,	5216,	4194,	5528,	2073,	7782,	5204,	6541,	846,	7743,	1756,	7288,	6084,	2455,	1273,   6482,	7629,	5746,	699,   2443,	3840,	3878,	3262,	1810, 	4646,	2141,	3090,	3198,	10565,	5279,	3686,	3619,	5420,	3770,	3972,	2962,	1076,	3102,  6609,	6622,	1438,	2833,	648,	4913]
x_AML = [782,	490,	1648,	528,    99,    1203,	1561,	1628,	1784,	1214,	1583,	1439,	666,     764,   1683,	1629,	469,	420,	1151,	1012,   614,	2284,	1453,	986,	720]
y_ALL = [4778,	2700,	4926,	5403,	3440,	3179,	3978,	3293,	7324,	2676,	6134,	2056,	10669,	1912,	9211,	3345,	2360,	1316,	2492,	6464,	524,    3253,	3796,   4093,	1689,	5204,	2581,  3633,	522,    5358,	1338,	8921,	4174,	6400,	3598,	5600,	7477,	6841,	1814,	1608,	2420,	6203,	9155,	2474,	3375,	2417,	7867]
y_AML = [498,   165,    1309,   852,	1484,	1283,	1525,	811,	1032,	1024,	1827,   1342,	1062,	583,    1451,	626,	851,	751,    528,	754,	456,	836,	1152,	227,	1957]
z_ALL = [1320,	898,	597,	1644,	1322,	787,	946,	1917,	1440,	442,	617,	474,	1969,	686,	2572,	1439,	989,	1186,	1224,	4555,	2707,	274,	590,	1823,	553,	1909,	1076,  1484,	606,	1751,	1052,	2428,	1467,	1479,	2148,	1955,	1275,	980,	1277,	828,    1361,	3923,	1794,	929,	821,	1297,	1087]
z_AML = [299,	389,	126,	190,	275,	353,	279,	250,	381,	671,	200,    139,	388,	110,	197,	282,	196,	268,	461,	446,	375,	528,    253,	450,	328]

# On x axis we have input to  the normalization function of the genes and on y axis we have output
# using data we know we plot the graph separate for each one of ALL and AML
# we need to sort first in order to get graph

x_ALL.sort()

# Formula of mean and standard deviation

x_ALL_mean = np.mean(x_ALL)
x_ALL_std = np.std(x_ALL)
# To plot the graph

pdf_x_ALL = stats.norm.pdf(x_ALL, x_ALL_mean, x_ALL_std)

# Sorting to plot normal distribution

x_AML.sort()
x_AML_mean = np.mean(x_AML)
x_AML_std = np.std(x_AML)
pdf_x_AML = stats.norm.pdf(x_AML, x_AML_mean, x_AML_std)

# plt.plot(x_AML, pdf_x_AML, 'r')

plt.plot(x_ALL, pdf_x_ALL, 'g',  label = 'Graph of ALL set 1')
plt.plot(x_AML, pdf_x_AML, 'r',  label = 'Graph of AML set 1')

# So that label could appear at corner

plt.legend()

variable1 = 1439

# To get desired labels on x anf y axis

plt.xlabel('Input to  the normalization function')
plt.ylabel('Output')

# Formula is used so that we can get y axis of corresponding x value for both ALL AND AML

ll_x_ALL = 1/(x_ALL_std * np.sqrt(2 * np.pi)) * np.exp(-(variable1 - x_ALL_mean)**2 / (2 * x_ALL_std**2))
print("Y coordinate of that corresponds to x_ALL is :", ll_x_ALL)

# input_z_ALL = input("Enter your value of x for which you want to get x: ")

ll_x_AML = 1/(x_AML_std * np.sqrt(2 * np.pi)) * np.exp(-(variable1 - x_AML_mean)**2 / (2 * x_AML_std**2))
print("Y coordinate that corresponds to x_AML is:", ll_x_AML)

# To get the final plot
plt.show()