# 如何拖动窗口
一些人在开发应用程序时，都会遇到如何拖动窗口，如何贴靠窗口的问题。
其实这都是可以使用`win32`来解决的，你需要先了解什么是[Win32](https://docs.microsoft.com/zh-cn/windows/win32/desktop-programming),
和什么是[hWnd](https://docs.microsoft.com/zh-CN/windows/apps/develop/ui-input/retrieve-hwnd)。才能听懂一下教程，嗯？你说什么，
你要复制粘贴代码？好吧，当我没说过。

--- 

## window_move方法
我们在`tkinterDev`中开发了一个`window_move`的方法，如果你想要快速使用就先来看这里。`window_move`在`tkdev`里面。
如果需要了解这个方法是如何运作的，请看[hWnd概述](http://1688xf.top/course/window_move.html#hwnd)

| 参数名    | 参数类型           | 默认数值 | 介绍          |
|--------|----------------|------|-------------|
| widget | tkinter.Widget | 必填   | 设置用于移动窗口的组件 |
| window | tkinter.Tk     | 必填   | 设置被拖动的窗口    |

```python
from tkdev import DevWindow, window_move
from tkinter import Frame

Root = DevWindow()
TitleBar = Frame(Root, background="#000000")
TitleBar.pack(fill="x", ipady=30)
window_move(TitleBar, Root)
Root.mainloop()
```


## hWnd概述
欸嘿，如果你很懒得话，就直接看着篇就行了。`hWnd`就是窗口的句柄，可以用于获取窗口。
我们需要使用`win32`来进行下一步，所以请看我之前的[安装教程](http://1688xf.top/quickstart.html#id2)


### 获取窗柄
tkinter很容易窗柄获取，`可以直接使用winfo_id()`来获取到ID，之后使用`win32gui.GetParent()`得到窗柄。
但是，直接使用是不行的，我们需要延迟几秒，等待创建窗口完毕，如果使用下面代码控制台输出0，就代表没有获取到`hWnd`，那么请调高after等待的毫秒时间。
```python
from win32gui import GetParent
from tkinter import Tk

Root = Tk()
Root.after(1, lambda: print(GetParent(Root.winfo_id())))
Root.mainloop()
```
我们为了保存参数，定义一个参数来保存窗柄，定义一个函数，来将窗柄设置成窗柄参数
```python
from win32gui import GetParent
from tkinter import Tk

hWnd = 0

def Get_hWnd():
    global hWnd
    hWnd = GetParent(Root.winfo_id())
    print(hWnd)
    
Root = Tk()
Root.after(1, Get_hWnd)
Root.mainloop()
```
现在得到了窗柄，就可以对窗口进行更改了。我们先创建一个事件，为`<B1-Motion>`，在按下左键拖动组件使发送消息，告诉窗口移动。
我们可以使用`pywin32gui.SendMessage()`进行发送。先定义一个组件用于拖动窗口。我这边先用`tkinter.Frame`来充当标题栏。
```python
from win32gui import GetParent, ReleaseCapture, SendMessage
from win32con import WM_SYSCOMMAND, SC_MOVE, HTCAPTION
from tkinter import Tk, Frame

hWnd = 0

def Get_hWnd():
    global hWnd
    hWnd = GetParent(Root.winfo_id())
    
    def Move(Evt=None):
        ReleaseCapture()
        SendMessage(GetParent(Root.winfo_id()), WM_SYSCOMMAND,
                    SC_MOVE + HTCAPTION, 0)
        
    TitleBar.bind("<B1-Motion>", Move)
    
    
Root = Tk()
TitleBar = Frame(Root, background="#000000")
TitleBar.pack(fill="x", ipady=30)
Root.after(1, Get_hWnd)
Root.mainloop()
```
尝试复杂上面代码运行，试试拖动一下黑色框架。