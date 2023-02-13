from cProfile import label
from matplotlib import markers
from matplotlib.lines import lineStyles
import matplotlib.pyplot as plt

plt.figure(figsize = (10,6))
#Pais 1
x = [2016, 2017, 2018, 2019, 2020, 2021]
y =[40, 43, 47, 42, 49, 50]
#Pais 2
x2 = [2016, 2017, 2018, 2019, 2020, 2021]
y2 =[43, 43, 45, 46, 49, 57]
plt.plot(x, y, marker = 'o', linestyle = '--', color = 'r', label = "Colombia")
plt.plot(x2, y2, marker = 'o', linestyle = '--', color = 'g', label = "Argentina")
plt.title("Line Time")
plt.xlabel("Años")
plt.ylabel("Población")
plt.legend()
plt.savefig("GraficaPoblacion.png")
plt.show()

#######################################################################################

x = ["Colombia", "Argentina", "Peru"]
y = [40, 50, 30]

plt.bar(x,y)
plt.show()
plt.pie(y, labels=x)
plt.show()

#######################################################################################
