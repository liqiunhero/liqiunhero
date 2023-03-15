# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import clear_output, display

# 生成数据
x = np.arange(100).reshape(100, 1)
# 按照y = 10x + 100 生成数据， 并且数据会上下100随机误差
y = 10 * x + 100  + np.random.randint(-100, 100, size=(100, 1))
# 初始化 h = ax + b, a=0, b=0
# 假设函数 h = ax + b
# 初始化参数, 这里都设置为0, 也能设置两个随机数
a = 0
b = 0
learning_rate = 0.00001 # 学习率
while True:
    a_spread = np.mean((a*x+b-y)*x)
    b_spread = np.mean(a*x+b-y)
    a = a - a_spread * learning_rate
    b = b - b_spread * learning_rate
    # 画出函数图像
    _x = np.linspace(x[0], x[-1], 100*len(x))
    _y = _x * a + b
    # 这里可以每隔一定次数在画出图像, 因为b参数会变化很慢
    # plt.pause(0.01)
    plt.clf()  # 清除打印信息
    plt.ylim(0, 1300)  # 控制y轴显示范围
    plt.xlim(0, 200)  # 控制x轴显示范围
    plt.scatter(x, y, s=5)  # 画出散点图
    plt.plot(_x, _y, color='red', linewidth=2.0, linestyle='--')  # 画出假设函数h图像
    # plt.annotate(  # 显示一个文本框指向最后一个数据
       # s=f"{a=:.2f} {b=:.2f}",  # 文本内容
       # xy=(_x[-1], _y[-1]),  # 箭头点所在坐标
       # xytext=(_x[-1]+10, _y[-1]-100),  # 文本内容所在坐标
      #  weight='bold',  # 字体线型
       # color='aqua',  # 字体颜色
       # arrowprops=dict(arrowstyle='-|>', connectionstyle='arc3', color='red'),
      #  bbox=dict(boxstyle='round,pad=0.5', fc='yellow', ec='k',lw=1 ,alpha=0.4)
  #  )
    plt.pause(0.01)
    if abs(a_spread) <= 0.1 and abs(b_spread) <= 0.1:
        plt.savefig('result.png', bbox_inches='tight', pad_inches=0)  # 保存结果
        plt.close()
        break
