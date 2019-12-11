"""
http://matplotlib.org/
Color Examples - colormaps_reference 颜色映射
"""
import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x ** 2 for x in x_values]
# plt.scatter(x_values, y_values, c='red', edgecolors='none', s=40)
# plt.scatter(x_values, y_values, c=[(0.5, 0.5, 1)], edgecolors='none', s=40)
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=40)
plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=13)
plt.axis([0, 1100, 0, 1100000])
# plt.show()
plt.savefig('squares_plot.png', bbox_inches='tight')
