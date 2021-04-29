# 创建时间：2021/2/22 15:51
import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# 设置表格样式为‘seaborn’
plt.style.use('seaborn')

fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# 设置图表标题并给坐标轴上加上标签
ax.set_title('pinching', fontsize=24)
ax.set_xlabel('zhi', fontsize=14)
ax.set_ylabel('Shingling', fontsize=4)

# 设置刻度标记的大小
ax.tick_params(axis='both', labelsize=14)

plt.show()
