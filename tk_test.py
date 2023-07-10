import tkinter as tk
import time
import Yeastar_test

# 创建一个窗口对象
window = tk.Tk()

# 设置窗口标题和大小
window.title("sql_merge")
window.geometry("{}x{}+{}+{}".format(600, 400, 400, 250))

input1 = tk.Text(window, height=8)
input2 = tk.Text(window, height=5)
output = tk.Text(window, height=8)

input1.pack(pady=10)
input2.pack(pady=10)
output.pack(pady=10)

ytt = Yeastar_test.YeastarTestTools()


# 创建一个按钮对象和相应的事件处理函数
def on_click():
    output.delete("1.0", "end")
    sql_str = input1.get("1.0", "end")
    param_str = input2.get("1.0", "end")
    window.update()

    time.sleep(0.5)
    output.insert("end", ytt.sql_string_merge(sql_str, param_str))

def clear_text():
    input1.delete("1.0", "end")
    input2.delete("1.0", "end")
    output.delete("1.0", "end")
    window.update()

button = tk.Button(window, text="合并sql", command=on_click)
button_clear = tk.Button(window, text="清空数据", command=clear_text)

# 将按钮放置在标签下方
button.place(x=450, y=350)
button_clear.place(x=350, y=350)

# 进入主循环，等待事件发生
window.mainloop()
print(123)
print(456)

"""
1. 调整控件位置：
    pack()、place() 和 grid()

2.
    label.config(text="Button clicked!")

3.
    input1 = tk.Entry(window, width=30)
    output = tk.Text(window, height=10)
"""
