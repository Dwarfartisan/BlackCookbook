# 订餐示例

订餐服务示例演示了如何用 Parsec 和编辑距离算法模拟一个对话服务。程序根据用户的输入找到最接近的
日期、餐次和菜谱。

## 安装和运行

下载 BlackCookbook 项目后，可以在 python/takeout 目录下找到这个项目。

该项目需要预先在python环境中安装 ipython 和 pyparsec 。

IPython 在 pip 中可以找到，pyparsec 暂时只能从 http://github.com/Dwarfartisan/pyparsec
下载后手工部署。该项目的源码在 src/parsec 目录下，引用后的 package 名应该为 parsec 。

用户可以执行
```
    python recipe.py 命令
```

查看程序运行的效果，命令可以是  \[今天|明天|后天\]\[早餐|午餐|晚餐\]菜谱|简称 。

也可以执行

```
    python takeout.py
```

会进入一个 ipython shell ，执行  order("xxx") 可以看到与上例相同的效果。执行 today(),
tommorrow() 或 after_tommorrow() ，可以查看今天、明天、后天的菜单。
