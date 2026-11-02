# Python 核心语法与时空数据分析 · 讲义

> 本讲义由交互网页《Python 核心语法档案 · 1 小时速成》整理而成。网页里的全部 Python 代码已逐段在标准 CPython 中运行校验,错误之处已修改;每段代码下方的「运行结果」都是真实运行输出,不是手写的。修改明细见文末附录。

## 使用说明

**运行环境**

- Python 3.10 及以上(本讲义在 Python 3.13 上逐段验证)。
- 第 L18 关用到 numpy 与 pandas:`pip install numpy pandas`。其余各关只用标准库。
- 从 L13 起,不少代码会用到内置数据集 `dataset`(56 个城市、50 个监测站、20 个省级区域、3 条气温序列、12×12 网格)。请把随讲义附带的 **dataset.py** 放在代码同一个文件夹,代码开头的 `from dataset import dataset` 就能直接用。

**怎么读**

1. 每关依次是:导语 → 讲解与示例 → 本关完整示例 → 动手练习 → 随堂检测。
2. 带 `input()` 的代码,运行结果里已模拟了键盘输入(输入值紧跟在提示语后面)。
3. 同一关里的代码按顺序运行(例如 L08 前一段写的文件,后一段会读到)。
4. 随堂检测的答案收在每题下方的「答案与解析」里,先自己做再展开。

**网格方向约定**(L35、L37、L38):`dataset.pm_grid["values"][0]` 是最南边一行(从 latMin 开始),行号越大越往北,列号越大越往东。

## 目录

| 编号 | 标题 | 分组 | 建议用时 |
|---|---|---|---|
| L01 | Python 是什么 & 第一个程序 | 起步 | 4 分钟 |
| L02 | 变量、数据类型与类型转换 | 起步 | 6 分钟 |
| L03 | 字符串与 f-string 拼接 | 起步 | 5 分钟 |
| L04 | 条件判断 if / elif / else | 起步 | 6 分钟 |
| L05 | 循环 for 与 while | 流程与函数 | 7 分钟 |
| L06 | 函数:把代码打包复用 | 流程与函数 | 7 分钟 |
| L07 | 列表与字典:装数据的两个容器 | 流程与函数 | 8 分钟 |
| L08 | 文件读写:让数据留下来 | 进阶技巧 | 5 分钟 |
| L09 | 模块与导入:站在别人的肩膀上 | 进阶技巧 | 4 分钟 |
| L10 | 类与对象:把数据和动作包在一起 | 进阶技巧 | 8 分钟 |
| L11 | 错误处理 try / except | 进阶技巧 | 5 分钟 |
| L12 | 综合实战:一个完整的小程序 | 进阶技巧 | 8 分钟 |
| L13 | 运算符与类型转换:%、//、\*\* 与 int/float/str | 语言补强 | 9 分钟 |
| L14 | 元组与坐标点:把一对数值捆在一起 | 语言补强 | 9 分钟 |
| L15 | 迭代与算法思维:累加器、最值、线性搜索 | 语言补强 | 10 分钟 |
| L16 | 调试与常见错误:看懂报错、定位问题 | 语言补强 | 9 分钟 |
| L17 | 日期时间与集合:给数据装上时间轴 | 语言补强 | 10 分钟 |
| L18 | 数组与表格:数据一多,循环就不够用了 | 第二层 · 数据与统计 | 9 分钟 |
| L22 | 时间序列:趋势、季节性与滑动平均 | 第二层 · 数据与统计 | 12 分钟 |
| L24 | 时间序列预测:最简单的三种方法 | 第二层 · 数据与统计 | 12 分钟 |
| L23 | 线性回归:用一条直线做预测 | 第二层 · 预测:回归 | 11 分钟 |
| L26 | k 近邻分类:看看邻居是谁 | 第二层 · 预测:分类 | 11 分钟 |
| L28 | 分类的评估:混淆矩阵与精确率/召回率 | 第二层 · 分类评估 | 12 分钟 |
| L29 | 聚类入门:k-means 怎么把点分成几堆 | 第二层 · 聚类 | 13 分钟 |
| L30 | 聚类进阶:怎么决定分几类 + DBSCAN | 第二层 · 聚类 | 14 分钟 |
| L31 | 空间数据的第一件事:坐标系与距离 | 第二层 · 空间分析 | 13 分钟 |
| L33 | 空间关系:包围盒、缓冲区与空间连接 | 第二层 · 空间分析 | 13 分钟 |
| L35 | 空间自相关:莫兰指数与热点识别 | 第二层 · 空间分析 | 15 分钟 |
| L32 | 轨迹数据:两点之间怎么算「走得快不快」 | 第二层 · 时空分析 | 12 分钟 |
| L37 | 时空立方体:把「哪里」和「何时」拼在一起 | 第二层 · 时空分析 | 13 分钟 |
| L38 | 综合项目:一份小型时空分析报告 | 第二层 · 综合项目 | 15 分钟 |

> 编号沿用原网页(原网页的编号本身不连续,L19–L21、L27、L34、L36 不存在;原 L25 与 L37 内容重复,已合并到 L37)。


---

# 起步

## L01 · Python 是什么 & 第一个程序

> 关键词:零基础 · 环境 · print | 建议用时 4 分钟

Python 是一种**用接近英文的语法**指挥计算机做事的语言。它的最大特点是:**代码短、读起来像句子**。

本讲义的每一段代码都在标准 **Python 3**(3.10 及以上)里实际运行过,代码下方附有**真实运行结果**。建议边读边把代码粘到自己的编辑器(VS Code / PyCharm / Jupyter)里运行。

先看一个最小的程序。它的意思是「把引号里的内容打印到屏幕上」:

```python
print("Hello, Python!")
```

运行结果:

```text
Hello, Python!
```

> **【要点】三个必须记住的点**
>
> - `print(...)` 是「输出」,括号里放什么就显示什么。
> - 文字(字符串)必须用**引号**包起来:单引号 `'abc'` 和双引号 `"abc"` 都行,但左右要配对。
> - Python **对大小写敏感**:`Print` 不是 `print`,写错会报 NameError。

> **【注意】新手第一大坑:缩进和冒号**
>
> Python 用**缩进**(行首的空格)来表示代码的层级,而不是用大括号。后面每遇到 `if` `for` `def` 这类语句,行尾必须有一个**英文冒号** `:`,下一行必须**向右缩进 4 个空格**。这是全课程最需要形成肌肉记忆的一点。

再看一个能和你对话的程序。`input()` 负责「读入你输入的内容」:

```python
name = input("你叫什么名字?")
print("你好," + name + "!")
```

运行结果:

```text
你叫什么名字?小明
你好,小明!
```

> **【提示】怎么学最快**
>
> - 读完讲解后,把代码复制到自己的编辑器里运行,再动手改一改 —— 光看不练记不住。
> - 先自己预测输出,再对照代码下方的「运行结果」。
> - 每关末尾的**随堂检测**先独立作答,再看答案与解析 —— 做错不要紧,解析会告诉你为什么错。

### 本关完整示例

```python
print("Hello, Python!")
print("我正在 1 小时速成 Python")

name = input("你叫什么名字? ")
print("你好," + name + "!")
print("这是我写的第", 3, "行输出")
```

运行结果(运行时依次输入:小明):

```text
Hello, Python!
我正在 1 小时速成 Python
你叫什么名字? 小明
你好,小明!
这是我写的第 3 行输出
```

### 动手练习

1. 把第一行的 Hello 改成你自己的名字,重新运行。
2. 再加一行 print,输出你今天的心情。
3. 故意删掉一个引号,看看报错长什么样 —— 认识报错比背语法重要。

### 随堂检测

**1. 下面哪一行能正确输出 Hello?**

- A. `print "Hello"`
- B. `Print("Hello")`
- C. `print("Hello")`
- D. echo Hello

<details><summary>答案与解析</summary>

**答案:C**。print 必须小写,参数必须放在英文括号里。Print(大写)会报 NameError;print "Hello" 在 Python 3 里是语法错误;echo 是 shell 命令。

</details>

**2. input() 拿到的东西是什么类型?**

- A. 自动变成数字
- B. 布尔值
- C. 列表
- D. 永远是字符串 str

<details><summary>答案与解析</summary>

**答案:D**。input() 永远返回字符串。要当数字用必须 int(input(...)) 或 float(input(...)) 转换 —— 这是第 02 关的重点。

</details>

## L02 · 变量、数据类型与类型转换

> 关键词:核心中的核心 | 建议用时 6 分钟

变量就是**给一个值起个名字**,方便后面反复使用。用等号 `=` 赋值(注意:等号在 Python 里是「赋值」,不是数学里的「相等」)。

Python 是**动态类型**语言:同一个变量可以先装数字、再装文字,类型跟着值走,不用提前声明。

```python
age = 18            # int 整数
price = 9.9         # float 小数
name = "小明"       # str 字符串
is_student = True   # bool 布尔(只有 True / False)
nothing = None      # NoneType 空值
```

| 类型 | 含义 | 例子 | 常用转换 |
|---|---|---|---|
| int | 整数 | `1、-5、100` | `int("18") → 18` |
| float | 小数 | `3.14、2.0` | `float("3.14") → 3.14` |
| str | 文本 | "你好" | `str(18) → "18"` |
| bool | 真假 | `True / False` | `bool(0) → False` |
| NoneType | 空值 | None | 表示「什么都没有」 |

> **【注意】类型转换:新手第二大坑**
>
> 输入进来的东西**永远是字符串**。如果你想做加法,必须先转成数字,否则 `"18" + "1"` 会得到 `"181"`(字符串拼接),而不是 19。而把字符串和数字直接相加(比如 `"18"` + 1)会报 **TypeError** —— 这是新手最常见的报错之一。

```python
a = input("第一个数: ")
b = input("第二个数: ")
print(a + b)                 # 结果是拼接!比如 1 和 2 得到 12
print(int(a) + int(b))       # 正确:转成整数再相加 = 3
```

运行结果:

```text
第一个数: 1
第二个数: 2
12
3
```

用 `type()` 可以随时查看一个值的类型,这是排错利器:

```python
print(type(18))       # <class 'int'>
print(type("18"))     # <class 'str'>
print(type(18.0))     # <class 'float'>
```

运行结果:

```text
<class 'int'>
<class 'str'>
<class 'float'>
```

> **【规范】命名规范(现在养成,受益终身)**
>
> - 变量名用小写字母 + 下划线:`user_name`、`total_price`。
> - 不能以数字开头,不能有空格,不能用 Python 关键字(如 `if`、`for`)。
> - 名字要能表达意思 —— `a1` 不如 `score`。

### 本关完整示例

```python
# Python 是动态类型:同一个变量可以先装数字,再装文字
a = 18
print(a, type(a))          # int 整数
a = "18"
print(a, type(a))          # str 字符串
a = 18.5
print(a, type(a))          # float 小数
a = True
print(a, type(a))          # bool 布尔

b = "18"
print(b + "1")             # 字符串 + 字符串 = 拼接
print(int(b) + 1)          # 转成整数才是加法
print(float(b) + 0.5)
print(f"18 的平方是 {18 ** 2}")
```

运行结果(运行时依次输入:1、2):

```text
18 <class 'int'>
18 <class 'str'>
18.5 <class 'float'>
True <class 'bool'>
181
19
18.5
18 的平方是 324
```

### 补充示例

```python
a = input("第一个数: ")
b = input("第二个数: ")
print("直接相加:", a + b)
print("转成整数后相加:", int(a) + int(b))

price = float("9.9")
count = 3
print("总价:", price * count)          # 浮点误差:9.9 * 3 不是精确的 29.7
print("保留两位:", round(price * count, 2))
print("类型:", type(price), type(count))
```

运行结果(运行时依次输入:1、2):

```text
第一个数: 1
第二个数: 2
直接相加: 12
转成整数后相加: 3
总价: 29.700000000000003
保留两位: 29.7
类型: <class 'float'> <class 'int'>
```

### 动手练习

1. 把 int(a) + int(b) 改成 float(a) + float(b),输入 1.5 和 2 试试。
2. 新建变量 city 存你的城市,再打印 "我住在" + city。
3. 用 type() 打印 city 的类型。

### 随堂检测

**1. 执行 print("3" + "4") 的结果是?**

- A. 7
- B. `"34"`
- C. 34
- D. 报错

<details><summary>答案与解析</summary>

**答案:C**。两边都是字符串,+ 就变成拼接,得到 "34"。想得到 7 必须 int("3") + int("4")。

</details>

**2. int("3.5") 会怎样?**

- A. 报 ValueError
- B. 得到 3
- C. 得到 3.5
- D. 得到 "3.5"

<details><summary>答案与解析</summary>

**答案:A**。int() 只接受纯整数字符串。"3.5" 要先 float("3.5") 再 int(...),也就是 int(float("3.5"))。

</details>

**3. 下面哪个变量名不合法?**

- A. total2
- B. user\_name
- C. 2name
- D. \_count

<details><summary>答案与解析</summary>

**答案:C**。变量名不能以数字开头。其余三个都合法。

</details>

## L03 · 字符串与 f-string 拼接

> 关键词:天天都要用 | 建议用时 5 分钟

程序里出现最多的数据类型就是字符串。学会**拼字符串**和**取子串**,你就能立刻写出有用的小工具。

Python 推荐的拼接方式是 **f-string**:在引号前加一个 `f`,然后在里面用 `{}` 直接嵌入变量。

```python
name = "小明"
age = 18

# 老办法:用 + 拼,必须手动 str() 转换,又长又容易错
print("我叫" + name + ",今年" + str(age) + "岁")

# 推荐:f-string,变量直接放进 {} 里
print(f"我叫{name},今年{age}岁")
print(f"明年我就 {age + 1} 岁了")     # {} 里可以写表达式
```

运行结果:

```text
我叫小明,今年18岁
我叫小明,今年18岁
明年我就 19 岁了
```

> **【要点】f-string 记住三件事**
>
> - 引号前面要有 `f`:`f"..."`,没有 f 就不会替换。
> - `{}` 里可以直接写变量名,也可以写运算,如 `{price * 0.8}`。
> - 格式化小数:`{pi:.2f}` 保留两位小数,`{n:>5}` 右对齐宽度 5。

字符串还可以像「一串珠子」那样**按位置取**。位置叫**下标**,从 **0** 开始数;负数表示从后往前数(-1 是最后一个):

```python
s = "Python"
print(s[0])      # P   第一个
print(s[-1])     # n   最后一个
print(s[0:3])    # Pyt 切片:从 0 取到 3(不含 3)
print(s[2:])     # thon 从 2 取到结尾
print(len(s))    # 6   长度
```

运行结果:

```text
P
n
Pyt
thon
6
```

| 操作 | 写法 | 结果 |
|---|---|---|
| 转大写 | `s.upper()` | `"PYTHON"` |
| 去首尾空格 | `" hi ".strip()` | `"hi"` |
| 替换 | `s.replace("P","J")` | `"Jython"` |
| 按空格切分 | `"a b c".split()` | `['a','b','c']` |
| 拼接列表 | `"".join(["a","b"])` | `"ab"` |
| 是否以…开头 | `s.startswith("Py")` | True |

> **【注意】字符串是不可变的**
>
> 不能写 `s[0] = "J"` —— 会报 TypeError。所有「修改」其实是**生成一个新字符串**,所以要写成 `s = s.replace(...)`,把结果重新赋给变量。

### 本关完整示例

```python
name = "小明"
age = 18
score = 95.678

print(f"我叫{name},今年{age}岁")
print(f"明年 {age + 1} 岁")
print(f"成绩:{score:.2f} 分")     # 保留两位小数

s = "Python"
print("首字母:", s[0], "| 末字母:", s[-1])
print("前三个:", s[0:3], "| 长度:", len(s))
print("大写:", s.upper())
print("替换:", s.replace("P", "J"))
print("切分:", "苹果 香蕉 橘子".split())
```

运行结果:

```text
我叫小明,今年18岁
明年 19 岁
成绩:95.68 分
首字母: P | 末字母: n
前三个: Pyt | 长度: 6
大写: PYTHON
替换: Jython
切分: ['苹果', '香蕉', '橘子']
```

### 动手练习

1. 定义一个变量 city,用 f-string 输出 "我在{city}学 Python"。
2. 用 .split() 把 "1,2,3" 切成列表(提示:写 .split(","))。
3. 把 score 改成一位小数输出(提示::.1f)。

### 随堂检测

**1. print(f"{1 + 2}") 输出什么?**

- A. 报错
- B. `1 + 2`
- C. 3
- D. `{1 + 2}`

<details><summary>答案与解析</summary>

**答案:C**。f-string 的花括号里可以写任意表达式,会先算出结果再插进字符串,所以输出 3。

</details>

**2. "abcdef"[1:4] 的结果是?**

- A. bcd
- B. bcde
- C. abcd
- D. cde

<details><summary>答案与解析</summary>

**答案:A**。切片含头不含尾:下标 1、2、3 三个字符,即 bcd。记住口诀「包头不包尾」。

</details>

**3. 字符串能否用 s[0] = "X" 修改?**

- A. 不能,字符串不可变
- B. 要看长度
- C. 只有第一个字符能改
- D. 能

<details><summary>答案与解析</summary>

**答案:A**。字符串是不可变对象。要「改」只能生成新字符串:s = "X" + s[1:]。

</details>

## L04 · 条件判断 if / elif / else

> 关键词:让程序会思考 | 建议用时 6 分钟

条件判断让程序**分岔**:满足条件走一条路,不满足走另一条。

写法:`if` 条件**冒号** + 缩进代码块。`elif` 是「否则如果」,`else` 是「剩下所有情况」。

```python
score = 85

if score >= 90:
    print("优秀")
elif score >= 60:
    print("及格")
else:
    print("不及格")
```

运行结果:

```text
及格
```

> **【图示】执行规则:从上到下,命中即止**
>
> Python 会从第一个 `if` 开始依次检查,**只要有一个条件成立,执行完对应的代码块就跳出整条链**,后面的 elif/else 全部跳过。所以条件的**顺序很重要**。

> **【注意】如果把顺序写反了**
>
> 若先写 `if` score >= 60,那么 95 分会先命中「及格」而永远不会走到「优秀」。**范围窄的条件要写在前面**。

| 比较运算符 | 含义 |
|---|---|
| `==` | 相等(两个等号!一个等号是赋值) |
| `!=` | 不相等 |
| >=  <= | 大于 / 小于 / 大于等于 / 小于等于 |
| `in / not in` | 是否包含,如 "a" in "cat" |
| `is / is not` | 是否是同一个对象(新手少用) |

| 逻辑运算符 | 含义 | 例子 |
|---|---|---|
| and | 两个都真才真 | `score >= 60 and age >= 18` |
| or | 有一个真就真 | day == "六" or day == "日" |
| not | 取反 | not is\_raining |

> **【说明】真假的规则(真值判断)**
>
> - 假的值:`False`、`0`、`0.0`、`""`(空字符串)、`[]`(空列表)、`{}`(空字典)、`None`。
> - 其他都是真。所以 `if` 列表名: 就是判断「列表非空」的惯用写法。
> - 常见错误:`if` x == 1 or 2: 这里的 `2` 会被当成独立条件,永远为真。要写 `x == 1 or x == 2`。

### 本关完整示例

```python
score = 85

if score >= 90:
    print("优秀")
elif score >= 60:
    print("及格,继续加油")
else:
    print("不及格,要补考")

# 组合条件
age = 20
has_card = True
if age >= 18 and has_card:
    print("可以进入")
else:
    print("不能进入")

# 真值判断:空列表为假
cart = []
if cart:
    print("购物车非空")
else:
    print("购物车是空的")
```

运行结果:

```text
及格,继续加油
可以进入
购物车是空的
```

### 动手练习

1. 把 score 改成 95,看输出是否变成"优秀"。
2. 把 score 改成 59,再试一次。
3. 加一个判断:如果 score 是 100,输出"满分!"(提示:放在第一个 if 前面,或者写成 >= 100)。

### 随堂检测

**1. 下面哪一行语法正确?**

- A. `if x > 5`
- B. `if x > 5 then:`
- C. `if (x > 5)`
- D. `if x > 5:`

<details><summary>答案与解析</summary>

**答案:D**。条件后面必须有英文冒号,下一行必须缩进。括号不是必需的;then 是其他语言的写法。

</details>

**2. score = 95 时,先判断 if score >= 60 再 elif score >= 90,会输出什么?**

- A. "及格"(永远到不了优秀)
- B. "优秀"
- C. 两个都输出
- D. 报错

<details><summary>答案与解析</summary>

**答案:A**。从上到下命中即止。95 先满足 >= 60,后面的 elif 直接被跳过 —— 所以范围窄的条件要写前面。

</details>

**3. if []: 会执行哪个分支?**

- A. else 分支
- B. 都不执行
- C. 报错
- D. if 分支

<details><summary>答案与解析</summary>

**答案:A**。空列表是「假值」,所以走 else。这是判断容器是否为空的惯用写法。

</details>


---

# 流程与函数

## L05 · 循环 for 与 while

> 关键词:让程序重复干活 | 建议用时 7 分钟

循环让程序**把同一件事做很多遍**。这是计算机最擅长的事,也是「自动化」的起点。

`for` 用于「遍历一个序列里的每个元素」;`while` 用于「条件成立就一直做」。

```python
# for + range:重复固定次数
for i in range(5):        # i = 0,1,2,3,4(注意:不含 5)
    print(i)

# 遍历列表的每个元素
fruits = ["苹果", "香蕉", "橘子"]
for f in fruits:
    print(f"我喜欢{f}")
```

运行结果:

```text
0
1
2
3
4
我喜欢苹果
我喜欢香蕉
我喜欢橘子
```

> **【说明】range 的三种写法**
>
> - `range(5)` → 0,1,2,3,4(从 0 开始,**不含**结尾)
> - `range(1, 6)` → 1,2,3,4,5(从 1 开始,不含 6)
> - `range(0, 10, 2)` → 0,2,4,6,8(第三个参数是步长)

```python
# while:条件为真就一直做(适合"不知道要做几次"的场景)
count = 3
while count > 0:
    print(f"倒计时 {count}")
    count = count - 1          # * 必须有这一行,否则死循环!
print("发射!")
```

运行结果:

```text
倒计时 3
倒计时 2
倒计时 1
发射!
```

> **【注意】死循环:新手最常踩的坑**
>
> `while` 循环体里**必须**有让条件最终变成 False 的操作。忘了 `count = count - 1`,程序就会永远跑下去。真实 Python 不会替你停下来,程序会一直跑;这时按 **Ctrl + C** 强行中断(Jupyter 里点「中断内核」)。

| 关键字 | 作用 |
|---|---|
| break | 立即跳出整个循环 |
| continue | 跳过本次剩余代码,直接进入下一次循环 |
| else | 循环正常结束(没被 break)时执行,很少用 |
| enumerate | 同时拿到下标和值:for i, x in enumerate(list) |

```python
for i in range(1, 11):
    if i == 5:
        break            # 到 5 就停,后面 6~10 不再执行
    if i % 2 == 0:
        continue         # 偶数跳过,不打印
    print(i)             # 输出 1 3
```

运行结果:

```text
1
3
```

> **【说明】什么时候用 for,什么时候用 while**
>
> - 知道要做几次 / 要遍历一堆东西 → 用 **for**(90% 的情况)。
> - 不知道要几次,只知道「做到某个条件为止」→ 用 **while**(如:让用户输密码直到正确)。

循环最经典的用法:**累加**。先准备一个「容器变量」,再在循环里不断更新它:

```python
total = 0
for n in [85, 92, 78, 96]:
    total = total + n        # 累加
print(f"总分 {total},平均 {total / 4}")
```

运行结果:

```text
总分 351,平均 87.75
```

### 本关完整示例

```python
# 1) 数数
for i in range(1, 6):
    print(f"第 {i} 次")

# 2) 累加求和
total = 0
scores = [85, 92, 78, 96]
for s in scores:
    total = total + s
print(f"总分:{total},平均:{total / len(scores):.1f}")

# 3) while 倒计时
count = 3
while count > 0:
    print(f"倒计时 {count}")
    count = count - 1
print("发射!")
```

运行结果:

```text
第 1 次
第 2 次
第 3 次
第 4 次
第 5 次
总分:351,平均:87.8
倒计时 3
倒计时 2
倒计时 1
发射!
```

### 动手练习

1. 把 range(1, 6) 改成 range(1, 11),打印 1 到 10。
2. 用循环算出 1 到 100 的和(提示:range(1, 101))。
3. 把 while 里的 count = count - 1 删掉运行看看 —— 程序会停不下来,按 Ctrl + C 中断。

### 随堂检测

**1. range(1, 5) 会产生哪些数?**

- A. 1,2,3,4
- B. 2,3,4,5
- C. 1,2,3,4,5
- D. 0,1,2,3,4

<details><summary>答案与解析</summary>

**答案:A**。range 含头不含尾:从 1 开始,到 5 之前结束,即 1,2,3,4。

</details>

**2. 下面哪个循环是死循环?**

- A. `for c in "abc": print(c)`
- B. `while n > 0: n = n - 1`
- C. `while True: print("x")`
- D. `for i in range(3): print(i)`

<details><summary>答案与解析</summary>

**答案:C**。while True 的条件永远为真,循环体内又没有 break,所以永不停止。

</details>

**3. 求和的正确起手式是?**

- A. total = 0,再在循环里 total = total + x
- B. `total = []`
- C. 直接用 sum 之外的变量名
- D. `total = 1`

<details><summary>答案与解析</summary>

**答案:A**。累加要先初始化一个 0,再在循环里累加。若初始化成 1,结果会多 1;若用列表,则变成收集而不是求和。

</details>

## L06 · 函数:把代码打包复用

> 关键词:从脚本到程序 | 建议用时 7 分钟

函数把一段代码**打包成一个可以反复调用的名字**。它是「不重复自己」的核心工具。

写法:`def` 函数名(参数): 然后缩进写函数体,用 `return` 把结果送回去。

```python
def greet(name):            # 定义:name 是"参数"
    return f"你好,{name}!"   # return 把结果送回去

msg = greet("小明")         # 调用:把"小明"传进去
print(msg)                   # 你好,小明!
```

运行结果:

```text
你好,小明!
```

> **【说明】参数 vs 返回值**
>
> - **参数**是函数的「输入口」,写在括号里。
> - **return** 是函数的「输出口」,把结果交回给调用者,函数**立刻结束**。
> - 没写 return 的函数返回 `None`。
> - 有默认值的参数可以不传:`def greet(name="朋友")`。

```python
def area(w, h=1):          # h 有默认值 1
    return w * h

print(area(3, 4))          # 12
print(area(5))             # 5(用了默认值 h=1)
```

运行结果:

```text
12
5
```

> **【注意】print 和 return 的区别(极高频错误)**
>
> `print` 只是在屏幕上显示一下,值**不会**被交回来;只有 `return` 才把结果交回。如果函数里只 print 不 return,外面拿到的是 `None`,再参与计算就会报 TypeError。

关于变量的可见范围(**作用域**):函数内部能读到外面的全局变量,但函数内部新赋值的变量是**局部的**,函数一结束就消失:

```python
rate = 0.8                 # 全局变量

def discounted(price):
    return price * rate    # 能读到外面的 rate

print(discounted(100))

def broken():
    total = 1              # 这是局部变量,外面看不见
broken()
print(total)               # ✗ NameError: total 没有定义
```

运行结果(本段故意演示报错):

```text
80.0
Traceback (most recent call last):
  ...
NameError: name 'total' is not defined
```

> **【说明】为什么一定要用函数**
>
> - 改一处,处处生效 —— 不用在 10 个地方重复改同一段逻辑。
> - 有了名字,代码变成「句子」,读起来就是流程说明。
> - 可以单独测试一小块,排错范围大幅缩小。
> - 经验法则:同一段逻辑写第**二**遍时,就该把它变成函数。

### 本关完整示例

```python
def greet(name):
    return f"你好,{name}!"

def bmi(weight, height):
    return weight / (height ** 2)

def grade(score):
    if score >= 90:
        return "优秀"
    elif score >= 60:
        return "及格"
    return "不及格"          # 兜底:上面都不满足

print(greet("小明"))
print(f"BMI = {bmi(65, 1.75):.1f}")
for s in [95, 72, 45]:
    print(f"{s} 分 → {grade(s)}")
```

运行结果:

```text
你好,小明!
BMI = 21.2
95 分 → 优秀
72 分 → 及格
45 分 → 不及格
```

### 动手练习

1. 写一个函数 add(a, b) 返回两数之和,并打印 add(3, 4)。
2. 写一个函数 is\_even(n) 返回 True/False,判断是否是偶数(提示:n % 2 == 0)。
3. 故意把 grade 函数里的 return 改成 print,看看外面打印出来是什么(会是 None)。

### 随堂检测

**1. 下面函数返回什么?def f(x): print(x) 然后 f(5)**

- A. 报错
- B. 5
- C. `""`
- D. None

<details><summary>答案与解析</summary>

**答案:D**。函数只 print 没有 return,所以返回值是 None(屏幕上会显示 5,但那是打印效果,不是返回值)。

</details>

**2. 调用带默认值参数的函数 area(5),h 等于多少?**

- A. 报错
- B. None
- C. 默认值
- D. 0

<details><summary>答案与解析</summary>

**答案:C**。def area(w, h=1) 中,h 没传时就用默认值。有默认值的参数必须放在没有默认值的参数后面。

</details>

**3. 函数内部新赋值的变量,函数外能直接访问吗?**

- A. 只要同名就能
- B. 能
- C. 打印后才能
- D. 不能,它是局部变量

<details><summary>答案与解析</summary>

**答案:D**。函数内赋值默认创建局部变量,函数结束后就销毁。外部访问会报 NameError。

</details>

## L07 · 列表与字典:装数据的两个容器

> 关键词:用得最多的两种结构 | 建议用时 8 分钟

**列表 list** 是有顺序的一排格子,用下标取,用 `[]` 定义。

**字典 dict** 是「键 → 值」的查找表,用名字取,用 `{}` 定义。选对容器,代码会短一半。

```python
fruits = ["苹果", "香蕉", "橘子"]    # 列表:有序、按下标
print(fruits[0])        # 苹果
print(fruits[-1])       # 橘子
print(len(fruits))      # 3

person = {"name": "小明", "age": 18}   # 字典:按键查找
print(person["name"])   # 小明
person["city"] = "北京" # 新增键值对
print(person)
```

运行结果:

```text
苹果
橘子
3
小明
{'name': '小明', 'age': 18, 'city': '北京'}
```

| 列表操作 | 写法 | 效果 |
|---|---|---|
| 尾部追加 | fruits.append("梨") | 列表末尾多一个元素 |
| 取出并删除 | `x = fruits.pop()` | x 是最后一个元素 |
| 删除指定值 | fruits.remove("苹果") | 删掉第一个匹配项 |
| 排序 | `nums.sort()` | 原地从小到大 |
| 长度 | `len(fruits)` | 元素个数 |
| 判断存在 | "苹果" in fruits | `True / False` |

| 字典操作 | 写法 | 效果 |
|---|---|---|
| 取值 | `person["name"]` | 键不存在会报 KeyError |
| 安全取值 | person.get("sex", "未知") | 不存在返回默认值,不报错 |
| 新增/修改 | `person["age"] = 19` | 键存在就覆盖 |
| 遍历 | `for k, v in person.items():` | 同时拿到键和值 |
| 所有键 | `list(person.keys())` | 键的列表 |

> **【提示】怎么选:列表还是字典?**
>
> - 要**按顺序排一排**、要按下标取、会重复 → **列表**。如:成绩单、待办事项。
> - 要**用名字查东西**、一对一对应 → **字典**。如:用户信息、单词表、计数器。
> - 嵌套是常态:`students = [{"name":"小明","score":95}, ...]` —— 列表套字典,这就是真实数据的形状。

```python
# 列表套字典:一行代表一个对象
students = [
    {"name": "小明", "score": 95},
    {"name": "小红", "score": 88},
]
for s in students:
    print(f"{s['name']} 考了 {s['score']} 分")

# 字典当计数器:统计词频
words = ["苹果", "香蕉", "苹果", "苹果"]
count = {}
for w in words:
    count[w] = count.get(w, 0) + 1
print(count)     # {'苹果': 3, '香蕉': 1}
```

运行结果:

```text
小明 考了 95 分
小红 考了 88 分
{'苹果': 3, '香蕉': 1}
```

> **【注意】两个高频错误**
>
> - **IndexError**:下标超出范围。3 个元素的列表,合法下标只有 0/1/2(或 -1/-2/-3)。
> - **KeyError**:字典里没这个键。不确定时用 `.get(键, 默认值)`。

### 本关完整示例

```python
# 列表
scores = [85, 92, 78]
scores.append(96)
print("成绩:", scores, "| 最高:", max(scores), "| 平均:", sum(scores) / len(scores))

# 字典
person = {"name": "小明", "age": 18}
person["city"] = "北京"
for k, v in person.items():
    print(f"  {k} = {v}")
print("安全取值:", person.get("sex", "未填写"))

# 列表套字典
team = [
    {"name": "小明", "score": 95},
    {"name": "小红", "score": 88},
]
for m in team:
    print(f"{m['name']}: {m['score']}")
```

运行结果:

```text
成绩: [85, 92, 78, 96] | 最高: 96 | 平均: 87.75
  name = 小明
  age = 18
  city = 北京
安全取值: 未填写
小明: 95
小红: 88
```

### 动手练习

1. 往 scores 里再 append 一个 100,看看 max 变成多少。
2. 用 .get("sex", "未填写") 换成直接 person["sex"],观察 KeyError 报错内容。
3. 给 team 再加一个成员,然后打印所有人的平均分。

### 随堂检测

**1. [10, 20, 30] 中,元素 30 的下标是?**

- A. 2
- B. 3
- C. 1
- D. `-3`

<details><summary>答案与解析</summary>

**答案:A**。正向下标从 0 开始,30 是第 3 个元素,下标是 2。负下标从 -1 开始倒着数:-1 取到的也是 30,而 -3 取到的是 10。

</details>

**2. 字典取值时最安全的写法是?**

- A. `d(k)`
- B. `d["k"]`
- C. d.get("k", 默认值)
- D. `d.k`

<details><summary>答案与解析</summary>

**答案:C**。d["k"] 在键不存在时抛 KeyError;.get() 可以给默认值,不会中断程序。

</details>

**3. 要统计每个单词出现次数,最适合用?**

- A. 字典
- B. 整数
- C. 字符串
- D. 列表

<details><summary>答案与解析</summary>

**答案:A**。「词 → 次数」是一对一映射,正是字典的用途:count[w] = count.get(w, 0) + 1。

</details>


---

# 进阶技巧

## L08 · 文件读写:让数据留下来

> 关键词:程序重启数据还在 | 建议用时 5 分钟

程序跑完,变量就没了。想让数据**留下来**,就要写进文件。

三步走:**打开 → 读写 → 关闭**。

```python
# 写文件
f = open("note.txt", "w", encoding="utf-8")   # "w" = 写入(会清空原内容)
f.write("今天学了 Python\n")
f.write("第 08 关:文件读写")
f.close()                                      # 一定要关

# 读文件
f = open("note.txt", "r", encoding="utf-8")   # "r" = 只读
content = f.read()                             # 一次性读全部
f.close()
print(content)
```

运行结果:

```text
今天学了 Python
第 08 关:文件读写
```

| 模式 | 含义 | 注意 |
|---|---|---|
| `"r"` | 只读(默认) | 文件不存在会报 FileNotFoundError |
| `"w"` | 写入 | <b>会清空原内容!</b>文件不存在则新建 |
| `"a"` | 追加 | 在末尾接着写,不清空 |
| `"r+"` | 读写 | 一般用不到 |

> **【说明】读取的三种方式**
>
> - `f.read()` → 整个文件变成一个字符串。
> - `f.readlines()` → 每行一个元素,变成列表。
> - `for` line `in` f: → 一行一行处理,**大文件首选**(不占内存)。

```python
f = open("note.txt", "a", encoding="utf-8")   # 追加,不清空
f.write("\n又加了一行")
f.close()

# 按行读:for line in f 逐行处理,大文件也不占内存
f = open("note.txt", "r", encoding="utf-8")
for line in f:
    print("读到:", line.strip())    # strip() 去掉行尾换行符
f.close()
```

运行结果:

```text
读到: 今天学了 Python
读到: 第 08 关:文件读写
读到: 又加了一行
```

> **【对照】关于 with(真实项目里的标准写法)**
>
> 真实项目里推荐写成 `with` open(...) as f: —— 离开缩进块时**自动关闭文件**,即使中途报错也不会漏关。上面先用 open / close 是为了让你看清「打开 → 读写 → 关闭」三步,下面的主代码就改用 with 写法。另外,读写中文时请加上 `encoding="utf-8"`,否则在 Windows 上容易出现乱码或 UnicodeDecodeError。

> **【注意】最容易踩的坑**
>
> - 用 "w" 打开一个已有文件 → **内容立刻被清空**,只剩你新写进去的。想保留请用 "a"。
> - 忘记 f.close() → 内容可能没真正写入。
> - 行尾换行符:写的时候要自己加 `\n`,读的时候用 `.strip()` 去掉。

### 本关完整示例

```python
# 写("w" 会清空原内容)
with open("diary.txt", "w", encoding="utf-8") as f:
    f.write("2024-01-01 学会写文件\n")
    f.write("2024-01-02 学会读文件\n")
print("写入完成")

# 追加("a" 在末尾接着写)
with open("diary.txt", "a", encoding="utf-8") as f:
    f.write("2024-01-03 复习了一遍\n")

# 读:离开 with 块时文件自动关闭
with open("diary.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(" ", line.strip())
```

运行结果:

```text
写入完成
  2024-01-01 学会写文件
  2024-01-02 学会读文件
  2024-01-03 复习了一遍
```

### 动手练习

1. 把写入模式 "w" 改成 "a" 再运行两次,观察文件内容是否被清空。
2. 读完之后统计一共有几行(提示:用一个计数变量在循环里 +1)。
3. 把主代码改回 open() / close() 的写法,对比一下 with 写法省掉了什么、多保证了什么。

### 随堂检测

**1. 用 "w" 模式打开一个已有内容的文件会怎样?**

- A. 原内容被清空
- B. 报错
- C. 原内容被备份
- D. 保留并在末尾追加

<details><summary>答案与解析</summary>

**答案:A**。"w" 表示重写,打开瞬间就清空。要保留原内容用 "a"(追加)。

</details>

**2. 读一个文件时,最省内存的方式是?**

- A. f.readlines() 全读进列表
- B. 都一样
- C. f.read() 全读进来
- D. for line in f: 逐行处理

<details><summary>答案与解析</summary>

**答案:D**。逐行迭代同一时刻只把一行放进内存;read()/readlines() 会把整个文件读进来,大文件会吃掉大量内存。

</details>

**3. 把多行文本读成列表用哪个方法?**

- A. `readlines()`
- B. `write()`
- C. `read()`
- D. `split()`

<details><summary>答案与解析</summary>

**答案:A**。readlines() 返回列表,每个元素是一行(带换行符)。

</details>

## L09 · 模块与导入:站在别人的肩膀上

> 关键词:不重复造轮子 | 建议用时 4 分钟

模块就是**别人写好的一包功能**。用 `import` 拿进来就能用,不必自己从零实现。

这是 Python 最强大的地方:生态里几乎每个常见需求都有成熟模块。

```python
import math                      # 导入整个模块
print(math.sqrt(16))             # 4.0
print(math.pi)                   # 3.141592653589793

from math import sqrt, pi        # 只导入需要的名字
print(sqrt(25))                  # 5.0
print(pi)
```

运行结果:

```text
4.0
3.141592653589793
5.0
3.141592653589793
```

| 写法 | 含义 | 调用方式 |
|---|---|---|
| import math | 导入整个模块 | math.sqrt(9) —— 要带前缀 |
| from math import sqrt | 只导入某个函数 | sqrt(9) —— 不用前缀 |
| import math as m | 起别名 | `m.sqrt(9)` |
| import numpy as np | 惯例别名(生态默契) | `np.array(...)` |

> **【说明】标准库与第三方库**
>
> **math**(数学)、**random**(随机)、**time**(时间)属于 Python **标准库**,装好 Python 就能直接 import。numpy、pandas、requests 这类属于**第三方库**,要先在命令行执行 `pip install numpy pandas` 安装 —— 但**导入和调用的写法完全一样**,学会了就能无缝迁移。

```python
import random
print(random.randint(1, 6))       # 掷骰子:1~6 随机整数
print(random.choice(["石头", "剪刀", "布"]))

import math
print(f"斜边 = {math.hypot(3, 4)}")   # 5.0
```

运行结果(含随机数,每次运行结果可能不同):

```text
4
剪刀
斜边 = 5.0
```

> **【说明】自己写模块(知道就行)**
>
> 任何一个 `.py` 文件都是一个模块。把常用的函数写进 `tools.py`,在同目录下 `import` tools,就能用 `tools.函数名()` 调用了 —— 你已经会写函数(第 06 关),所以这就是自然延伸。

### 本关完整示例

```python
import math
from math import sqrt

print("圆周率:", round(math.pi, 4))
print("16 的平方根:", math.sqrt(16))
print("不用前缀:", sqrt(81))
print("向上取整:", math.ceil(3.2), "| 向下取整:", math.floor(3.8))

import random
print("随机 1~6:", random.randint(1, 6))
print("从列表随机选:", random.choice(["石头", "剪刀", "布"]))

# 实战:用 math 算圆的面积
def circle_area(r):
    return math.pi * r ** 2
print(f"半径 3 的圆面积 = {circle_area(3):.2f}")
```

运行结果(含随机数,每次运行结果可能不同):

```text
圆周率: 3.1416
16 的平方根: 4.0
不用前缀: 9.0
向上取整: 4 | 向下取整: 3
随机 1~6: 2
从列表随机选: 石头
半径 3 的圆面积 = 28.27
```

### 动手练习

1. 用 math.factorial(5) 算 5 的阶乘。
2. 用 random.randint 模拟掷 3 次骰子并求和(提示:用 for 循环)。
3. 把 import math 改成 import math as m,然后改调用方式。

### 随堂检测

**1. import math 之后,求平方根怎么写?**

- A. `Math.sqrt(9)`
- B. `math->sqrt(9)`
- C. `sqrt(9)`
- D. `math.sqrt(9)`

<details><summary>答案与解析</summary>

**答案:D**。import 整个模块要带模块名前缀。想直接写 sqrt(9) 得用 from math import sqrt。

</details>

**2. from math import sqrt 与 import math 的区别是?**

- A. 没有区别
- B. 前者可以直接写 sqrt(),后者要写 math.sqrt()
- C. 后者更快
- D. 前者不能用于 Python 3

<details><summary>答案与解析</summary>

**答案:B**。本质一样,只是名字有没有被带进当前命名空间的区别。

</details>

**3. 在真实 Python 里,处理表格数据最常用的模块是?**

- A. random
- B. math
- C. pandas
- D. time

<details><summary>答案与解析</summary>

**答案:C**。pandas 是表格数据分析的事实标准。它需要先 pip install pandas,import pandas as pd 的写法你已经会了。

</details>

## L10 · 类与对象:把数据和动作包在一起

> 关键词:理解别人的代码 | 建议用时 8 分钟

类是**模具**,对象是用模具做出来的**一个个成品**。

当你需要「一样东西既有它自己的数据,又有它自己能做的动作」时,就该用类。

```python
class Dog:
    def __init__(self, name, age):   # 构造函数:创建对象时自动执行
        self.name = name             # self = 这个对象自己
        self.age = age

    def bark(self):                  # 方法:第一个参数永远是 self
        return f"{self.name} 汪汪叫!"

    def birthday(self):
        self.age = self.age + 1      # 修改自己的数据

wang = Dog("旺财", 3)                # 用模具造一个对象
print(wang.name)                     # 旺财
print(wang.bark())                   # 旺财 汪汪叫!
wang.birthday()
print(wang.age)                      # 4
```

运行结果:

```text
旺财
旺财 汪汪叫!
4
```

> **【要点】四个必须理解的概念**
>
> - **class** 是定义模具,`Dog("旺财",3)` 才是造出成品。
> - <b>\_\_init\_\_</b> 是「出厂设置」,创建对象时自动运行,用来给对象装上数据。
> - **self** 指「这个对象自己」,方法里访问自己的数据必须写 `self.属性`。
> - **属性**是数据(`self.name`),**方法**是动作(`def bark`)。

```python
# 常见写法:把相关数据用字典列表装,不如用类更清晰
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def passed(self):
        return self.score >= 60

    def __str__(self):                 # 定义 print 时显示成什么样
        return f"{self.name}({self.score}分)"

team = [Student("小明", 95), Student("小红", 52)]
for s in team:
    print(s, "→", "及格" if s.passed() else "不及格")
```

运行结果:

```text
小明(95分) → 及格
小红(52分) → 不及格
```

> **【说明】什么时候该用类(以及不该用)**
>
> - **该用**:同一类东西有很多个,每个都有自己的数据,还带自己的动作(如:多个学生、多个游戏角色、多个订单)。
> - **不该用**:只是把一个数字/字符串传来传去 —— 普通变量和函数就够了,别为了「显得高级」而用类。
> - 你现在读任何 Python 库的文档,看到 `对象.方法()` 就知道背后是类 —— 这是读懂别人代码的钥匙。

> **【注意】初学者三个必错点**
>
> - 忘写 `self`:方法定义里第一个参数必须是 self,调用时**不用**传它。
> - 调用时写成 `Dog.bark()` —— 必须用对象调用:`wang.bark()`。
> - 在 `__init__` 里把 `self.name` 写成 `name`,导致属性没装上。

### 本关完整示例

```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def passed(self):
        return self.score >= 60

    def add_score(self, delta):
        self.score = self.score + delta

    def __str__(self):
        return f"{self.name}({self.score} 分)"

team = [Student("小明", 95), Student("小红", 52)]
for s in team:
    print(s, "→", "及格" if s.passed() else "不及格")

team[1].add_score(10)
print("小红补考加 10 分后:", team[1])
```

运行结果:

```text
小明(95 分) → 及格
小红(52 分) → 不及格
小红补考加 10 分后: 小红(62 分)
```

### 动手练习

1. 给 Student 加一个方法 level(),分数 >= 90 返回"优秀",>= 60 返回"及格",否则"不及格"。
2. 再加一个属性 city,并在 \_\_str\_\_ 里也显示出来。
3. 把 \_\_str\_\_ 删掉运行,看看 print(s) 变成什么样。

### 随堂检测

**1. 方法定义里第一个参数通常是什么?**

- A. self
- B. this
- C. cls
- D. 不用写参数

<details><summary>答案与解析</summary>

**答案:A**。Python 用 self 表示「这个对象自己」,必须显式写在参数列表第一位(调用时不用传)。

</details>

**2. \_\_init\_\_ 什么时候执行?**

- A. 创建对象时自动执行
- B. 手动调用时
- C. 程序结束时
- D. import 时

<details><summary>答案与解析</summary>

**答案:A**。\_\_init\_\_ 是构造函数,写 Dog("旺财", 3) 的瞬间自动执行,用来初始化属性。

</details>

**3. print(对象) 想显示自定义内容,要定义哪个方法?**

- A. \_\_init\_\_
- B. show
- C. \_\_print\_\_
- D. \_\_str\_\_

<details><summary>答案与解析</summary>

**答案:D**。定义 \_\_str\_\_ 返回一个字符串,print() 就会显示它。

</details>

## L11 · 错误处理 try / except

> 关键词:让程序不轻易崩溃 | 建议用时 5 分钟

程序出错就会**中断**。用 `try` / `except` 可以「兜住」错误,让程序优雅地继续。

记住:错误不是坏事 —— 报错信息是**最详细的调试线索**。

```python
try:
    n = int("abc")        # 这里一定会出错
    print(n)
except ValueError:
    print("输入的不是数字,已帮你兜住")

print("程序继续往下走")
```

运行结果:

```text
输入的不是数字,已帮你兜住
程序继续往下走
```

| 异常名 | 什么时候出现 | 怎么避免 |
|---|---|---|
| ValueError | int("abc") 类型对但值不合法 | 先判断 or 用 try 兜住 |
| TypeError | str + int 混用、参数个数不对 | 统一类型、检查参数 |
| NameError | 变量没定义/拼错 | 检查拼写和赋值顺序 |
| IndexError | 列表下标越界 | 用 len() 检查范围 |
| KeyError | 字典没有这个键 | 用 .get(键, 默认值) |
| ZeroDivisionError | 除以 0 | 先判断除数不为 0 |
| FileNotFoundError | 文件不存在 | 先判断或先写入 |

> **【说明】完整结构**
>
> - `try`:放可能出错的代码。
> - `except` 具体异常名:出错时执行的补救代码(尽量写具体类型,别只写 except:)。
> - `finally`:无论成功失败都执行(常用于关文件)。
> - `as` e:把错误对象接住,`e` 里带着错误信息。

```python
# 实战:让用户输入一个数字,错了就重来
text = "abc"          # 假装这是用户输入
try:
    n = int(text)
    print(f"你输入了 {n}")
except ValueError as e:
    print(f"转换失败:{e}")
    print("→ 提示用户重新输入数字")
finally:
    print("(这一步总会执行)")
```

运行结果:

```text
转换失败:invalid literal for int() with base 10: 'abc'
→ 提示用户重新输入数字
(这一步总会执行)
```

> **【注意】不要用 try 掩盖真正的 bug**
>
> 如果你不知道这行**为什么会错**,就用 try 把它包起来,错误只是被藏起来了,后面会在更远的地方以更难懂的方式爆发。正确姿势:先看报错信息 → 找到原因 → 让代码不会出错;只有面对**不可控的外部输入**(用户输入、文件、网络)时才用 try 兜底。

> **【提示】怎么看报错(Traceback)**
>
> - **最后一行**是错误类型和原因 —— 先读这一行。
> - 往上找 `File "xxx.py", line N` —— 那里指出了出错的行号。
> - 比如最后一行是 `ValueError: invalid literal for int() with base 10: 'abc'`:冒号左边是错误类型,右边是具体原因。

### 本关完整示例

```python
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "除数不能为 0"

print(safe_divide(10, 2))
print(safe_divide(10, 0))

# 兜住类型转换错误
for text in ["18", "abc", "3.5"]:
    try:
        print(f"{text} → {int(text)}")
    except ValueError:
        print(f"{text} → 不是整数,跳过")

# finally 总会执行
try:
    print("打开资源")
    raise ValueError("模拟一个错误")
except ValueError as e:
    print("兜住错误:", e)
finally:
    print("无论成败都要做的收尾工作")
```

运行结果:

```text
5.0
除数不能为 0
18 → 18
abc → 不是整数,跳过
3.5 → 不是整数,跳过
打开资源
兜住错误: 模拟一个错误
无论成败都要做的收尾工作
```

### 动手练习

1. 把 int(text) 改成 float(text),看看 "3.5" 能否通过。
2. 给 safe\_divide 加上 except TypeError,处理 a 或 b 不是数字的情况。
3. 故意删掉 try/except,运行后读一读 Traceback 的最后一行写了什么。

### 随堂检测

**1. int("abc") 会抛出哪种异常?**

- A. KeyError
- B. ValueError
- C. NameError
- D. TypeError

<details><summary>答案与解析</summary>

**答案:B**。类型是对的(字符串),但内容不合法,所以是 ValueError。如果是 int(None) 则是 TypeError。

</details>

**2. finally 块的代码什么时候执行?**

- A. 只有出错时
- B. 从不执行
- C. 只有成功时
- D. 无论成功或出错都执行

<details><summary>答案与解析</summary>

**答案:D**。finally 用于收尾(如关闭文件、释放资源),try 是否成功都会执行。

</details>

**3. [1,2,3] 访问 [5] 会抛出?**

- A. ValueError
- B. KeyError
- C. IndexError
- D. TypeError

<details><summary>答案与解析</summary>

**答案:C**。列表下标越界是 IndexError;字典的键不存在才是 KeyError。

</details>

## L12 · 综合实战:一个完整的小程序

> 关键词:把 11 关全部串起来 | 建议用时 8 分钟

最后一关不教新语法 —— 而是把前面学的**全部串起来**,写一个真正有用的小程序。

看完你会有一种「我好像真的会写程序了」的感觉。

我们要做的是**学生成绩管理器**。程序包含:数据容器、函数封装、循环遍历、条件判断、f-string 输出。拆成四步:

1. 用**列表套字典**存数据(第 07 关)。
2. 把「算平均分」「找最高分」「判断等级」写成**函数**(第 06 关)。
3. 用**循环**遍历打印每个人的成绩(第 05 关)。
4. 用**条件判断**给出等级,用 **f-string** 排版输出(第 03、04 关)。

```python
def average(scores):
    return sum(scores) / len(scores)

def top_student(students):
    best = students[0]
    for s in students:
        if s["score"] > best["score"]:
            best = s
    return best

def level(score):
    if score >= 90:
        return "优秀"
    if score >= 60:
        return "及格"
    return "不及格"
```

> **【说明】这个程序用到的全部知识**
>
> - 变量与类型(02)· 字符串与 f-string(03)
> - if / elif / else(04)· for 循环与累加(05)
> - def 定义函数与 return(06)· 列表与字典嵌套(07)
> - 把「找最高分」的初始值设成第一个元素,这是**很实用的技巧**(避免用 -1 之类的魔法数字)。

> **【完成】恭喜:接下来该做什么**
>
> - **马上用**:挑一个你自己的重复劳动(整理文件、算账、统计数据),用今天学的写出来 —— 哪怕只有 20 行。
> - <b>再补 20%</b>:列表推导式、字典推导式、with 语句、pandas 基础。
> - **看懂报错**比背语法更重要;遇到不会的,把报错信息原样搜索。
> - **真正分水岭**:能不能把一个大任务拆成若干个小函数 —— 这才是编程能力的核心。

### 本关完整示例

```python
def average(scores):
    return sum(scores) / len(scores)

def level(score):
    if score >= 90:
        return "优秀"
    if score >= 60:
        return "及格"
    return "不及格"

def top_student(students):
    best = students[0]
    for s in students:
        if s["score"] > best["score"]:
            best = s
    return best

students = [
    {"name": "小明", "score": 95},
    {"name": "小红", "score": 88},
    {"name": "小刚", "score": 52},
    {"name": "小美", "score": 76},
]

print("=" * 34)
print("         成绩单")
print("=" * 34)

all_scores = []
for s in students:
    print(f"{s['name']:<4} {s['score']:>4} 分   {level(s['score'])}")
    all_scores.append(s["score"])

print("-" * 34)
print(f"平均分:{average(all_scores):.1f}")
print(f"最高分:{max(all_scores)}  最低分:{min(all_scores)}")
best = top_student(students)
print(f"第一名:{best['name']}({best['score']} 分)")
print("=" * 34)

# 统计各等级人数(字典当计数器)
stat = {}
for s in students:
    lv = level(s["score"])
    stat[lv] = stat.get(lv, 0) + 1
print("等级分布:", stat)
```

运行结果:

```text
==================================
         成绩单
==================================
小明     95 分   优秀
小红     88 分   及格
小刚     52 分   不及格
小美     76 分   及格
----------------------------------
平均分:77.8
最高分:95  最低分:52
第一名:小明(95 分)
==================================
等级分布: {'优秀': 1, '及格': 2, '不及格': 1}
```

### 动手练习

1. 加一个学生,看看平均分和第一名会不会变。
2. 给每个学生加一个 "city" 字段,并在输出里也打印出来。
3. 把「找最高分」改成「找最低分」(提示:把 > 改成 <)。
4. 挑战:改用字典统计各等级人数后,用循环按人数从多到少打印出来。

### 随堂检测

**1. 求列表平均分最简洁的写法是?**

- A. `list / len(list)`
- B. `sum(list) / len(list)`
- C. `sum(list)`
- D. `len(list) / sum(list)`

<details><summary>答案与解析</summary>

**答案:B**。总和除以个数。注意要先确认列表非空,否则会 ZeroDivisionError。

</details>

**2. 找最大值时,把初始 best 设成第一个元素的好处是?**

- A. 省内存
- B. 运行更快
- C. 语法必须这样
- D. 不用假设数据的取值范围,更通用

<details><summary>答案与解析</summary>

**答案:D**。若初始值设成 -1 或 0,当所有数据都是负数时就会出错。用第一个元素作起点永远安全。

</details>

**3. 把大任务写好代码的关键是?**

- A. 拆成多个职责单一的小函数
- B. 多用全局变量
- C. 写在一个大函数里
- D. 尽量少写注释

<details><summary>答案与解析</summary>

**答案:A**。每个函数只做一件事,才能单独理解和测试。这是从「会语法」到「会编程」的分水岭。

</details>


---

# 语言补强

## L13 · 运算符与类型转换:%、//、\*\* 与 int/float/str

> 关键词:算术运算符 · 取余 · 整除 · 幂 · 类型转换 | 建议用时 9 分钟

前 12 幕你已经会用 `+` `-` `*` `/` 了。但 Python 里还有三个被新手忽略、实际天天要用的运算符:`%`(取余)、`//`(整除)、`**`(幂)。

为什么非要单独讲它们?因为**把连续的量切成一段一段**这件事,全靠这三个符号。经度怎么分箱、日期怎么算月份差、一批数据怎么分成几组 —— 都是用取余和整除做的。<b>不会它们,后面所有按区间统计的代码都写不出来。</b>

先把算术运算符摆成一张表。前四个你都见过,后三个是这一幕的重点:

| 运算符 | 名称 | 例子 | 结果 |
|---|---|---|---|
| `+` | 加 | `7 + 3` | 10 |
| `-` | 减 | `7 - 3` | 4 |
| `*` | 乘 | `7 * 3` | 21 |
| `/` | 除(永远得到小数) | `7 / 2` | `3.5` |
| `//` | 整除:只取商,扔掉余数 | `7 // 2` | 3 |
| `%` | 取余:只要余数 | `7 % 2` | 1 |
| `**` | 幂 | `2 ** 10` | 1024 |

```python
total = 7380          # 秒
minutes = total // 60  # 商:一共多少整分钟
seconds = total % 60   # 余:剩下多少秒
print(minutes, "分", seconds, "秒")
print(minutes * 60 + seconds, "= 原来的总秒数")
```

运行结果:

```text
123 分 0 秒
7380 = 原来的总秒数
```

> **【要点】// 和 % 是一对搭档**
>
> `//` 只保留「够几个」,`%` 只保留「剩多少」。它们永远满足一条铁律:**商 × 除数 + 余数 = 被除数**。所以拿 `n % 2` 判断奇偶(余 0 是偶数、余 1 是奇数),拿 `n // 2` 做「两个一组」的分堆,都是在用这条铁律。

取余最有价值的用法是**分箱**:把连续的数值切成一段一段,同一段里的值强行变成同一个编号。这是「按区间统计」的全部秘密:

```python
from dataset import dataset

bins = {}
for c in dataset.cities:
    bucket = int(c["lon"] // 5 * 5)   # 每 5 度一箱:116.4 → 115
    if bucket in bins:
        bins[bucket] = bins[bucket] + 1
    else:
        bins[bucket] = 1
print("分了多少箱:", len(bins))
for k in sorted(bins.keys())[0:3]:
    print("第", k, "箱:", bins[k], "个城市")
```

运行结果:

```text
分了多少箱: 9
第 75 箱: 1 个城市
第 85 箱: 1 个城市
第 90 箱: 2 个城市
```

> **【要点】分箱公式:先除、再砍掉小数、再乘回来**
>
> `x // 5 * 5` 的意思是:先用整除看看 x 落在第几个 5 度的格里,再乘回 5 还原成「这一格的起点」。所以 116.4 会变成 115、112.5 会变成 110。**箱号 = (值 − 起点) // 箱宽** 是同一个公式的另一种写法,记哪一个都行,关键是别把 `//` 又写成 `/`。

幂运算 `**` 比乘号多一个星号,别写成 `^`(那是别的语言里的异或,Python 里写 `^` 不会报错但结果是错的):

```python
print(2 ** 10)         # 1024
print(3 ** 2)          # 9
print(10 ** 0.5)       # 3.1622776601683795
print(round(10 ** 0.5, 2))   # 3.16
print(9 ** 0.5)        # 3.0  —— 开方也能用 ** 0.5
```

运行结果:

```text
1024
9
3.1622776601683795
3.16
3.0
```

接下来是比较与逻辑运算符。`and` / `or` / `not` 有一个很容易踩的特性:**短路** —— 左边的结果一出来,右边就懒得算了:

```python
pm = 58
print(pm > 50 and pm < 100)   # 两个都真才真
print(pm < 10 or pm > 50)     # 一个真就真
print(not pm > 50)            # 取反

print(True or never_defined)  # 左边已经是真 → 右边不执行,不报错!
print(False and never_defined)
```

运行结果:

```text
True
True
False
True
False
```

> **【注意】短路会「藏住」错误**
>
> 上面那两行没报 NameError,不是因为写法正确,而是因为 **and / or 在左边就能决定结果时,直接跳过右边**。这有三个真会咬人的后果:一是把本该报错的地方悄悄跳过,错误拖到很久以后才爆;二是判断顺序会影响结果 —— `if len(vals) > 0 and vals[0] > 5:` 能跑,把两个条件换个个儿就 IndexError;三是 `and` / `or` 返回的不是 True/False 而是「决定结果的那个值」,`print(0 or "默认值")` 输出的是字符串。想让它老老实实变成真假,外面套一层 `bool(...)`。

最后是类型转换。规则只有四条,但**三条会失败**,失败时会抛 ValueError:

| 写法 | 结果 | 什么情况下失败 |
|---|---|---|
| `int("42")` | 42 | 字符串不是纯整数就失败 —— int("3.5")、int("abc") 都报 ValueError |
| `float("3.5")` | `3.5` | 字符串不是数字就失败 —— float("abc") 报 ValueError |
| `str(42)` | `"42"` | 几乎不会失败(任何值都能变成字符串) |
| `bool(0)` | False | 不会失败:0、0.0、""、[]、{}、None 都是 False |

```python
for text in ["42", "3.5", "abc"]:
    try:
        print("int(\"" + text + "\") =", int(text))
    except ValueError:
        print("int(\"" + text + "\") 失败:不是纯整数")
```

运行结果:

```text
int("42") = 42
int("3.5") 失败:不是纯整数
int("abc") 失败:不是纯整数
```

> **【注意】int("3.5") 会直接报错,别指望它帮你砍小数**
>
> 这是新手最常撞的一堵墙:`int()` 只接受**纯整数**字符串。`"3.5"` 里有小数点,所以报 `ValueError`。正确做法是两步走:`int(float("3.5"))` —— 先变成小数、再砍掉小数部分。同样的坑还有第二个:取余和整除对**负数**的行为和很多语言不一样,Python 是「向下取整」:`-7 // 2` 得 `-4`(不是 -3),`-7 % 3` 得 `2`(不是 -1)。做经度、天数这类可能有负值的分箱时,一定要先想清楚这一条。

> **【对照】这段手写代码 ↔ 真实项目里的写法**
>
> - 手写 `(x - lo) // size * size + lo` 分箱 ↔ `pandas.cut(s, bins=10)` 或 `pd.cut(s, np.arange(lo, hi, size))`
> - 手写 `x // 5 * 5` 取整到 5 的倍数 ↔ `(s // 5 * 5)`,向量化写法一模一样;想四舍五入到整数倍则用 `np.round(s / 5) * 5`
> - 手写 `n % 2 == 0` 判奇偶 ↔ `n % 2 == 0`(完全一样),向量化是 `s % 2 == 0`
> - `a ** 2` ↔ `np.power(a, 2)` 或 `np.square(a)`
> - `int(float("3.5"))` ↔ `pd.to_numeric(s, errors="coerce")`(转不了的变 NaN);数据干净时可直接 `s.astype(int)`,含缺失值时用 `s.astype("Int64")`
> - 手写 `try / except ValueError` 挡脏数据 ↔ 读 CSV 时用 `pd.read_csv(..., na_values=["", "NA"])`

> **【提示】为什么 / 永远得到小数**
>
> Python 3 里 `7 / 2` 一定得 `3.5`,想要整数结果必须显式写 `7 // 2`。这是有意设计的:除法不丢信息,「丢掉小数」是你主动要求的动作。所以凡是「整除」,一定要想清楚用哪个符号 —— 把 `//` 写成 `/`,`116.4 / 5 * 5` 还是 116.4,分箱就完全失效了。还要注意:**浮点数做 // 结果仍是浮点数**(`116.4 // 5` 得 `23.0`),所以分箱代码外面再套一层 `int()`,箱号才是干净的 115,而不是 115.0 —— 否则 115 和 115.0 混用时很容易对不上。

### 本关完整示例

```python
# ===== L13:运算符与类型转换 =====

from dataset import dataset

print("=== 1) 整除与取余:把秒拆成分和秒 ===")
total = 7380
minutes = total // 60
seconds = total % 60
print(total, "秒 =", minutes, "分", seconds, "秒")
print("验证: 商 × 除数 + 余数 =", minutes * 60 + seconds)
print()

print("=== 2) 取余判奇偶 ===")
for n in [7, 12, 25, 30]:
    if n % 2 == 0:
        print(n, "是偶数")
    else:
        print(n, "是奇数")
print()

print("=== 3) 幂运算 ** ===")
print("2 ** 10 =", 2 ** 10)
print("3 ** 2 =", 3 ** 2)
print("开方用 ** 0.5:", round(10 ** 0.5, 2))
print("北京到上海约 1067 公里,来回", 1067 * 2, "公里")
print()

print("=== 4) 用整除给经度分箱(每 5 度一箱)===")
counts = {}
for c in dataset.cities:
    bucket = int(c["lon"] // 5 * 5)   # 分箱:先整除、再乘回来;int() 让箱号是整数
    if bucket in counts:
        counts[bucket] = counts[bucket] + 1
    else:
        counts[bucket] = 1
keys = sorted(counts.keys())
total_city = 0
for k in keys:
    print("第", k, "箱:", counts[k], "个城市")
    total_city = total_city + counts[k]
print("合计:", total_city, "个城市(56 个城市一个不少)")
print()

print("=== 5) 类型转换与失败情形 ===")
print(int("42") + 1)
print(float("3.5") * 2)
print(str(42) + " 号站点")
print(type(42), type("42"))
for text in ["42", "3.5", "abc"]:
    try:
        v = int(text)
        print("int(\"" + text + "\") 成功:", v)
    except ValueError:
        print("int(\"" + text + "\") 失败:不是纯整数")
print()

print("=== 6) and / or / not 与短路 ===")
print("50 > 40 and 50 < 60 :", 50 > 40 and 50 < 60)
print("50 > 90 or 50 < 60  :", 50 > 90 or 50 < 60)
print("not 50 > 90         :", not 50 > 90)
print("True or 未定义的变量 :", True or never_defined, "  (右边没执行,所以不报错)")
print("0 or \"默认值\"        :", 0 or "默认值", "  (or 返回的是决定结果的那个值)")
```

运行结果:

```text
=== 1) 整除与取余:把秒拆成分和秒 ===
7380 秒 = 123 分 0 秒
验证: 商 × 除数 + 余数 = 7380

=== 2) 取余判奇偶 ===
7 是奇数
12 是偶数
25 是奇数
30 是偶数

=== 3) 幂运算 ** ===
2 ** 10 = 1024
3 ** 2 = 9
开方用 ** 0.5: 3.16
北京到上海约 1067 公里,来回 2134 公里

=== 4) 用整除给经度分箱(每 5 度一箱)===
第 75 箱: 1 个城市
第 85 箱: 1 个城市
第 90 箱: 2 个城市
第 100 箱: 5 个城市
第 105 箱: 7 个城市
第 110 箱: 17 个城市
第 115 箱: 10 个城市
第 120 箱: 9 个城市
第 125 箱: 4 个城市
合计: 56 个城市(56 个城市一个不少)

=== 5) 类型转换与失败情形 ===
43
7.0
42 号站点
<class 'int'> <class 'str'>
int("42") 成功: 42
int("3.5") 失败:不是纯整数
int("abc") 失败:不是纯整数

=== 6) and / or / not 与短路 ===
50 > 40 and 50 < 60 : True
50 > 90 or 50 < 60  : True
not 50 > 90         : True
True or 未定义的变量 : True   (右边没执行,所以不报错)
0 or "默认值"        : 默认值   (or 返回的是决定结果的那个值)
```

### 动手练习

1. 把分箱宽度从 5 改成 10,看箱数和每箱的城市数怎么变 —— 箱越宽,箱内越多。
2. 把 7380 秒改成 3661 秒,验证输出是 61 分 1 秒(取余这一路最容易算错)。
3. 把 dataset.cities 换成 dataset.stations,用同样的办法给 pm25 每 20 一箱,看哪个箱最挤。
4. 故意写 print(10 / 0) 和 print(10 % 0),比较两种报错信息有什么不同。
5. 把 int("3.5") 改成 int(float("3.5")),看它能不能跑通,结果是多少。

### 随堂检测

**1. 17 % 5 的结果是?**

- A. `3.4`
- B. 12
- C. 2
- D. 3

<details><summary>答案与解析</summary>

**答案:C**。17 ÷ 5 = 3 余 2,取余 % 只要余数,所以是 2。选 3 的人是把「商」当成了答案(那是 17 // 5);选 3.4 是把它当成了普通除法(那是 17 / 5);选 12 是把它当成了减法。

</details>

**2. 要判断 n 是不是偶数,下面哪种写法对?**

- A. `n / 2 == 0`
- B. `n ** 2 == 0`
- C. `n % 2 == 0`
- D. `n // 2 == 0`

<details><summary>答案与解析</summary>

**答案:C**。偶数除以 2 余数为 0,所以用取余。n / 2 == 0 只有在 n 是 0 时才成立;n // 2 == 0 判断的是「n 小于 2」(4 // 2 = 2,不是 0),把 4 这种偶数判成了假;n \*\* 2 == 0 和奇偶毫无关系。

</details>

**3. int("3.5") 会发生什么?**

- A. 得到 3.5
- B. 得到 3
- C. 得到 "3"
- D. 报 ValueError,因为不是纯整数字符串

<details><summary>答案与解析</summary>

**答案:D**。int() 只接受纯整数文本。想要 3 必须写成 int(float("3.5")) —— 先转成小数,再砍掉小数部分。选「得到 3」的人是把 int() 当成了「截断小数」的工具,它对字符串不做这种宽容处理。

</details>

**4. print(True or 未定义的变量) 会输出什么?**

- A. True,而且不会报错
- B. False
- C. 报 NameError
- D. None

<details><summary>答案与解析</summary>

**答案:A**。or 从左往右看,左边已经是 True,结果已经确定为真,右边根本不会执行 —— 这叫短路。所以不报错,直接输出 True。这说明「不报错」不等于「写对了」:右手里藏着的错会被短路悄悄跳过,等哪天左手变成 False 才突然爆出来。

</details>

**5. 分箱公式 x // 5 \* 5 的作用是?**

- A. 把 x 落到它所在那一箱的起点(5 的倍数)
- B. 把 x 除以 5
- C. 把 x 四舍五入到最近的 5 的倍数
- D. 把 x 变成字符串

<details><summary>答案与解析</summary>

**答案:A**。先 //5 得到「落在第几格」,再 \*5 还原成这一格的起点,所以 116 和 119 都会变成 115,112 会变成 110(向下取整,不是四舍五入 —— 119 也变成 115,而不是离它更近的 120)。想四舍五入到 5 的倍数得写 round(x / 5) \* 5。

</details>

## L14 · 元组与坐标点:把一对数值捆在一起

> 关键词:元组 · 解包 · 不可变 · 交换变量 · 返回多值 | 建议用时 9 分钟

你已经会用列表装一串数据了。但有一种情况列表很别扭:**这两个数天生是一对,拆开就没意义**。比如一个坐标点 —— 经度和纬度必须成对出现,单拿一个纬度出来什么也说明不了。

这种「捆在一起才有意义的小组合」用<b>元组(tuple)</b>装。写法就是把列表的方括号换成圆括号:`(116.407, 39.904)`。这一幕要讲清元组和列表到底该选哪个,以及它带来的两个顺手操作:**解包**和**一次返回多个值**。

先看一个点。从数据里取出的城市是字典,经度和纬度是分开的两个字段;把它们捆成元组,这个点才能被整个传进函数:

```python
beijing = (116.407, 39.904)
print(beijing)
print(beijing[0], beijing[1])    # 下标和列表一样,从 0 开始
print(len(beijing))              # 2
print(beijing[0:2])              # 切片也行
```

运行结果:

```text
(116.407, 39.904)
116.407 39.904
2
(116.407, 39.904)
```

> **【要点】元组和列表:只差一个括号,差别在哪**
>
> - **列表可以改**:`lst[0] = 1` 合法,`lst.append(x)` 合法。列表是「一筐会变多的东西」。
> - **元组不能改**:`t[0] = 1` 直接报 TypeError,也没有 append。元组是「一个定好就不动的组合」。
> - **什么时候用元组**:元素个数固定、而且顺序有意义的时候。坐标点 `(lon, lat)`、年月 `(2023, 1)`、函数返回的「最小值 + 最大值」都是元组。
> - **什么时候用列表**:元素个数会变、要不断往里追加的时候。比如「56 个城市的点」应该是一个列表,列表里每个元素才是元组。
> - 一句话:<b>列表装「一堆同类」,元组装「一组配套」。</b>

元组最舒服的地方是**打包与解包**。打包是把几个值写进一对括号;解包是把元组里的值一次性分给几个变量:

```python
p = (116.407, 39.904)   # 打包
lon, lat = p            # 解包:个数必须对得上
print(lon, lat)

# 解包最常见的用途:交换两个变量
a = 1
b = 2
a, b = b, a             # 一行搞定,不用中间变量 temp
print(a, b)             # 2 1
```

运行结果:

```text
116.407 39.904
2 1
```

> **【要点】a, b = b, a 是怎么做到的**
>
> 等号右边先算完,打成元组 `(b, a)`,再解包给左边两个变量。所以它**不需要一个临时变量来存中间值** —— 其他语言里交换两个数要写三行(还要一个 temp),Python 一行就够。同样的语法也出现在 `for i, v in enumerate(lst):` 里,那个 i, v 就是解包。

元组的第二个大用途是**让函数返回多个值**。别的语言要专门造一个结构,Python 直接 `return a, b`:

```python
from dataset import dataset

def lonlat(name):
    for c in dataset.cities:
        if c["name"] == name:
            return c["lon"], c["lat"]   # 逗号一隔就是元组
    return None, None                    # 找不到也要返回两个值,调用方好处理

x, y = lonlat("上海")
print(x, y)
r = lonlat("上海")
print(type(r), len(r))
```

运行结果:

```text
121.474 31.23
<class 'tuple'> 2
```

现在把元组用到真实的时空分析里。第一步是把城市变成点、装进列表;第二步是让点成对地算距离(下面这段是标准的经纬度球面距离公式):

```python
import math

def distance(p, q):
    # dlat / dlon 是两个点纬度和经度的差,先转成弧度
    dlat = math.radians(q[1] - p[1])
    dlon = math.radians(q[0] - p[0])
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(p[1])) * math.cos(math.radians(q[1])) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return round(6371 * c, 2)     # 6371 是地球平均半径(公里)

print(distance((116.407, 39.904), (121.474, 31.23)), "公里")
```

运行结果:

```text
1067.36 公里
```

> **【要点】为什么距离公式长这样**
>
> 这个公式叫 haversine。它算的是「球面上两点之间的大圆距离」—— 假设地球是个球,沿着球面走最短的那条弧。`6371` 是地球的平均半径(公里),最后乘上去就把弧度换算成了公里。你现在只要知道两件事:**传进去的是两个点(元组),传出来的是一个公里数**;以及经度是第 0 个、纬度是第 1 个 —— 顺序搞反,算出来的距离会差上千公里。

> **【注意】解包个数对不上,就是 ValueError**
>
> `lon, lat = p` 要求两边个数严格相等。写 `lon, lat, alt = p`(p 只有 2 个元素)报 `ValueError`;写 `lon = p`(把整个元组塞给一个变量)不报错,但 lon 里装的是**一整个元组**,后面 `lon > 100` 就会变成 TypeError。这类「结构错了但没报错」的 bug 比直接报错更难查 —— **所以从函数里解包之前,先确认它到底返回几个值**。

> **【注意】元组可以比大小,但要清楚它是怎么比的**
>
> 在 Python 里 `(2022, 3) < (2022, 7)` 是合法的,按「先比第 0 个、相同再比第 1 个」的**字典序**比较,结果是 True;装着元组的列表也可以直接 `sort()`,同样按这个规则排。这很方便,但要清楚它比的是什么:坐标点 `(lon, lat)` 排序就是「先按经度、经度相同再按纬度」,不一定是你想要的。想按别的字段排,就写清楚比哪一项,比如 `sorted(pts, key=lambda p: p[1])` 按纬度排。

> **【对照】这段手写代码 ↔ 真实项目里的写法**
>
> - `p = (116.407, 39.904)` ↔ `shapely.geometry.Point(lon, lat)`,或 `geopandas` 里的一行 geometry
> - 列表装元组 `[(lon, lat), ...]` ↔ `np.array([[lon, lat], ...])`,形状 `[n, 2]`
> - `lon, lat = p` 解包 ↔ `lon, lat = arr[:, 0], arr[:, 1]`(整列拆开)
> - `return lo, hi` ↔ `return (lo, hi)`,或 `return {"min": lo, "max": hi}`(字段多了就别用元组)
> - 手写 haversine ↔ `geopy.distance.geodesic(p1, p2).km`,或 `sklearn.metrics.pairwise.haversine_distances(X, Y)`
> - 手写双层循环两两算距离 ↔ `scipy.spatial.distance.cdist(A, B)`

> **【提示】什么时候该给点起个名字**
>
> 元组的缺点是「靠位置记意思」:`p[0]` 是经度还是纬度?写代码的人记得,三个月后就不一定了。所以字段一多(超过 3 个)就该换字典或类,用 `p["lon"]` 代替 `p[0]`。上课用元组是因为**两个数的组合最典型**,真实项目里判断标准很简单:数得清、顺序不容易记混,就用元组。

### 本关完整示例

```python
# ===== L14:元组与坐标点 =====
import math
from dataset import dataset

def distance(p, q):
    # p、q 都是 (经度, 纬度) 的元组;返回公里数
    dlat = math.radians(q[1] - p[1])
    dlon = math.radians(q[0] - p[0])
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(p[1])) * math.cos(math.radians(q[1])) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return round(6371 * c, 2)

print("=== 1) 元组就是一个点 ===")
beijing = (116.407, 39.904)
print("北京:", beijing)
print("经度:", beijing[0], " 纬度:", beijing[1], " 一共", len(beijing), "个数")
lon, lat = beijing
print("解包后 lon =", lon, " lat =", lat)
print()

print("=== 2) 元组不可变 ===")
try:
    beijing[0] = 120.0
except TypeError as e:
    print("改不动:", e)
print()

print("=== 3) 一行交换两个变量 ===")
a = 1
b = 2
a, b = b, a
print("交换后 a =", a, " b =", b)
print()

print("=== 4) 列表装元组:一堆点 ===")
pts = []
for c in dataset.cities[0:5]:
    pts.append((c["lon"], c["lat"]))
    print(c["name"], "->", (c["lon"], c["lat"]))
print("点数:", len(pts))
print()

print("=== 5) 函数一次返回两个值 ===")
def lonlat(name):
    for c in dataset.cities:
        if c["name"] == name:
            return c["lon"], c["lat"]
    return None, None

x, y = lonlat("上海")
print("上海:", x, y)
print("查一个不存在的城市:", lonlat("不存在的城市"))
print()

print("=== 6) 两两算距离,找最近的一对 ===")
print("北京 -> 上海:", distance(pts[0], (121.474, 31.23)), "公里")
best = distance(pts[0], pts[1])
bi = 0
bj = 1
for i in range(len(pts)):
    for j in range(i + 1, len(pts)):
        d = distance(pts[i], pts[j])
        if d < best:
            best = d
            bi = i
            bj = j
print("这 5 个城市里最近的一对:")
print(" ", dataset.cities[bi]["name"], pts[bi], "->", dataset.cities[bj]["name"], pts[bj])
print("  距离", best, "公里")
```

运行结果:

```text
=== 1) 元组就是一个点 ===
北京: (116.407, 39.904)
经度: 116.407  纬度: 39.904  一共 2 个数
解包后 lon = 116.407  lat = 39.904

=== 2) 元组不可变 ===
改不动: 'tuple' object does not support item assignment

=== 3) 一行交换两个变量 ===
交换后 a = 2  b = 1

=== 4) 列表装元组:一堆点 ===
北京 -> (116.407, 39.904)
天津 -> (117.2, 39.133)
石家庄 -> (114.514, 38.042)
太原 -> (112.549, 37.857)
呼和浩特 -> (111.749, 40.842)
点数: 5

=== 5) 函数一次返回两个值 ===
上海: 121.474 31.23
查一个不存在的城市: (None, None)

=== 6) 两两算距离,找最近的一对 ===
北京 -> 上海: 1067.36 公里
这 5 个城市里最近的一对:
  北京 (116.407, 39.904) -> 天津 (117.2, 39.133)
  距离 109.44 公里
```

### 动手练习

1. 把 pts 的范围从 dataset.cities[0:5] 改成 [0:8],看最近的一对会不会变。
2. 故意写 lon, lat, alt = beijing,看报什么错 —— 这就是解包个数对不上。
3. 加一行 print(type(pts), type(pts[0])),确认「列表装元组」这个结构。
4. 把 distance 里的 p[0] 和 p[1] 对调,再算北京到上海 —— 看距离变成多少,体会顺序搞反的后果。
5. 写一个函数 minmax(vals),用 return 一次返回最小值和最大值,再解包接收。

### 随堂检测

**1. 下面哪个操作对元组 (1, 2) 是非法的?**

- A. `print(t[0])`
- B. `t[0] = 9`
- C. `print(len(t))`
- D. `print(t[0:2])`

<details><summary>答案与解析</summary>

**答案:B**。元组不可变,不能给它的元素重新赋值,会报 TypeError。读下标、取长度、切片都是读操作,完全没问题。这也正是元组和列表最大的区别。

</details>

**2. a, b = b, a 这一行做的是什么?**

- A. 把 a 和 b 相加
- B. 把 a 赋成 b,然后 b 变成原来的 a,结果不变
- C. 报错
- D. 交换 a 和 b 的值

<details><summary>答案与解析</summary>

**答案:D**。等号右边的 b, a 会先被打包成一个元组,然后才解包给左边。因为右边先算完,两个变量的原值都还在,所以交换一次就成。如果语言不支持这种写法,就必须借一个临时变量 temp。

</details>

**3. 坐标点适合用哪种容器装?**

- A. 单独的经度和单独的纬度两个变量
- B. 列表 [lon, lat]
- C. 字符串 "lon,lat"
- D. 元组 (lon, lat)

<details><summary>答案与解析</summary>

**答案:D**。坐标是「个数固定、顺序有意义」的配套数据,正是元组的场景。列表也行但语义偏松(会让人以为可以随便 append 第三个元素);字符串要反复 split 和转数字;拆成两个变量则没法把「一个点」作为一个整体传进函数。

</details>

**4. def f(): return 1, 2 之后,r = f(),r 是什么?**

- A. 报错
- B. 元组 (1, 2)
- C. 列表 [1, 2]
- D. 第一个值 1

<details><summary>答案与解析</summary>

**答案:B**。return 后面的逗号会把值打包成元组,所以 r 是 (1, 2)。如果想只取第一个,写 x, y = f() 解包,或者 r[0]。这也解释了为什么函数「返回多个值」在 Python 里根本不需要特殊语法。

</details>

**5. 解包 lon, lat = p 时,如果 p 里有 3 个元素会怎样?**

- A. 自动补 None
- B. 多出来的元素被丢掉
- C. 报 ValueError:个数对不上
- D. lat 变成剩下的元组

<details><summary>答案与解析</summary>

**答案:C**。解包要求左右个数严格相等,多一个少一个都报 ValueError。想只取前两个得写 lon, lat = p[0], p[1]。记住:报错信息里出现 too many values to unpack 或 not enough values to unpack,就是这里的个数不匹配。

</details>

## L15 · 迭代与算法思维:累加器、最值、线性搜索

> 关键词:累加器 · 最值陷阱 · 计数筛选 · 线性搜索 · 嵌套循环 | 建议用时 10 分钟

前 12 幕你学会了 `for` 的写法,但「会写循环」和「会用循环解决问题」是两件事。真实的数据处理,九成都是这几件事的重复:**把一堆数加起来、找出最大/最小的那个、数一数满足条件的有几个、按条件挑出来、找一个特定的东西**。

这几个套路有名字,叫**累加器模式**、**最值模式**、**计数/筛选**、**线性搜索**。第二层里那些看起来复杂的算法,骨架全都是它们。这一幕把它们一个个写清楚,以后你遇到新问题,先想「它属于这几个里的哪一个」。

第一个套路是**累加器**:准备一个变量存「到目前为止的结果」,然后每读一个数就更新它一次。求和、求平均、求个数,都是同一个模子:

```python
from dataset import dataset

vals = []
for st in dataset.stations:
    vals.append(st["pm25"])

total = 0                     # 累加器:从 0 开始
total = total + vals[0]
total = total + vals[1]
print("前两个:", total, " 全部 50 个:", sum(vals))
print("平均:", round(sum(vals) / len(vals), 2))
```

运行结果:

```text
前两个: 100  全部 50 个: 2252
平均: 45.04
```

> **【要点】累加器模式的四步**
>
> - **第一步**:循环外面给累加器一个初始值(`total = 0`)。
> - **第二步**:循环里面,每读到一个值就把它并进累加器(`total = total + v`)。
> - **第三步**:循环结束后,累加器里就是最终结果 —— **打印必须在循环外面**,写在里面会打出一路中间值。
> - **第四步**:要用总数除以个数时,个数用 `len(vals)` 而不是硬写一个常数。

第二个套路是**求最值**。它最容易出错的地方不是循环,而是**初始值**:

```python
from dataset import dataset

vals = []
for st in dataset.stations:
    vals.append(st["pm25"])

# 正确:拿第一个值当前任擂主
best = vals[0]
for v in vals:
    if v > best:
        best = v
print("最大:", best)

# 危险:从 0 起手 —— 现在恰好对,换一批全负的数据就错了
zero_start = 0
for v in vals:
    if v > zero_start:
        zero_start = v
print("从 0 起手:", zero_start)
```

运行结果:

```text
最大: 91
从 0 起手: 91
```

> **【注意】最值初始值的两种错法**
>
> 求最大时写 `best = 0`,如果数据里全是负数(比如全年最冷月的零下气温),结果永远是 0 —— 一个根本不在数据里的数。求最小时写 `best = 0` 更糟,它会把任何正数都判成「更小」,最后返回 0。**正确做法:拿数据里的第一个值当前任擂主(`best = vals[0]`),让真实数据自己比出来**。还有两个同源的坑:空列表上写 `vals[0]` 会 IndexError(所以要先判断 `len(vals) > 0`),以及想同时求最大和最小必须用两个独立变量、不能共用一个。

第三个套路是**计数与筛选**,区别只在于:计数是「符合就加 1」,筛选是「符合就装进新列表」:

```python
from dataset import dataset

vals = []
for st in dataset.stations:
    vals.append(st["pm25"])

cnt = 0                       # 计数
for v in vals:
    if v > 50:
        cnt = cnt + 1
print("超过 50 的站点:", cnt)

picked = []                   # 筛选
for st in dataset.stations:
    if st["pm25"] > 50:
        picked.append(st["name"])
print("名单:", picked[0:5], "...共", len(picked))
```

运行结果:

```text
超过 50 的站点: 18
名单: ['石家庄站', '太原站', '唐山站', '保定站', '南京站'] ...共 18
```

第四个套路是**线性搜索**:从前往后一个一个看,找到就停。这里的 `break` 不是省事,而是真的省时间 —— **数据整理好时,找到就能提前退出**:

```python
from dataset import dataset

target = None
for st in dataset.stations:
    if st["pm25"] > 85:
        target = st
        break                 # 找到第一个就退出,后面不用再看
if target is None:
    print("没有符合条件的站点")
else:
    print("第一个:", target["name"], target["pm25"])
```

运行结果:

```text
第一个: 哈尔滨站 91
```

> **【要点】搜索要区分「第一个」和「全部」**
>
> - 要「第一个符合条件的」→ 循环里 `break`,循环后判断是否找到。
> - 要「所有符合条件的」→ 不要 break,把结果 `append` 进列表。
> - 要「是否存在」→ 也是一找到就 break,最后看标志变量。
> - 找不到时返回什么?函数里写成 `return` None 比 `return` 0 安全 —— 0 有可能是一个合法结果,None 不会。

第五个套路是**双层循环**:外层每走一步,内层要把一整轮走完。它是「任意两个元素互相比较」的标准写法 —— 找最近的两个站、算两两之间的相似度,都用它:

```python
names = ["A", "B", "C", "D"]
for i in range(len(names)):
    for j in range(i + 1, len(names)):
        print(names[i], "-", names[j])
# 4 个元素 → 6 对。组合数是 n*(n-1)/2,不是 n*n
```

运行结果:

```text
A - B
A - C
A - D
B - C
B - D
C - D
```

> **【注意】内层从 i + 1 开始,不是从 0 开始**
>
> 写成 `for j in range(len(names))` 会把每一对算两遍(A-B 和 B-A),还会跟自己配成一对(A-A、B-B)。标准写法是 **内层从 i + 1 开始**,这样每一对只出现一次,数量正好是 n(n−1)/2。**代价提醒**:双层循环的步数是 n² 级增长。56 个城市要跑 1540 对,几百个点就变成几万对,几千个点就要上千万次 —— 真实项目里这一步要换成向量化的成对距离矩阵,不是用双层循环硬算

> **【对照】这段手写代码 ↔ 真实项目里的写法**
>
> - 手写累加器 `total = total + v` ↔ `sum(vals)` / `np.sum(a)` / `df["pm25"].sum()`
> - 手写求最大 `best = vals[0]` + 循环 ↔ `max(vals)` / `df["pm25"].max()`;要连位置一起拿用 `max(range(n), key=lambda i: vals[i])` 或 `a.argmax()`
> - 手写计数 `cnt = cnt + 1` ↔ `len(df[df["pm25"] > 50])` 或 `(a > 50).sum()`(布尔值当 1/0 求和)
> - 手写筛选 `picked.append(...)` ↔ `df[df["pm25"] > 50]` / `[x for x in vals if x > 50]`(列表推导式)
> - 手写线性搜索 + break ↔ `df.index[df["pm25"] > 85][0]`,或 `next(i for i, v in enumerate(vals) if v > 85)`
> - 手写双层循环配对 ↔ `scipy.spatial.distance.pdist(A)`
> - 手写字典计数 ↔ `df["region"].value_counts()` / `collections.Counter`

> **【提示】把重复做的事抽象成循环,再抽象成函数**
>
> 写代码的顺序永远是这样:先写死一遍(处理第 1 个),再把「加一」换成循环变量,让它处理第 2 个到第 n 个,最后如果这段逻辑要复用,把它包成 `def`。本幕主代码里 `find_max`、`count_if` 就是这么来的 —— **先会手写,再学会把套路函数化**,下一步才是用内置的 `max` / `sum` 替换掉自己的版本。

### 本关完整示例

```python
# ===== L15:迭代与算法思维(用 50 个监测站)=====

from dataset import dataset

vals = []
for st in dataset.stations:
    vals.append(st["pm25"])

print("=== 1) 累加器:越写越长的加法 ===")
total = 0
for v in vals:
    total = total + v
print("个数:", len(vals), " 总和:", total, " 均值:", round(total / len(vals), 2))
print()

print("=== 2) 求最值:初始值不能瞎写 ===")
best = vals[0]          # 正确:拿第一个值当前任擂主
for v in vals:
    if v > best:
        best = v
print("手写最大:", best, " 内置 max:", max(vals))
zero_start = 0
for v in vals:
    if v > zero_start:
        zero_start = v
print("从 0 起手:", zero_start, "(这批数据恰好对,换成全负的数据就错)")
print()

print("=== 3) 计数与筛选 ===")
cnt = 0
for v in vals:
    if v > 50:
        cnt = cnt + 1
print("超过 50 的站点数:", cnt)
picked = []
for st in dataset.stations:
    if st["pm25"] > 50:
        picked.append(st["name"])
print("前 5 个:", picked[0:5], " 共", len(picked), "个")
print()

print("=== 4) 线性搜索与提前退出 ===")
target = None
for st in dataset.stations:
    if st["pm25"] > 85:
        target = st
        break
if target is None:
    print("没有超过 85 的站点")
else:
    print("第一个超过 85 的:", target["name"], target["pm25"])
print()

print("=== 5) 双层循环:两两配对 ===")
names = ["A", "B", "C", "D"]
pairs = 0
for i in range(len(names)):
    for j in range(i + 1, len(names)):
        pairs = pairs + 1
print("4 个站两两配对共", pairs, "对;公式 4*3/2 =", 4 * 3 // 2)
print()

print("=== 6) 把套路写成函数 ===")
def find_max(vals):
    best = vals[0]
    for v in vals:
        if v > best:
            best = v
    return best

def count_if(vals, threshold):
    cnt = 0
    for v in vals:
        if v > threshold:
            cnt = cnt + 1
    return cnt

print("find_max:", find_max(vals), "  count_if(> 50):", count_if(vals, 50))
print()

print("=== 7) 套路组合:按大区统计 PM2.5 ===")
city_region = {}
for c in dataset.cities:
    city_region[c["name"]] = c["region"]

sums = {}
counts = {}
for st in dataset.stations:
    r = city_region[st["city"]]
    if r in sums:
        sums[r] = sums[r] + st["pm25"]
        counts[r] = counts[r] + 1
    else:
        sums[r] = st["pm25"]
        counts[r] = 1
print("合计站点:", len(dataset.stations), "个")
for r in sums:
    print(r, "站点", counts[r], "个,平均 PM2.5", round(sums[r] / counts[r], 2))
```

运行结果:

```text
=== 1) 累加器:越写越长的加法 ===
个数: 50  总和: 2252  均值: 45.04

=== 2) 求最值:初始值不能瞎写 ===
手写最大: 91  内置 max: 91
从 0 起手: 91 (这批数据恰好对,换成全负的数据就错)

=== 3) 计数与筛选 ===
超过 50 的站点数: 18
前 5 个: ['石家庄站', '太原站', '唐山站', '保定站', '南京站']  共 18 个

=== 4) 线性搜索与提前退出 ===
第一个超过 85 的: 哈尔滨站 91

=== 5) 双层循环:两两配对 ===
4 个站两两配对共 6 对;公式 4*3/2 = 6

=== 6) 把套路写成函数 ===
find_max: 91   count_if(> 50): 18

=== 7) 套路组合:按大区统计 PM2.5 ===
合计站点: 50 个
华北 站点 8 个,平均 PM2.5 57.5
华东 站点 12 个,平均 PM2.5 45.42
华南 站点 9 个,平均 PM2.5 28.67
华中 站点 6 个,平均 PM2.5 43.67
西南 站点 6 个,平均 PM2.5 32.0
西北 站点 6 个,平均 PM2.5 53.17
东北 站点 3 个,平均 PM2.5 72.0
```

### 动手练习

1. 把「超过 50」改成「超过均值」—— 先算均值再当阈值,体会阈值也可以是算出来的。
2. 把求最大的初始值故意改成 0,再把 vals 换成 [-5, -9, -2],看结果为什么不对。
3. 用同样的套路求 PM2.5 的最小值,并找出它属于哪个站(提示:最小值用小于号)。
4. 把「第一个超过 85」的 break 删掉,改成收集所有超过 85 的站点,比较两种写法的输出。
5. 把双层循环的配对数量公式改成 8 个站,先算 8\*7/2,再跑代码验证。

### 随堂检测

**1. 求一组数的最大值时,best 的初始值应该取什么?**

- A. 一个很大的数
- B. 0
- C. 1
- D. 数据里的第一个值 vals[0]

<details><summary>答案与解析</summary>

**答案:D**。拿第一个值当前任擂主,让剩下的数据自己来比,结果一定是数据里真实存在的值。写 0 的话,如果数据全是负数,最大值就永远是 0 —— 一个不存在于数据里的数;写很大的数在求最小值时是同理的错法。

</details>

**2. 累加器 total = total + v 里的 total,初始值一般是多少?**

- A. 第一个值 vals[0]
- B. 1
- C. 0
- D. 不用给初始值

<details><summary>答案与解析</summary>

**答案:C**。求和从 0 开始,因为加 0 不改变结果。求积才是从 1 开始。注意和「求最值」区分:最值必须用 vals[0] 起手,不能沿用 0 —— 这两个套路长得很像,但初始值的规则完全不同,这是最容易混的一处。

</details>

**3. 双层循环配对时,内层为什么写成 for j in range(i + 1, len(names))?**

- A. 防止下标越界,不这么写会报错
- B. 这样每一对只算一次,不会重复也不会自己和自己配
- C. 因为 j 必须比 i 大
- D. 这样跑得更快

<details><summary>答案与解析</summary>

**答案:B**。如果内层从 0 开始,A-B 和 B-A 会被算两遍,还会出现 A-A 这种自己配自己的情况,总数从 6 变成 16。从 i+1 开始,每一对无重复地出现一次,总数正好是 n(n−1)/2。它不这么写也不会报错(只是结果错),所以更危险。

</details>

**4. 要在站点列表里找「第一个 PM2.5 超过 85 的站」,循环里该怎么做?**

- A. 不能用循环,必须排序
- B. 找到就继续循环完,最后看最后一个
- C. 用 while True 死循环
- D. 找到就记下来并 break,循环后判断是否找到

<details><summary>答案与解析</summary>

**答案:D**。「第一个」意味着找到就没有必要再看后面,break 是对的。别忘了循环后判断「到底找到没有」—— 如果没有 break 过,结果变量还是初始值,直接打印会打出一个不存在的结果或者报错。要找全部而不是第一个,才需要去掉 break。

</details>

**5. 「统计满足条件的个数」和「筛选出满足条件的数据」有什么不同?**

- A. 计数只累加一个数字,筛选要把符合条件的元素装进新列表
- B. 完全一样
- C. 筛选不能用 if
- D. 计数必须用 while

<details><summary>答案与解析</summary>

**答案:A**。两者的判断条件一模一样,区别只在「符合之后做什么」:计数是 cnt = cnt + 1(只留数量),筛选是 picked.append(x)(留下内容)。实际分析里常常先计数看看有多少,再筛选出来具体看是哪些 —— 所以两个套路经常一起出现。

</details>

## L16 · 调试与常见错误:看懂报错、定位问题

> 关键词:常见错误 · 读报错 · print 排查 · 二分定位 · 防御式编程 | 建议用时 9 分钟

写代码的时间,**一大半花在「为什么它不work」上**。所以「看懂报错」不是附加技能,而是核心技能。好消息是:Python 的报错信息其实非常直白,它告诉了你**错在哪一行、错在哪一类、往往还告诉你具体是哪个值**。

这一幕做三件事:把最常见的几类报错和它们的典型触发条件列清楚;教你一套定位问题的固定动作(打印中间变量、二分法缩小范围);最后讲**防御式编程** —— 与其等它崩,不如一开始就把不合规的数据挡在门外。

先看报错长什么样。Python 的报错是**从下往上读**的:最后一行是结论(错误类型 + 说明),上面几行是「调用链」,告诉你是从哪条路走到这里的。下面这段故意写错(分母没做保护),第一组能跑出结果,第二组传了空列表:

```python
def avg(vals):
    total = 0
    for v in vals:
        total = total + v
    return total / len(vals)     # vals 为空时,这里就是「除以 0」

try:
    print("第一组:", avg([50, 40]))
    print("第二组:", avg([]))      # ← 崩在这一行
except ZeroDivisionError as e:
    print("崩了:", e)
    print("读法:错误类型是 ZeroDivisionError,说明里写着除数为 0")
```

运行结果:

```text
第一组: 45.0
崩了: division by zero
读法:错误类型是 ZeroDivisionError,说明里写着除数为 0
```

> **【要点】读报错的三步固定动作**
>
> - **第一步**:看最后一行冒号左边的类型 —— 它直接告诉你是哪一类问题(类型错?下标越界?键不存在?除以零?)。
> - **第二步**:看最后一行冒号右边的说明,通常会带上具体的值(比如 `KeyError: 'b'` 直接告诉你缺的是哪个键,`IndexError: list index out of range` 告诉你下标越界了)。
> - **第三步**:往上找**最后一个属于你自己文件的行号**(跳过解释器和库的行),那就是要改的地方。
> - 顺序反了会很痛苦:只盯着最后一行不看行号,只能猜;只看行号不看类型,又会去改错方向。

下面是零基础阶段几乎一定会撞上的八类报错。记住典型触发条件,出问题时第一眼就能对上号:

| 错误类型 | 典型触发 | 怎么改 |
|---|---|---|
| NameError | 变量名拼错,或者用在了赋值之前(比如循环外用了循环变量) | 检查拼写;把变量先赋初值 |
| TypeError | "5" + 5 字符串加数字;给函数传错类型;len(5) | 用 int() / str() 转换,或先 type() 看看是什么 |
| ValueError | int("abc")、int("3.5") 这类「类型对但值不对」 | 先清洗数据,或用 try / except 挡掉 |
| IndexError | 列表只有 3 个元素却取 [5];循环里 i+1 越界 | 打印 len() 核对;注意 range 的边界 |
| KeyError | 字典里没有这个键,比如把 "北京站" 当键去查 "北京" | 先 if k in d 判断,或用 d.get(k, 默认值) |
| ZeroDivisionError | 除以 0,或对空列表求平均(个数是 0) | 先判断分母/长度是否大于 0 |
| IndentationError | 该缩进的地方没缩进,或空格和 Tab 混用 | 统一用 4 个空格;看报错指出的行 |
| AttributeError | 调了对象没有的方法或属性,比如 x = 5 后写 x.upper()、dataset.city | 检查拼写和类型;Python 3.10+ 常会提示 Did you mean: ... |

光认识类型还不够,得会定位。最朴素也最有效的方法是**打印中间变量** —— 让程序把「它以为的」告诉你:

```python
from dataset import dataset

vals = []
for st in dataset.stations[0:3]:
    print("[调试] 读到的站点:", st["id"], st["pm25"])   # 先确认它到底读到了什么
    vals.append(st["pm25"])
print("[调试] 累加前 vals =", vals, " 长度 =", len(vals))
print("平均:", round(sum(vals) / len(vals), 2))
```

运行结果:

```text
[调试] 读到的站点: S001 50
[调试] 读到的站点: S002 50
[调试] 读到的站点: S003 74
[调试] 累加前 vals = [50, 50, 74]  长度 = 3
平均: 58.0
```

> **【要点】二分法缩小范围**
>
> 报错只说「最后崩在哪」,但真正的错误往往在前面就埋下了。定位办法和查字典一样:**在代码中间插一句打印,看这一句的输出对不对**。对,说明问题在下半段;不对,问题在上半段。每查一次范围就砍一半,几十行代码三五次就能锁定。打印调试的时候给输出加个标记(比如 `[调试]`),改完记得全删掉 —— 这也是为什么真实项目里用日志而不是 print。

> **【注意】三种「不报错但结果是错的」最费时间**
>
> 报错其实是好事,它至少告诉你有问题。真正难查的是这三种:**一是变量名写成了另一个存在的变量**(把 `pm25` 写成 `temp`,不报错,结果全错);**二是循环里把结果累加进了错误的变量**(把 `sums[r]` 写成了 `sums["北京"]`,所有大区的结果都一样);**三是缩进层级错了**(把 `total = total + v` 写到了 `if` 里面,少累加了本该累加的值)。这三种都只能靠**打印中间结果 + 手算一个小例子对答案**来发现 —— 所以写完一段统计代码,永远先用 3 个数据手算一遍,对上了再上真实数据集。

最后是防御式编程:与其等坏数据让程序崩在半路,不如在函数的入口就把不合规的挡回去。它和 try / except 的区别是 —— **try 是事后补救,校验是事前预防**:

```python
def average(vals):
    if len(vals) == 0:        # 先挡空列表,否则下面除以 0
        return None
    for v in vals:
        if v < 0:             # PM2.5 不可能是负的
            return None
    total = 0
    for v in vals:
        total = total + v
    return round(total / len(vals), 2)

print(average([50, 40, 60]))   # 50.0
print(average([]))             # None
print(average([50, -1, 60]))   # None
```

运行结果:

```text
50.0
None
None
```

> **【要点】校验失败时返回什么**
>
> - 返回 `None` 表示「这个问题我答不了」,调用方一看就知道要跳过。
> - 不要返回 0 —— 0 是一个合法结果(PM2.5 可以是 0),调用方分不清「真的是 0」还是「出错了」。
> - 也可以直接 `raise` ValueError 让程序停下来并说清原因,适合「这个错误绝不能忍」的场景。
> - 真实项目里这一步叫<b>数据校验(data validation)</b>,通常写成独立函数,在读入数据的入口统一做一次。

> **【对照】这段手写代码 ↔ 真实项目里的写法**
>
> - `if k in d:` / `d.get(k, 0)` 防 KeyError ↔ `df.reindex(...)` / `collections.defaultdict(int)`
> - `if len(vals) == 0: return None` ↔ `np.mean([])` 会给出 nan + 警告;专业做法是 `pd.Series(vals).mean(skipna=True)`
> - 手写 `if v < 0: return None` ↔ `pd.to_numeric(s, errors="coerce")` / `df.clip(lower=0)` / `df.dropna()`
> - `print("[调试]", x)` ↔ `logging.debug(...)`、`breakpoint()`,或 VS Code / PyCharm 里打断点单步调试
> - 手写二分定位 ↔ `pdb` 的 `n`(下一行)/ `p 变量`(打印)/ `c`(继续)三件套
> - `try / except ValueError` 兜底 ↔ 读表时 `pd.read_csv(..., na_values=["", "NA", "-"])`

> **【提示】报错信息要读完整**
>
> 很多人看到一片红字就慌了,开始乱改。正确动作是**把最后一行读完**:`KeyError: 'pm2'` 已经告诉你缺的是哪个键;Python 3.10 以后,拼错名字时还会附上提示,比如 `NameError: name 'totl' is not defined. Did you mean: 'total'?` —— 它常常已经告诉你要改成什么了。

### 本关完整示例

```python
# ===== L16:调试与常见错误 =====

from dataset import dataset

print("=== 1) 六种最常撞上的报错 ===")
cases = ["name", "type", "value", "index", "key", "zero"]
for k in cases:
    try:
        if k == "name":
            print(never_defined)
        elif k == "type":
            print("编号:" + 7)
        elif k == "value":
            print(int("abc"))
        elif k == "index":
            print([10, 20][5])
        elif k == "key":
            print({"a": 1}["b"])
        else:
            print(7 % 0)
    except NameError as e:
        print("NameError       : 变量名打错,或者还没赋值就用了")
    except TypeError as e:
        print("TypeError       : 类型不匹配,不能这样运算")
    except ValueError as e:
        print("ValueError      : 类型对但值不对,转换失败")
    except IndexError as e:
        print("IndexError      : 下标越界")
    except KeyError as e:
        print("KeyError        : 字典里没有这个键")
    except ZeroDivisionError as e:
        print("ZeroDivisionError: 除数是 0")
print()

print("=== 2) 打印中间变量:让程序告诉你它看到了什么 ===")
vals = []
for st in dataset.stations[0:4]:
    print("[调试] 读到", st["id"], st["name"], "pm25 =", st["pm25"])
    vals.append(st["pm25"])
print("[调试] 累加前 vals =", vals, " 长度 =", len(vals))
print("平均值:", round(sum(vals) / len(vals), 2))
print()

print("=== 3) 二分法定位:先看一半对不对 ===")
print("中途快照 → 全部读完,两次打印一对照,就知道是哪一段开始不对")
part = vals[0:2]
print("  前半段:", part, " 它自己的均值:", round(sum(part) / len(part), 2))
print("  后半段:", vals[2:4], " 它自己的均值:", round(sum(vals[2:4]) / len(vals[2:4]), 2))
print()

print("=== 4) 防御式编程:先把不合规的挡在门外 ===")
def average(vals):
    if len(vals) == 0:
        return None          # 空列表 → 不能算,返回 None
    for v in vals:
        if v < 0:
            return None      # PM2.5 不可能是负的 → 数据有问题
    total = 0
    for v in vals:
        total = total + v
    return round(total / len(vals), 2)

print("正常数据:", average([50, 40, 60]))
print("空列表  :", average([]))
print("含负数  :", average([50, -1, 60]))
print()

print("=== 5) 真实数据上的排查:先体检,再统计 ===")
pms = []
for st in dataset.stations:
    pms.append(st["pm25"])
print("样本数:", len(pms))
print("最小:", min(pms), " 最大:", max(pms), " 均值:", round(sum(pms) / len(pms), 2))
zero = 0
for v in pms:
    if v == 0:
        zero = zero + 1
print("等于 0 的样本:", zero, "个(如果很多,要怀疑 0 其实是缺测值,不是真的没有污染)")
```

运行结果:

```text
=== 1) 六种最常撞上的报错 ===
NameError       : 变量名打错,或者还没赋值就用了
TypeError       : 类型不匹配,不能这样运算
ValueError      : 类型对但值不对,转换失败
IndexError      : 下标越界
KeyError        : 字典里没有这个键
ZeroDivisionError: 除数是 0

=== 2) 打印中间变量:让程序告诉你它看到了什么 ===
[调试] 读到 S001 北京站 pm25 = 50
[调试] 读到 S002 天津站 pm25 = 50
[调试] 读到 S003 石家庄站 pm25 = 74
[调试] 读到 S004 太原站 pm25 = 52
[调试] 累加前 vals = [50, 50, 74, 52]  长度 = 4
平均值: 56.5

=== 3) 二分法定位:先看一半对不对 ===
中途快照 → 全部读完,两次打印一对照,就知道是哪一段开始不对
  前半段: [50, 50]  它自己的均值: 50.0
  后半段: [74, 52]  它自己的均值: 63.0

=== 4) 防御式编程:先把不合规的挡在门外 ===
正常数据: 50.0
空列表  : None
含负数  : None

=== 5) 真实数据上的排查:先体检,再统计 ===
样本数: 50
最小: 12  最大: 91  均值: 45.04
等于 0 的样本: 0 个(如果很多,要怀疑 0 其实是缺测值,不是真的没有污染)
```

### 动手练习

1. 把第 1 段里的 "type" 分支改成 print("abc" - 1),看报的错误类型是不是还是 TypeError。
2. 故意把某个 st["pm25"] 写成 st["pm2"],看 KeyError 的最后一行显示的是哪个键。
3. 在 average 里把 len(vals) == 0 的判断删掉,再调 average([]),看 ZeroDivisionError 长什么样。
4. 写一个 first\_station(city) 函数,找不到时返回 None,调用处必须判断后再用。
5. 把 dataset.stations 换成 dataset.cities,统计 pop 的均值和 0 值个数。

### 随堂检测

**1. 看到报错时,应该先看哪一行?**

- A. 最后一行:错误类型 + 说明
- B. 中间最长的那行
- C. 第一行的 Traceback
- D. 随便看哪行都一样

<details><summary>答案与解析</summary>

**答案:A**。Python 的报错从下往上读:最后一行给出错误类型和具体说明(经常连值是哪个都写了),往上才是调用链和行号。先看最后一行能立刻确定问题大类,再往上找自己文件的行号定位到要改的地方。

</details>

**2. int("abc") 会报什么错?**

- A. NameError
- B. 不报错,返回 0
- C. TypeError
- D. ValueError

<details><summary>答案与解析</summary>

**答案:D**。int() 拿到的是字符串 —— 类型是对的,所以不是 TypeError;但这个字符串的内容不是一个整数,属于「值不对」,所以是 ValueError。区分方法:TypeError 是「这个东西根本不能这么用」,ValueError 是「类型可以,但值不行」。

</details>

**3. 下面哪种情况会报 KeyError?**

- A. 除以 0
- B. 用列表越界的下标 lst[9]
- C. 用字典里不存在的键去取值 d["b"]
- D. 变量名拼错

<details><summary>答案与解析</summary>

**答案:C**。字典靠键取值,键不存在就是 KeyError;列表靠下标取值,下标越界是 IndexError —— 这两个最容易混。除法是 ZeroDivisionError,变量名拼错是 NameError。记住:字典找不到是 Key,列表找不到是 Index。

</details>

**4. 程序跑出来结果明显不对,但一行报错都没有,最有效的第一步是什么?**

- A. 把代码全部重写
- B. 换个 Python 版本
- C. 在代码中间打印关键变量,看它从哪一步开始不对
- D. 加大数据量再跑一次

<details><summary>答案与解析</summary>

**答案:C**。不报错说明每个操作单独看都合法,问题藏在中途的某个值上。打印中间变量(或二分法插打印)能立刻看出是哪一段开始偏的。重写会浪费时间还可能引入新错;换版本和数据量都改变不了逻辑本身的错误。

</details>

**5. 函数算不出结果时,返回 None 比返回 0 好在哪?**

- A. 返回 0 会报错
- B. 没有区别
- C. None 运行更快
- D. 0 可能是合法的真实结果,调用方分不清「真的是 0」还是「出错了」

<details><summary>答案与解析</summary>

**答案:D**。PM2.5、气温、计数这些量都可能是 0,所以 0 是一个有意义的答案。返回 None 是一个不可能与真实结果混淆的信号,调用方写 if v is None 就能准确地跳过或提示。这就是「缺失值要用单独的标记」的原因 —— pandas 里用 NaN 也是同一个道理。

</details>

## L17 · 日期时间与集合:给数据装上时间轴

> 关键词:月份编码 · 时间比较 · 月份加减 · set 去重 · 邻域集合 | 建议用时 10 分钟

前面几幕里,数据都是「空间」的 —— 点、坐标、距离。但**时空分析的另一半是时间**,而原课程一直没讲时间怎么在代码里表示。

时间有一个和数字不太一样的地方:**它不是一条连续的线,而是「年 + 月 + 日」这种分层结构**。所以「2023 年 1 月」比「2021 年 12 月」晚,不能直接当数字比;「2023 年 1 月再过一个月」也不是加 1 等于 2023 年 2 月。这一幕讲清怎么在代码里表示和运算时间,以及怎么用字典的键来模拟「集合」做去重和找共同元素。

先看最省事的表示法。既然数据里的时间本来就是 `"2021-01"` 这样的文本,那就别急着转换 —— **只要格式统一成「年-月」、月份补足两位,字符串本身就能直接比大小和排序**:

```python
print("2023-01" > "2021-12")     # True:先比第 1 个字符
print("2021-09" < "2021-10")     # True:前 5 个字符相同,第 6 个字符 "0" < "1"
months = ["2023-01", "2021-05", "2022-11"]
months.sort()
print(months)                     # 自动按时间先后排好
```

运行结果:

```text
True
True
['2021-05', '2022-11', '2023-01']
```

> **【要点】字符串为什么能直接比时间**
>
> 字符串比较是**从左到右逐位比字符的编码**。只要格式固定成「4 位年 - 2 位月 - 2 位日」,高位在前,逐位比较的结果就和按时间比较完全一致。**前提是月份必须补零**:`"2021-9"` 和 `"2021-10"` 按字符串比会得出 9 比 1 大(于是 9 月排在 10 月后面),这就是经典的坑。时间的文本格式永远统一成补零的定长格式,是这一行能成立的全部原因。

第二种表示法是**把年月压成一个整数**:`2021 年 1 月 → 202101`。它的好处是能直接做加减法 —— 算月份差、加几个月都不用重新拆:

```python
def parse_month(s):
    # "2021-01" → 202101
    return int(s[0:4]) * 100 + int(s[5:7])

def add_month(ym, k):
    # 202101 加 k 个月。思路:先换算成「从 0 年 1 月起的总月数」,加完再换回来
    y = ym // 100          # 取出年
    m = ym % 100           # 取出月
    total = y * 12 + (m - 1) + k   # 总月数
    return total // 12 * 100 + total % 12 + 1

print(parse_month("2021-01"))
print(add_month(202301, 1))    # 202302
print(add_month(202312, 1))    # 跨年 → 202401
print(add_month(202101, -1))   # 往回走 → 202012
```

运行结果:

```text
202101
202302
202401
202012
```

> **【要点】add\_month 在算什么**
>
> 月不是十进制的一位,不能直接加 —— 202312 加 1 不能得 202313。**正确思路是换一个「每月都是一个整数」的坐标系**:总月数 = 年 × 12 + (月 − 1)。在这个坐标系里加减就是普通整数加减,加完再反算回「年 × 100 + 月」。减 1 表示上月、减 12 表示去年同月、加 12 表示明年同月 —— **L22 的季节性分析(拿去年同月对比)用的就是这个偏移量**。

现在把时间轴接到真实数据上。`dataset.temp_series` 里每个城市有一个 `start`(起点月份)和一个 36 个月的气温列表。**知道起点、又知道「值是按月连续排的」,就能把任意一个下标翻译成具体的年月** —— 这里先用两条朴素公式(把年月压成 202101 这样的整数、加几个月就换算成总月数再换回来)演示这件事:

```python
from dataset import dataset

t = dataset.temp_series[0]
vals = t["values"]
start = int(t["start"][0:4]) * 100 + int(t["start"][5:7])   # "2021-01" → 202101
print("城市:", t["city"], " 起点:", t["start"], " 共", len(vals), "个月")
for i in [0, 11, 12, 35]:
    total = start // 100 * 12 + (start % 100 - 1) + i      # 换算成「总月数」再加偏移
    ym = total // 12 * 100 + total % 12 + 1                # 换回「年 × 100 + 月」
    print("  第", i, "个数 =", vals[i], "度,对应", ym)
```

运行结果:

```text
城市: 北京  起点: 2021-01  共 36 个月
  第 0 个数 = -2.3 度,对应 202101
  第 11 个数 = -1 度,对应 202112
  第 12 个数 = -2.6 度,对应 202201
  第 35 个数 = -0.2 度,对应 202312
```

接下来是这一幕的第二半:**集合**。Python 有专门的 `set`(集合)类型,不过我们先用**字典的键**把集合的原理写一遍,再看 set 的标准写法。道理很简单:**字典的键天生不重复** —— 同一个键写两次,后面的会覆盖前面的,于是键的集合就是去重后的结果:

```python
from dataset import dataset

region_set = {}          # 用字典当集合:键就是元素
region_order = []        # 想保留出现顺序,就再拿一个列表记着
for c in dataset.cities:
    r = c["region"]
    if r not in region_set:
        region_set[r] = 1
        region_order.append(r)
print("56 个城市归成", len(region_set), "个大区")
print(region_order)
```

运行结果:

```text
56 个城市归成 7 个大区
['华北', '华东', '华南', '华中', '西南', '西北', '东北']
```

> **【要点】用字典键模拟集合的三个操作**
>
> - **去重**:`d[x] = 1`,最后 `len(d)` 就是不同元素的个数。
> - **判断是否在集合里**:`if x in d:`。这比在列表里写 `if x in lst` 快得多 —— 列表要一个个看过去,字典直接查键。
> - <b>求交集(共同元素)</b>:两个字典都建好,遍历其中一个,`if k in other:` 就说明两边都有。
> - <b>求差集(只在一边)</b>:同样遍历一个,`if k not in other:`。
> - 顺序问题:Python 3.7 起字典保证按插入顺序遍历,但 **set 是无序的**,要稳定输出就自己 `sorted()` 一下。

最后把两个半边拼起来:用集合找「有站点的城市」和「56 个城市」的交集与差集。这是时空数据最常见的对齐工作 —— **两份数据要对得上,先看它们的键重合多少**:

```python
from dataset import dataset

station_cities = {}
for st in dataset.stations:
    station_cities[st["city"]] = 1

both = []
for c in dataset.cities:
    if c["name"] in station_cities:
        both.append(c["name"])
print("既在 56 城表里、又有监测站的:", len(both), "个")

only_city = []
for c in dataset.cities:
    if c["name"] not in station_cities:
        only_city.append(c["name"])
print("只有城市、没有站的:", len(only_city), "个")
```

运行结果:

```text
既在 56 城表里、又有监测站的: 50 个
只有城市、没有站的: 6 个
```

理解了字典版之后,再看 Python 自带的 `set`:`add()` 加元素,`&` 求交集,`-` 求差集,`|` 求并集:

```python
from dataset import dataset

regions = set()
for c in dataset.cities:
    regions.add(c["region"])          # 重复的自动合并
print("大区个数:", len(regions))

station_cities = set()
for st in dataset.stations:
    station_cities.add(st["city"])
city_names = set()
for c in dataset.cities:
    city_names.add(c["name"])

print("交集(有站的城市):", len(city_names & station_cities), "个")
print("差集(没站的城市):", sorted(city_names - station_cities))
```

运行结果:

```text
大区个数: 7
交集(有站的城市): 50 个
差集(没站的城市): ['吉林', '喀什', '大庆', '敦煌', '长春', '齐齐哈尔']
```

> **【注意】两个真要踩的坑:月份补零 和 日期顺序**
>
> **坑一**:月份没补零。`"2021-9"` 和 `"2021-10"` 按字符串比较时,前 5 个字符相同,第 6 个字符 "9" 大于 "1",于是 `"2021-9" > "2021-10"` 得到 True —— 9 月被排到了 10 月后面。而且 `"2021-9"[5:7]` 只切出 `"9"`,和 `"2021-09"[5:7]` 的 `"09"` 也对不齐。所以数据进来第一件事就是统一成补零的定长格式。**坑二**:`add_month` 里的 `m - 1` 和最后的 `+ 1` 是一对,少一个都会错位:比如把 `(m - 1)` 写成 `m`,202101 加 1 个月会算成 202103;两个都漏掉,202111 加 1 个月会得到 202200(0 月,不存在)。

> **【对照】这段手写代码 ↔ 真实项目里的写法**
>
> - 手写 `parse_month / add_month` ↔ `datetime.datetime.strptime(s, "%Y-%m")` 与 `dateutil.relativedelta.relativedelta(months=1)`(真实项目里月份加减必须用它,自己写容易漏掉闰年和月末)
> - 手写 `"2021-01" < "2021-10"` 比字符串 ↔ `pd.to_datetime(s)` 之后交给 pandas 的时间类型比较
> - `202101` 这种整数编码 ↔ `pd.Period("2021-01", freq="M")` 或 `df.index.to_period("M")`
> - `parse_month(t["start"])` 得到起点 ↔ `pd.date_range(start="2021-01", periods=36, freq="MS")` 直接生成时间轴
> - 字典当集合去重 `d[x] = 1` ↔ `set(lst)` / `sorted(set(lst))`
> - 求交集 `for k in a: if k in b` ↔ `set(a) & set(b)`;差集用 `set(a) - set(b)`
> - 按年月排序 `sorted(lst)` ↔ `df.sort_values("month")` / `df.sort_index()`

> **【提示】为什么第二层的时间序列「起点」字段这么重要**
>
> 一串 36 个气温值本身**不带时间信息** —— 光看 `vals[5]` 没人知道它是哪个月的。所以数据集里必须另存一个 `start`,再约定「值是按月连续排列的」。这两条合起来才构成一条时间轴:**下标 i ↔ 起点 + i 个月**。后面 L22 做季节性(取每 12 个一组)、L24 做预测(用去年同月)、L37 做时空立方体,第一步都是先用这个公式把下标翻译成月份。

### 本关完整示例

```python
# ===== L17:日期时间与集合 =====

from dataset import dataset

def parse_month(s):
    # "2021-01" → 202101
    return int(s[0:4]) * 100 + int(s[5:7])

def add_month(ym, k):
    # 202101 加 k 个月;减 1 是上月,减 12 是去年同月
    y = ym // 100
    m = ym % 100
    total = y * 12 + (m - 1) + k
    return total // 12 * 100 + total % 12 + 1

print("=== 1) 时间可以拿字符串直接比 ===")
print("2023-01 晚于 2021-12 ?", "2023-01" > "2021-12")
print("2021-09 早于 2021-10 ?", "2021-09" < "2021-10")
dates = ["2023-01", "2021-05", "2022-11"]
dates.sort()
print("排序后:", dates)
print()

print("=== 2) 手写月份加减 ===")
print("2021-01 加 0 个月:", add_month(202101, 0))
print("2021-01 加 1 个月:", add_month(202101, 1))
print("2021-12 加 1 个月:", add_month(202112, 1), "(跨年)")
print("2021-01 加 12 个月:", add_month(202101, 12), "(明年同月)")
print("2023-01 减 1 个月:", add_month(202301, -1))
print("2023-01 减 13 个月:", add_month(202301, -13))
print()

print("=== 3) 给气温序列装上时间轴 ===")
for t in dataset.temp_series:
    vals = t["values"]
    start = parse_month(t["start"])
    best_i = 0
    for i in range(len(vals)):
        if vals[i] > vals[best_i]:
            best_i = i
    print(t["city"], "起点", t["start"], "共", len(vals), "个月")
    print("   最热月", add_month(start, best_i), "气温", vals[best_i], "度")
    y2 = round(sum(vals[12:24]) / 12, 2)
    y3 = round(sum(vals[24:36]) / 12, 2)
    print("   2022 年均温", y2, " 2023 年均温", y3, " 差", round(y3 - y2, 2))
print()

print("=== 4) 用字典键当集合:去重 ===")
region_set = {}
region_order = []
for c in dataset.cities:
    r = c["region"]
    if r not in region_set:
        region_set[r] = 1
        region_order.append(r)
print("56 个城市归成", len(region_set), "个大区")
print(region_order)
print()

print("=== 5) 集合运算:交集与差集 ===")
station_cities = {}
for st in dataset.stations:
    station_cities[st["city"]] = 1

both = []
only_city = []
for c in dataset.cities:
    if c["name"] in station_cities:
        both.append(c["name"])
    else:
        only_city.append(c["name"])
print("有站点的城市:", len(both), "个")
print("只有城市没有站的:", len(only_city), "个,例如", only_city[0:5])
print("两边的键一共涉及:", len(both) + len(only_city), "个城市")
```

运行结果:

```text
=== 1) 时间可以拿字符串直接比 ===
2023-01 晚于 2021-12 ? True
2021-09 早于 2021-10 ? True
排序后: ['2021-05', '2022-11', '2023-01']

=== 2) 手写月份加减 ===
2021-01 加 0 个月: 202101
2021-01 加 1 个月: 202102
2021-12 加 1 个月: 202201 (跨年)
2021-01 加 12 个月: 202201 (明年同月)
2023-01 减 1 个月: 202212
2023-01 减 13 个月: 202112

=== 3) 给气温序列装上时间轴 ===
北京 起点 2021-01 共 36 个月
   最热月 202307 气温 28.9 度
   2022 年均温 13.51  2023 年均温 14.12  差 0.61
上海 起点 2021-01 共 36 个月
   最热月 202107 气温 29.3 度
   2022 年均温 17.46  2023 年均温 17.7  差 0.24
广州 起点 2021-01 共 36 个月
   最热月 202207 气温 29.9 度
   2022 年均温 22.82  2023 年均温 23.11  差 0.29

=== 4) 用字典键当集合:去重 ===
56 个城市归成 7 个大区
['华北', '华东', '华南', '华中', '西南', '西北', '东北']

=== 5) 集合运算:交集与差集 ===
有站点的城市: 50 个
只有城市没有站的: 6 个,例如 ['喀什', '敦煌', '长春', '吉林', '大庆']
两边的键一共涉及: 56 个城市
```

### 动手练习

1. 把 add\_month(202301, -13) 改成 add\_month(202301, -12),看结果是不是去年同月。
2. 给每个城市算「2023 年 7 月」的气温(提示:7 月是起始月 + 6 个月),打印城市和气温。
3. 把 region\_set 换成给 dataset.stations 的 id 去重,看有多少个站点(提示:应该是 50)。
4. 把 only\_city 打印完整,看这 6 个城市是哪些 —— 它们就是「有城市数据但没监测站」的缺口。
5. 故意把 "2021-01" 改成 "2021-1" 再跑第 1 段,看比较结果怎么变。

### 随堂检测

**1. 为什么 "2021-09" < "2021-10" 能得到正确结果?**

- A. 其实是巧合,换个年份就错了
- B. 因为月份补足了两位,字符串逐位比较的顺序与时间顺序一致
- C. 因为 Python 认识日期格式
- D. 因为字符串会自动转成数字

<details><summary>答案与解析</summary>

**答案:B**。Python 并不知道这是日期,它只是逐位比较字符编码。格式固定成 4 位年 + 2 位月,高位在前,逐位比较的结果就和按时间比较一致。一旦月份没补零("2021-9"),"9" 大于 "1",9 月就会排到 10 月后面 —— 说明这个方法成立的前提是格式严格统一。

</details>

**2. 202312 加 1 个月应该是多少?**

- A. 202412
- B. 202313
- C. 2023121
- D. 202401

<details><summary>答案与解析</summary>

**答案:D**。12 月过后是下一年的 1 月,所以是 202401(不能写成 202313,那不是一个合法的月份)。正确算法是先把年月换成「总月数」再加减:2023×12+11=24287,加 1 得 24288,反算回 2024 年 1 月。

</details>

**3. 用字典的键做去重,靠的是字典的什么性质?**

- A. 字典的键只能是字符串
- B. 字典比列表快
- C. 键不重复:同一个键写两次,后一次会覆盖前一次
- D. 字典会自动排序

<details><summary>答案与解析</summary>

**答案:C**。字典的键必须唯一,所以把元素当键写进去,重复的自然被合并,最后 len(d) 就是不同元素的个数。真实代码里直接用 set 更简洁;但字典版还能顺带用 d[k] 存计数,所以两种都要会。

</details>

**4. 要找出两份数据「都有的城市」(交集),标准写法是?**

- A. 用双重循环打印所有名字
- B. 把两边的长度相加
- C. 把两个列表拼起来再排序
- D. 把一边建成字典,遍历另一边,if 名字 in 字典 就记下来

<details><summary>答案与解析</summary>

**答案:D**。把一边建成字典后,查「在不在里面」是一次键查询,很快。遍历另一边的每一项做这个判断,得到的就是两边都有的元素。双重循环也能得到交集,但慢得多,而且不容易去重。

</details>

**5. dataset.temp\_series 里为什么要单独存一个 start 字段?**

- A. 因为 values 是从 1 月开始排的
- B. pandas 要求必须有这个字段
- C. 36 个数值本身不带时间信息,必须靠起点才能把下标翻译成月份
- D. 为了好看

<details><summary>答案与解析</summary>

**答案:C**。一串气温值只是一个数字列表,没有任何时间标记。有了 start 和「按月连续排列」这条约定,才能用「起点 + 下标个月」算出每一项对应的年月。这也是所有时间序列数据的通用做法:值数组和时间轴分开存,靠约定对齐。

</details>


---

# 第二层 · 数据与统计

## L18 · 数组与表格:数据一多,循环就不够用了

> 关键词:ndarray · DataFrame · 向量化 | 建议用时 9 分钟

前 12 幕你一直在用**列表**装数据。列表很好用,但当数据变成「几千行 × 十几列」时,**用 for 循环一个个算就太慢了**,写起来也啰嗦。

这一幕引入两个新容器:<b>数组(array)</b>装一排数字,<b>表格(DataFrame)</b>装一整张表。它们的共同点是 —— **一次对整个容器做运算**,这叫「向量化」。

先看一个对比。假设要算 8 个城市气温的平均值,用第一层的列表写法是这样:

```python
temp = [21.5, 22.1, 25.3, 24.8, 26.1, 23.4, 22.9, 25.0]
total = 0
for t in temp:
    total = total + t
print("平均值:", round(total / len(temp), 2))
```

运行结果:

```text
平均值: 23.89
```

能算,但要写 4 行。换成**数组**,同一件事只要一行:

```python
import numpy as np

temp = np.array([21.5, 22.1, 25.3, 24.8, 26.1, 23.4, 22.9, 25.0])
print("平均值:", round(temp.mean(), 2))
print("最大值:", temp.max())
print("几个数:", temp.size)
```

运行结果:

```text
平均值: 23.89
最大值: 26.1
几个数: 8
```

> **【要点】向量化的三个好处**
>
> - **短**:求平均、最大、求和各一个方法,不用自己写循环。
> - **快**:数值计算库是整块内存一次算完,比逐元素循环快几十倍。
> - **不容易错**:不用管下标从哪开始、边界怎么算。

> **【提示】shape:数组的「形状」**
>
> 每个数组都有 `.shape`,告诉你它有几维、每维多长。一维数组 shape 是 `(8,)`;二维(矩阵)shape 是 `(行数, 列数)`,DataFrame 也一样。**形状不对是数据计算里最常见的错误**,后面每一步都要留意。

再看**数组最重要的能力:整块判断**。下面一次判断 8 个城市,得到一串真假 —— 这叫**布尔掩码**,是筛选数据的核心写法:

```python
import numpy as np

temp = np.array([21.5, 22.1, 25.3, 24.8, 26.1, 23.4, 22.9, 25.0])
mask = temp > 24
print("布尔掩码:", mask.tolist())
print("大于 24 的有几个:", mask.sum())
```

运行结果:

```text
布尔掩码: [False, False, True, True, True, False, False, True]
大于 24 的有几个: 4
```

> **【要点】mask.sum() 为什么能数个数**
>
> 布尔值在数值计算里被当成 **True=1、False=0**。所以把一串真假加起来,得到的就是「有几个真」。这是统计满足条件个数的标准写法,记住它。

> **【注意】最容易懵的一点:掩码长度必须和行数相同**
>
> 用布尔数组筛选表格时,掩码的**个数必须等于行数**,否则程序会报错。因为它的含义是「每一行要不要留下」,长度对不上就无法一一对应。

现在用**真实数据**。讲义附带的 dataset.py 里内置了 56 个中国城市(含经纬度、人口、所属大区)和 50 个环境监测站。先看一个站点长什么样:

```python
from dataset import dataset

print("站点总数:", len(dataset.stations))
print("第 1 个站点:", dataset.stations[0]["name"], dataset.stations[0]["pm25"])
```

运行结果:

```text
站点总数: 50
第 1 个站点: 北京站 50
```

50 个字典手写起来太累。下面把它们变成<b>表格(DataFrame)</b> —— 你可以把它理解成「一个字典,每个键对应一整列」:

```python
import pandas as pd
from dataset import dataset

ids = []
pms = []
cities = []
for st in dataset.stations:
    ids.append(st["id"])
    pms.append(st["pm25"])
    cities.append(st["city"])

df = pd.DataFrame({"id": ids, "pm25": pms, "city": cities})
print("表格形状:", df.shape)
print("列名:", list(df.columns))
print(df.head(3))
```

运行结果:

```text
表格形状: (50, 3)
列名: ['id', 'pm25', 'city']
     id  pm25 city
0  S001    50   北京
1  S002    50   天津
2  S003    74  石家庄
```

表格真正的威力是**筛选**。下面筛出 PM2.5 高于 50 的站点:

```python
import pandas as pd
from dataset import dataset

ids = []
pms = []
for st in dataset.stations:
    ids.append(st["id"])
    pms.append(st["pm25"])

df = pd.DataFrame({"id": ids, "pm25": pms})
dirty = df[df["pm25"] > 50]
print("PM2.5 高于 50 的站点数:", dirty.shape[0])
print("全部站点平均:", round(df["pm25"].mean(), 2))
```

运行结果:

```text
PM2.5 高于 50 的站点数: 18
全部站点平均: 45.04
```

> **【要点】df[条件] 为什么能筛出整行**
>
> `df["pm25"] > 50` 得到一串真假(每个站点一个);把这串真假放回方括号里,表格就知道**哪几行要留下**。这是 pandas 里使用频率最高的一行代码 —— 记住它的形状,以后每天都会用到。

最后是**分组聚合**:把 50 个站点按所在**大区**归类,自动算每组的数量与均值(数据里每个城市只有一个站,按城市分组每组只有 1 行,看不出效果):

```python
import pandas as pd
from dataset import dataset

# 每个城市只有 1 个站,按城市分组没意义;先借城市表查出每个站所在的大区
city_region = {}
for c in dataset.cities:
    city_region[c["name"]] = c["region"]

pms = []
regions = []
for st in dataset.stations:
    pms.append(st["pm25"])
    regions.append(city_region[st["city"]])

df = pd.DataFrame({"pm25": pms, "region": regions})
g = df.groupby("region")["pm25"].agg(["count", "mean"]).round(2)
print("大区个数:", g.shape[0])
print(g)
```

运行结果:

```text
大区个数: 7
        count   mean
region              
东北          3  72.00
华东         12  45.42
华中          6  43.67
华北          8  57.50
华南          9  28.67
西北          6  53.17
西南          6  32.00
```

> **【对照】本关用到的 numpy / pandas 写法速记**
>
> - 安装:`pip install numpy pandas`;导入惯例:`import numpy as np`、`import pandas as pd`
> - `np.array(列表)`:列表 → 数组;常用 `a.mean() / a.max() / a.sum() / a.shape`
> - `pd.DataFrame({列名: 列表})`:字典 → 表格;常用 `df.shape`、`list(df.columns)`、`df.head()`
> - `df[df["pm25"] > 50]`:布尔筛选
> - `df.groupby("region")["pm25"].agg(["count", "mean"])`:分组聚合

### 本关完整示例

```python
import numpy as np
import pandas as pd
from dataset import dataset

# 1) 数组:一次算完一整排数字
temp = np.array([21.5, 22.1, 25.3, 24.8, 26.1, 23.4, 22.9, 25.0])
print("城市气温:", temp.tolist())
print("形状:", temp.shape)
print("平均:", round(temp.mean(), 2))
print("最高:", temp.max())
print("最低:", temp.min())
print()

# 2) 布尔掩码:整块判断
mask = temp > 24
print("哪些城市超过 24 度:", mask.tolist())
print("超过 24 度的个数:", mask.sum())
print()

# 3) 表格:从真实数据集建一张表
city_region = {}
for c in dataset.cities:
    city_region[c["name"]] = c["region"]

ids = []
pms = []
regions = []
for st in dataset.stations:
    ids.append(st["id"])
    pms.append(st["pm25"])
    regions.append(city_region[st["city"]])

df = pd.DataFrame({"id": ids, "pm25": pms, "region": regions})
print("站点表形状:", df.shape)
print("列名:", list(df.columns))
print("PM2.5 平均值:", round(df["pm25"].mean(), 2))
print()

# 4) 筛选:挑出污染较重的站点
dirty = df[df["pm25"] > 50]
print("PM2.5 高于 50 的站点数:", dirty.shape[0])
print("占比:", round(dirty.shape[0] / df.shape[0] * 100), "%")
print()

# 5) 分组:按大区汇总
print(df.groupby("region")["pm25"].agg(["count", "mean"]).round(2))
```

运行结果:

```text
城市气温: [21.5, 22.1, 25.3, 24.8, 26.1, 23.4, 22.9, 25.0]
形状: (8,)
平均: 23.89
最高: 26.1
最低: 21.5

哪些城市超过 24 度: [False, False, True, True, True, False, False, True]
超过 24 度的个数: 4

站点表形状: (50, 3)
列名: ['id', 'pm25', 'region']
PM2.5 平均值: 45.04

PM2.5 高于 50 的站点数: 18
占比: 36 %

        count   mean
region              
东北          3  72.00
华东         12  45.42
华中          6  43.67
华北          8  57.50
华南          9  28.67
西北          6  53.17
西南          6  32.00
```

### 动手练习

1. 把阈值 50 改成 30,重新运行 —— 看筛出的站点数怎么变化。
2. 加一行 print(temp.shape[1]),看看报什么错,理解「维度不够」的报错。
3. 试着不用布尔掩码、只用 for 循环筛出 pm25 > 50 的站点,体会向量化省了多少代码。

### 随堂检测

**1. np.array([1, 2, 3]).mean() 的结果是?**

- A. `1.0`
- B. `2.0`
- C. `3.0`
- D. `6.0`

<details><summary>答案与解析</summary>

**答案:B**。(1+2+3)/3 = 2.0(numpy 的 mean 返回浮点数)。数组的 mean() 直接给出平均值,不用自己写循环求和再除。

</details>

**2. df["pm25"] > 50 得到的是什么?**

- A. 一串真假值,每个站点一个
- B. 一张新表
- C. True 或 False
- D. 一个数字

<details><summary>答案与解析</summary>

**答案:A**。整列和 50 比较是逐元素进行的,结果长度与行数相同。把这串真假放进 df[...] 就能筛出整行。

</details>

**3. mask.sum() 为什么能统计出满足条件的个数?**

- A. 其实是巧合
- B. sum 会数非零元素个数
- C. 布尔值在数值计算里被当成 1 和 0
- D. Python 自动转换

<details><summary>答案与解析</summary>

**答案:C**。True 当 1、False 当 0,相加就是「有几个真」。这是 numpy/pandas 的通用约定。

</details>

**4. 用布尔掩码筛选表格时,掩码长度必须?**

- A. 等于 1
- B. 等于表格列数
- C. 没有要求
- D. 等于表格行数

<details><summary>答案与解析</summary>

**答案:D**。掩码的含义是「每一行留不留」,个数必须等于行数,否则无法一一对应。

</details>

**5. 向量化(用数组运算)相比 for 循环的主要优势是?**

- A. 只能用向量化,循环不行
- B. 代码更短、运行更快、更不容易写错
- C. 向量化不需要内存
- D. 向量化结果更精确

<details><summary>答案与解析</summary>

**答案:B**。三者都有。数值库在底层一次处理一整块内存,比 Python 逐元素循环快很多,而且不用自己管下标和边界。

</details>

## L22 · 时间序列:趋势、季节性与滑动平均

> 关键词:趋势 · 季节性 · 滑动平均 · 同比 | 建议用时 12 分钟

前面几幕的数据都是「一堆互不相干的点」。但真实数据里最常见的一种是**按时间排好的一串数** —— 每天的气温、每小时的车流、每月的销量。这种数据叫**时间序列**。

时间序列有个麻烦:它身上同时压着两股力量。**季节性**是「每年重复的形态」(夏天热、冬天冷),**趋势**是「三年下来慢慢在变的方向」。两股力量搅在一起,直接看曲线根本分不清是变暖了还是又到夏天了。这一幕要做的事就是**把它们拆开**。

先看数据。数据集里有 3 个城市的月均气温,每座城市 **36 个月**(2021-01 到 2023-12),北京排在第 1 个:

```python
from dataset import dataset

for t in dataset.temp_series:
    vals = t["values"]
    print(t["city"], "起始", t["start"], "共", len(vals), "个月")
    print("  前 6 个月:", vals[0:6])
```

运行结果:

```text
北京 起始 2021-01 共 36 个月
  前 6 个月: [-2.3, 1, 7.9, 14.7, 20.7, 25]
上海 起始 2021-01 共 36 个月
  前 6 个月: [4.2, 7.1, 10.1, 15.9, 20.5, 24.4]
广州 起始 2021-01 共 36 个月
  前 6 个月: [14.4, 15.2, 18.2, 23, 26.4, 27.9]
```

36 个数一长串,看不出什么。第一步先**按年切开** —— 每 12 个月一年,摆成三列对照:

```python
from dataset import dataset

vals = dataset.temp_series[0]["values"]
year1 = vals[0:12]
year2 = vals[12:24]
year3 = vals[24:36]
for m in [0, 3, 6, 9]:
    print(m + 1, "月: ", year1[m], "  ", year2[m], "  ", year3[m])
```

运行结果:

```text
1 月:  -2.3    -2.6    -2
4 月:  14.7    15    15.5
7 月:  26.6    27.1    28.9
10 月:  14.8    15.4    14.6
```

一眼就能看出:**1 月最冷、7 月最热,三年都是这个形态** —— 这就是季节性。而三列之间整体在慢慢往上抬,那是趋势。下面把它量化。

> **【要点】拆解时间序列的两个动作**
>
> - **拿趋势**:把每年 12 个月压成一个「年度均值」。一年一个数,季节波动被压掉了,剩下的就是长期方向。
> - **拿季节性**:把同一个月份在三年里平均。年际的涨落被抹平,剩下的就是「这个月份的典型气温」。
> - 一句话:<b>横着平均拿趋势,竖着平均拿季节性。</b>

> **【注意】求年均千万别写成 total / 12**
>
> 气温序列是 <b>36 个月(3 年)</b>,不是 12 个月。写 `total / 12` 会把三年加总当一年,北京的年均气温会算成 **41 度**。永远写 `total / len(vals)` —— 让代码自己去数,不要手写一个想当然的常数。

接下来是这一幕的主角:**滑动平均**。它的想法很朴素 —— **个别月份的上下跳多半是噪声,把它和左右邻居平均一下,噪声就被抹掉一部分**。

> **【要点】滑动平均在算什么**
>
> - 对每个位置取「以它结尾的连续 w 个数」求平均,作为该位置的新值。窗口一路向右滑,所以叫滑动平均。
> - 窗口大小 w 决定抹掉多细的波动:**w 越大越平滑,但留下的点越少、也越迟钝**。
> - 代价有两个:一是**会丢点**(36 个数、窗口 3 只能得到 34 个平滑值,头两个月凑不满窗口);二是平滑后的值不再是真实观测,而是「这一段的平均」。
> - 气温序列有个特殊性:窗口取 12 时,每个窗口正好是完整的一年,季节波动被整个平均掉,剩下的几乎就是趋势线。

```python
from dataset import dataset

def moving_average(vals, w):
    # 只保留窗口完整的位置,所以结果比原始序列短 w-1 个
    result = []
    for i in range(w - 1, len(vals)):
        total = 0
        for j in range(i - w + 1, i + 1):
            total = total + vals[j]
        result.append(round(total / w, 2))
    return result

series = dataset.temp_series[0]["values"]
print("原始:", len(series), "个 窗口3:", len(moving_average(series, 3)), "个 窗口12:", len(moving_average(series, 12)), "个")
print("窗口 3 的前 4 个平滑值:", moving_average(series, 3)[0:4])
```

运行结果:

```text
原始: 36 个 窗口3: 34 个 窗口12: 25 个
窗口 3 的前 4 个平滑值: [2.2, 7.87, 14.43, 20.13]
```

看数据就明白窗口在干什么:窗口 3 的第 1 个平滑值是 `(-2.3 + 1 + 7.9) / 3 = 2.2`,第 3 个是 `(7.9 + 14.7 + 20.7) / 3 = 14.43`。每个平滑值代表「最近三个月的平均」,所以曲线整体比原始序列「慢半拍」。这不是错误,而是滑动平均的固有代价 —— **它给你趋势的平滑,收走的是对拐点的敏感度**。

怎么知道平滑有效?看**相邻两点平均变化多少度**,这个数字越小曲线越平顺。原始序列是 5.05 度,窗口 3 之后是 4.63 度,窗口 12 之后只有 **0.07** 度 —— 因为 12 个月的窗口把一整年的季节波动正好平均掉了。

> **【提示】滑动平均不是预测方法**
>
> 很多人以为「滑动平均 = 预测」。不是。滑动平均是**描述工具**:它把历史的噪声压平,让你看清走势,而且最后一个位置永远拿不到完整窗口。按定义它依赖「当前及之前」的真实观测,所以它给出的曲线**不能当作未来的预测**。下一幕 L24 会讲真正能往前预报的方法。

最后一个日常最常见的比较思路:**同比**。要说「今年是暖还是冷」,不能拿今年 7 月和今年 1 月比(那比的是季节),要拿**今年同月**和**去年同月**比。这样季节这一项被两边同时抵消,剩下的才是真正的年际变化。

> **【对照】这段手写代码 ↔ 真实项目里的写法**
>
> - `series[0:12]` 按年切片 ↔ `df.resample("YE").mean()` 或 `df.groupby(df.index.year).mean()`
> - 手写 `moving_average(vals, 3)` ↔ `s.rolling(3).mean()`(要居中就加 `center=True`)
> - 窗口 12 抽趋势 ↔ `statsmodels.tsa.seasonal.seasonal_decompose(s, model="additive")` 的 `.trend`
> - 各月三年平均(季节形态) ↔ 分解结果里的 `.seasonal`,或 `s.groupby(s.index.month).mean()`
> - 同比(今年同月 − 去年同月) ↔ `s.diff(12)` / `s.pct_change(12)`

### 本关完整示例

```python
# ===== L22:气温序列的趋势、季节性与滑动平均 =====

from dataset import dataset

# 1) 北京的 36 个月月均气温(北京是 temp_series 里的第 1 个城市)
series = dataset.temp_series[0]["values"]
year1 = series[0:12]
year2 = series[12:24]
year3 = series[24:36]
print("共", len(series), "个月: 2021-01 ~ 2023-12")
print()

# 2) 同月对比:季节性是「每年重复的形态」
print("=== 同月对比 ===")
print("月份   2021     2022     2023")
for m in range(12):
    print(" ", m + 1, "  ", year1[m], "   ", year2[m], "   ", year3[m])
print()

# 3) 趋势:年度均值,把每年 12 个月压成一个数
print("=== 趋势(年度均值)===")
y1 = round(sum(year1) / len(year1), 2)
y2 = round(sum(year2) / len(year2), 2)
y3 = round(sum(year3) / len(year3), 2)
print(y1, "/", y2, "/", y3, "度   三年累计变化:", round(y3 - y1, 2), "度")
print()

# 4) 季节性:每个月的三年平均,消掉年际波动留下月形态
season = []
years = [year1, year2, year3]
for m in range(12):
    sameMonth = []
    for y in years:
        sameMonth.append(y[m])
    season.append(round(sum(sameMonth) / len(sameMonth), 2))
coldest = 0
hottest = 0
for m in range(12):
    if season[m] < season[coldest]:
        coldest = m
    if season[m] > season[hottest]:
        hottest = m
print("=== 季节性(各月三年平均)===")
print(season)
print("最冷", coldest + 1, "月", season[coldest], "度   最热", hottest + 1, "月", season[hottest], "度   年内振幅", round(season[hottest] - season[coldest], 2), "度")
print()

# 5) 手写滑动平均:取「以 i 结尾的连续 w 个数」求平均
def moving_average(vals, w):
    result = []
    for i in range(w - 1, len(vals)):
        total = 0
        for j in range(i - w + 1, i + 1):
            total = total + vals[j]
        result.append(round(total / w, 2))
    return result

def roughness(vals):
    total = 0
    for i in range(1, len(vals)):
        total = total + abs(vals[i] - vals[i - 1])
    return total / (len(vals) - 1)

smooth3 = moving_average(series, 3)
smooth12 = moving_average(series, 12)

# 6) 原始 vs 平滑:前 12 个月逐月对照
print("=== 原始 vs 3 个月滑动平均(前 12 个月)===")
print("月   原始    平滑3")
for i in range(12):
    if i < 2:
        print(" ", i + 1, "   ", series[i], "   (前两个月窗口不满)")
    else:
        print(" ", i + 1, "   ", series[i], "   ", smooth3[i - 2])
print()

# 7) 平滑效果:平均每月变化幅度,越小越平滑
print("=== 平滑效果(平均每月变化幅度)===")
print("原始", round(roughness(series), 2), "度 / 窗口3", round(roughness(smooth3), 2), "度 / 窗口12", round(roughness(smooth12), 2), "度")
print("12 个月窗口头 3 值:", smooth12[0:3], " 末 3 值:", smooth12[len(smooth12) - 3:len(smooth12)])
print()

# 8) 同比:今年同月 减 去年同月,季节项被两边同时抵消
print("=== 同比:2022 年各月 减 2021 年同月 ===")
total = 0
warmer = 0
for m in range(12):
    d = round(year2[m] - year1[m], 2)
    total = total + d
    if d > 0:
        warmer = warmer + 1
    if m in [0, 3, 6, 9]:
        print("  ", m + 1, "月:", year2[m], "-", year1[m], "=", d)
print("12 个月里有", warmer, "个月比去年同期更暖,平均同比", round(total / 12, 2), "度")
```

运行结果:

```text
共 36 个月: 2021-01 ~ 2023-12

=== 同月对比 ===
月份   2021     2022     2023
  1    -2.3     -2.6     -2
  2    1     -0.1     1.4
  3    7.9     7.7     7.5
  4    14.7     15     15.5
  5    20.7     22     22.2
  6    25     24.9     25.6
  7    26.6     27.1     28.9
  8    26.5     25.7     27.5
  9    22     20.8     22.6
  10    14.8     15.4     14.6
  11    5.6     6.6     5.8
  12    -1     -0.4     -0.2

=== 趋势(年度均值)===
13.46 / 13.51 / 14.12 度   三年累计变化: 0.66 度

=== 季节性(各月三年平均)===
[-2.3, 0.77, 7.7, 15.07, 21.63, 25.17, 27.53, 26.57, 21.8, 14.93, 6.0, -0.53]
最冷 1 月 -2.3 度   最热 7 月 27.53 度   年内振幅 29.83 度

=== 原始 vs 3 个月滑动平均(前 12 个月)===
月   原始    平滑3
  1     -2.3    (前两个月窗口不满)
  2     1    (前两个月窗口不满)
  3     7.9     2.2
  4     14.7     7.87
  5     20.7     14.43
  6     25     20.13
  7     26.6     24.1
  8     26.5     26.03
  9     22     25.03
  10     14.8     21.1
  11     5.6     14.13
  12     -1     6.47

=== 平滑效果(平均每月变化幅度)===
原始 5.05 度 / 窗口3 4.63 度 / 窗口12 0.07 度
12 个月窗口头 3 值: [13.46, 13.43, 13.34]  末 3 值: [14.17, 14.1, 14.12]

=== 同比:2022 年各月 减 2021 年同月 ===
   1 月: -2.6 - -2.3 = -0.3
   4 月: 15 - 14.7 = 0.3
   7 月: 27.1 - 26.6 = 0.5
   10 月: 15.4 - 14.8 = 0.6
12 个月里有 6 个月比去年同期更暖,平均同比 0.05 度
```

### 动手练习

1. 把窗口从 3 改成 6、再改成 12,看「平均每月变化幅度」怎么变小,以及边界丢掉的点怎么变多。
2. 把城市换成「广州」(dataset.temp\_series[2])再跑一遍:它的年内振幅比北京小多少?为什么?
3. 改代码算 2023 年 vs 2022 年的同比,和幕里的 2022 vs 2021 对比,看趋势是否一致。
4. 试着把 year1 / year2 / year3 换成半年一片(每 6 个月),看看「趋势」会变成什么样。

### 随堂检测

**1. dataset.temp\_series[0]["values"] 里一共有多少个数?**

- A. 24 个,两年
- B. 3 个,每年一个数
- C. 36 个,3 年 × 12 月
- D. 12 个,一年的 12 个月

<details><summary>答案与解析</summary>

**答案:C**。这份数据是 2021-01 到 2023-12 的月均气温,共 36 个月。选 12 的人通常是凭「气温序列 = 12 个月」的常识去猜 —— 这正是求年均时最容易写错 total / 12 的原因。

</details>

**2. 滑动平均的窗口从 3 改成 12,会发生什么?**

- A. 结果完全不变
- B. 曲线更抖动
- C. 曲线更平滑,但边界丢掉的点更多、对突变更迟钝
- D. 点数变多

<details><summary>答案与解析</summary>

**答案:C**。窗口越大,平均覆盖的时间越长,噪声压得越平(北京 12 个月窗口的平均月变化只有 0.07 度),代价是首尾留下的点更少,真实拐点也会被「抹圆」。「更抖动」说反了;平滑值个数是「原始长度 − 窗口 + 1」,窗口越大点数越少,所以「结果不变」「点数变多」也都不对。

</details>

**3. 「拿今年 7 月的气温和去年 7 月比」这种比较叫什么?**

- A. 滑动平均
- B. 同比
- C. 回归
- D. 环比

<details><summary>答案与解析</summary>

**答案:B**。跨年度、比同一个月份叫同比。环比是拿这个月和上个月比 —— 那比出来的是季节性(7 月当然比 6 月热),不是年际变化。滑动平均和回归是另外两种完全不同的方法。

</details>

**4. 要看出「三年下来气温是慢慢升高还是基本没变」,应该看哪个结果?**

- A. 原始 36 个月的曲线
- B. 每个月的同比
- C. 各月三年平均
- D. 年度均值(或 12 个月滑动平均)

<details><summary>答案与解析</summary>

**答案:D**。判断长期方向必须先把季节项压掉,年度均值和 12 个月滑动平均都在做这件事。各月三年平均给出的是「1 月冷 7 月热」的季节形态;原始曲线里季节波动比趋势大几十倍,根本看不清方向。

</details>

**5. 滑动平均能不能直接用来预测下个月的数值?**

- A. 能,只要窗口够大
- B. 不能,因为它是随机方法
- C. 不能,它用到的是历史观测值,不是未来的值
- D. 能,把最后一个平滑值当预测就行

<details><summary>答案与解析</summary>

**答案:C**。每个平滑值都由窗口里的真实观测算出来,而预测时未来的观测并不存在。如果硬把「含当期的平均值」当预测,等于让模型看了答案,分数会虚高 —— 这类错误叫信息泄漏。真正的预报方法在下一幕 L24。

</details>

## L24 · 时间序列预测:最简单的三种方法

> 关键词:朴素预测 · 季节朴素 · MAE · 测试区间 | 建议用时 12 分钟

上一幕把历史拆开了。现在要回答一个更难的问题:<b>下个月大概多少度?</b>

学术界做过一个有点尴尬的统计:在很多真实时间序列上,**花哨的模型打不过几个「朴素到不好意思写进论文」的方法**。所以这一幕先把这三个基准(baseline)老老实实写出来 —— 以后不管用什么复杂模型,都要先跟它们比。

三种朴素方法,一句话就能说清:**朴素**用上个月的值,**季节朴素**用去年同月的值,**移动平均**用最近几个真实值的平均。先看怎么把数据切成训练区和测试区:

```python
from dataset import dataset

series = dataset.temp_series[0]["values"]   # 北京
train = series[0:24]     # 前 24 个月用来「学规律」
test = series[24:36]     # 后 12 个月用来「考试」

print("训练几个月:", len(train), " 测试几个月:", len(test))
print("训练区间的最后 3 个月:", train[21:24])
print("测试区间的真实值:", test)
```

运行结果:

```text
训练几个月: 24  测试几个月: 12
训练区间的最后 3 个月: [15.4, 6.6, -0.4]
测试区间的真实值: [-2, 1.4, 7.5, 15.5, 22.2, 25.6, 28.9, 27.5, 22.6, 14.6, 5.8, -0.2]
```

> **【要点】为什么要留出一个测试区间**
>
> - 如果拿全部 36 个月去「算规律」又拿全部 36 个月去「打分」,分数一定好看 —— 因为答案早就看过了。这叫**自欺**。
> - 正确做法是把时间**按先后切开**:前面一段只用来学(训练区间),后面一段完全不许看(测试区间),最后只在测试区间上打分。
> - 注意时间序列**不能随机切**。打乱顺序就等于让模型提前看到未来,分数会虚假地变好。
> - 留出测试区间的意义在于:<b>它模拟的是「真实上线后遇到没见过的新数据」</b>。

有了预测,就要能打分。回归任务最常用的指标是 <b>MAE(平均绝对误差)</b>:把每个月「猜错多少度」的绝对值加起来取平均。单位就是原来的单位(度),所以好读。

> **【要点】MAE 在算什么**
>
> - **MAE = Σ|真实值 − 预测值| / 个数**:先算每一期错了多少,取绝对值(否则正负会互相抵消),再平均。
> - MAE = 1.5 度的意思是:**平均每个月猜错 1.5 度**。
> - 对比之下,RMSE 会先把误差平方再开方 —— 它更「记仇」,对偶尔的大错罚得更重。想突出「别出大错」用 RMSE,想如实描述「平均错多少」用 MAE。
> - 还有 MAPE(把误差除以真实值再取平均)给出百分比,但真实值接近 0 时它会爆炸 —— 气温冬天就在 0 度附近,所以这里不用 MAPE。

```python
from dataset import dataset

series = dataset.temp_series[0]["values"]   # 北京
train = series[0:24]
test = series[24:36]

p_naive = []
for i in range(12):
    if i == 0:
        p_naive.append(train[23])      # 第 1 个月只能拿训练区最后一个月
    else:
        p_naive.append(test[i - 1])    # 其余用上个月的真实值

p_season = []
for i in range(12):
    p_season.append(train[12 + i])     # 去年同月

print("1 月: 真实", test[0], " 朴素", p_naive[0], " 季节朴素", p_season[0])
print("7 月: 真实", test[6], " 朴素", p_naive[6], " 季节朴素", p_season[6])
```

运行结果:

```text
1 月: 真实 -2  朴素 -0.4  季节朴素 -2.6
7 月: 真实 28.9  朴素 25.6  季节朴素 27.1
```

> **【注意】移动平均预测有个藏起来的陷阱**
>
> 要预测测试期第 i 个月,「最近 3 个值」必须**只来自已知的过去**。写成 `test[i-3:i+1]` 就把**要预测的那个月自己**放进输入了 —— 分数会好得不真实,上线后立刻打回原形。这类错误叫**数据泄漏**,是时间序列项目里最常见的事故。

三种方法都跑完,MAE 会把结论直接摆在桌面上。北京的结果:整体均值(傻瓜基准)**9.79** 度、朴素(用上月)**5.13** 度、移动平均(前 3 月)**9.28** 度、季节朴素(去年同月)**0.91** 度。

> **【要点】为什么季节朴素能赢这么多**
>
> 因为它**押中了数据的生成机制**:气温的规律是「一年一轮回」,去年 1 月和今年 1 月处在同一个季节位置。移动平均拿最近 3 个月平均,而那 3 个月都在「爬坡」或「下坡」,平均下来必然滞后于真实值 —— 这就是它在**有季节性的数据**上打不过季节朴素的原因。换个没有季节规律的数据集(比如股票日收益),结论可能完全反过来:所以基准要一个个试,不能凭感觉选。

> **【对照】这段手写代码 ↔ 真实项目里的写法**
>
> - 手写 `train[0:24]` / `test[24:36]` ↔ `sklearn.model_selection.TimeSeriesSplit(n_splits=3)`,或 `train_test_split(..., shuffle=False)`
> - 朴素预测(用上一期) ↔ `s.shift(1)`,或 `statsmodels.tsa.arima.model.ARIMA(s, order=(0,1,0))`
> - 季节朴素(用去年同月) ↔ `s.shift(12)`,或 `SARIMAX(s, order=(0,0,0), seasonal_order=(0,1,0,12))`
> - 手写 `mae(pred, actual)` ↔ `sklearn.metrics.mean_absolute_error(y_true, y_pred)`
> - 移动平均预测 ↔ `s.shift(1).rolling(3).mean()`(先 shift 再 rolling,shift 那一步就是防泄漏)

### 本关完整示例

```python
# ===== L24:三种朴素预测 + 手写 MAE =====

from dataset import dataset

# 1) 按时间先后切开:前 24 个月学习,后 12 个月考试
series = dataset.temp_series[0]["values"]
train = series[0:24]
test = series[24:36]
print("训练: 前", len(train), "个月 (2021-01 ~ 2022-12)   测试: 后", len(test), "个月 (2023-01 ~ 2023-12)")
print("测试区间真实气温:", test)
print()

# 2) MAE:每个月的「猜错多少度」取绝对值再平均
def mae(pred, actual):
    total = 0
    for i in range(len(actual)):
        total = total + abs(actual[i] - pred[i])
    return total / len(actual)

# 3) 方法一:朴素预测 —— 用上个月的值
p_naive = []
for i in range(12):
    if i == 0:
        p_naive.append(train[23])
    else:
        p_naive.append(test[i - 1])

# 4) 方法二:季节朴素 —— 用去年同月的值
p_season = []
for i in range(12):
    p_season.append(train[12 + i])

# 5) 方法三:移动平均预测 —— 用「这个月之前」最近 3 个真实值(训练区末尾也算已知)
p_move = []
for i in range(12):
    history = train + test[0:i]                 # 预测第 i 个月时已知的全部过去
    past = history[len(history) - 3:]           # 最近 3 个月
    p_move.append(round(sum(past) / len(past), 2))

# 6) 参照物:永远回答「训练期的平均气温」
grand = sum(train) / len(train)
p_mean = []
for i in range(12):
    p_mean.append(round(grand, 2))
print("训练期整体平均气温:", round(grand, 2), "度(傻瓜基准)")
print()

# 7) 逐月对照
print("月份   真实    朴素    季节朴素  移动平均  整体均值")
for i in range(12):
    print(" ", i + 1, "   ", test[i], "   ", p_naive[i], "    ", p_season[i], "     ", p_move[i], "    ", p_mean[i])
print()

# 8) 四种方法的 MAE 比拼
maeMean = round(mae(p_mean, test), 2)
maeNaive = round(mae(p_naive, test), 2)
maeMove = round(mae(p_move, test), 2)
maeSeason = round(mae(p_season, test), 2)
print("=== MAE 比较(单位:度,越小越好)===")
print("整体均值(傻瓜基准)  :", maeMean)
print("朴素(用上个月)      :", maeNaive)
print("移动平均(前 3 个月) :", maeMove)
print("季节朴素(去年同月)  :", maeSeason)
print()

# 9) 谁最好,让数字自己说话
best = "整体均值"
bestv = maeMean
if maeNaive < bestv:
    best = "朴素(用上个月)"
    bestv = maeNaive
if maeMove < bestv:
    best = "移动平均"
    bestv = maeMove
if maeSeason < bestv:
    best = "季节朴素(去年同月)"
    bestv = maeSeason
print("最好的方法:", best, " MAE =", bestv, "度")
print("原因: 气温的规律是「一年一轮回」,去年同月比上个月更接近真相")
print()

# 10) 换两个城市再验一遍,证明结论不是巧合
for idx in [1, 2]:
    t = dataset.temp_series[idx]
    tr = t["values"][0:24]
    te = t["values"][24:36]
    n1 = []
    s1 = []
    for i in range(12):
        if i == 0:
            n1.append(tr[23])
        else:
            n1.append(te[i - 1])
        s1.append(tr[12 + i])
    print(t["city"], " MAE 朴素 =", round(mae(n1, te), 2), " MAE 季节朴素 =", round(mae(s1, te), 2))
```

运行结果:

```text
训练: 前 24 个月 (2021-01 ~ 2022-12)   测试: 后 12 个月 (2023-01 ~ 2023-12)
测试区间真实气温: [-2, 1.4, 7.5, 15.5, 22.2, 25.6, 28.9, 27.5, 22.6, 14.6, 5.8, -0.2]

训练期整体平均气温: 13.48 度(傻瓜基准)

月份   真实    朴素    季节朴素  移动平均  整体均值
  1     -2     -0.4      -2.6       7.2      13.48
  2     1.4     -2      -0.1       1.4      13.48
  3     7.5     1.4      7.7       -0.33      13.48
  4     15.5     7.5      15       2.3      13.48
  5     22.2     15.5      22       8.13      13.48
  6     25.6     22.2      24.9       15.07      13.48
  7     28.9     25.6      27.1       21.1      13.48
  8     27.5     28.9      25.7       25.57      13.48
  9     22.6     27.5      20.8       27.33      13.48
  10     14.6     22.6      15.4       26.33      13.48
  11     5.8     14.6      6.6       21.57      13.48
  12     -0.2     5.8      -0.4       14.33      13.48

=== MAE 比较(单位:度,越小越好)===
整体均值(傻瓜基准)  : 9.79
朴素(用上个月)      : 5.13
移动平均(前 3 个月) : 9.28
季节朴素(去年同月)  : 0.91

最好的方法: 季节朴素(去年同月)  MAE = 0.91 度
原因: 气温的规律是「一年一轮回」,去年同月比上个月更接近真相

上海  MAE 朴素 = 3.93  MAE 季节朴素 = 0.51
广州  MAE 朴素 = 2.48  MAE 季节朴素 = 0.52
```

### 动手练习

1. 把训练区改成前 12 个月(只用一年),测试区改成后 24 个月,看季节朴素还灵不灵 —— 它的「去年同月」只剩一年数据可用。
2. 给「方法三」加一个窗口参数 w,分别试 w=1、3、6、12,打印 MAE 随 w 的变化。
3. 故意把要预测的当月也放进窗口(比如 history = train + test[0:i + 1]),看 MAE 掉到多低 —— 体会数据泄漏有多危险。
4. 把 mae 改成 rmse(先平方、平均、再开方),看四种方法的排名会不会变。

### 随堂检测

**1. 时间序列做训练/测试划分时,为什么不能随机打乱?**

- A. 打乱会让模型提前看到未来,测试分数虚高
- B. 打乱后数据变少
- C. 会影响 MAE 的单位
- D. 随机打乱会报错

<details><summary>答案与解析</summary>

**答案:A**。时间序列的顺序本身就是信息。随机划分会让「未来的样本」跑进训练集,模型等于看过答案。正确做法是按时间先后切:前面的训练、后面的测试。

</details>

**2. 季节朴素预测用的是什么值?**

- A. 去年同一个月份的真实值
- B. 上个月的值
- C. 最近三个月的平均值
- D. 历史平均值

<details><summary>答案与解析</summary>

**答案:A**。「季节」指一年一轮回的周期,所以取 12 期之前的同月份值(代码里就是 train[12 + i])。用上个月是朴素预测,用最近三个月平均是移动平均 —— 三个方法的区别就在「取哪一段历史」。

</details>

**3. MAE = 1.5 度的含义是?**

- A. 平均每次预测大约猜错 1.5 度
- B. 最多猜错 1.5 度
- C. 有 1.5% 的预测是错的
- D. 预测值总是偏低 1.5 度

<details><summary>答案与解析</summary>

**答案:A**。MAE 是误差绝对值的平均,描述的是「平均错多少」。它既不是最坏情况(那是 max 误差),也不看方向(取了绝对值,偏低偏高都算正)。

</details>

**4. 在北京这个数据集上,为什么「移动平均(前 3 个月)」的 MAE 比「季节朴素」差这么多?**

- A. 因为移动平均不能用整数
- B. 因为气温有强烈的季节性,最近 3 个月的平均必然滞后于真实值
- C. 因为窗口 3 太大
- D. 因为移动平均算错了

<details><summary>答案与解析</summary>

**答案:B**。气温的生成机制是「一年一轮回」。移动平均用的是趋势上相邻的月份,在爬坡段给出的是偏低的估计,一年里必然有一半时间严重滞后。季节朴素押中了「去年同月」这个位置,所以误差小一个数量级。

</details>

**5. 「整体均值」方法的 MAE 是 9.79 度,这个数字有什么用?**

- A. 它等于数据的标准差
- B. 它说明这个方法最好
- C. 它是基准线,任何模型都要比它好才值得用
- D. 它没有意义

<details><summary>答案与解析</summary>

**答案:C**。一个永远回答平均值的「傻瓜预测」给出了 9.79 度的误差。任何新方法如果打不过这条线,说明它连「什么都不学」都不如 —— 这就是基准线的作用。

</details>


---

# 第二层 · 预测:回归

## L23 · 线性回归:用一条直线做预测

> 关键词:最小二乘 · 损失 · 决定系数 | 建议用时 11 分钟

前面 13 幕都在**描述**数据:平均值多少、有多少个超标。从这一幕开始,我们要做**预测** —— 根据已知的规律,猜出还没见过的值。

第一个模型最简单也最有用:**用一条直线去拟合数据**。比如「纬度越高、气温越低」,我们能不能把这条规律量化成一个公式?

先看原始数据。数据集的城市表里有纬度,气温序列里有月均气温,我们把两者配成一对对坐标 (纬度, 气温):

```python
from dataset import dataset

print("可用城市:", len(dataset.temp_series))
for t in dataset.temp_series:
    total = 0
    for v in t["values"]:
        total = total + v
    months = len(t["values"])
    print(t["city"], "共", months, "个月, 年均气温", round(total / months, 1))
```

运行结果:

```text
可用城市: 3
北京 共 36 个月, 年均气温 13.7
上海 共 36 个月, 年均气温 17.5
广州 共 36 个月, 年均气温 22.9
```

> **【注意】求平均时务必数清楚有几个数**
>
> 气温序列里是 <b>36 个月的月均值(3 年)</b>。如果按 12 去除,结果会是真实年均气温的 3 倍 —— 北京会算成 41 度。所以求平均要写 `total / len(vals)`,**不要手写一个想当然的常数**。这是数据处理里最常见的低级错误之一。

把「纬度」当横轴、「气温」当纵轴,我们要找一条直线 **y = kx + b**,让它尽量贴近所有点。这条线的 k 叫**斜率**(纬度每高 1 度,气温变化多少),b 叫**截距**。

> **【要点】什么叫「尽量贴近」**
>
> - 对每个点,直线都会给出一个预测值,和真实值之间有差 —— 这个差叫**残差**。
> - 把所有残差**平方后相加**,得到一个总误差(叫 SSE,误差平方和)。
> - 平方有两个作用:一是让正负差不会互相抵消;二是让偏离很远的点受到更重的惩罚。
> - **最小二乘法**就是去找让这个总误差最小的那条线。

数学上可以一步算出最优的 k 和 b(令 SSE 对 k、b 的偏导数等于 0,解方程即得),先看代码。这里用的就是上面算出的三座城市年均气温:

```python
xs = [39.904, 31.23, 23.129]    # 北京、上海、广州的纬度
ys = [13.7, 17.5, 22.9]         # 对应的年均气温(上一段算出)
n = len(xs)
mx = sum(xs) / n
my = sum(ys) / n
num = 0
den = 0
for i in range(n):
    num = num + (xs[i] - mx) * (ys[i] - my)
    den = den + (xs[i] - mx) ** 2
k = num / den
b = my - k * mx
print("斜率 k =", round(k, 3))
print("截距 b =", round(b, 3))
print("预测北纬 45 度的气温:", round(k * 45 + b, 1))
```

运行结果:

```text
斜率 k = -0.547
截距 b = 35.225
预测北纬 45 度的气温: 10.6
```

> **【要点】这两个公式在算什么**
>
> - **斜率 k = Σ(x−x̄)(y−ȳ) / Σ(x−x̄)²**:分子衡量「x 变大时 y 是否同向变化」,分母衡量「x 本身有多分散」。
> - 若 x 与 y 同增同减,分子为正 → k 为正;反向则 k 为负。
> - **截距 b = ȳ − k·x̄**:让这条线**一定穿过数据的中心点** (x̄, ȳ)。
> - 分母是平方和,恒为正,所以 k 一定算得出来(除非所有 x 完全相同)。

有了线,还要知道它**好不好**。最常用的指标是 <b>R²(决定系数)</b>:它回答「气温的变化里,有多少比例能被纬度解释」。

```python
xs = [39.904, 31.23, 23.129]    # 北京、上海、广州的纬度
ys = [13.7, 17.5, 22.9]         # 对应的年均气温(上一段算出)
n = len(xs)
mx = sum(xs) / n
my = sum(ys) / n
num = 0
den = 0
for i in range(n):
    num = num + (xs[i] - mx) * (ys[i] - my)
    den = den + (xs[i] - mx) ** 2
k = num / den
b = my - k * mx
sse = 0
sst = 0
for i in range(n):
    sse = sse + (ys[i] - (k * xs[i] + b)) ** 2
    sst = sst + (ys[i] - my) ** 2
print("误差平方和 SSE =", round(sse, 2))
print("总平方和 SST =", round(sst, 2))
print("R2 =", round(1 - sse / sst, 3))
```

运行结果:

```text
误差平方和 SSE = 0.61
总平方和 SST = 42.75
R2 = 0.986
```

> **【提示】R² 怎么读**
>
> `R² = 1 − SSE/SST`。SST 是「什么都不做、直接用平均值预测」的误差;SSE 是用直线预测的误差。所以 R² 的含义是 <b>「相比瞎猜平均值,这条线把误差减少了百分之多少」</b>。R²=1 是完美拟合,R²=0 表示这条线不比平均值强,**R² 为负说明还不如直接用平均值**。

> **【注意】线性回归的三个坑**
>
> - **相关不等于因果**:k 为负只说明「纬度高的地方气温低」,不代表纬度造成了气温低。
> - **不要外推太远**:用 3 个城市拟合出的线,预测北纬 80 度没有意义。
> - **离群点影响极大**:最小二乘用平方惩罚,一个极远的点就能把整条线拽歪。

> **【对照】这段手写代码 ↔ 真实项目里的写法**
>
> - 手写的最小二乘(k、b 两个公式) ↔ `np.polyfit(xs, ys, 1)`
> - 整个流程(拟合 + 预测 + R²) ↔ `sklearn.linear_model.LinearRegression().fit(X, y)`
> - 评估指标 `R²` ↔ `model.score(X, y)`
> - 误差 `SSE` ↔ `sklearn.metrics.mean_squared_error(y, y_pred) * len(y)`

### 本关完整示例

```python
import math
from dataset import dataset

# 1) 准备数据:把城市纬度和年均气温配成对
names = []
xs = []
ys = []
print("城市     纬度     年均气温")
print("-" * 30)

for t in dataset.temp_series:
    city = t["city"]
    total = 0
    for v in t["values"]:
        total = total + v
    months = len(t["values"])
    annual = total / months
    # 从城市表里找这个城市的纬度
    lat = 0
    for c in dataset.cities:
        if c["name"] == city:
            lat = c["lat"]
    names.append(city)
    xs.append(lat)
    ys.append(annual)
    print(city, "   ", lat, "   ", round(annual, 1))

print()

# 2) 最小二乘:一步算出最优的斜率与截距
n = len(xs)
mx = 0
my = 0
for v in xs:
    mx = mx + v
for v in ys:
    my = my + v
mx = mx / n
my = my / n

num = 0
den = 0
for i in range(n):
    num = num + (xs[i] - mx) * (ys[i] - my)
    den = den + (xs[i] - mx) ** 2

k = num / den
b = my - k * mx
print("拟合直线: 气温 =", round(k, 3), "* 纬度 +", round(b, 3))
print("含义: 纬度每升高 1 度, 年均气温变化", round(k, 3), "度")
print()

# 3) 评估:误差平方和 与 R2
sse = 0
sst = 0
for i in range(n):
    pred = k * xs[i] + b
    sse = sse + (ys[i] - pred) ** 2
    sst = sst + (ys[i] - my) ** 2

print("SSE (误差平方和) =", round(sse, 2))
print("SST (总平方和)   =", round(sst, 2))
r2 = 1 - sse / sst
print("R2  =", round(r2, 3))
print("解释: 纬度能解释", round(r2 * 100), "% 的气温差异")
print()

# 4) 用模型做预测
for lat in [23.1, 31.2, 39.9, 45.0]:
    print("北纬", lat, "度 → 预测年均气温", round(k * lat + b, 1), "度")
print()

# 5) 看每个城市的预测误差
print("城市      真实气温   预测气温   误差")
print("-" * 42)
for i in range(n):
    pred = k * xs[i] + b
    print(names[i], "    ", round(ys[i], 1), "     ", round(pred, 1), "    ", round(ys[i] - pred, 2))
```

运行结果:

```text
城市     纬度     年均气温
------------------------------
北京     39.904     13.7
上海     31.23     17.5
广州     23.129     22.9

拟合直线: 气温 = -0.545 * 纬度 + 35.127
含义: 纬度每升高 1 度, 年均气温变化 -0.545 度

SSE (误差平方和) = 0.63
SST (总平方和)   = 42.43
R2  = 0.985
解释: 纬度能解释 99 % 的气温差异

北纬 23.1 度 → 预测年均气温 22.5 度
北纬 31.2 度 → 预测年均气温 18.1 度
北纬 39.9 度 → 预测年均气温 13.4 度
北纬 45.0 度 → 预测年均气温 10.6 度

城市      真实气温   预测气温   误差
------------------------------------------
北京      13.7       13.4      0.31
上海      17.5       18.1      -0.65
广州      22.9       22.5      0.34
```

### 动手练习

1. 把北纬 45 度改成一个更极端的值(比如 80 度),看预测结果是否还合理 —— 体会「不要外推太远」。
2. 在 xs / ys 里再加一对明显异常的数据(比如纬度 20、气温 -10),看 k 和 R² 怎么被拽歪。
3. 把 SST 换成「用直线预测」的误差会怎样?试着手工理解 R² 为什么能衡量"比平均值好多少"。

### 随堂检测

**1. 最小二乘法里的「二乘」指的是什么?**

- A. 把每个残差平方
- B. 做两次拟合
- C. 乘以 2
- D. 用两个变量

<details><summary>答案与解析</summary>

**答案:A**。把残差平方后求和作为总误差。平方让正负差不互相抵消,同时让偏离远的点受更重惩罚。

</details>

**2. 拟合出的斜率 k = -0.5 表示什么?**

- A. 因变量每增加 1,自变量减少 0.5
- B. 因变量总是 -0.5
- C. 没有一点关系
- D. 自变量每增加 1,因变量平均减少 0.5

<details><summary>答案与解析</summary>

**答案:D**。斜率是「x 每变化 1 个单位,y 平均变化多少」。负号表示反向变化。注意不能说成因果。

</details>

**3. 为什么拟合直线一定穿过数据点的中心 (x̄, ȳ)?**

- A. 因为截距取了 b = ȳ − k·x̄
- B. 这是巧合
- C. 因为最小二乘要求如此但没道理
- D. 因为数据对称

<details><summary>答案与解析</summary>

**答案:A**。最小二乘解的截距就是 ȳ − k·x̄,代回直线方程可得 x = x̄ 时 y=ȳ,所以必然过中心点。

</details>

**4. R² = 0 说明什么?**

- A. 这条线不比直接用平均值更好
- B. 拟合完美
- C. 数据有问题
- D. 斜率为 0

<details><summary>答案与解析</summary>

**答案:A**。R²=1−SSE/SST。R²=0 意味着 SSE=SST,即用直线预测的误差和直接用平均值一样大。

</details>

**5. 用 3 个城市拟合的直线去预测北极圈气温,主要问题是什么?**

- A. 斜率会变大
- B. 外推超出了训练数据的范围,不可靠
- C. R² 会变成负数
- D. 计算会报错

<details><summary>答案与解析</summary>

**答案:B**。模型只在训练数据覆盖的范围内有依据。范围之外的真实规律可能完全不同(比如极地是另一套气候机制)。

</details>


---

# 第二层 · 预测:分类

## L26 · k 近邻分类:看看邻居是谁

> 关键词:距离 · 投票 · 混淆矩阵 | 建议用时 11 分钟

回归预测的是**连续的数字**(气温多少度)。分类预测的是**类别**(这个站点属于哪个区域?这封邮件是不是垃圾邮件?)。

最简单的分类算法叫 <b>k 近邻(k-NN)</b>,它的思想朴素到不可思议:<b>看离它最近的 k 个邻居都是什么类别,然后少数服从多数。</b>

先理解「距离」。两个点的距离用勾股定理就能算:横坐标之差与纵坐标之差的平方和,再开根号。

```python
import math

def dist(p, q):
    dx = p[0] - q[0]
    dy = p[1] - q[1]
    return math.sqrt(dx * dx + dy * dy)

print("(0,0) 到 (3,4) 的距离:", dist([0, 0], [3, 4]))
print("(0,0) 到 (1,1) 的距离:", round(dist([0, 0], [1, 1]), 3))
```

运行结果:

```text
(0,0) 到 (3,4) 的距离: 5.0
(0,0) 到 (1,1) 的距离: 1.414
```

> **【提示】为什么要开根号**
>
> 其实在「比谁更近」这件事上,**平方距离和真实距离的排序完全一样**(都是正数,平方是单调的)。所以很多实现里省掉开根号来提速。但讲距离时还是用真实距离,数字更好懂。

现在给一批「已知答案」的样本(叫**训练集**),再看一个新点落在哪类。核心代码就三段:算距离 → 排序 → 取前 k 个投票。

```python
import math

def dist(p, q):
    dx = p[0] - q[0]
    dy = p[1] - q[1]
    return math.sqrt(dx * dx + dy * dy)

# 训练集:三个华北城市,三个华南城市(坐标是经纬度)
train = [
    ["北京", 116.4, 39.9, "华北"],
    ["天津", 117.2, 39.1, "华北"],
    ["石家庄", 114.5, 38.0, "华北"],
    ["广州", 113.3, 23.1, "华南"],
    ["深圳", 114.1, 22.5, "华南"],
    ["南宁", 108.3, 22.8, "华南"]
]

query = [115.5, 30.0]

# 1) 算每个训练样本到新点的距离
pairs = []
for row in train:
    d = dist([row[1], row[2]], query)
    pairs.append([d, row[3]])

# 2) 按距离从小到大排序(冒泡,个数少够用)
for i in range(len(pairs)):
    for j in range(len(pairs) - 1 - i):
        if pairs[j][0] > pairs[j + 1][0]:
            tmp = pairs[j]
            pairs[j] = pairs[j + 1]
            pairs[j + 1] = tmp

print("最近的 3 个邻居:")
for i in range(3):
    print("   ", pairs[i][1], "距离", round(pairs[i][0], 2))
```

运行结果:

```text
最近的 3 个邻居:
    华南 距离 7.24
    华南 距离 7.63
    华北 距离 8.06
```

> **【要点】k 怎么选**
>
> - **k 太小**(比如 1):对噪声极敏感,一个标错的数据就能让预测翻车。
> - **k 太大**:把远处无关的样本也拉进来投票,预测变"糊"。
> - **k 取奇数**:二分类时避免票数打平(3:3 无法决断)。
> - 实践中常从 3 或 5 开始试,用验证集挑最好的那个 —— 这个动作叫**调参**。

光有预测不够,还要能**衡量准不准**。最直观的工具是**混淆矩阵**:把「预测」和「真实」交叉列表,一眼看出错在哪。

```python
# 真实标签 vs 预测标签
truth = ["华北", "华北", "华南", "华南", "华北", "华南"]
pred  = ["华北", "华南", "华南", "华南", "华北", "华北"]

# 混淆矩阵:行是真实类别,列是预测类别
labels = ["华北", "华南"]
print("            预测华北  预测华南")
for t in labels:
    row = []
    for p in labels:
        n = 0
        for i in range(len(truth)):
            if truth[i] == t and pred[i] == p:
                n = n + 1
        row.append(n)
    print("  真实" + t, "    ", row[0], "       ", row[1])

right = 0
for i in range(len(truth)):
    if truth[i] == pred[i]:
        right = right + 1
print("总共", len(truth), "个, 预测对", right, "个(对角线之和)")
print("准确率:", round(right / len(truth) * 100, 1), "%")
```

运行结果:

```text
            预测华北  预测华南
  真实华北      2         1
  真实华南      1         2
总共 6 个, 预测对 4 个(对角线之和)
准确率: 66.7 %
```

> **【注意】准确率会骗人**
>
> 如果 100 个样本里有 95 个是「华北」,那么一个**永远回答华北**的傻瓜模型准确率也有 95%。所以除了准确率,还要看**精确率**(预测为某类的里面有多少是对的)和**召回率**(某类真实样本里被抓出来多少)。精确率和召回率的调和平均叫 **F1**(L28 详细讲)。

> **【对照】这段手写代码 ↔ 真实项目里的写法**
>
> - 手写的距离 + 排序 + 投票 ↔ `sklearn.neighbors.KNeighborsClassifier(n_neighbors=3).fit(X, y)`
> - 手写混淆矩阵 ↔ `sklearn.metrics.confusion_matrix(y_true, y_pred)`
> - 准确率 ↔ `sklearn.metrics.accuracy_score(y_true, y_pred)`
> - 精确率/召回率/F1 ↔ `sklearn.metrics.classification_report(y_true, y_pred)`
> - 重要提醒:特征量纲不同(比如人口和纬度)时必须先标准化(`StandardScaler`),否则数值范围大的特征会主导距离;经纬度两个特征单位相同,但 1 度经度的实际长度随纬度变化(见 L31)

### 本关完整示例

```python
import math

def dist(p, q):
    dx = p[0] - q[0]
    dy = p[1] - q[1]
    return math.sqrt(dx * dx + dy * dy)

# 训练集:用真实城市的经纬度与所属大区
# 为了让分类任务清晰,只取差异明显的两个区域
train = [
    ["北京", 116.4, 39.9, "北方"],
    ["天津", 117.2, 39.1, "北方"],
    ["石家庄", 114.5, 38.0, "北方"],
    ["太原", 112.5, 37.9, "北方"],
    ["呼和浩特", 111.7, 40.8, "北方"],
    ["广州", 113.3, 23.1, "南方"],
    ["深圳", 114.1, 22.5, "南方"],
    ["南宁", 108.3, 22.8, "南方"],
    ["海口", 110.3, 20.0, "南方"],
    ["昆明", 102.7, 25.0, "南方"]
]

# 待分类的点:几个没参与训练的位置
queries = [
    ["济南附近(36.7N)", 117.0, 36.7],
    ["武汉附近(30.6N)", 114.3, 30.6],
    ["长沙附近(28.2N)", 113.0, 28.2],
    ["沈阳附近(41.8N)", 123.4, 41.8]
]

K = 3

for q in queries:
    pairs = []
    for row in train:
        d = dist([row[1], row[2]], [q[1], q[2]])
        pairs.append([d, row[0], row[3]])

    # 冒泡排序:训练样本少,够用且直观
    n = len(pairs)
    for i in range(n):
        for j in range(n - 1 - i):
            if pairs[j][0] > pairs[j + 1][0]:
                tmp = pairs[j]
                pairs[j] = pairs[j + 1]
                pairs[j + 1] = tmp

    # 投票
    votes = {}
    for i in range(K):
        label = pairs[i][2]
        if label in votes:
            votes[label] = votes[label] + 1
        else:
            votes[label] = 1

    # 取票数最多的
    best = ""
    bestN = 0
    for label in votes:
        if votes[label] > bestN:
            best = label
            bestN = votes[label]

    print(q[0], "→ 预测:", best)
    print("     最近的 3 个邻居:", pairs[0][1], "/", pairs[1][1], "/", pairs[2][1])
    print("     投票:", votes)
    print()

# 评估:混淆矩阵
print("=== 留一法:每个城市轮流当「新点」,用其余 9 个城市投票 ===")
truth = []
pred = []
for row in train:
    pairs = []
    for other in train:
        if other[0] == row[0]:
            continue
        d = dist([other[1], other[2]], [row[1], row[2]])
        pairs.append([d, other[3]])
    n = len(pairs)
    for i in range(n):
        for j in range(n - 1 - i):
            if pairs[j][0] > pairs[j + 1][0]:
                tmp = pairs[j]
                pairs[j] = pairs[j + 1]
                pairs[j + 1] = tmp
    votes = {}
    for i in range(K):
        label = pairs[i][1]
        if label in votes:
            votes[label] = votes[label] + 1
        else:
            votes[label] = 1
    best = ""
    bestN = 0
    for label in votes:
        if votes[label] > bestN:
            best = label
            bestN = votes[label]
    truth.append(row[3])
    pred.append(best)

right = 0
for i in range(len(truth)):
    if truth[i] == pred[i]:
        right = right + 1

print("样本数:", len(truth), " 预测正确:", right)
labels = ["北方", "南方"]
print("混淆矩阵(行=真实, 列=预测):", labels)
for t in labels:
    row = []
    for p in labels:
        n = 0
        for i in range(len(truth)):
            if truth[i] == t and pred[i] == p:
                n = n + 1
        row.append(n)
    print("  ", t, row)
print("准确率:", round(right / len(truth) * 100, 1), "%")
print()
print("逐条结果:")
for i in range(len(truth)):
    mark = "OK"
    if truth[i] != pred[i]:
        mark = "错"
    print("   ", train[i][0], " 真实:", truth[i], " 预测:", pred[i], mark)
```

运行结果:

```text
济南附近(36.7N) → 预测: 北方
     最近的 3 个邻居: 天津 / 石家庄 / 北京
     投票: {'北方': 3}

武汉附近(30.6N) → 预测: 北方
     最近的 3 个邻居: 石家庄 / 太原 / 广州
     投票: {'北方': 2, '南方': 1}

长沙附近(28.2N) → 预测: 南方
     最近的 3 个邻居: 广州 / 深圳 / 南宁
     投票: {'南方': 3}

沈阳附近(41.8N) → 预测: 北方
     最近的 3 个邻居: 天津 / 北京 / 石家庄
     投票: {'北方': 3}

=== 留一法:每个城市轮流当「新点」,用其余 9 个城市投票 ===
样本数: 10  预测正确: 10
混淆矩阵(行=真实, 列=预测): ['北方', '南方']
   北方 [5, 0]
   南方 [0, 5]
准确率: 100.0 %

逐条结果:
    北京  真实: 北方  预测: 北方 OK
    天津  真实: 北方  预测: 北方 OK
    石家庄  真实: 北方  预测: 北方 OK
    太原  真实: 北方  预测: 北方 OK
    呼和浩特  真实: 北方  预测: 北方 OK
    广州  真实: 南方  预测: 南方 OK
    深圳  真实: 南方  预测: 南方 OK
    南宁  真实: 南方  预测: 南方 OK
    海口  真实: 南方  预测: 南方 OK
    昆明  真实: 南方  预测: 南方 OK
```

### 动手练习

1. 把 K 从 3 改成 1 和 7,分别运行,看哪几个查询点的预测结果发生了变化。
2. 在训练集里加一个明显放错位置的点(比如把广州标成"北方"),看它如何影响邻近查询点的预测。
3. 把「济南附近」的坐标改成明显在北方的位置,验证预测跟着变。
4. 想一想:如果把「人口」也作为一个特征加进去,距离公式该怎么改?两个量纲差这么多会不会有问题?

### 随堂检测

**1. k-NN 中的 k 代表什么?**

- A. 分 k 个类别
- B. 距离的 k 次方
- C. 迭代 k 次
- D. 参考最近的 k 个邻居来投票

<details><summary>答案与解析</summary>

**答案:D**。k 是邻居个数。预测时找距离最近的 k 个训练样本,让它们投票决定新点的类别。

</details>

**2. k 取偶数在二分类任务中的主要风险是什么?**

- A. 距离算不出来
- B. 准确率必然下降
- C. 可能出现票数打平,无法决断
- D. 计算会变慢

<details><summary>答案与解析</summary>

**答案:C**。比如 3:3 平票时没有明确多数。取奇数可以避免这种僵局。

</details>

**3. k-NN 训练阶段实际做了什么?**

- A. 几乎什么都没做,只是把训练数据存起来
- B. 反复迭代优化参数
- C. 计算每个特征的权重
- D. 构建一棵决策树

<details><summary>答案与解析</summary>

**答案:A**。k-NN 属于「懒惰学习」:训练时只是记住数据,所有计算都推迟到预测时。代价是预测慢。

</details>

**4. 一个有 95% 样本属于 A 类的数据集,傻瓜模型(永远答 A)准确率是多少?**

- A. `50%`
- B. `95%`
- C. `0%`
- D. `5%`

<details><summary>答案与解析</summary>

**答案:B**。这正是准确率的陷阱。所以还要看精确率与召回率,才能发现模型其实完全没学到东西。

</details>

**5. 为什么实际项目里用 k-NN 前通常要先把特征标准化?**

- A. 为了节省内存
- B. 不同特征的数值范围差太多会主导距离计算
- C. 标准化能提高准确率到 100%
- D. 不标准化会报错

<details><summary>答案与解析</summary>

**答案:B**。比如人口(百万级)和纬度(几十)放在一起算距离,人口会完全压过纬度。标准化把各特征拉到同一量级。

</details>


---

# 第二层 · 分类评估

## L28 · 分类的评估:混淆矩阵与精确率/召回率

> 关键词:真正例 · 精确率 · 召回率 · F1 | 建议用时 12 分钟

L26 用了一个数字 —— **准确率** —— 来评价分类器。这个方法有一个很危险的毛病:**当两类样本数量悬殊时,准确率会骗人**。

这一幕把「预测对/预测错」拆成四种情况,再引出三个更靠谱的指标:**精确率、召回率、F1**,并说清楚它们各自回答什么问题。

先看一个极端的例子。假设要在一批监测数据里找出「污染较重」的站点,10 个站点里只有 1 个真的重污染。有个模型永远回答「不重」:

```python
total = 10
real_heavy = 1
always_light_right = total - real_heavy
print("永远回答“不重”的准确率:", round(always_light_right / total * 100, 1), "%")
print("但它一个重污染站点都没找出来:", 0, "个")
```

运行结果:

```text
永远回答“不重”的准确率: 90.0 %
但它一个重污染站点都没找出来: 0 个
```

> **【注意】准确率的陷阱:样本不平衡时它几乎没有信息量**
>
> 上面这个「傻瓜模型」什么也没学到,准确率却有 90%。在真实场景里更危险:1000 条交易里只有 3 条欺诈,一个永远说「正常」的系统准确率 99.7%,但它对业务**毫无价值**。所以评估一个分类器,**第一步永远是看两类样本各有多少**,不能只看准确率。

解决办法是把预测结果分成四格,这叫**混淆矩阵**。以「重污染」为正类(Positive):

> **【要点】混淆矩阵的四格**
>
> - **真正例 TP**:真的重污染,模型也说重 —— 抓对了。
> - **假正例 FP**:其实不重,模型说重 —— 虚惊一场(误报)。
> - **假反例 FN**:其实重污染,模型说不重 —— 漏掉了(漏报)。
> - **真反例 TN**:确实不重,模型也说不重 —— 正确地排除。
> - 四个数加起来 = 样本总数。准确率 = (TP+TN)/总数。

从这四格里能算出三个更有用的指标。先记住它们各自回答的问题:

> **【要点】精确率、召回率、F1 在问什么**
>
> - <b>精确率 P = TP / (TP+FP)</b> —— 「你说重的那些里,几成是真的重?」模型报出来的警报有多少可信。
> - <b>召回率 R = TP / (TP+FN)</b> —— 「真的重污染里,你抓出来几成?」有没有漏掉。
> - <b>F1 = 2PR/(P+R)</b> —— P 和 R 的调和平均,一个数把两者折中。只有两个都高,F1 才高。
> - 注意分子都是 TP:两个指标一个看「分母含不含误报」,一个看「分母含不含漏报」。

下面的例子里,P 和 R 会互相拉扯。用\*\*温度\*\*去猜 PM2.5 是否偏高:温度阈值定得越低,模型越保守(报得少、报得准,但漏得多);定得越高,越激进(几乎不漏,但误报一堆)。

```python
import math

tp = 18
fp = 4
fn = 5
tn = 23

acc = (tp + tn) / (tp + fp + fn + tn)
p = tp / (tp + fp)
r = tp / (tp + fn)
f1 = 2 * p * r / (p + r)
print("准确率:", round(acc * 100, 1), "%")
print("精确率:", round(p * 100, 1), "%")
print("召回率:", round(r * 100, 1), "%")
print("F1    :", round(f1, 3))
```

运行结果:

```text
准确率: 82.0 %
精确率: 81.8 %
召回率: 78.3 %
F1    : 0.8
```

> **【提示】为什么 F1 用调和平均,不用普通平均**
>
> 如果 P=1.0、R=0.1,普通平均是 0.55,看起来「还行」;调和平均只有 0.18,准确反映出「其中一个很差」。**调和平均会被小的那个数拉下来**,这正是我们要的:精确率和召回率任何一个拉胯,F1 就应该难看。(顺便说:数学上调和平均永远 ≤ 普通平均。)关键在于, **F1 高才代表两个指标都不差**。

> **【注意】别用训练数据所在的样本来测准确率**
>
> 如果拿「拟合时用过的那些站点」去算指标,数字一定漂亮,但这只说明模型**背下了答案**。真实项目里必须把数据切成**训练集**和**测试集**(常见 7:3 或 8:2),用测试集算 P/R/F1。更严格的还会切三份:训练 / 验证(调参用)/ 测试(最后只用一次)。**测试集在最后一刻之前不能碰**,碰了就相当于提前看了考卷。

```python
import math

# 最简单的切分:按顺序每 5 个留 1 个做测试集
rows = []
for i in range(20):
    rows.append(i)
test = []
train = []
for i in range(len(rows)):
    if i % 5 == 0:
        test.append(rows[i])
    else:
        train.append(rows[i])
print("训练集", len(train), "个, 测试集", len(test), "个")
print("测试集下标:", test)
```

运行结果:

```text
训练集 16 个, 测试集 4 个
测试集下标: [0, 5, 10, 15]
```

> **【对照】这段手写代码 ↔ 真实项目里的写法**
>
> - 手写四格计数 ↔ `sklearn.metrics.confusion_matrix(y_true, y_pred)`
> - 手写 P / R / F1 ↔ `sklearn.metrics.precision_score / recall_score / f1_score`
> - 三个指标一起看 ↔ `sklearn.metrics.classification_report(y_true, y_pred)`
> - 按顺序切训练/测试 ↔ `sklearn.model_selection.train_test_split(X, y, test_size=0.2, random_state=0)`
> - **真实项目第一件事是看类别比例** ↔ `y.value_counts()`(pandas)

### 本关完整示例

```python
import math
from dataset import dataset

# 全部 50 个监测站:PM2.5 >= 50 记为「重」
T = 18   # 温度阈值:温度 <= T 就猜「重」

tp = 0
fp = 0
fn = 0
tn = 0
real_heavy = 0
for st in dataset.stations:
    truth = "轻"
    if st["pm25"] >= 50:
        truth = "重"
        real_heavy = real_heavy + 1
    pred = "轻"
    if st["temp"] <= T:
        pred = "重"
    if truth == "重" and pred == "重":
        tp = tp + 1
    elif truth == "轻" and pred == "重":
        fp = fp + 1
    elif truth == "重" and pred == "轻":
        fn = fn + 1
    else:
        tn = tn + 1

print("真实重污染站点:", real_heavy, "个 / 共", len(dataset.stations), "个")
print("于是「永远猜轻」的准确率 =", round((len(dataset.stations) - real_heavy) / len(dataset.stations) * 100, 1), "%")
print()
print("=== 温度阈值 T =", T, "时的混淆矩阵 ===")
print("              预测重     预测轻")
print("  真实重      ", tp, "       ", fn)
print("  真实轻      ", fp, "       ", tn)
print()
acc = (tp + tn) / (tp + fp + fn + tn)
p = tp / (tp + fp)
r = tp / (tp + fn)
f1 = 2 * p * r / (p + r)
print("准确率 =", round(acc * 100, 1), "%")
print("精确率 =", round(p * 100, 1), "%   (报出来的警里有多少是真的)")
print("召回率 =", round(r * 100, 1), "%   (真的重污染里抓到了多少)")
print("F1     =", round(f1, 3))
print()

# 换个阈值,看 P 和 R 怎么互相拉扯
print("T    准确率   精确率   召回率   F1")
for TT in [16, 18, 20, 22]:
    tp = 0
    fp = 0
    fn = 0
    tn = 0
    for st in dataset.stations:
        truth = "轻"
        if st["pm25"] >= 50:
            truth = "重"
        pred = "轻"
        if st["temp"] <= TT:
            pred = "重"
        if truth == "重" and pred == "重":
            tp = tp + 1
        elif truth == "轻" and pred == "重":
            fp = fp + 1
        elif truth == "重" and pred == "轻":
            fn = fn + 1
        else:
            tn = tn + 1
    a = (tp + tn) / (tp + fp + fn + tn)
    pp = tp / (tp + fp)
    rr = tp / (tp + fn)
    print(TT, "  ", round(a, 2), "    ", round(pp, 2), "    ", round(rr, 2), "   ", round(2 * pp * rr / (pp + rr), 2))
```

运行结果:

```text
真实重污染站点: 23 个 / 共 50 个
于是「永远猜轻」的准确率 = 54.0 %

=== 温度阈值 T = 18 时的混淆矩阵 ===
              预测重     预测轻
  真实重       18         5
  真实轻       4         23

准确率 = 82.0 %
精确率 = 81.8 %   (报出来的警里有多少是真的)
召回率 = 78.3 %   (真的重污染里抓到了多少)
F1     = 0.8

T    准确率   精确率   召回率   F1
16    0.8      0.84      0.7     0.76
18    0.82      0.82      0.78     0.8
20    0.78      0.69      0.96     0.8
22    0.68      0.59      1.0     0.74
```

### 动手练习

1. 把 T 改成 14 和 26,分别运行 —— 观察精确率和召回率谁先崩,F1 在哪一档最高。
2. 把「重」的定义从 pm25 >= 50 改成 pm25 >= 60,重新看四个格子里的数怎么变(真实重污染变少了)。
3. 想一个场景(比如地震预警、垃圾邮件拦截),判断它更怕误报还是更怕漏报,然后说该优先优化 P 还是 R。
4. 试着只统计「重」这一类,把「轻」当正类重做一遍 —— 会发现 P 和 R 完全换了一组数。

### 随堂检测

**1. 一个模型在 100 个样本上准确率 95%,但其中 95 个都是负类。这个数字说明什么?**

- A. 几乎不能说明模型有用,可能它永远回答负类
- B. 模型一定是过拟合了
- C. 模型很优秀
- D. 精确率一定是 96%

<details><summary>答案与解析</summary>

**答案:A**。永远回答负类的模型准确率正好 95%(95/100)。要看这类问题必须先知道类别比例,再看精确率和召回率,否则无法区分「学到了」和「瞎猜多数类」。

</details>

**2. 精确率 P = TP/(TP+FP) 回答的是哪个问题?**

- A. 模型说是正类的那些里,有多少真的是正类
- B. 模型总共预测对了多少
- C. 负类被预测对了多少
- D. 真正的正类里,模型抓出了多少

<details><summary>答案与解析</summary>

**答案:A**。分母 TP+FP 是「模型报出来的全部警报」,所以它在问「报警的可信度」。「真正的正类里抓出了多少」是召回率的含义,「总共预测对了多少」是准确率。

</details>

**3. 如果最怕漏掉真正的重污染站点,应该重点看哪个指标?**

- A. 样本总数
- B. 精确率 P
- C. 召回率 R
- D. 准确率

<details><summary>答案与解析</summary>

**答案:C**。召回率的分母 TP+FN 正是「所有真正的正类」,它衡量漏了多少。只看精确率会出现「报得很少、每次都准,但漏掉一大半」的情况。

</details>

**4. F1 = 2PR/(P+R) 里,如果 P = 1.0、R = 0.1,F1 大约是多少?**

- A. `0.18`
- B. `0.55`
- C. `1.00`
- D. `0.10`

<details><summary>答案与解析</summary>

**答案:A**。2×1×0.1/1.1 ≈ 0.18。普通平均会是 0.55,但调和平均会被小的数拉低 —— 这是故意的,用来惩罚「一个指标很好、另一个很差」的模型。

</details>

**5. 为什么评估模型不能直接在训练数据上算准确率?**

- A. 训练数据太少
- B. 模型可能只是记住了训练样本,分数虚高
- C. 训练数据一定没有标签
- D. 算出来会很慢

<details><summary>答案与解析</summary>

**答案:B**。模型见过这些样本的答案,在它们上面表现好不能说明对新样本有效。所以要留出测试集,而且测试集在最终评估前不能用来看或调参。

</details>


---

# 第二层 · 聚类

## L29 · 聚类入门:k-means 怎么把点分成几堆

> 关键词:质心 · 分配-更新 · inertia | 建议用时 13 分钟

前面做的是**有监督**学习:每个样本都带着正确答案(区域、类别、数值),模型的任务是学会这个对应关系。

现在换一种:**没人告诉我们答案**。手上只有 50 个监测站的坐标,想让程序自己指出「这些站凑在一起、那些站凑在一起」。这类任务叫**聚类**,最常用的算法是 **k-means**。

k-means 的想法非常朴素:先随便点 k 个位置当「堆的中心」,然后重复两件事 —— 把每个点分给最近的中心、把中心挪到这堆点的正中间。挪到不再动,就分好了。

> **【要点】两个词先记住**
>
> - <b>质心(centroid)</b>:一个簇的中心位置,就是这个簇里所有点的坐标平均值。它不一定落在某个真实站点上。
> - <b>inertia(簇内平方和)</b>:每个点到它所属质心的距离**平方**再求和。它衡量「这些簇紧不紧凑」,越小越好。
> - 为什么用平方不用距离本身?和最小二乘一样:平方让远点受更重的惩罚,而且求最优质心时可以一步算出来 —— 就是平均值。

「把质心挪到簇的平均位置」不是随便定的。可以证明:固定分配关系后,让 inertia 最小的质心位置**正是该簇所有点的平均值**。所以更新这一步不是拍脑袋,是在解一个小优化问题。

```python
import math

# 三个点,证明「平均值就是让平方距离和最小的位置」
xs = [0.0, 10.0, 20.0]
for cand in [0.0, 5.0, 10.0, 15.0, 20.0]:
    s = 0.0
    for x in xs:
        s = s + (x - cand) ** 2
    print("中心放在", cand, " 平方距离和 =", round(s, 2))

# 平均值
tot = 0.0
for x in xs:
    tot = tot + x
print("平均值 =", round(tot / len(xs), 2), " → 平方距离和最小")
```

运行结果:

```text
中心放在 0.0  平方距离和 = 500.0
中心放在 5.0  平方距离和 = 275.0
中心放在 10.0  平方距离和 = 200.0
中心放在 15.0  平方距离和 = 275.0
中心放在 20.0  平方距离和 = 500.0
平均值 = 10.0  → 平方距离和最小
```

> **【注意】k-means 一定会给你 k 个簇,哪怕数据里根本没有簇**
>
> k 是你指定的,算法不会说「这里其实没有分堆结构」。如果拿一份均匀随机的点去跑 k=3,它照样会画出三个簇,还会给你一份看起来很像样的结果。**所以跑完聚类一定要回头看 inertia 的变化、看簇的大小是否悬殊**,而不是看到输出就相信。另外它还有个真实坑:**不同的初始质心可能得到不同的最终结果**,这叫陷入局部最优。实践里通常跑多次(每次换随机起点)取 inertia 最小的那次 —— sklearn 的参数叫 `n_init`(1.4 版起默认值是 "auto",配合默认的 k-means++ 初始化只跑 1 次;想多跑几次就显式写 `n_init=10`)。

怎么判断「挪到不动了」?算一下每轮质心移动了多少,小于一个很小的数(比如 0.001)就停。下面这段是迭代的骨架:

```python
from dataset import dataset

pts = []
for st in dataset.stations:
    pts.append([st["lon"], st["lat"]])

cents = [[116.3, 39.9], [117.2, 32.0], [113.3, 23.1]]

for it in range(1, 9):
    # 分配 —— 每个点找最近的质心
    labels = []
    for p in pts:
        best = 0
        bd = 1e18
        for ci in range(len(cents)):
            d = (p[0] - cents[ci][0]) ** 2 + (p[1] - cents[ci][1]) ** 2
            if d < bd:
                bd = d
                best = ci
        labels.append(best)

    # 更新 —— 质心挪到本簇的平均位置
    sums = []
    cnts = []
    for ci in range(len(cents)):
        sums.append([0.0, 0.0])
        cnts.append(0)
    for i in range(len(pts)):
        ci = labels[i]
        sums[ci][0] = sums[ci][0] + pts[i][0]
        sums[ci][1] = sums[ci][1] + pts[i][1]
        cnts[ci] = cnts[ci] + 1
    moved = 0.0
    for ci in range(len(cents)):
        if cnts[ci] > 0:
            nlon = sums[ci][0] / cnts[ci]
            nlat = sums[ci][1] / cnts[ci]
            moved = moved + abs(nlon - cents[ci][0]) + abs(nlat - cents[ci][1])
            cents[ci] = [nlon, nlat]
    if moved < 0.001:
        break

print("第", it, "轮后停止,最终质心:")
for c in cents:
    print("   (", round(c[0], 2), ",", round(c[1], 2), ")")
```

运行结果:

```text
第 4 轮后停止,最终质心:
   ( 112.59 , 38.53 )
   ( 117.63 , 30.31 )
   ( 108.13 , 24.88 )
```

> **【提示】比距离时可以省掉开根号**
>
> 「谁最近」只比大小,而平方是单调的,所以 `dx*dx + dy*dy` 和真实距离的排序完全一样。省掉 50×3 次开根号,在大数据上很值。但算 inertia 时别省 —— 要注意 inertia 用的是**平方距离**,这已经是约定俗成的定义,不是我们偷懒。

还有一个容易被忽略的细节:**经纬度的量纲不一样**。1 度纬度约 111 km,1 度经度在北纬 40 度只有约 85 km。如果直接拿 (lon, lat) 算距离,等于假设经度方向「更长」,簇会被拉扁。真实项目里要么先做投影,要么乘一个 `cos(纬度)` 校正。

> **【对照】这段手写代码 ↔ 真实项目里的写法**
>
> - 手写「分配 + 更新」循环 ↔ `sklearn.cluster.KMeans(n_clusters=3, n_init=10, random_state=0).fit(X)`
> - 手写的 inertia ↔ `KMeans.inertia_`(注意 sklearn 里是「到质心的平方距离和」,定义完全一样)
> - 每个点的簇号 ↔ `KMeans.labels_`
> - 质心坐标 ↔ `KMeans.cluster_centers_`
> - 特征标准化(避免经度压倒纬度) ↔ `sklearn.preprocessing.StandardScaler().fit_transform(X)`

### 本关完整示例

```python
import math
from dataset import dataset

# 50 个监测站的坐标
pts = []
names = []
for st in dataset.stations:
    pts.append([st["lon"], st["lat"]])
    names.append(st["name"])

# 初始质心:先随手挑 3 个位置
cents = [[116.3, 39.9], [117.2, 32.0], [113.3, 23.1]]

labels = []
for i in range(len(pts)):
    labels.append(0)

for it in range(1, 9):
    # 第一步:分配 —— 每个点找最近的质心
    for i in range(len(pts)):
        best = 0
        bd = 1e18
        for ci in range(len(cents)):
            dx = pts[i][0] - cents[ci][0]
            dy = pts[i][1] - cents[ci][1]
            d = dx * dx + dy * dy
            if d < bd:
                bd = d
                best = ci
        labels[i] = best

    # 第二步:更新 —— 质心挪到本簇的平均位置
    sums = []
    cnts = []
    for ci in range(len(cents)):
        sums.append([0.0, 0.0])
        cnts.append(0)
    for i in range(len(pts)):
        ci = labels[i]
        sums[ci][0] = sums[ci][0] + pts[i][0]
        sums[ci][1] = sums[ci][1] + pts[i][1]
        cnts[ci] = cnts[ci] + 1

    # 打印这一轮:inertia、质心位置、簇大小、每个站属于哪个簇
    inertia = 0.0
    for i in range(len(pts)):
        ci = labels[i]
        dx = pts[i][0] - cents[ci][0]
        dy = pts[i][1] - cents[ci][1]
        inertia = inertia + dx * dx + dy * dy
    print("第", it, "轮:inertia =", round(inertia, 2))
    line = ""
    for i in range(len(pts)):
        line = line + str(labels[i])
    for ci in range(len(cents)):
        print("   簇", ci, "中心 (", round(cents[ci][0], 2), ",", round(cents[ci][1], 2), ") 共", cnts[ci], "个站")
    print("   labels =", line)

    moved = 0.0
    for ci in range(len(cents)):
        if cnts[ci] > 0:
            nlon = sums[ci][0] / cnts[ci]
            nlat = sums[ci][1] / cnts[ci]
            moved = moved + abs(nlon - cents[ci][0]) + abs(nlat - cents[ci][1])
            cents[ci] = [nlon, nlat]
    if moved < 0.001:
        print("质心几乎不动了,停止迭代")
        break

# 最后看看每个簇里都有谁
print()
for ci in range(len(cents)):
    mem = []
    for i in range(len(pts)):
        if labels[i] == ci:
            mem.append(names[i])
    print("簇", ci, "中心 (", round(cents[ci][0], 2), ",", round(cents[ci][1], 2), ") 共", len(mem), "个:")
    print("   ", mem)
```

运行结果:

```text
第 1 轮:inertia = 3277.97
   簇 0 中心 ( 116.3 , 39.9 ) 共 16 个站
   簇 1 中心 ( 117.2 , 32.0 ) 共 17 个站
   簇 2 中心 ( 113.3 , 23.1 ) 共 17 个站
   labels = 00000000111101112111222222222121111222222100001000
第 2 轮:inertia = 2641.8
   簇 0 中心 ( 113.0 , 39.52 ) 共 18 个站
   簇 1 中心 ( 116.31 , 31.78 ) 共 17 个站
   簇 2 中心 ( 109.01 , 25.05 ) 共 15 个站
   labels = 00000000111101111111222222222111111222222000000000
第 3 轮:inertia = 2569.35
   簇 0 中心 ( 112.54 , 38.96 ) 共 20 个站
   簇 1 中心 ( 117.1 , 30.83 ) 共 15 个站
   簇 2 中心 ( 108.13 , 24.88 ) 共 15 个站
   labels = 00000000111101111111222222222110011222222000000000
第 4 轮:inertia = 2557.4
   簇 0 中心 ( 112.59 , 38.53 ) 共 20 个站
   簇 1 中心 ( 117.63 , 30.31 ) 共 15 个站
   簇 2 中心 ( 108.13 , 24.88 ) 共 15 个站
   labels = 00000000111101111111222222222110011222222000000000
质心几乎不动了,停止迭代

簇 0 中心 ( 112.59 , 38.53 ) 共 20 个:
    ['北京站', '天津站', '石家庄站', '太原站', '呼和浩特站', '唐山站', '保定站', '大同站', '济南站', '郑州站', '洛阳站', '西安站', '兰州站', '乌鲁木齐站', '西宁站', '银川站', '咸阳站', '沈阳站', '大连站', '哈尔滨站']
簇 1 中心 ( 117.63 , 30.31 ) 共 15 个:
    ['上海站', '南京站', '杭州站', '苏州站', '青岛站', '合肥站', '福州站', '厦门站', '南昌站', '无锡站', '宁波站', '武汉站', '长沙站', '宜昌站', '襄阳站']
簇 2 中心 ( 108.13 , 24.88 ) 共 15 个:
    ['广州站', '深圳站', '南宁站', '海口站', '珠海站', '东莞站', '佛山站', '三亚站', '桂林站', '成都站', '重庆站', '昆明站', '贵阳站', '拉萨站', '绵阳站']
```

### 动手练习

1. 把初始质心改成 [[126.6, 45.8], [112.5, 34.6], [109.5, 18.3]],重新运行 —— 看迭代轮数和最终 inertia 有没有变。
2. 把簇数从 3 改成 4,需要在哪些地方改?改完看 inertia 是变大还是变小。
3. 把坐标换成 [lon \* 0.79, lat],重新跑 —— 看哪几个站的归属发生了改变,体会量纲校正的影响。
4. 给每个簇算一个「平均 pm25」,看看靠地理位置分出来的簇,在污染水平上有没有差别。

### 随堂检测

**1. k-means 的「更新」这一步具体做什么?**

- A. 计算所有点之间的距离
- B. 重新随机挑 k 个点
- C. 把每个质心挪到本簇所有点的平均位置
- D. 删除最小的簇

<details><summary>答案与解析</summary>

**答案:C**。更新就是把质心设成簇内点的均值,因为可以证明这个位置让簇内平方距离和最小。重新随机挑点是某些初始化策略(比如 k-means++)的做法,不是迭代里的更新。

</details>

**2. inertia 的定义是什么?**

- A. 质心到原点的距离
- B. 簇的个数
- C. 所有点之间的平均距离
- D. 每个点到所属质心的平方距离之和

<details><summary>答案与解析</summary>

**答案:D**。inertia 衡量簇有多紧凑,越小说明点聚得越紧。注意它随 k 增大一定单调下降(k 越多,每个点离自己的质心当然越近),所以不能直接拿它来选 k。

</details>

**3. 为什么说「k-means 一定会给出 k 个簇」是个坑?**

- A. 质心必须落在真实数据点上
- B. 簇里至少有 10 个点
- C. k 只能是 3
- D. k 由人指定,算法不会判断数据里是否真有分堆结构

<details><summary>答案与解析</summary>

**答案:D**。算法只负责在给定 k 下最小化 inertia,没有「这里不该分堆」的判断能力。所以必须配合 L30 的肘部法、轮廓系数一起看。

</details>

**4. 用不同的初始质心跑 k-means,可能得到不同结果,这叫什么?**

- A. 维度灾难
- B. 数据泄漏
- C. 过拟合
- D. 陷入局部最优

<details><summary>答案与解析</summary>

**答案:D**。k-means 是在一个非凸的目标上做坐标下降,起点不同可能停在不同的局部最优。实践里跑多次取 inertia 最小的那次(sklearn 的 n\_init 参数)。

</details>

**5. 两个簇的质心一定落在某个真实数据点上吗?**

- A. 一定,否则算法会报错
- B. 只有 k=1 时才落在点上
- C. 一定,因为它是从数据里选的
- D. 不一定,质心是坐标平均值,可以是空的区域

<details><summary>答案与解析</summary>

**答案:D**。质心是簇内所有点的平均坐标,通常落在点与点之间。和它对比:k-medoids 的簇中心(medoid)一定是真实样本点;DBSCAN 则根本没有「簇中心」这个概念。

</details>

## L30 · 聚类进阶:怎么决定分几类 + DBSCAN

> 关键词:肘部法 · 轮廓系数 · eps · 噪声点 | 建议用时 14 分钟

L29 的代码里 k=3 是**我们拍脑袋定的**。真实项目里没人告诉你该分几类,而这个选择直接决定结果。

这一幕解决两件事:**怎么用数据判断 k**(肘部法 + 轮廓系数),以及**换一种不要求「每类都是球」的算法**(DBSCAN)。

先说一个坏消息:inertia 随着 k 增大一定越来越小。因为 k 越大,每个点离最近的质心只会更近,不可能更远。所以「inertia 最小」不能当选择标准 —— k=50 时每个点自己就是一个簇,inertia 是 0,毫无意义。

有用的信号是 **inertia 下降的速度**。如果从 k=3 加到 k=4 只让 inertia 少了一点点,说明第 4 个簇没带来新信息。把 k 和 inertia 画成曲线,找那个从「陡」转「平」的拐弯处,这叫**肘部法**。

```python
# 主代码(多起点 k-means)真实算出的 inertia
inertias = [3863.66, 2332.35, 1469.06, 1052.37, 757.55, 654.54]
prev = 0.0
for k in range(1, 7):
    cur = inertias[k - 1]
    if prev > 0:
        print("k =", k, " inertia =", round(cur, 2), " 比上一档下降", round((prev - cur) / prev * 100, 1), "%")
    else:
        print("k =", k, " inertia =", round(cur, 2))
    prev = cur
```

运行结果:

```text
k = 1  inertia = 3863.66
k = 2  inertia = 2332.35  比上一档下降 39.6 %
k = 3  inertia = 1469.06  比上一档下降 37.0 %
k = 4  inertia = 1052.37  比上一档下降 28.4 %
k = 5  inertia = 757.55  比上一档下降 28.0 %
k = 6  inertia = 654.54  比上一档下降 13.6 %
```

> **【要点】肘部法看的是「下降幅度的突变」**
>
> - k=1 → 2 → 3:每多一个簇都砍掉近 40%(很陡,大块结构还没分完)。
> - k=3 → 4 → 5:降幅收窄到 28% 左右。
> - k=5 → 6:只降了 14%,明显变平。
> - **这份数据的肘部并不尖锐**:k=3 附近由陡转缓,k=5 之后才真正变平。真实数据里肘部不明显是常态,所以还需要第二个指标来帮忙。
> - 注意:k 增大时 inertia 必然下降,所以「哪一种 k 的 inertia 更小」永远不是理由。

肘部法靠肉眼,不够客观。第二个工具是**轮廓系数**,它对每个点算一个 −1 到 1 之间的分数:

> **【要点】轮廓系数在算什么**
>
> - **a** = 这个点到**同簇**其他点的平均距离(和自家人有多近)。
> - **b** = 这个点到**最近的另一个簇**里所有点的平均距离(和外家人有多远)。
> - <b>s = (b − a) / max(a, b)</b>:近朱者赤就接近 1,两边差不多就接近 0,**贴错堆会变成负数**。
> - 把所有点的 s 求平均,就是这次聚类的分数。越高越好,和 inertia 不同,它**不会随 k 自动变好**,所以可以用来比较不同 k。

下面几个 k 的轮廓系数是主代码用 50 个站点的坐标真算出来的。k=5 最高(0.43),但它多出来的那个簇只有拉萨、乌鲁木齐 2 个站 —— 本质是把两个远在西部的孤立站单独拎了出来。指标只能给参考,最终分几类要看这些簇在业务上能不能解释。

```python
# 用主代码算好的结果对比两个指标
names = [2, 3, 4, 5, 6]
sils = [0.37, 0.399, 0.409, 0.43, 0.424]
for i in range(len(names)):
    print("k =", names[i], " 平均轮廓系数 =", round(sils[i], 3))
print("轮廓系数在 k=5 最高;肘部法在 k=3 由陡转缓、k=5 之后变平 → k=3~5 都说得通,看业务需要几类")
```

运行结果:

```text
k = 2  平均轮廓系数 = 0.37
k = 3  平均轮廓系数 = 0.399
k = 4  平均轮廓系数 = 0.409
k = 5  平均轮廓系数 = 0.43
k = 6  平均轮廓系数 = 0.424
轮廓系数在 k=5 最高;肘部法在 k=3 由陡转缓、k=5 之后变平 → k=3~5 都说得通,看业务需要几类
```

> **【注意】轮廓系数在 50 个点上算很贵,别写成三重循环还每次重算距离**
>
> 轮廓系数要对每个点算「到其他所有点的距离」,朴素写法是 50×50,再乘上「试 5 个 k」就是 12500 次开根号。真正跑得动的写法是**先把两两距离算成一张表 D[50][50] 存起来**,后面反复查表。这个技巧在真实项目里的对应物是 `scipy.spatial.distance.pdist` / `sklearn.metrics.pairwise_distances` —— 库函数帮你算了这张表并缓存。

k-means 还有一个更根本的限制:它假设每个簇是**一团比较圆的点**,而且所有簇大小差不多。如果数据是弯的(比如一条弧形),或者两簇密度差很多,它就分不对。

DBSCAN 换了个思路:<b>不找中心,而是找「密的地方」</b>。规则只有两句 —— 半径 `eps` 内至少有 `minPts` 个点(含自己)叫**核心点**;从一个核心点出发,把所有能连上的核心点拉进同一个簇。**连不上任何核心点的点就是噪声点**,不给它分配簇。

> **【要点】DBSCAN 的两个参数**
>
> - **eps**:邻居的搜索半径。调小 → 很多点不够密,大量变噪声;调大 → 不同簇被连成一片。
> - **minPts**:成为核心点所需的最少邻居数(含自己)。二维数据常用 3~5。
> - 它**不需要指定簇数**,簇数由数据和参数自己长出来。
> - 它能把不规则形状、密度不均的簇分出来,这是 k-means 做不到的。
> - 代价:结果对 eps 非常敏感,而且高维数据上「距离」本身会失去意义。

```python
import math
from dataset import dataset

pts = []
names = []
for st in dataset.stations:
    pts.append([st["lon"] * 0.79, st["lat"]])   # 与主代码一样,经度乘 cos(约 38°) 做校正
    names.append(st["city"])
n = len(pts)

def dbscan(eps, min_pts):
    # 1) 每个点在半径 eps 内的邻居(含自己)
    nbrs = []
    for i in range(n):
        row = []
        for j in range(n):
            d = math.sqrt((pts[i][0] - pts[j][0]) ** 2 + (pts[i][1] - pts[j][1]) ** 2)
            if d <= eps:
                row.append(j)
        nbrs.append(row)
    # 2) 先全部标成噪声 -1,再从每个还没归簇的核心点出发「扩张」
    labels = [-1] * n
    cid = 0
    for i in range(n):
        if labels[i] != -1 or len(nbrs[i]) < min_pts:
            continue                     # 已经有簇了,或者不是核心点
        labels[i] = cid
        queue = [i]
        while len(queue) > 0:
            p = queue.pop()
            if len(nbrs[p]) < min_pts:
                continue                 # 边界点:收进簇,但不再往外扩
            for q in nbrs[p]:
                if labels[q] == -1:
                    labels[q] = cid
                    queue.append(q)
        cid = cid + 1
    return labels, cid

for eps in [1.5, 2.0, 2.5, 3.0]:
    labels, k = dbscan(eps, 3)
    print("eps =", eps, " 簇数 =", k, " 噪声点 =", labels.count(-1))

labels, k = dbscan(2.5, 3)
print()
print("eps = 2.5 时每个簇里的城市:")
for c in range(k):
    mem = []
    for i in range(n):
        if labels[i] == c:
            mem.append(names[i])
    print("  簇", c, ":", mem)
```

运行结果:

```text
eps = 1.5  簇数 = 3  噪声点 = 33
eps = 2.0  簇数 = 3  噪声点 = 32
eps = 2.5  簇数 = 5  噪声点 = 21
eps = 3.0  簇数 = 4  噪声点 = 14

eps = 2.5 时每个簇里的城市:
  簇 0 : ['北京', '天津', '石家庄', '太原', '呼和浩特', '唐山', '保定', '大同', '济南']
  簇 1 : ['上海', '南京', '杭州', '苏州', '合肥', '无锡', '宁波']
  簇 2 : ['南昌', '武汉', '长沙', '宜昌', '襄阳']
  簇 3 : ['广州', '深圳', '珠海', '东莞', '佛山']
  簇 4 : ['成都', '重庆', '绵阳']
```

eps 从 1.5 放宽到 2.5,噪声点从 33 个降到 21 个,并分出 5 个很有地理意义的簇:京津冀、长三角、长江中游、珠三角、成渝;再放宽到 3.0,噪声只剩 14 个,但簇数反而从 5 降到 4 —— 相邻的簇开始被连成一片。eps 选多大,没有唯一正确答案,要看你想在什么尺度上找「密集区」。

> **【对照】这段手写代码 ↔ 真实项目里的写法**
>
> - 手写肘部法循环 ↔ `KMeans(n_clusters=k).fit(X).inertia_` 包一个 for
> - 手写轮廓系数 ↔ `sklearn.metrics.silhouette_score(X, labels)`(每个点的分数用 `silhouette_samples`)
> - 手写 DBSCAN ↔ `sklearn.cluster.DBSCAN(eps=2.5, min_samples=3).fit(X)`
> - 噪声点 ↔ `labels_ == -1`
> - 真实项目里 eps 常用「k 距离图」估:先算每个点到第 minPts 近邻的距离,排序后找拐点 ↔ `sklearn.neighbors.NearestNeighbors(n_neighbors=3).kneighbors(X)`

### 本关完整示例

```python
import math
from dataset import dataset

pts = []
for st in dataset.stations:
    pts.append([st["lon"] * 0.79, st["lat"]])
n = len(pts)

# 两点之间的距离先算好,后面反复用
D = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(math.sqrt((pts[i][0] - pts[j][0]) ** 2 + (pts[i][1] - pts[j][1]) ** 2))
    D.append(row)

def run_kmeans(k, start):
    # 起点:先放第 start 个站点,然后每次挑「离已有质心最远」的点
    cents = [[pts[start][0], pts[start][1]]]
    while len(cents) < k:
        far = 0
        fd = -1.0
        for i in range(n):
            nd = 1e18
            for c in cents:
                dx = pts[i][0] - c[0]
                dy = pts[i][1] - c[1]
                d = dx * dx + dy * dy
                if d < nd:
                    nd = d
            if nd > fd:
                fd = nd
                far = i
        cents.append([pts[far][0], pts[far][1]])
    labels = []
    for i in range(n):
        labels.append(0)
    for it in range(20):
        for i in range(n):
            best = 0
            bd = 1e18
            for ci in range(k):
                dx = pts[i][0] - cents[ci][0]
                dy = pts[i][1] - cents[ci][1]
                d = dx * dx + dy * dy
                if d < bd:
                    bd = d
                    best = ci
            labels[i] = best
        sums = []
        cnts = []
        for ci in range(k):
            sums.append([0.0, 0.0])
            cnts.append(0)
        for i in range(n):
            ci = labels[i]
            sums[ci][0] = sums[ci][0] + pts[i][0]
            sums[ci][1] = sums[ci][1] + pts[i][1]
            cnts[ci] = cnts[ci] + 1
        moved = 0.0
        for ci in range(k):
            if cnts[ci] > 0:
                nl = sums[ci][0] / cnts[ci]
                na = sums[ci][1] / cnts[ci]
                moved = moved + abs(nl - cents[ci][0]) + abs(na - cents[ci][1])
                cents[ci] = [nl, na]
        if moved < 0.0001:
            break
    inertia = 0.0
    for i in range(n):
        ci = labels[i]
        dx = pts[i][0] - cents[ci][0]
        dy = pts[i][1] - cents[ci][1]
        inertia = inertia + dx * dx + dy * dy
    return labels, inertia

def best_kmeans(k):
    # 多起点:每个站点轮流当第一个质心,一共跑 n 次,留 inertia 最小的那次
    # (相当于 sklearn 的 n_init,避免某一次起点不好、陷入局部最优)
    best_labels, best_inertia = run_kmeans(k, 0)
    for s in range(1, n):
        labels, inertia = run_kmeans(k, s)
        if inertia < best_inertia:
            best_labels = labels
            best_inertia = inertia
    return best_labels, best_inertia

print("k    inertia    比上一档下降")
prev = 0.0
best_labels = {}                  # 存下每个 k 的最优分簇,后面算轮廓系数直接用,不必重跑
for k in range(1, 7):
    labels, inertia = best_kmeans(k)
    best_labels[k] = labels
    if prev > 0:
        print(k, "  ", round(inertia, 2), "   ", round((prev - inertia) / prev * 100, 1), "%")
    else:
        print(k, "  ", round(inertia, 2))
    prev = inertia

print()
for k in [2, 3, 4, 5, 6]:
    labels = best_labels[k]
    sils = []
    for i in range(n):
        cnt = []
        sd = []
        for c in range(k):
            cnt.append(0)
            sd.append(0.0)
        for j in range(n):
            if j != i:
                cnt[labels[j]] = cnt[labels[j]] + 1
                sd[labels[j]] = sd[labels[j]] + D[i][j]
        if cnt[labels[i]] == 0:
            sils.append(0.0)          # 单点簇:按惯例记 0(与 sklearn 一致)
            continue
        a = sd[labels[i]] / cnt[labels[i]]
        b = 1e18
        for c in range(k):
            if c != labels[i] and cnt[c] > 0 and sd[c] / cnt[c] < b:
                b = sd[c] / cnt[c]
        if b > 1e17:
            sils.append(0.0)
        else:
            sils.append((b - a) / max(a, b))
    tot = 0.0
    for s in sils:
        tot = tot + s
    sizes = []
    for c in range(k):
        sizes.append(labels.count(c))
    print("k =", k, " 平均轮廓系数 =", round(tot / n, 3), "  各簇站点数:", sizes)
```

运行结果:

```text
k    inertia    比上一档下降
1    3863.66
2    2332.35     39.6 %
3    1469.06     37.0 %
4    1052.37     28.4 %
5    757.55     28.0 %
6    654.54     13.6 %

k = 2  平均轮廓系数 = 0.37   各簇站点数: [30, 20]
k = 3  平均轮廓系数 = 0.399   各簇站点数: [10, 16, 24]
k = 4  平均轮廓系数 = 0.409   各簇站点数: [10, 13, 12, 15]
k = 5  平均轮廓系数 = 0.43   各簇站点数: [12, 2, 11, 13, 12]
k = 6  平均轮廓系数 = 0.424   各簇站点数: [13, 1, 11, 1, 12, 12]
```

### 动手练习

1. 把坐标里的 0.79 改成 1.0(即不做校正),再跑一遍肘部法,看拐点会不会移动。
2. 把 dbscan(eps, 3) 里的 3 改成 5(即 minPts = 5),重新运行:簇会变多还是变少,噪声会变多还是变少?
3. 在 50 个站点之外,手工加一个孤立的点(比如 [80.0, 50.0]),看它会被判成噪声还是被拉进某个簇。
4. 想一想:如果把 k 一路加到 50, inertia 会变成多少?为什么这时候 inertia 不能作为评价标准?

### 随堂检测

**1. 为什么不能直接选「inertia 最小」的那个 k?**

- A. inertia 随 k 增大必然下降,k 越大越小
- B. inertia 越大说明聚类越好
- C. inertia 计算有随机数
- D. inertia 只在 k=1 时有意义

<details><summary>答案与解析</summary>

**答案:A**。每多一个质心,点只可能离最近的质心更近,所以 inertia 单调不增。k=50 时每个点自成一簇,inertia=0 却毫无意义。要看的是下降速度的拐点。

</details>

**2. 轮廓系数 s = (b−a)/max(a,b) 里的 a 和 b 分别是什么?**

- A. a 和 b 都是到原点的距离
- B. a 是准确率,b 是召回率
- C. a 是质心距离,b 是簇数
- D. a 是同簇平均距离,b 是到最近其他簇的平均距离

<details><summary>答案与解析</summary>

**答案:D**。a 衡量「和自家人多近」,b 衡量「和外家人多远」。b 明显大于 a 时 s 接近 1;若 a 更大(点其实更贴别的簇),s 变负。

</details>

**3. DBSCAN 相比 k-means 最主要的好处是什么?**

- A. 结果一定更准
- B. 不需要任何参数
- C. 计算一定更快
- D. 不需要预先指定簇数,还能识别噪声点

<details><summary>答案与解析</summary>

**答案:D**。DBSCAN 的簇数由 eps 和 minPts 以及数据自己决定,并且会把不密的点标成噪声。但它有 eps 和 minPts 两个同样难调的参数,高维下也会失效。

</details>

**4. 把 DBSCAN 的 eps 调得过大,会发生什么?**

- A. 簇数一定会增加
- B. 算法不收敛
- C. 所有点都变成噪声
- D. 原本分开的簇被连成一片,噪声点变少

<details><summary>答案与解析</summary>

**答案:D**。eps 是搜索半径,越大越容易「从任何一个核心点走到很远的地方」,于是不同簇被连通,同时更多点满足了核心点条件,噪声减少。反过来 eps 太小则大量点变噪声。

</details>

**5. DBSCAN 结果里的 −1 表示什么?**

- A. 聚类失败了
- B. 噪声点,不属于任何簇
- C. 不知道的标签
- D. 第一个簇

<details><summary>答案与解析</summary>

**答案:B**。sklearn 和我们手写的实现都用 −1 标记噪声。注意这些点仍然有坐标和属性,只是算法认为它们不属于任何密集区域,后续分析里要单独处理。

</details>


---

# 第二层 · 空间分析

## L31 · 空间数据的第一件事:坐标系与距离

> 关键词:经纬度 · haversine · 弧度 · 投影 | 建议用时 13 分钟

数据一旦带上经纬度,就属于**空间数据**了。看起来只多了两个数字,但坑多得惊人 —— 最常见的错误是**把经纬度当成平面坐标直接算距离**。

这一幕讲清楚三件事:为什么经度和纬度不能同样对待、球面距离公式怎么来、以及地图为什么要「投影」。

先看后果。北京 (116.407, 39.904) 和上海 (121.474, 31.230),如果直接把两个坐标当平面上的 (x, y) 算距离:

```python
import math

lon1 = 116.407
lat1 = 39.904
lon2 = 121.474
lat2 = 31.23

d = math.sqrt((lon2 - lon1) ** 2 + (lat2 - lat1) ** 2)
print("「度数距离」=", round(d, 3))
print("如果硬按 1 度 = 111.32 km 换算:", round(d * 111.32, 2), "km")
print("真实球面距离约 1067 km —— 差了", round(d * 111.32 - 1067.4, 2), "km")
```

运行结果:

```text
「度数距离」= 10.046
如果硬按 1 度 = 111.32 km 换算: 1118.27 km
真实球面距离约 1067 km —— 差了 50.87 km
```

> **【注意】经度和纬度的「1 度」根本不一样长**
>
> 纬度每 1 度约 111 km,几乎不变;经度每 1 度的长度要乘 `cos(纬度)` —— 赤道上也是 111 km,到北纬 40 度只剩约 85 km,到两极变成 0。所以拿经纬度当平面坐标,等于假装地球在每个纬度上都一样宽。**纬度越高,经度方向被拉伸得越厉害**,算出来的距离和图形都会变形。

正确的做法是在**球面**上量距离,用 haversine 公式。它的推导思路是:先算两点之间那段大圆弧对应的**圆心角 c**,再乘地球半径。

> **【要点】haversine 公式,逐项拆开看**
>
> - **φ、λ 是弧度的纬度和经度**:三角函数吃的是弧度。纬度差 Δφ = φ2 − φ1,经度差 Δλ = λ2 − λ1。
> - <b>sin²(Δφ/2)</b>:南北方向的错开量。**除以 2** 是半角公式的产物 —— haversine 的定义就是 hav(θ) = sin²(θ/2) = (1−cos θ)/2。
> - <b>cos φ1 · cos φ2 · sin²(Δλ/2)</b>:东西方向的错开量。乘以两个 cos 纬度,是因为同样的经度差,纬度越高对应的实际弧长越短 —— 这就是「经度 1 度不一样长」在公式里的体现。
> - **a** = 这两项之和,可以理解成「弧长一半的正弦的平方」。
> - <b>c = 2·asin(√a)</b>:反推出圆心角。**asin 是把 sin 的值还原回角度**,乘 2 是因为 a 里存的是半角。
> - **d = R · c**:半径 6371 km 乘圆心角(弧度)= 弧长。

为什么最后用 `2·asin(√a)`,不用 `2·atan2(√a, √(1−a))`?两者在数学上完全等价(所以下面两个结果一模一样)。但 **√a 只是半角的正弦值,丢掉了一个象限的信息**,当 a 很接近 1(两点几乎在对跖点)时,浮点误差会让 asin 变得不稳;atan2 同时用 y=√a 和 x=√(1−a) 两个分量,能稳定地还原角度。教学和大多数实现用 asin 就够,真实工程里的高精度库会换成 atan2 或 Vincenty 公式。

```python
import math

R = 6371.0
p1 = math.radians(39.904)
p2 = math.radians(31.23)
dp = math.radians(31.23 - 39.904)
dl = math.radians(121.474 - 116.407)

a = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
c = 2 * math.asin(math.sqrt(a))
print("a =", round(a, 6), " 圆心角 c =", round(c, 6), "弧度 =", round(math.degrees(c), 4), "度")
print("d = 6371 * c =", round(R * c, 2), "km")

# 等价的 atan2 写法
c2 = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
print("atan2 写法:", round(R * c2, 2), "km —— 和上面完全相同")
```

运行结果:

```text
a = 0.007  圆心角 c = 0.167534 弧度 = 9.599 度
d = 6371 * c = 1067.36 km
atan2 写法: 1067.36 km —— 和上面完全相同
```

如果忘了转弧度,程序**不会报错**,但结果会错得离谱 —— 这种最难发现:

```python
import math

R = 6371.0
lat1 = 39.904
lat2 = 31.23
lon1 = 116.407
lon2 = 121.474

p1 = math.radians(lat1)
p2 = math.radians(lat2)
a_right = math.sin(math.radians(lat2 - lat1) / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(math.radians(lon2 - lon1) / 2) ** 2
# 故意不转弧度
a_wrong = math.sin((lat2 - lat1) / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin((lon2 - lon1) / 2) ** 2
print("正确 a =", round(a_right, 6), "→", round(R * 2 * math.asin(math.sqrt(a_right)), 2), "km")
print("忘转弧度 a =", round(a_wrong, 6), "→", round(R * 2 * math.asin(math.sqrt(a_wrong)), 2), "km")

# 为什么不报错:sin/cos 把 39.904 当成 39.904 弧度照算,
# 公式本身对任意角度都成立,a 仍落在 0~1 之间,于是给出一个「看似合理」的错误距离
```

运行结果:

```text
正确 a = 0.007 → 1067.36 km
忘转弧度 a = 0.675545 → 12293.04 km
```

> **【注意】同一个地点可能有不止一套坐标**
>
> 中国的互联网地图(高德、百度、腾讯)用的是 \*\*GCJ-02\*\*(俗称火星坐标),GPS 设备输出的是 \*\*WGS-84\*\*,百度还有一套 BD-09。三套之间的偏差在几百米量级 —— 在城市里做「500 米内的店铺」这类分析时,这个偏差足以改变结论。判断方法:如果坐标是直接从 GPS 或国际数据集拿的,一般是 WGS-84;如果是通过国内地图接口拿的,基本是 GCJ-02。**混用之前必须先转换**(常用工具:`coord-convert`、`pyproj` 的自定义转换)。

那为什么我们平时用的地图看起来是平的?因为做了**投影** —— 把球面「摊平」到纸上。任何投影都会变形,区别只是牺牲什么:有的保住面积,有的保住角度,有的保住距离。

> **【要点】投影的直觉:为什么地图是「压扁」的**
>
> - 把橘子皮摊平一定会裂开或起皱 —— 球面不可能**无变形**地铺成平面,这是几何事实,不是技术不够好。
> - 常见做法:**等距圆柱投影**把经纬度当 x、y 直接画(最简单,高纬度严重变形);**Web 墨卡托**保住角度和形状,但面积失真(格陵兰看起来和非洲一样大)。
> - 中国常用的**高斯-克吕格投影**(CGCS2000 坐标系下按 3° 或 6° 分带)和国际通用的 **UTM** 都是横轴墨卡托类的**等角投影**,在一个带内距离和角度都很准,适合做局部空间分析。注意 CGCS2000 本身是坐标系(基准),不是投影。
> - 工程上的经验:**要算距离就选等距或局部投影,不要用墨卡托;要画地图才考虑墨卡托**。像「北京 300 公里内有哪些城市」这种问题,直接用 haversine 在球面上算最省事。

> **【对照】这段手写代码 ↔ 真实项目里的写法**
>
> - 手写 haversine ↔ `geopy.distance.great_circle((lat1, lon1), (lat2, lon2))` 或 `geopy.distance.distance(...)`
> - 向量化批量算 ↔ `sklearn.metrics.pairwise.haversine_distances(X, Y)`(注意它要的是弧度)
> - 把经纬度投影成平面坐标 ↔ `gdf.to_crs(epsg=32650)`(UTM 50N,覆盖东经 114°~120°)或 CGCS2000 高斯-克吕格分带(如 `EPSG:4547`);`EPSG:4490` 是 CGCS2000 的经纬度坐标,不是投影;`EPSG:3857`(Web 墨卡托)只适合画图,不适合量距离
> - 坐标系转换(WGS-84 ↔ GCJ-02) ↔ 没有标准库,用 `coord-convert` / `eviltransform` 之类的社区实现
> - 椭球面上的精确距离 ↔ `pyproj.Geod(ellps="WGS84").inv(lon1, lat1, lon2, lat2)`(按椭球体计算,比正球更准;不含高程)

### 本关完整示例

```python
import math
from dataset import dataset

R = 6371.0

def hav(lon1, lat1, lon2, lat2):
    # 1) 先把角度换成弧度
    p1 = math.radians(lat1)
    p2 = math.radians(lat2)
    dp = math.radians(lat2 - lat1)
    dl = math.radians(lon2 - lon1)
    # 2) 南北项 + 东西项(东西项要乘两个 cos 纬度)
    a = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    # 3) 反解圆心角,再乘半径
    return R * 2 * math.asin(math.sqrt(a))

bj = dataset.cities[0]
sh = dataset.cities[8]
print("北京 - 上海 的拆解:")
print("  经纬度:", bj["lon"], bj["lat"], "→", sh["lon"], sh["lat"])
p1 = math.radians(bj["lat"])
p2 = math.radians(sh["lat"])
dp = math.radians(sh["lat"] - bj["lat"])
dl = math.radians(sh["lon"] - bj["lon"])
ns = math.sin(dp / 2) ** 2
ew = math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
a = ns + ew
c = 2 * math.asin(math.sqrt(a))
print("  南北项 =", round(ns, 6), " 东西项 =", round(ew, 6))
print("  a =", round(a, 6), " 圆心角 =", round(math.degrees(c), 4), "度")
print("  球面距离 =", round(R * c, 2), "km")
print()

# 直接当平面算会错多少
flat = math.sqrt((sh["lon"] - bj["lon"]) ** 2 + (sh["lat"] - bj["lat"]) ** 2)
print("把经纬度当平面坐标算出来的「度数距离」=", round(flat, 3))
print("硬按 1 度 = 111.32 km 换算 =", round(flat * 111.32, 2), "km")
print("误差 =", round(flat * 111.32 - R * c, 2), "km")
print()

# 用真实球面距离给 56 个城市排序:离北京最近的 6 个
pairs = []
for cty in dataset.cities:
    if cty["name"] != bj["name"]:
        pairs.append([hav(bj["lon"], bj["lat"], cty["lon"], cty["lat"]), cty["name"]])

# 每个元素是 [距离, 城市名],列表排序时先比第 0 项,正好按距离从小到大
pairs.sort()

print("离北京最近的 6 个城市(真实球面距离):")
for i in range(6):
    print("  ", pairs[i][1], round(pairs[i][0], 1), "km")
print()

# 顺便验证一个常识:同样是「经度差 1 度」,纬度越高实际距离越短
print("经度差 1 度,在不同纬度上的实际距离:")
for lat in [20, 40, 60]:
    print("  北纬", lat, "度:", round(hav(110, lat, 111, lat), 1), "km")
```

运行结果:

```text
北京 - 上海 的拆解:
  经纬度: 116.407 39.904 → 121.474 31.23
  南北项 = 0.005719  东西项 = 0.001282
  a = 0.007  圆心角 = 9.599 度
  球面距离 = 1067.36 km

把经纬度当平面坐标算出来的「度数距离」= 10.046
硬按 1 度 = 111.32 km 换算 = 1118.27 km
误差 = 50.91 km

离北京最近的 6 个城市(真实球面距离):
   天津 109.4 km
   保定 140.3 km
   唐山 154.5 km
   石家庄 263.9 km
   大同 265.5 km
   济南 367.0 km

经度差 1 度,在不同纬度上的实际距离:
  北纬 20 度: 104.5 km
  北纬 40 度: 85.2 km
  北纬 60 度: 55.6 km
```

### 动手练习

1. 把 R 从 6371 改成 6378(赤道半径)和 6357(极半径),看北京到上海的距离变化多少 —— 体会「地球不是正球」。
2. 故意删掉公式里两个 cos 纬度,再算北京到上海,看结果差多少,理解这一项为什么不能省。
3. 用 haversine 算一遍「北京到乌鲁木齐」,和 2410.9 km 对比。(提示:dataset.cities 里能找到乌鲁木齐。)
4. 把最远的那几个城市找出来(比如喀什),想一想:为什么跨国分析必须用球面距离而不是平面距离?

### 随堂检测

**1. 为什么经纬度不能直接当平面坐标算距离?**

- A. 因为经纬度单位不一样
- B. 1 度经度的实际长度随纬度变化,1 度纬度基本不变
- C. 因为经度是负数
- D. 因为地球是圆的所以距离永远算不准

<details><summary>答案与解析</summary>

**答案:B**。1 度经度 = 111.32 × cos(纬度) km,在北纬 40 度只有约 85 km。当成平面就等于假设所有纬度上地球一样宽,高纬度的东西方向会被拉伸。

</details>

**2. haversine 公式里为什么要先 math.radians 把角度转成弧度?**

- A. 因为球面距离公式要求用弧度
- B. 防止结果是负数
- C. 为了统一单位方便打印
- D. math.sin/cos 的参数是弧度,直接传角度会得到错误的值

<details><summary>答案与解析</summary>

**答案:D**。sin 的自变量是弧度。传 39.9 会被当成 39.9 弧度而不是 39.9 度,结果毫无意义,而且通常不会报错,所以最难查。

</details>

**3. 公式里的 cos φ1 · cos φ2 这一项起什么作用?**

- A. 把结果换算成公里
- B. 校正「同样的经度差在高纬度对应的弧长更短」
- C. 计算纬度方向的错开量
- D. 保证 a 小于 1

<details><summary>答案与解析</summary>

**答案:B**。东西方向的弧长 = 经度差 × cos(纬度)。两个点各有一个纬度,所以取两个 cos 的乘积,相当于沿路径的平均压缩。纬度方向的错开量已经在 sin²(Δφ/2) 那一项里了。

</details>

**4. 为什么最后要乘 2、并用 asin 反解?**

- A. 为了让结果保持正数
- B. a 里存的是半角的正弦平方,所以要还原成整段的圆心角
- C. 因为 asin 比 acos 快
- D. 半径的单位是度

<details><summary>答案与解析</summary>

**答案:B**。hav(θ) = sin²(θ/2),所以 √a = sin(c/2),反解得到 c/2 再乘 2 才是圆心角 c。最后 d = R × c 是「半径 × 弧度 = 弧长」。

</details>

**5. 关于地图投影,下面哪个说法是对的?**

- A. 不可能把球面无变形地画成平面,只能选择保住面积或保住角度
- B. 好的投影可以做到零变形
- C. 投影只影响画图,不影响距离计算
- D. 墨卡托投影适合用来算距离

<details><summary>答案与解析</summary>

**答案:A**。球面到平面不存在等距映射(高斯绝妙定理)。Web 墨卡托保住角度但面积严重失真(格陵兰看起来和非洲差不多大),所以算距离要在投影坐标或球面上做。

</details>

## L33 · 空间关系:包围盒、缓冲区与空间连接

> 关键词:bbox · 缓冲区 · 空间连接 · point-in-polygon | 建议用时 13 分钟

空间分析问得最多的不是「有多远」,而是 <b>「谁挨着谁」「谁在谁里面」</b>:这个监测站属于哪个省?这家店周边 3 公里有多少用户?

这一幕用三个最基础的工具回答这些问题:<b>包围盒(bbox)</b>、**缓冲区**、**空间连接**。它们都只需要距离和大小比较,不需要任何高级库。

最省事的空间判定是**包围盒**(bounding box,简称 bbox):用一个矩形把一块区域框住,矩形的四条边就是这块区域的最小经度、最小纬度、最大经度、最大纬度。判断一个点在不在里面,只要比四次。

```python
b = [116.36, 30.75, 121.95, 35.13]   # 江苏省的 bbox

def in_bbox(lon, lat, box):
    return lon >= box[0] and lon <= box[2] and lat >= box[1] and lat <= box[3]

print("南京 (118.8, 32.1) 在江苏省 bbox 里吗?", in_bbox(118.8, 32.1, b))
print("广州 (113.3, 23.1) 在江苏省 bbox 里吗?", in_bbox(113.3, 23.1, b))
print("上海 (121.5, 31.2) 在江苏省 bbox 里吗?", in_bbox(121.5, 31.2, b))
```

运行结果:

```text
南京 (118.8, 32.1) 在江苏省 bbox 里吗? True
广州 (113.3, 23.1) 在江苏省 bbox 里吗? False
上海 (121.5, 31.2) 在江苏省 bbox 里吗? True
```

> **【注意】bbox 只能「宁可错抓,不可放过」**
>
> 矩形永远比真实形状大,尤其是狭长或不规则的省(内蒙古的 bbox 从东经 97 度横到 126 度,把大半个北方都框进去了)。用 bbox 判断归属一定会**误判**:上海的坐标正好落进了江苏省的 bbox(实测命中),北京同时落进北京市、河北省、内蒙古自治区三个 bbox。所以 bbox 只适合做「先粗筛」,精确归属必须用真正的**多边形包含判断**(point-in-polygon,射线法)。

先看这个误判有多普遍。下面拿数据集里 20 个省级区域的 bbox 去框几个典型城市(数据集里**没有重庆市和甘肃省**,注意看重庆和兰州的结果):

```python
from dataset import dataset

for name in ["北京", "上海", "哈尔滨", "重庆", "兰州"]:
    for c in dataset.cities:
        if c["name"] == name:
            hits = []
            for p in dataset.provinces:
                b = p["bbox"]
                if b[0] <= c["lon"] <= b[2] and b[1] <= c["lat"] <= b[3]:
                    hits.append(p["name"])
            print(name, "→", hits, "(", len(hits), "个候选)")
```

运行结果:

```text
北京 → ['北京市', '河北省', '内蒙古自治区'] ( 3 个候选)
上海 → ['上海市', '江苏省'] ( 2 个候选)
哈尔滨 → ['吉林省', '黑龙江省'] ( 2 个候选)
重庆 → ['四川省'] ( 1 个候选)
兰州 → [] ( 0 个候选)
```

> **【要点】候选有多个时怎么办**
>
> - bbox 判断是**必要条件**不是充分条件:命中不代表真的在里面,没命中则一定不在。
> - 常见的补救办法:在有多个候选时,选**面积最小的那个** —— 小框更贴合真实边界。
> - 但这个补救也只是启发式:实测哈尔滨会被判给吉林省(黑龙江省的 bbox 太大)。
> - 想真正做到准确,得用多边形边界(GeoJSON)+ 射线法,或者直接调 `geopandas` 的 `sjoin`。

第二个工具是**缓冲区**:以某个点为中心、给定半径画一个圈,问「圈里有哪些东西」。这在选址、选址评估、服务范围分析里天天用到。

```python
import math
from dataset import dataset

def hav(lon1, lat1, lon2, lat2):
    R = 6371.0
    p1 = math.radians(lat1)
    p2 = math.radians(lat2)
    dp = math.radians(lat2 - lat1)
    dl = math.radians(lon2 - lon1)
    a = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return R * 2 * math.asin(math.sqrt(a))

bj = dataset.cities[0]
print("北京 300 km 缓冲区内的城市:")
for c in dataset.cities:
    if c["name"] != bj["name"]:
        d = hav(bj["lon"], bj["lat"], c["lon"], c["lat"])
        if d <= 300:
            print("   ", c["name"], round(d, 1), "km")
```

运行结果:

```text
北京 300 km 缓冲区内的城市:
    天津 109.4 km
    石家庄 263.9 km
    唐山 154.5 km
    保定 140.3 km
    大同 265.5 km
```

第三个工具是**空间连接**:把一张点表(城市)和一张面表(省)接起来,给每个点补上「它属于哪个面」。这是空间数据里最常见的一步,做完之后才能按区域汇总统计。

```python
from dataset import dataset

cnt = {}
none = 0
for c in dataset.cities:
    best = ""
    bestA = -1
    for p in dataset.provinces:
        b = p["bbox"]
        if c["lon"] >= b[0] and c["lon"] <= b[2] and c["lat"] >= b[1] and c["lat"] <= b[3]:
            if bestA < 0 or p["area"] < bestA:
                bestA = p["area"]
                best = p["name"]
    if best == "":
        none = none + 1
    elif best in cnt:
        cnt[best] = cnt[best] + 1
    else:
        cnt[best] = 1
print("没有落到任何省的城市数:", none)
for k in cnt:
    print(k, cnt[k])
```

运行结果:

```text
没有落到任何省的城市数: 10
北京市 1
天津市 1
山西省 5
内蒙古自治区 2
河北省 2
上海市 1
江苏省 4
浙江省 2
山东省 2
福建省 2
广东省 6
湖北省 2
湖南省 1
河南省 1
四川省 4
新疆维吾尔自治区 3
辽宁省 2
吉林省 3
黑龙江省 2
```

> **【提示】为什么用点代表一个城市就够了**
>
> 城市是有边界的多边形,但做区域汇总时通常只用它的**行政中心点**。这是一种常见的简化:点落进哪个面,就认为这个城市属于哪里。真实项目里要小心两种边界情况:**点正好落在边界上**(按惯例「左闭右开」,但不同库的约定不一样),以及**城市跨省**(中心点和实际辖区不一致)。遇到争议点最好人工核对。

> **【对照】这段手写代码 ↔ 真实项目里的写法**
>
> - 手写 bbox 判断 ↔ `shapely.geometry.box(minx, miny, maxx, maxy).contains(point)`,或直接比 `geometry.bounds`
> - 手写「选最小面积的候选」 ↔ `gpd.sjoin(points, polys, how="inner", predicate="within")`
> - 手写缓冲区距离筛选 ↔ `point.buffer(0.05)`(注意:shapely 的 buffer 用的是**坐标本身的单位**,经纬度下 0.05 是「度」,落到地面上是一个东西窄、南北长的椭圆;要按公里画圆,先投影到 UTM 等米制坐标再 buffer)
> - 更专业的半径查询 ↔ `geopandas.sjoin_nearest(left, right, max_distance=...)`(投影坐标下)或 `scipy.spatial.cKDTree`
> - 真正精确的点面判断 ↔ `shapely` 的射线法实现(`contains` / `within` / `intersects`)

### 本关完整示例

```python
import math
from dataset import dataset

def hav(lon1, lat1, lon2, lat2):
    R = 6371.0
    p1 = math.radians(lat1)
    p2 = math.radians(lat2)
    dp = math.radians(lat2 - lat1)
    dl = math.radians(lon2 - lon1)
    a = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return R * 2 * math.asin(math.sqrt(a))

bj = dataset.cities[0]

# 1) bbox:先看北京所在的「粗范围」
print("北京的坐标:", bj["lon"], bj["lat"])
for p in dataset.provinces:
    b = p["bbox"]
    if bj["lon"] >= b[0] and bj["lon"] <= b[2] and bj["lat"] >= b[1] and bj["lat"] <= b[3]:
        print("  落在 bbox 里:", p["name"], "面积", p["area"])
print("  → 同时命中多个 bbox,bbox 只能粗筛")
print()

# 2) 缓冲区:距北京 300 km 内的城市
print("北京 300 km 缓冲区内的城市:")
inside = 0
for cty in dataset.cities:
    if cty["name"] != bj["name"]:
        d = hav(bj["lon"], bj["lat"], cty["lon"], cty["lat"])
        if d <= 300:
            inside = inside + 1
            print("  ", cty["name"], round(d, 1), "km")
print("  共", inside, "个(总城市数", len(dataset.cities), ")")
print()

# 3) 空间连接:56 个城市各自归属到哪个省
cnt = {}
none = 0
multi = 0
for cty in dataset.cities:
    best = ""
    bestA = -1
    hit = 0
    for p in dataset.provinces:
        b = p["bbox"]
        if cty["lon"] >= b[0] and cty["lon"] <= b[2] and cty["lat"] >= b[1] and cty["lat"] <= b[3]:
            hit = hit + 1
            if bestA < 0 or p["area"] < bestA:
                bestA = p["area"]
                best = p["name"]
    if hit > 1:
        multi = multi + 1
    if best == "":
        none = none + 1
    elif best in cnt:
        cnt[best] = cnt[best] + 1
    else:
        cnt[best] = 1

print("空间连接结果(按最小 bbox 归属):")
print("  落进多个 bbox、需要取舍的城市:", multi, "个")
print("  一个 bbox 都没落进的:", none, "个")
total = 0
for k in cnt:
    total = total + cnt[k]
print("  成功归属的:", total, "个")
print()
print("落进城市最多的 5 个省")
keys = []
for k in cnt:
    keys.append(k)
for i in range(len(keys)):
    for j in range(len(keys) - 1 - i):
        if cnt[keys[j]] < cnt[keys[j + 1]]:
            tmp = keys[j]
            keys[j] = keys[j + 1]
            keys[j + 1] = tmp
for i in range(5):
    print("  ", keys[i], cnt[keys[i]], "个城市")
print()
print("手工核对几个已知会出问题的点:")
for name in ["哈尔滨", "重庆", "兰州"]:
    for cty in dataset.cities:
        if cty["name"] == name:
            best = ""
            bestA = -1
            for p in dataset.provinces:
                b = p["bbox"]
                if cty["lon"] >= b[0] and cty["lon"] <= b[2] and cty["lat"] >= b[1] and cty["lat"] <= b[3]:
                    if bestA < 0 or p["area"] < bestA:
                        bestA = p["area"]
                        best = p["name"]
            if best == "":
                best = "(一个都没命中)"
            print("  ", name, "→", best)
```

运行结果:

```text
北京的坐标: 116.407 39.904
  落在 bbox 里: 北京市 面积 16410
  落在 bbox 里: 河北省 面积 188800
  落在 bbox 里: 内蒙古自治区 面积 1183000
  → 同时命中多个 bbox,bbox 只能粗筛

北京 300 km 缓冲区内的城市:
   天津 109.4 km
   石家庄 263.9 km
   唐山 154.5 km
   保定 140.3 km
   大同 265.5 km
  共 5 个(总城市数 56 )

空间连接结果(按最小 bbox 归属):
  落进多个 bbox、需要取舍的城市: 22 个
  一个 bbox 都没落进的: 10 个
  成功归属的: 46 个

落进城市最多的 5 个省
   广东省 6 个城市
   山西省 5 个城市
   江苏省 4 个城市
   四川省 4 个城市
   新疆维吾尔自治区 3 个城市

手工核对几个已知会出问题的点:
   哈尔滨 → 吉林省
   重庆 → 四川省
   兰州 → (一个都没命中)
```

### 动手练习

1. 把缓冲区半径从 300 km 改成 500 km 和 1000 km,看城市个数怎么涨 —— 想想这种增长方式说明城市分布的什么特点。
2. 把「选面积最小的 bbox」改成「选第一个命中的 bbox」,重新跑空间连接,看结果变了多少 —— 体会「算法细节影响结论」。
3. 给空间连接加一条规则:如果命中多个 bbox 就记为「待人工确认」,统计这类城市有几个。
4. 试着自己写一个射线法 point-in-polygon 的思路:从点向右发一条水平射线,数它和边界相交几次(奇数在里面,偶数在外面)。

### 随堂检测

**1. 用 bbox 判断点是否在省内,主要问题是什么?**

- A. 需要联网
- B. 只能判断正方形区域
- C. 矩形比真实边界大,会误判(尤其狭长或不规则的省)
- D. 计算太慢

<details><summary>答案与解析</summary>

**答案:C**。bbox 是真实形状的外接矩形,一定包含一些实际不属于该区域的点。实测上海会命中江苏省的 bbox,北京同时命中三个。所以它只能做粗筛。

</details>

**2. 「缓冲区」在空间分析里指什么?**

- A. 以某个要素为中心、给定半径覆盖的范围
- B. 两块区域的公共边
- C. 数据的备份区域
- D. 省界的中心线

<details><summary>答案与解析</summary>

**答案:A**。缓冲区是围绕点/线/面生成的一个范围,用来回答「半径内有哪些东西」。做这类查询时,距离必须用球面或投影距离,不能用经纬度差。

</details>

**3. 空间连接(spatial join)的作用是?**

- A. 把坐标转成字符串
- B. 合并两个数据库
- C. 按空间位置把两张表连起来,比如给每个城市补上所属省份
- D. 把两张表按行号直接拼在一起

<details><summary>答案与解析</summary>

**答案:C**。普通 join 靠相同的键值匹配,空间连接靠几何关系(在内部、相交、最近)匹配,典型用途就是点归属到面,然后按面汇总统计。

</details>

**4. 为什么 shapely 里对经纬度坐标直接调 .buffer() 会得到椭圆而不是圆?**

- A. buffer 用的是坐标单位(度),而 1 度经度和 1 度纬度长度不同
- B. 因为 buffer 默认是正方形
- C. 因为地球是椭球体
- D. 因为 shapely 有 bug

<details><summary>答案与解析</summary>

**答案:A**。buffer(0.05) 的含义是「坐标值加减 0.05」,在经纬度下就是 0.05 度。由于经度方向的实际长度随纬度缩短,落到地面上就成了一个东西窄、南北长的椭圆。正确做法是先投影到等距坐标系(如 UTM)再做 buffer。

</details>

**5. 实测哈尔滨被 bbox 方法判给了吉林省,这说明了什么?**

- A. 启发式规则(选最小 bbox)也会出错,精确归属需要用真实多边形
- B. 应该改成选最大 bbox
- C. 数据集里的省界标错了
- D. 哈尔滨真的属于吉林

<details><summary>答案与解析</summary>

**答案:A**。黑龙江省的 bbox 很大,和吉林省的 bbox 有重叠,而「选面积最小」的规则在重叠区会偏向小框。这类问题只有用真实边界多边形做 point-in-polygon 才能避免,也说明了为什么真实项目依赖 geopandas/shapely 而不是比大小。

</details>

## L35 · 空间自相关:莫兰指数与热点识别

> 关键词:空间权重 · 莫兰指数 I · LISA · Getis-Ord Gi\* | 建议用时 15 分钟

普通统计只关心「这些数值分布如何」,空间统计多问一句:<b>这些数值在空间上是随机撒开的,还是扎堆的?</b>

判断这件事的核心指标叫**莫兰指数**。它只有一个数,却能把「聚集」「随机」「棋盘格」三种完全不同的格局区分开。这一幕用 12×12 的真实 PM2.5 网格把它手算一遍。

先用直觉想一个场景。有两块地,每块都有 16 个格子的数值,均值一样、方差也一样,但一块是「高值连成一片」,另一块是「高高低低交错」。普通统计量完全分不出它们,空间统计可以。

> **【要点】先定义「谁是谁的邻居」:空间权重**
>
> - 任何空间自相关指标都需要一张**权重表 w<sub>ij</sub>**:第 i 个和第 j 个位置有多「近」。
> - 最常见两种:**邻接权重**(共边或共点就算 1,否则 0)和 **k 近邻权重**(离得最近的 k 个算 1)。
> - 还有一种 **距离衰减**:w = 1/d²,越远影响越小。
> - **行标准化**:把每行的权重除以该行之和,让每行加起来等于 1。它的含义是「每个位置只看邻居的**平均水平**」。
> - 网格数据一般用「上下左右四个邻居」(rook 邻接);不规则的点数据常用 k 近邻。

把「邻居的平均值」算出来,叫**空间滞后**。如果每个格子的值都和它邻居的平均值差不多(高值旁边也是高值),那就是聚集。莫兰指数就是在量化这件事:

```python
import math

# 用 4 个格子演示「空间滞后」
vals = [10.0, 12.0, 40.0, 42.0]
# 位置 0-1 相邻、2-3 相邻
nb = [[1], [0], [3], [2]]
for i in range(4):
    s = 0.0
    for j in nb[i]:
        s = s + vals[j]
    print("格子", i, "值 =", vals[i], " 邻居平均值 =", round(s / len(nb[i]), 2))
```

运行结果:

```text
格子 0 值 = 10.0  邻居平均值 = 12.0
格子 1 值 = 12.0  邻居平均值 = 10.0
格子 2 值 = 40.0  邻居平均值 = 42.0
格子 3 值 = 42.0  邻居平均值 = 40.0
```

> **【要点】莫兰指数公式,分子分母在算什么**
>
> - **I = (n / W) · ΣΣ w<sub>ij</sub>(x<sub>i</sub>−x̄)(x<sub>j</sub>−x̄) / Σ(x<sub>i</sub>−x̄)²**
> - **分母 Σ(x<sub>i</sub>−x̄)²**:所有点偏离均值的平方和 —— 就是「数据本身有多分散」,是个固定的尺子。
> - **分子**:对每一对邻居,把两个偏差**相乘**再加权求和。同号(都高于均值或都低于均值)相乘为正,异号相乘为负。
> - **n / W**:n 是点数,W 是所有 w<sub>ij</sub> 之和,用来把量级归一化。**如果做了行标准化,每一行权重和为 1,那么 W = n,这一项就是 1**,公式可以省掉它。
> - 所以 I 的本质是:<b>「邻居同号的强度」相对「整体分散程度」的比值</b>。

I 的取值范围大致在 −1 到 1 之间,读法很关键:

> **【要点】莫兰指数怎么读**
>
> - **I 接近 0**:邻居之间没有关系,高值低值随机撒开。
> - **I 接近 +1**:强正相关 —— 高值挨着高值、低值挨着低值,一片一片地扎堆。
> - **I 接近 −1**:强负相关 —— 高值旁边总是低值,像**棋盘格**一样交错。
> - 注意 I 为负不代表「没有规律」,而是「有规律的交替」。
> - 算出来的 I 是好是坏要看参照:通常和「把数值在空间上随机重排后算出的 I」比较,或者算 z 分数。

光有一个全局数字还不够 —— 它可能被少数几个区域主导。所以还要算<b>局部莫兰(LISA)</b>:给每个格点算一个局部值,看它自己和邻居的关系属于哪一类。

```python
# 局部莫兰 Ii = (自己的偏差) × (邻居的平均偏差) / 方差
# 还是上面那 4 个格子:0-1 相邻、2-3 相邻
vals = [10.0, 12.0, 40.0, 42.0]
nb = [[1], [0], [3], [2]]
n = len(vals)
mean = sum(vals) / n
var = 0.0
for v in vals:
    var = var + (v - mean) ** 2
var = var / n

for i in range(n):
    lag = 0.0
    for j in nb[i]:
        lag = lag + (vals[j] - mean)
    lag = lag / len(nb[i])
    li = (vals[i] - mean) * lag / var
    if vals[i] >= mean and lag >= 0:
        kind = "高-高"
    elif vals[i] < mean and lag < 0:
        kind = "低-低"
    elif vals[i] >= mean:
        kind = "高-低"
    else:
        kind = "低-高"
    print("格子", i, "值", vals[i], " 偏差", round(vals[i] - mean, 1), " 邻居平均偏差", round(lag, 1), " Ii =", round(li, 2), kind)
```

运行结果:

```text
格子 0 值 10.0  偏差 -16.0  邻居平均偏差 -14.0  Ii = 0.99 低-低
格子 1 值 12.0  偏差 -14.0  邻居平均偏差 -16.0  Ii = 0.99 低-低
格子 2 值 40.0  偏差 14.0  邻居平均偏差 16.0  Ii = 0.99 高-高
格子 3 值 42.0  偏差 16.0  邻居平均偏差 14.0  Ii = 0.99 高-高
```

> **【要点】LISA 的四种类型**
>
> - <b>高-高(HH)</b>:我自己高,邻居也高 —— 真正的热点核心区。
> - <b>低-低(LL)</b>:我自己低,邻居也低 —— 冷点区。
> - <b>高-低(HL)</b>:我自己高,周围低 —— 孤立的异常高值(要单独排查,可能是真实的特殊源,也可能是数据错误)。
> - <b>低-高(LH)</b>:我自己低,周围高 —— 低值被高值包围的「洼地」。
> - 前两类说明聚集,后两类说明**空间异常** —— 它们在业务上往往比聚集更值得看。

还有一套更直接找热点的指标叫 <b>Getis-Ord Gi\*</b>。思路更简单:把某个点**自己加上它邻居**的和算出来(带 \* 号就表示「含自己」),看这个「局部和」比随机情况下的期望高出多少个标准差。z 值大就是热点,z 值很负就是冷点。

```python
import math

# Gi* 的直觉:局部和减去期望,再除以标准差
mean = 62.14
sd = 29.09
n = 144
for local_sum in [250.0, 400.0, 700.0, 1000.0]:      # 期望值是 5 × 62.14 ≈ 310.7
    wi = 5.0          # Gi* 把自己也算进去:自己 + 上下左右 4 个邻居
    expect = mean * wi
    se = sd * math.sqrt(wi * (n - wi) / (n - 1.0))
    print("局部和(自己 + 4 个邻居) =", local_sum, " z =", round((local_sum - expect) / se, 2))
```

运行结果:

```text
局部和(自己 + 4 个邻居) = 250.0  z = -0.95
局部和(自己 + 4 个邻居) = 400.0  z = 1.39
局部和(自己 + 4 个邻居) = 700.0  z = 6.07
局部和(自己 + 4 个邻居) = 1000.0  z = 10.75
```

> **【注意】换一套空间权重,结论可能就变了**
>
> 莫兰指数**完全建立在权重定义上**。同一份数据,用 rook 邻接和用 queen 邻接、用 k=4 和用 k=8,算出来的 I 会有明显差别;如果用距离衰减权重,还要再选一个带宽。所以真实研究里必须**报告用了什么权重矩阵**,而且通常会做敏感性分析(换几套权重看结论是否稳健)。另一个真实坑是:空间自相关**很容易被虚假相关制造出来** —— 两个都在向北递减的变量(比如气温和 PM2.5),算出来的空间相关可能很高,但它们之间没有因果关系,这叫「空间混杂」。

> **【对照】这段手写代码 ↔ 真实项目里的写法**
>
> - 手写 rook 邻接权重 ↔ `libpysal.weights.Rook.from_dataframe(gdf)`,k 近邻用 `KNN.from_dataframe(gdf, k=4)`
> - 手写行标准化 ↔ `w.transform = "r"`
> - 手写全局莫兰指数 ↔ `esda.moran.Moran(y, w)`(结果对象里有 `.I`、`.z_sim`、`.p_sim`)
> - 手写局部莫兰 ↔ `esda.moran.Moran_Local(y, w)`(配合 `lisa_cluster` 画图)
> - 手写 Gi\* ↔ `esda.getisord.G_Local(y, w, star=True)`
> - 真实报告里还会做置换检验(几百次随机重排)↔ `Moran(y, w, permutations=999)`

### 本关完整示例

```python
import math
import random
from dataset import dataset

# 把 12×12 的 PM2.5 网格拉平成一串
rows = dataset.pm_grid["rows"]
cols = dataset.pm_grid["cols"]
vals = []
for r in range(rows):
    for c in range(cols):
        vals.append(dataset.pm_grid["values"][r][c])
n = len(vals)

# 空间权重:上下左右四个邻居(边界上少几个),后面做行标准化
nb = []
for r in range(rows):
    for c in range(cols):
        row = []
        if r > 0:
            row.append((r - 1) * cols + c)
        if r < rows - 1:
            row.append((r + 1) * cols + c)
        if c > 0:
            row.append(r * cols + (c - 1))
        if c < cols - 1:
            row.append(r * cols + (c + 1))
        nb.append(row)

# 均值和方差
tot = 0.0
ss = 0.0
for v in vals:
    tot = tot + v
    ss = ss + v * v
mean = tot / n
var = ss / n - mean * mean
sd = math.sqrt(var)
print("格点数 n =", n)
print("PM2.5 均值 =", round(mean, 2), " 标准差 =", round(sd, 2))
print("最大 =", round(max(vals), 2), " 最小 =", round(min(vals), 2))
print()

# 空间滞后:每个格子看它邻居的平均偏差
lag = []
for i in range(n):
    s = 0.0
    for j in nb[i]:
        s = s + (vals[j] - mean)
    lag.append(s / len(nb[i]))

# 全局莫兰指数(权重已行标准化,所以 n/W = 1)
num = 0.0
for i in range(n):
    num = num + (vals[i] - mean) * lag[i]
den = 0.0
for v in vals:
    den = den + (v - mean) ** 2
I = num / den
print("莫兰指数 I =", round(I, 4))
print("  接近 1 说明高值成片、低值成片(强空间聚集)")
print()

# 置换检验:把数值在网格上随机打乱 199 次,看打乱后的 I 能不能达到真实的 I
random.seed(42)                 # 固定随机种子,结果可复现

def moran(x):
    m = sum(x) / len(x)
    num = 0.0
    den = 0.0
    for i in range(len(x)):
        s = 0.0
        for j in nb[i]:
            s = s + (x[j] - m)
        num = num + (x[i] - m) * (s / len(nb[i]))
        den = den + (x[i] - m) ** 2
    return num / den

perm = 199
shuffled = vals[:]              # 复制一份再打乱,不动原数据
perm_I = []
larger = 0
for k in range(perm):
    random.shuffle(shuffled)
    v = moran(shuffled)
    perm_I.append(v)
    if v >= I:
        larger = larger + 1
print("随机打乱", perm, "次:I 的平均值 =", round(sum(perm_I) / perm, 4), " 最大值 =", round(max(perm_I), 4))
print("伪 p 值 = (", larger, "+ 1) / (", perm, "+ 1) =", round((larger + 1) / (perm + 1), 3))
print("  打乱后的 I 都在 0 附近,没有一次达到", round(I, 4), "→ 原来的聚集不是巧合")
print()

# 局部莫兰:每个格子属于哪一类
hh = 0
ll = 0
hl = 0
lh = 0
for i in range(n):
    li = (vals[i] - mean) * lag[i] / var
    if vals[i] >= mean and li > 0:
        hh = hh + 1
    elif vals[i] < mean and li > 0:
        ll = ll + 1
    elif vals[i] >= mean and li < 0:
        hl = hl + 1
    else:
        lh = lh + 1
print("LISA 分类:高-高", hh, " 低-低", ll, " 高-低", hl, " 低-高", lh, "(只按象限分类,未做显著性检验)")
print("  高-高和低-低多 → 聚集;高-低/低-高是空间异常点,值得单独排查")
print()

# Getis-Ord Gi*:邻居和比期望高多少个标准差
hot = 0
cold = 0
zmax = -99.0
zmin = 99.0
for i in range(n):
    s = vals[i]                  # Gi* 含自己
    for j in nb[i]:
        s = s + vals[j]
    wi = len(nb[i]) + 1.0
    expect = mean * wi
    se = sd * math.sqrt(wi * (n - wi) / (n - 1.0))
    z = (s - expect) / se
    if z > zmax:
        zmax = z
    if z < zmin:
        zmin = z
    if z > 2.0:
        hot = hot + 1
    if z < -2.0:
        cold = cold + 1
print("Gi* z 值范围:", round(zmin, 2), "~", round(zmax, 2))
print("热点格点(z > 2):", hot, " 冷点格点(z < -2):", cold)
```

运行结果:

```text
格点数 n = 144
PM2.5 均值 = 62.14  标准差 = 29.09
最大 = 143.6  最小 = 23

莫兰指数 I = 0.8013
  接近 1 说明高值成片、低值成片(强空间聚集)

随机打乱 199 次:I 的平均值 = -0.0035  最大值 = 0.148
伪 p 值 = ( 0 + 1) / ( 199 + 1) = 0.005
  打乱后的 I 都在 0 附近,没有一次达到 0.8013 → 原来的聚集不是巧合

LISA 分类:高-高 56  低-低 82  高-低 1  低-高 5 (只按象限分类,未做显著性检验)
  高-高和低-低多 → 聚集;高-低/低-高是空间异常点,值得单独排查

Gi* z 值范围: -2.8 ~ 5.24
热点格点(z > 2): 24  冷点格点(z < -2): 20
```

### 动手练习

1. 把邻接权重从「上下左右 4 个」改成「含对角线的 8 个」(queen 邻接),重算莫兰指数,看它变大还是变小,想想为什么。
2. 把置换次数从 199 改成 999、或换一个随机种子,看伪 p 值是否稳定 —— 理解置换检验为什么要「随机」打乱、而且次数要够多。
3. 把热点阈值从 2.0 改成 1.5 和 3.0,数一数热点格点各有多少个。
4. 用 row 0~3(南部)和 row 8~11(北部)分别算一次均值,比较网格南北两端的 PM2.5 水平(行号约定见 L37)。
5. 想一个反向的例子:什么样的 PM2.5 网格会让莫兰指数接近 −1?

### 随堂检测

**1. 莫兰指数 I 接近 −1 说明数据在空间上是什么格局?**

- A. 高值和低值交错分布,像棋盘格
- B. 高值全部聚在一起
- C. 完全是随机分布
- D. 数据有缺失值

<details><summary>答案与解析</summary>

**答案:A**。分子的每一项是两个邻居偏差的乘积,异号相乘为负,所以总分接近 −1 表示「高值旁边总是低值」。接近 0 才是随机,接近 +1 才是同号扎堆。

</details>

**2. 莫兰指数公式里分母 Σ(xi−x̄)² 的作用是什么?**

- A. 判断邻居的个数
- B. 计算总共有多少个点
- C. 把结果限制在 0 到 1 之间
- D. 衡量数据本身的分散程度,作为归一化的尺子

<details><summary>答案与解析</summary>

**答案:D**。分母是数据的总方差量级,把分子(邻居同号的强度)除一下,得到无量纲的比值,这样不同量纲、不同大小的数据才能相互比较。

</details>

**3. 如果空间权重做了行标准化(每行和为 1),公式里的 n/W 会变成什么?**

- A. 等于 n
- B. 等于 0
- C. 等于权重矩阵的行数
- D. 等于 1,可以直接省掉

<details><summary>答案与解析</summary>

**答案:D**。行标准化后每一行加起来是 1,总权重和 W = n,所以 n/W = 1。这也是为什么很多教材直接写没有这一项的公式 —— 它们默认用了行标准化。

</details>

**4. LISA 分类里的「高-低(HL)」表示什么?**

- A. 处于两个高值区之间
- B. 数据错误
- C. 自身是高值,但周围邻居偏低,属于空间异常点
- D. 整体都是高值区

<details><summary>答案与解析</summary>

**答案:C**。HL 的局部莫兰值为负(因为 (xi−x̄) 为正而邻居偏差之和为负)。它说明这个位置和周围环境不一致,可能是真实的特殊污染源,也可能是数据录入错误,所以值得单独排查。

</details>

**5. Getis-Ord Gi\* 的 z 值越大说明什么?**

- A. 这个位置的数值一定最大
- B. 这个位置加上邻居的值明显高于随机情况下的期望,是热点
- C. 数据方差越大
- D. 这个位置的邻居最多

<details><summary>答案与解析</summary>

**答案:B**。Gi\* 比较的是「局部和」与「期望和」的差距,再除以标准差,所以它是相对于整体均值和波动来判定的。一个格子自身数值高但周围都很低,Gi\* 不一定显著 —— 这正是它和单纯排名的区别。

</details>


---

# 第二层 · 时空分析

## L32 · 轨迹数据:两点之间怎么算「走得快不快」

> 关键词:haversine · 大圆距离 · 速度 · 异常点 | 建议用时 12 分钟

出租车、外卖骑手、快递车每天都在产生一种特别的数据:**带时间戳的一串经纬度点**,这叫**轨迹**。

轨迹分析要回答的第一个问题很朴素:这个点跑得多快?但要算出速度,先得算出**两个经纬度点之间有多远**。而「经纬度之间的距离」恰恰是一个很容易算错的地方。

先看数据。轨迹就是一串 `[时刻, 经度, 纬度]`,按时间排好:

```python
track = [
    ["08:00", 116.40, 39.90],
    ["09:00", 116.35, 39.60],
    ["10:00", 116.30, 39.30],
    ["11:00", 116.25, 39.00],
    ["12:00", 116.25, 39.00],
    ["13:00", 121.47, 31.23],
    ["14:00", 121.42, 31.00],
    ["15:00", 121.37, 30.70]
]
print("轨迹点个数:", len(track))
print("最后一段:", track[6], "→", track[7])
```

运行结果:

```text
轨迹点个数: 8
最后一段: ['14:00', 121.42, 31.0] → ['15:00', 121.37, 30.7]
```

> **【注意】最常见的错误:把经纬度当平面直角坐标**
>
> 很多人直接写 `sqrt((lon2-lon1)**2 + (lat2-lat1)**2) * 111`。这在**南北方向**上勉强能用,但在**东西方向**上错得很厉害 —— 北京那个纬度上 1 度经度只有 **85** 公里,不是 111 公里(要乘 cos(纬度))。所以纯东西向走 50 公里会高估 <b>30%</b>。

正确的做法是算<b>大圆距离(great-circle distance)</b>:把地球当成一个球,两点之间沿着球面走最短的那条弧。公式叫 **haversine**:

> **【要点】haversine 每一部分在算什么**
>
> - **math.radians**:三角函数吃的是弧度,而经纬度是角度,必须先换算。
> - **dlat / dlon**:两点在纬度、经度上的差(转成弧度后)。
> - **a**:把「南北方向的差」和「东西方向的差」合成一个 0~1 之间的量。东西向那一项乘了 `cos(纬度)` —— 这就是「越靠近两极,同样的经度差对应的实际距离越短」。
> - <b>2·asin(√a)</b>:由 a 反推出球心张角(弧度),再乘地球半径得到弧长。
> - **if a > 1: a = 1**:浮点误差可能让 a 稍微超过 1,那样 asin 会报错,所以先夹住。

```python
import math

def haversine(lon1, lat1, lon2, lat2):
    r = 6371.0088
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    if a > 1:
        a = 1
    return r * 2 * math.asin(math.sqrt(a))

print("北京 → 上海:", round(haversine(116.407, 39.904, 121.473, 31.230), 2), "公里")
```

运行结果:

```text
北京 → 上海: 1067.32 公里
```

有了距离,速度就是距离除以时间差。下面这段是整幕的核心,注意时间差是**从时间戳里逐段算出来的**,不是硬编码的:

```python
import math

p0 = ["12:00", 116.25, 39.00]
p1 = ["13:00", 121.47, 31.23]
r = 6371.0088
dlat = math.radians(p1[2] - p0[2])
dlon = math.radians(p1[1] - p0[1])
a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(p0[2])) * math.cos(math.radians(p1[2])) * math.sin(dlon / 2) ** 2
d = r * 2 * math.asin(math.sqrt(a))
def to_hours(hhmm):
    # "13:30" → 13.5 小时
    parts = hhmm.split(":")
    return int(parts[0]) + int(parts[1]) / 60

dt = to_hours(p1[0]) - to_hours(p0[0])
print("距离", round(d, 2), "km  耗时", dt, "小时  速度", round(d / dt, 2), "km/h")
```

运行结果:

```text
距离 985.39 km  耗时 1.0 小时  速度 985.39 km/h
```

> **【要点】速度异常点:两种都要抓**
>
> - <b>速度接近 0(停留)</b>:几小时的定位点几乎不动。这不是错误,而是「车停着」,但它会让「平均速度」被严重拉低。
> - <b>速度大得不可能(瞬移)</b>:比如 1 小时走 985 公里 —— 民航巡航也就 900 km/h。真实原因通常是定位漂移、设备跨城市重连、或者时间戳错乱。
> - 识别方法就是设阈值:**大于某个上限判为瞬移,小于某个下限判为停留**。阈值要按业务定(骑手 vs 高铁完全不是一个量级)。
> - 识别出来之后不能直接删掉就完事 —— 至少要记录「剔除了几段」,否则读者不知道你的平均速度是怎么来的。

把两类异常都标出来后重新算平均速度:剔除瞬移段之后,全程平均速度从 163.71 km/h 降到 **26.77** km/h。这就是「不清洗直接用」和「清洗后」的差距。

> **【对照】这段手写代码 ↔ 真实项目里的写法**
>
> - 手写 `haversine(...)` ↔ `geopy.distance.great_circle((lat1, lon1), (lat2, lon2)).km`
> - 更精确的椭球距离 ↔ `geopy.distance.geodesic(...)`(WGS84 椭球,长距离下和球面模型差几公里)
> - 逐段距离 + 速度 ↔ `movingpandas.Trajectory(gdf, traj_id=1, t="time")`,再 `traj.add_speed(units=("km", "h"))`(默认单位是 m/s)
> - 轨迹总长度 ↔ `traj.get_length()`
> - 停留点识别 ↔ `movingpandas.TrajectoryStopDetector(traj).get_stop_points(min_duration=..., max_diameter=...)`
> - 异常速度点过滤 ↔ `traj.df[traj.df["speed"] < 200]`(单位要与 add\_speed 设定的一致)

### 本关完整示例

```python
import math

# ===== L32:轨迹、两点距离与速度 =====

# 1) 大圆距离:把地球当半径 6371.0088 公里的球
def haversine(lon1, lat1, lon2, lat2):
    r = 6371.0088
    rlon1 = math.radians(lon1)
    rlat1 = math.radians(lat1)
    rlon2 = math.radians(lon2)
    rlat2 = math.radians(lat2)
    dlon = rlon2 - rlon1
    dlat = rlat2 - rlat1
    a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(rlat1) * math.cos(rlat2) * math.sin(dlon / 2) * math.sin(dlon / 2)
    if a > 1:
        a = 1
    return r * 2 * math.asin(math.sqrt(a))

# 2) 平面近似:把经纬度当平面坐标,再用「1 度约 111 公里」换算
def planar(lon1, lat1, lon2, lat2):
    dx = lon2 - lon1
    dy = lat2 - lat1
    return math.sqrt(dx * dx + dy * dy) * 111.0

# 3) 一条 8 个定位点的轨迹(手工构造的示例轨迹,不是真实采集数据)
#    每个点是 [时刻, 经度, 纬度]
track = [
    ["08:00", 116.40, 39.90],
    ["09:00", 116.35, 39.60],
    ["10:00", 116.30, 39.30],
    ["11:00", 116.25, 39.00],
    ["12:00", 116.25, 39.00],
    ["13:00", 121.47, 31.23],
    ["14:00", 121.42, 31.00],
    ["15:00", 121.37, 30.70]
]

def to_hours(hhmm):
    # "13:30" → 13.5 小时(分钟也要算进去)
    parts = hhmm.split(":")
    return int(parts[0]) + int(parts[1]) / 60

# 4) 逐段算距离与速度
print("=== 逐段:距离 与 速度 ===")
print("时段           大圆km    平面km   耗时h   速度km/h")
total = 0.0
hours = 0.0
for i in range(1, len(track)):
    p0 = track[i - 1]
    p1 = track[i]
    d = haversine(p0[1], p0[2], p1[1], p1[2])
    d2 = planar(p0[1], p0[2], p1[1], p1[2])
    dt = to_hours(p1[0]) - to_hours(p0[0])
    if dt <= 0:
        continue
    total = total + d
    hours = hours + dt
    print(p0[0], "-", p1[0], "   ", round(d, 2), "   ", round(d2, 2), "   ", dt, "     ", round(d / dt, 2))
print()

# 5) 轨迹总长度与整体平均速度
print("轨迹点个数:", len(track), " 总长度:", round(total, 2), "公里")
print("总耗时:", hours, "小时  全程平均速度:", round(total / hours, 2), "km/h")
print()

# 6) 大圆距离 vs 平面近似:错在哪里
print("=== 同样 1 度经度差,在不同纬度上的真实距离 ===")
for lat in [20.0, 30.0, 40.0, 50.0]:
    d = haversine(116.0, lat, 117.0, lat)
    print("  北纬", lat, "度 →", round(d, 2), "公里")
print("原因: 经线之间的距离随纬度升高而变短,要乘以 cos(纬度)")
print()
print("=== 平面近似在东西方向上的高估 ===")
for lon2 in [117.0, 119.0, 121.5]:
    a1 = haversine(116.4, 39.9, lon2, 39.9)
    a2 = planar(116.4, 39.9, lon2, 39.9)
    err = (a2 - a1) / a1 * 100
    print("  东经 116.4 →", lon2, " 大圆", round(a1, 2), " 平面", round(a2, 2), " 高估", round(err, 2), "%")
print()

# 7) 异常识别:速度过大是瞬移,速度接近 0 是停留
print("=== 速度异常识别(大于 200 视为瞬移, 小于 1 视为停留)===")
for i in range(1, len(track)):
    p0 = track[i - 1]
    p1 = track[i]
    d = haversine(p0[1], p0[2], p1[1], p1[2])
    dt = to_hours(p1[0]) - to_hours(p0[0])
    if dt <= 0:
        continue
    speed = d / dt
    if speed > 200:
        print(p0[0], "→", p1[0], " 距离", round(d, 2), "km  速度", round(speed, 2), "km/h  ← 瞬移")
    elif speed < 1:
        print(p0[0], "→", p1[0], " 距离", round(d, 3), "km  速度", round(speed, 3), "km/h  ← 停留")
print()

# 8) 去掉瞬移那一段,平均速度才可信
clean = 0.0
clean_h = 0.0
cnt = 0
for i in range(1, len(track)):
    d = haversine(track[i - 1][1], track[i - 1][2], track[i][1], track[i][2])
    dt = to_hours(track[i][0]) - to_hours(track[i - 1][0])
    if dt <= 0 or d / dt > 200:
        continue
    clean = clean + d
    clean_h = clean_h + dt
    cnt = cnt + 1
print("剔除瞬移段后: 有效段数", cnt, " 总长度", round(clean, 2), "km  平均速度", round(clean / clean_h, 2), "km/h")
```

运行结果:

```text
=== 逐段:距离 与 速度 ===
时段           大圆km    平面km   耗时h   速度km/h
08:00 - 09:00     33.63     33.76     1.0       33.63
09:00 - 10:00     33.63     33.76     1.0       33.63
10:00 - 11:00     33.64     33.76     1.0       33.64
11:00 - 12:00     0.0     0.0     1.0       0.0
12:00 - 13:00     985.39     1039.03     1.0       985.39
13:00 - 14:00     26.01     26.13     1.0       26.01
14:00 - 15:00     33.7     33.76     1.0       33.7

轨迹点个数: 8  总长度: 1146.0 公里
总耗时: 7.0 小时  全程平均速度: 163.71 km/h

=== 同样 1 度经度差,在不同纬度上的真实距离 ===
  北纬 20.0 度 → 104.49 公里
  北纬 30.0 度 → 96.3 公里
  北纬 40.0 度 → 85.18 公里
  北纬 50.0 度 → 71.47 公里
原因: 经线之间的距离随纬度升高而变短,要乘以 cos(纬度)

=== 平面近似在东西方向上的高估 ===
  东经 116.4 → 117.0  大圆 51.18  平面 66.6  高估 30.12 %
  东经 116.4 → 119.0  大圆 221.79  平面 288.6  高估 30.13 %
  东经 116.4 → 121.5  大圆 435.0  平面 566.1  高估 30.14 %

=== 速度异常识别(大于 200 视为瞬移, 小于 1 视为停留)===
11:00 → 12:00  距离 0.0 km  速度 0.0 km/h  ← 停留
12:00 → 13:00  距离 985.39 km  速度 985.39 km/h  ← 瞬移

剔除瞬移段后: 有效段数 6  总长度 160.61 km  平均速度 26.77 km/h
```

### 动手练习

1. 把 13:00 那个点改回正常值(比如 116.20, 38.70),重新运行,看总长度和平均速度怎么变。
2. 把「停留」那一段(11:00 → 12:00)的时间戳改成 11:30,看停留的判定会不会变化。
3. 自己写一个 planar2,把 111 换成 111 \* cos(纬度),再和 haversine 比,看误差降到多少。
4. 把速度阈值从 200 改成 100,看会多剔除哪几段 —— 想想阈值定得太低会有什么后果。

### 随堂检测

**1. 为什么不能直接把经纬度当平面坐标算距离?**

- A. 因为经纬度是整数
- B. 因为平面公式算不出正数
- C. 因为经度 1 度对应的实际距离随纬度升高而变短,要乘 cos(纬度)
- D. 因为地球是完美的球

<details><summary>答案与解析</summary>

**答案:C**。经线在两极汇聚,所以同样 1 度经度差在北纬 20 度约 104 公里,在北纬 50 度只剩 71 公里。忽略这一点会系统性高估东西方向的距离(北京纬度上高估约 30%)。

</details>

**2. haversine 算出来的距离是?**

- A. 沿着道路的实际行驶距离
- B. 两点之间的直线(穿地而过)长度
- C. 球面上两点之间的最短弧长(大圆距离)
- D. 曼哈顿距离

<details><summary>答案与解析</summary>

**答案:C**。haversine 给出的是球面最短路径。穿地而过的弦长在短距离下和它几乎一样,但那不是它的定义;而道路距离一定大于等于它(所以「直线距离」常被当作行驶距离的下界)。

</details>

**3. 一个定位点 1 小时内移动了 985 公里,最合理的解释是?**

- A. 车开得很快
- B. 轨迹点顺序错了
- C. 距离算错了公式
- D. 定位漂移或时间戳错乱,属于需要剔除的异常

<details><summary>答案与解析</summary>

**答案:D**。985 km/h 超过民航巡航速度,地面交通不可能达到。真实数据里常见原因是设备跨城市重启、坐标系写错、或时间戳单位搞错(毫秒当秒)。这类点要靠速度阈值自动抓出来。

</details>

**4. 算速度时如果直接除以「常数 1」而不去算时间差,会发生什么?**

- A. 结果完全正确
- B. 只会影响第一段
- C. 只要采样间隔不全是 1 小时,速度就全错
- D. 会报错

<details><summary>答案与解析</summary>

**答案:C**。速度 = 距离 / 时间差。真实轨迹的采样间隔常常不均匀(有的 30 秒一条,有的断了几小时),必须用每个点自己的时间戳算差,不能假设间隔固定。

</details>

**5. 轨迹里的「停留点」为什么不能当异常值直接删掉?**

- A. 停留点没有经度
- B. 删掉会让程序报错
- C. 停留点和瞬移是一回事
- D. 停留是真实行为,删掉会丢掉「在这里停了多久」这类关键信息

<details><summary>答案与解析</summary>

**答案:D**。停留有业务含义(等红灯、装卸货、堵车),而瞬移是数据错误。两者都要「识别」,但处理方式不同:停留要保留并单独统计时长,瞬移要剔除或修正。

</details>

## L37 · 时空立方体:把「哪里」和「何时」拼在一起

> 关键词:空间分箱 · 时间窗 · 均值方差 · 热点 | 建议用时 13 分钟

前面几幕是分开的:L31、L33 只看「在哪里」,L22、L24 只看「什么时候」。但真实问题几乎都是两件事一起问的 —— <b>哪个地方、在什么时段污染最重?</b>

把「哪里」和「何时」拼起来,就得到一个 **格子 × 时刻** 的二维表,专业名词叫<b>时空立方体(spatio-temporal cube)</b>。这一幕就用它来区分两种完全不同的「重」:**一直很重**和**忽高忽低**。

先看这把「尺子」。`dataset.pm_grid` 是一张 12×12 的 PM2.5 网格 —— 相当于把一片区域切成 144 个小方块,每块一个平均值:

```python
from dataset import dataset

g = dataset.pm_grid
print("行数:", g["rows"], " 列数:", g["cols"])
print("左下角经纬度:", g["lonMin"], g["latMin"], " 每格边长:", g["cellSize"], "度")
print("经度范围:", g["lonMin"], "~", round(g["lonMin"] + g["cellSize"] * g["cols"], 2))
print("纬度范围:", g["latMin"], "~", round(g["latMin"] + g["cellSize"] * g["rows"], 2))
print("第一行前 4 格:", g["values"][0][0:4])
```

运行结果:

```text
行数: 12  列数: 12
左下角经纬度: 115 39  每格边长: 0.05 度
经度范围: 115 ~ 115.6
纬度范围: 39 ~ 39.6
第一行前 4 格: [31, 54.2, 69.3, 79.6]
```

> **【约定】网格的方向约定(L35、L37、L38 通用)**
>
> `values[0]` 是**最南边**的一行(从纬度 latMin 开始),行号越大越往北;列号越大越往东。所以第 r 行、第 c 列格子的中心坐标是 `(lonMin + (c + 0.5)·cellSize, latMin + (r + 0.5)·cellSize)`。数据集只给了左下角 (lonMin, latMin),这条约定必须写清楚,否则「南北」会整个颠倒。

> **【要点】什么叫「空间分箱」**
>
> - 原始数据是**一个个点**(监测站在某经纬度测到一个值)。点太散,不好比较,也不方便和别的地图叠。
> - <b>分箱(binning)</b>就是在地图上铺一层规则的方格,把落在同一格里的点归到一起,用它们的平均(或总和)代表这一格。
> - 好处:规则格子可以逐格比较、可以求和求平均、可以直接画成热力图。
> - 代价:**格子的边长决定了你能看到多细的结构**。格子太大,热点被抹平;格子太小,每格又没几个点,噪声大。

但一个时刻的网格只是一张**平面**照片。要做时空分析,需要多个时刻的网格叠成**立方体**。下面这段是这幕的重点 —— 因为数据集里只有一张网格,我们**用确定性规则派生出 3 个时刻**。

```python
import math

def factor(r, c, t):
    # 西南片区(行 0~5、列 0~5):稳步略升(代表这一带一直偏重)
    if r < 6 and c < 6:
        return 1.0 + 0.02 * t
    # 西北片区(行 6~11、列 0~5):大幅起伏(代表这一带忽高忽低)
    if r >= 6 and c < 6:
        return 1.0 + 0.4 * math.sin(2.0 * (t + r + c))
    # 东半部(列 6~11):随时间缓慢下降
    return 1.0 - 0.15 * t

print("(0,0) 三时刻倍率:", round(factor(0, 0, 0), 2), round(factor(0, 0, 1), 2), round(factor(0, 0, 2), 2))
print("(8,2) 三时刻倍率:", round(factor(8, 2, 0), 2), round(factor(8, 2, 1), 2), round(factor(8, 2, 2), 2))
```

运行结果:

```text
(0,0) 三时刻倍率: 1.0 1.02 1.04
(8,2) 三时刻倍率: 1.37 1.0 0.64
```

> **【注意】这 3 个时刻是派生的演示数据,不是真实观测**
>
> 真实的时空立方体里,每个时刻来自**那个时刻真正观测到的一张网格**(卫星反演、站点插值、模式模拟)。这里只有一张网格,所以用固定公式 `base × factor` 叠出三个时刻,目的是把「格子 × 时刻」这个结构演示清楚。**它的绝对数值没有物理意义**,能说明的只有结构本身。真实项目里绝不能用这种构造出来的数据下结论。

立方体建好以后,对**每个格子**沿时间轴做两件统计:求**时间均值**和**时间方差**。这两个数字合起来,就把格子分成了四类:

> **【要点】均值高 + 方差低 与 均值高 + 方差高 是两回事**
>
> - **均值高、方差低** = 一直重。这种格子是**稳定的治理靶子**:不管哪天去查,它都在那儿。
> - **均值高、方差高** = 有时爆表有时还好。这种格子要找的是**触发条件**(什么时段、什么风向才起来)。
> - **均值低、方差低** = 干净且稳定,通常不需要管。
> - **均值低、方差高** = 偶尔来一次。这类最容易被平均值掩盖掉,需要看最大值而不是均值。
> - 方差写成 `Σ(v − mean)² / n`:先算每个时刻偏离均值多少,平方(让正负不抵消、并放大偏离),再平均。

```python
import math
from dataset import dataset

grid = dataset.pm_grid
rowsN = grid["rows"]
colsN = grid["cols"]
base = grid["values"]

def factor(r, c, t):
    if r < 6 and c < 6:
        return 1.0 + 0.02 * t
    if r >= 6 and c < 6:
        return 1.0 + 0.4 * math.sin(2.0 * (t + r + c))
    return 1.0 - 0.15 * t

stats = []
for r in range(rowsN):
    for c in range(colsN):
        vals = []
        for t in range(3):
            vals.append(round(base[r][c] * factor(r, c, t), 2))
        mean = sum(vals) / len(vals)
        var = 0
        for v in vals:
            var = var + (v - mean) * (v - mean)
        stats.append([r, c, round(mean, 2), round(var / len(vals), 2), vals])
print("统计了几格:", len(stats))
print("左上角(0,0):", stats[0])
print("左下角(8,2):", stats[8 * colsN + 2])
```

运行结果:

```text
统计了几格: 144
左上角(0,0): [0, 0, 31.62, 0.26, [31.0, 31.62, 32.24]]
左下角(8,2): [8, 2, 107.08, 1011.47, [146.21, 106.72, 68.31]]
```

跑完的结果很干脆:**时间均值最高的 5 格全部落在西南片区**(它们的时间方差都在 5.5 以下 —— 三个时刻几乎没动过);**时间方差最大的 5 格全部落在西北片区**(方差 632 到 1023)。按四个片区汇总更明显:西南片区平均方差只有 **1.75**,西北片区是 **320.96**,相差近 200 倍。这说明**均值 + 方差这个组合确实能把「一直高」和「忽高忽低」分开**。

> **【提示】为什么方差要用「每个格子自己的均值」**
>
> 方差衡量的是「这个格子自己随时间波动多大」。如果拿**全域均值**去算,那么一个常年 120 的格子和一个常年 20 的格子都会得到巨大的方差 —— 算出来的成了「它跟别人的差距」,不是「它自己的波动」。所以务必先按格子求均值,再算该格子的方差。

> **【对照】这段手写代码 ↔ 真实项目里的写法**
>
> - 带坐标的网格数据 ↔ `xarray.DataArray(data, dims=("time","lat","lon"), coords={...})`
> - 手写 `cube[t][r][c]` ↔ `cube.sel(time=t, lat=lat, lon=lon)` 或 `cube.isel(time=t, lat=r, lon=c)`
> - 沿时间轴求均值 ↔ `cube.mean(dim="time")`
> - 沿时间轴求方差 ↔ `cube.var(dim="time")`
> - 按空间分区聚合 ↔ `cube.groupby("region").mean()` / `df.groupby(["row","col"])["pm25"].mean()`
> - 原始数据是一堆带时间的点(不是网格)时 ↔ 用 `geopandas` 做 `sjoin` 落到格子里,或 `pandas.cut` 分箱

### 本关完整示例

```python
import math
from dataset import dataset

# ===== L25:时空立方体(格子 × 时刻)=====

# 1) 拿到空间网格
grid = dataset.pm_grid
rowsN = grid["rows"]
colsN = grid["cols"]
base = grid["values"]
lon0 = grid["lonMin"]
lat0 = grid["latMin"]
size = grid["cellSize"]
times = ["T1", "T2", "T3"]

print("=== 空间分箱 ===")
print("网格:", rowsN, "行 x", colsN, "列 =", rowsN * colsN, "个格子")
print("经度范围:", lon0, "~", round(lon0 + size * colsN, 2), " 纬度范围:", lat0, "~", round(lat0 + size * rowsN, 2))
print("第一行前 4 格:", base[0][0:4])
print()

# 2) 派生 3 个时刻(演示用,不是真实观测)
#    规则写死、不用随机数,保证每次运行结果完全一样
def factor(r, c, t):
    if r < 6 and c < 6:
        return 1.0 + 0.02 * t
    if r >= 6 and c < 6:
        return 1.0 + 0.4 * math.sin(2.0 * (t + r + c))
    return 1.0 - 0.15 * t

cube = []
for t in range(3):
    frame = []
    for r in range(rowsN):
        line = []
        for c in range(colsN):
            line.append(round(base[r][c] * factor(r, c, t), 2))
        frame.append(line)
    cube.append(frame)

print("=== 三个时刻的全域均值 ===")
for t in range(3):
    total = 0
    n = 0
    for r in range(rowsN):
        for c in range(colsN):
            total = total + cube[t][r][c]
            n = n + 1
    print("时刻", times[t], ":", round(total / n, 2))
print()

# 3) 每个格子沿时间轴求均值与方差
stats = []
for r in range(rowsN):
    for c in range(colsN):
        vals = [cube[0][r][c], cube[1][r][c], cube[2][r][c]]
        mean = sum(vals) / len(vals)
        var = 0
        for v in vals:
            var = var + (v - mean) * (v - mean)
        stats.append([r, c, round(mean, 2), round(var / len(vals), 2), vals])
print("参与统计的格子数:", len(stats), " 左上角格子三时刻:", stats[0][4])
print()

# 4) 排序:按时间均值(一直高)与按时间方差(忽高忽低)
def rank_by(index):
    arr = []
    for s in stats:
        arr.append(s)
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j][index] < arr[j + 1][index]:
                tmp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = tmp
    return arr

byMean = rank_by(2)
print("=== 时间均值最高的 5 格:一直高 ===")
for i in range(5):
    s = byMean[i]
    print("  行", s[0], "列", s[1], " 均值", s[2], " 方差", s[3], " 三时刻", s[4])
print()

byVar = rank_by(3)
print("=== 时间方差最大的 5 格:忽高忽低 ===")
for i in range(5):
    s = byVar[i]
    print("  行", s[0], "列", s[1], " 均值", s[2], " 方差", s[3], " 三时刻", s[4])
print()

# 5) 按四个片区聚合,验证两种形态各自扎堆在哪
zones = ["西南", "西北", "东南", "东北"]
zoneStats = {}
for z in zones:
    zoneStats[z] = [0, 0.0, 0.0]
for s in stats:
    r = s[0]
    c = s[1]
    if r < 6 and c < 6:
        z = "西南"
    elif r >= 6 and c < 6:
        z = "西北"
    elif r < 6 and c >= 6:
        z = "东南"
    else:
        z = "东北"
    zoneStats[z][0] = zoneStats[z][0] + 1
    zoneStats[z][1] = zoneStats[z][1] + s[2]
    zoneStats[z][2] = zoneStats[z][2] + s[3]

print("=== 四个片区的均值与方差 ===")
print("片区   格子数  平均时间均值  平均时间方差")
for z in zones:
    info = zoneStats[z]
    print(z, "   ", info[0], "    ", round(info[1] / info[0], 2), "        ", round(info[2] / info[0], 2))
print()

# 6) 把网格坐标还原成经纬度,才能贴到地图上
print("=== 热点格子的真实位置 ===")
for i in range(3):
    s = byMean[i]
    lon = round(lon0 + size * (s[1] + 0.5), 3)
    lat = round(lat0 + size * (s[0] + 0.5), 3)
    print("  行", s[0], "列", s[1], " 中心经纬度 (", lon, ",", lat, ") 时间均值", s[2])
```

运行结果:

```text
=== 空间分箱 ===
网格: 12 行 x 12 列 = 144 个格子
经度范围: 115 ~ 115.6  纬度范围: 39 ~ 39.6
第一行前 4 格: [31, 54.2, 69.3, 79.6]

=== 三个时刻的全域均值 ===
时刻 T1 : 62.2
时刻 T2 : 58.16
时刻 T3 : 54.27

参与统计的格子数: 144  左上角格子三时刻: [31.0, 31.62, 32.24]

=== 时间均值最高的 5 格:一直高 ===
  行 2 列 3  均值 146.47  方差 5.49  三时刻 [143.6, 146.47, 149.34]
  行 3 列 3  均值 132.29  方差 4.49  三时刻 [129.7, 132.29, 134.89]
  行 1 列 3  均值 130.66  方差 4.37  三时刻 [128.1, 130.66, 133.22]
  行 2 列 2  均值 125.87  方差 4.07  三时刻 [123.4, 125.87, 128.34]
  行 2 列 4  均值 124.44  方差 3.97  三时刻 [122.0, 124.44, 126.88]

=== 时间方差最大的 5 格:忽高忽低 ===
  行 9 列 2  均值 114.92  方差 1022.95  三时刻 [116.88, 74.81, 153.08]
  行 8 列 2  均值 107.08  方差 1011.47  三时刻 [146.21, 106.72, 68.31]
  行 9 列 1  均值 94.98  方差 795.85  三时刻 [129.69, 94.66, 60.59]
  行 10 列 2  均值 101.2  方差 775.86  三时刻 [63.46, 129.85, 110.28]
  行 9 列 3  均值 91.33  方差 632.02  三时刻 [57.27, 117.19, 99.53]

=== 四个片区的均值与方差 ===
片区   格子数  平均时间均值  平均时间方差
西南     36      76.35          1.75
西北     36      59.2          320.96
东南     36      35.15          30.52
东北     36      62.16          92.98

=== 热点格子的真实位置 ===
  行 2 列 3  中心经纬度 ( 115.175 , 39.125 ) 时间均值 146.47
  行 3 列 3  中心经纬度 ( 115.175 , 39.175 ) 时间均值 132.29
  行 1 列 3  中心经纬度 ( 115.175 , 39.075 ) 时间均值 130.66
```

### 动手练习

1. 把 factor 里「左下半区」的 0.4 改成 0.1,重新运行,看方差最大的 5 格是否还落在左下区。
2. 给立方体加第 4 个时刻(t = 3),想想 T4 的 factor 应该怎么定才符合原规则。
3. 把「时间方差」改成「时间最大最小值之差」(极差),看排出来的前 5 格是否和方差一致,并解释为什么可能不同。
4. 把网格的 cellSize 想象得更大(比如 0.1),格子数会怎么变?这对「热点还能不能看出来」有什么影响?

### 随堂检测

**1. 时空立方体里的两个维度分别是?**

- A. 经度和纬度
- B. 空间格子和时间时刻
- C. 均值和方差
- D. 城市和人口

<details><summary>答案与解析</summary>

**答案:B**。立方体的两个轴是「哪里」和「何时」:空间上分成一个个格子,时间上分成一个个时刻,每个交叉点是一个数值。经度/纬度只是空间维内部的坐标,不是立方体的两个维度。

</details>

**2. 幕里那 3 个时刻的网格数据是怎么来的?**

- A. 随机数生成的
- B. 用固定公式在单张网格上派生出来的演示数据
- C. 50 个监测站的实测值
- D. 卫星真实观测

<details><summary>答案与解析</summary>

**答案:B**。数据集里的 pm\_grid 只有一张网格。为了演示「格子 × 时刻」的结构,代码用 base × factor 的确定性公式叠出三个时刻。它结构上像真实立方体,但绝对数值没有物理意义 —— 真实项目必须用每个时刻真正观测到的数据;随机数生成的写法也会让结果每次都不一样。

</details>

**3. 一个格子的时间均值很高、时间方差很低,说明?**

- A. 这个格子数据错了
- B. 这个格子的空间位置错了
- C. 这个格子长期稳定地偏高,是稳定的治理靶子
- D. 这个格子偶尔爆表

<details><summary>答案与解析</summary>

**答案:C**。均值高说明整体水平高,方差低说明它不怎么变。两个条件合起来就是「一直高」。反过来「偶尔爆表」是均值可能不高但方差大,需要用最大值而不是均值去发现。

</details>

**4. 计算某个格子的时间方差时,应当用哪个均值?**

- A. 这一行的均值
- B. 这个格子自己在各时刻的均值
- C. 全域所有格子的均值
- D. 0

<details><summary>答案与解析</summary>

**答案:B**。方差衡量的是「它自己随时间波动多少」。用全域均值会把「它天生就比别处高」当成波动,算出来的是空间差异而不是时间波动,结论会完全跑偏。

</details>

**5. 把网格的格子边长设得太大,主要风险是?**

- A. 程序会变慢
- B. 热点被平均掉,看不到局部细节
- C. 经纬度会算错
- D. 方差会变成负数

<details><summary>答案与解析</summary>

**答案:B**。格子越大,里面混进的不同性质的区域越多,高低值一平均就都变成中间值,局部热点消失(这是可变面积单元问题 MAUP 的一种表现)。格子太小则每格样本太少、噪声大。分箱尺度本身就是一个需要交代的分析选择。

</details>


---

# 第二层 · 综合项目

## L38 · 综合项目:一份小型时空分析报告

> 关键词:数据清洗 · 缺失值 · 异常值 · 聚合 · 结论 | 建议用时 15 分钟

前面每一幕都在练一个动作。这一幕把它们串成一条完整的流水线 —— 这也是真实项目里 80% 时间花在的地方:**读数据 → 清洗 → 空间聚合 → 时间聚合 → 热点识别 → 写结论**。

素材是一段真实的 CSV 文本(16 行,5 个城市),里面**故意留着 2 处缺失值和 1 处明显异常值**。我们不动手改数据,而是让代码自己把它们抓出来。

原始数据长这样(`dataset.csvSample` 是一段字符串,不是文件):

```python
from dataset import dataset

text = dataset.csvSample
lines = text.split("\n")
print("总行数:", len(lines), " (1 行表头 +", len(lines) - 1, "行数据)")
print("表头:", lines[0])
for i in range(1, 5):
    print(lines[i])
```

运行结果:

```text
总行数: 17  (1 行表头 + 16 行数据)
表头: date,city,temp,pm25,rain
2023-01-05,北京,-2.4,86,0
2023-01-06,北京,-3.8,102,0
2023-01-07,北京,-1.1,,0
2023-01-08,北京,0.6,74,0
```

> **【要点】清洗的三步,一步都不能省**
>
> - **识别空值**:CSV 里的缺失不是 None,而是「两个逗号挨在一起」,split 之后得到一个**空字符串**(长度为 0)。先 strip 再判断长度。
> - **类型转换要包 try/except**:`float("")` 和 `float("N/A")` 都会抛 `ValueError`。不接住它,整个程序就崩在第一个脏数据上。
> - **异常值要单独判**:空值靠「长度是不是 0」能查出来,但 999 这种值是**合法数字、非法含义**,只能用业务规则或统计规则去抓。
> - 顺序很重要:先剔除无法解析的行,**再算均值和标准差** —— 否则脏数据会污染判断标准本身。

先说一个**反直觉的坑**:很多人第一反应是「用均值 ± 3 倍标准差找异常值」。但如果数据里已经有一个 999,均值和标准差会一起被它抬高。

```python
from dataset import dataset

text = dataset.csvSample
lines = text.split("\n")
vals = []
for i in range(1, len(lines)):
    p = lines[i].split(",")
    if p[2].strip() == "" or p[3].strip() == "" or p[4].strip() == "":
        print("跳过空值:", p[0], p[1])
        continue
    vals.append(float(p[3]))

m = sum(vals) / len(vals)
sd = 0
for v in vals:
    sd = sd + (v - m) * (v - m)
sd = (sd / (len(vals) - 1)) ** 0.5
print("均值", round(m, 2), " 标准差", round(sd, 2), " 3 倍上限", round(m + 3 * sd, 2))
clean = []
for v in vals:
    if v <= 500:
        clean.append(v)
m2 = sum(clean) / len(clean)
sd2 = 0
for v in clean:
    sd2 = sd2 + (v - m2) * (v - m2)
sd2 = (sd2 / (len(clean) - 1)) ** 0.5
print("→ 去掉 999 后标准差只有", round(sd2, 2), ";混进 999 后被撑到", round(sd, 2), ",阈值被异常值自己抬高了")
```

运行结果:

```text
跳过空值: 2023-01-07 北京
跳过空值: 2023-02-05 上海
均值 129.71  标准差 250.93  3 倍上限 882.49
→ 去掉 999 后标准差只有 19.87 ;混进 999 后被撑到 250.93 ,阈值被异常值自己抬高了
```

> **【注意】用混着异常值的样本去估计「正常范围」,是自相矛盾的**
>
> 3σ 规则的隐含前提是「均值与标准差来自干净数据」。数据里混进一个 999 之后,标准差从 19.87 涨到 250.93 —— **阈值被异常值自己撑大了**。工程上的做法是先用**领域硬规则**把明显不可能的值拿掉(PM2.5 传感器量程上限一般是 500 或 1000 μg/m³,999 是典型的「错误码/溢出标记」),再在干净数据上算 3σ 做二次筛查。更稳的替代是**中位数 + MAD**:中位数不受极端值影响,阈值也不会被它带跑。

清洗完就进入聚合。空间维度**按城市分组**(等价于 L18 里学过的 groupby),时间维度在这里表现为「每条记录带日期」,可以按月份或时段再聚合一次。

```python
from dataset import dataset

text = dataset.csvSample
lines = text.split("\n")
final = []
for i in range(1, len(lines)):
    p = lines[i].split(",")
    if p[2].strip() == "" or p[3].strip() == "" or p[4].strip() == "":
        continue
    row = [p[0].strip(), p[1].strip(), float(p[2]), float(p[3]), float(p[4])]
    if row[3] <= 500:                      # 物理上限,先把 999 挡掉
        final.append(row)

cityRows = {}
for r in final:
    c = r[1]
    if c in cityRows:
        cityRows[c].append(r)
    else:
        cityRows[c] = [r]

for c in cityRows:
    vals = []
    for r in cityRows[c]:
        vals.append(r[3])
    print(c, " 条数", len(vals), " 平均 pm25 =", round(sum(vals) / len(vals), 2))
```

运行结果:

```text
北京  条数 3  平均 pm25 = 87.33
上海  条数 2  平均 pm25 = 51.5
广州  条数 3  平均 pm25 = 38.0
成都  条数 2  平均 pm25 = 60.5
哈尔滨  条数 3  平均 pm25 = 72.33
```

最后一步是把网格也拉进来做热点识别 —— 这一步把 L37 的时空立方体和本幕的城市聚合接在一起:城市聚合回答「哪个城市重」,网格热点回答「这片区域里哪一块重」。

> **【要点】结论要写成人话,不要只报数字**
>
> - 一条合格的结论要包含四个要素:**数据量、做了什么处理、关键数字、意味着什么**。
> - 「清洗后均值 62.85」不够,要写「原始 16 条里丢弃 2 条缺失记录、剔除 1 条 pm25=999 异常值,清洗后均值 62.85;不清洗会被抬到 129.71」。
> - 被剔除的记录必须**逐条列出来**(日期 + 城市 + 值)。审阅的人要能自己判断你剔得对不对。
> - 最后一定要留一句「本次分析的限制」—— 样本只有 16 条、时间跨度 5 个月、每个城市只有 2–3 条记录,这些都不能支撑强结论。

> **【对照】这段手写代码 ↔ 真实项目里的写法**
>
> - 手写 `text.split("\n")` + split(",") ↔ `pd.read_csv(io.StringIO(text))` 或 `pd.read_csv("data.csv")`
> - 空字符串判断 ↔ `df.replace("", np.nan)`,或读的时候直接 `pd.read_csv(..., na_values=["", "N/A"])`
> - 手写 try/except 转 float ↔ `pd.to_numeric(s, errors="coerce")`(转不了就变 NaN,不抛异常)
> - 剔除缺失行 ↔ `df.dropna(subset=["pm25", "temp"])`
> - 3σ 异常值筛查 ↔ `df[(df["pm25"] - m).abs() <= 3 * s]`,更稳的写法是中位数 + MAD 或 `sklearn.ensemble.IsolationForest`
> - 按城市聚合 ↔ `df.groupby("city")["pm25"].agg(["count", "mean", "min", "max"])`
> - 整条流水线 ↔ `df.pipe(clean).pipe(aggregate).pipe(report)` 或 `sklearn.pipeline.Pipeline`

### 本关完整示例

```python
import math
from dataset import dataset

# ===== L38:清洗 → 聚合 → 热点的完整流水线 =====

# ---------- 第 1 步:读数据 ----------
csvText = dataset.csvSample
lines = csvText.split("\n")
print("表头:", lines[0])
rows = []
for i in range(1, len(lines)):
    parts = lines[i].split(",")
    if len(parts) < 5:
        continue
    rows.append([parts[0].strip(), parts[1].strip(), parts[2].strip(), parts[3].strip(), parts[4].strip()])
print("原始记录:", len(rows), "条")
print()

# ---------- 第 2 步:清洗(缺失值 + 类型转换)----------
missing = 0
usable = []
for r in rows:
    if r[2] == "" or r[3] == "" or r[4] == "":
        missing = missing + 1
        print("丢弃(字段为空):", r[0], r[1])
        continue
    try:
        usable.append([r[0], r[1], float(r[2]), float(r[3]), float(r[4])])
    except ValueError as e:
        missing = missing + 1
        print("丢弃(转不成数字):", r[0], r[1])
print("清洗缺失值后剩余:", len(usable), "条")
print()

def mean_of(vals):
    total = 0
    for v in vals:
        total = total + v
    return total / len(vals)

def std_of(vals):
    m = mean_of(vals)
    total = 0
    for v in vals:
        total = total + (v - m) * (v - m)
    return (total / (len(vals) - 1)) ** 0.5

# ---------- 第 3 步:异常值 ----------
# 3a) 错误示范:直接在含 999 的数据上算 3 倍标准差
pms = []
for r in usable:
    pms.append(r[3])
naiveMean = mean_of(pms)
naiveSd = std_of(pms)
print("=== 直接用 3 倍标准差(错误示范)===")
print("均值", round(naiveMean, 2), " 标准差", round(naiveSd, 2), " 上限", round(naiveMean + 3 * naiveSd, 2))
print()

# 3b) 正确做法:先用物理上限 500 排除明显错误值,统计量才是干净的
cleanPm = []
for r in usable:
    if r[3] <= 500:
        cleanPm.append(r[3])
m = mean_of(cleanPm)
sd = std_of(cleanPm)
upper = m + 3 * sd

final = []
for r in usable:
    if r[3] > 500 or r[3] > upper:
        print("剔除异常值:", r[0], r[1], "pm25 =", r[3])
    else:
        final.append(r)
print("干净数据 pm25 均值", round(m, 2), " 标准差", round(sd, 2), " 3 倍上限", round(upper, 2))
print("→ 对比:干净数据的标准差", round(sd, 2), ",混进 999 后被撑到", round(naiveSd, 2))
print("最终可用记录:", len(final), "条")
print()

print("=== 清洗前后对比 ===")
finalPm = []
for r in final:
    finalPm.append(r[3])
print("清洗前均值:", round(naiveMean, 2), " 清洗后均值:", round(mean_of(finalPm), 2), " 相差:", round(naiveMean - mean_of(finalPm), 2))
print()

# ---------- 第 4 步:空间聚合(按城市)----------
cityOrder = []
cityRows = {}
for r in final:
    c = r[1]
    if c in cityRows:
        cityRows[c].append(r)
    else:
        cityOrder.append(c)
        cityRows[c] = [r]

print("=== 空间聚合:按城市 ===")
print("城市      条数   平均pm25   平均气温")
for i in range(len(cityOrder)):
    c = cityOrder[i]
    vs = []
    ts = []
    for r in cityRows[c]:
        vs.append(r[3])
        ts.append(r[2])
    print(c, "     ", len(vs), "    ", round(mean_of(vs), 2), "    ", round(mean_of(ts), 2))
print()

# ---------- 第 5 步:热点识别 ----------
hotCity = cityOrder[0]
coldCity = cityOrder[0]
hotVal = 0
coldVal = 0
for i in range(len(cityOrder)):
    c = cityOrder[i]
    vs = []
    for r in cityRows[c]:
        vs.append(r[3])
    v = mean_of(vs)
    if i == 0:
        hotVal = v
        coldVal = v
    if v > hotVal:
        hotCity = c
        hotVal = v
    if v < coldVal:
        coldCity = c
        coldVal = v
print("PM2.5 最高:", hotCity, round(hotVal, 2), "   PM2.5 最低:", coldCity, round(coldVal, 2))
print()

# ---------- 第 6 步:把空间网格也做成多时刻再聚合 ----------
# [!] 这一步的 3 个时刻是派生出来的演示数据,不是真实观测
grid = dataset.pm_grid
rowsN = grid["rows"]
colsN = grid["cols"]
base = grid["values"]

def factor(r, c, t):
    if r < 6 and c < 6:
        return 1.0 + 0.02 * t
    if r >= 6 and c < 6:
        return 1.0 + 0.4 * math.sin(2.0 * (t + r + c))
    return 1.0 - 0.15 * t

allCells = []
for r in range(rowsN):
    for c in range(colsN):
        s = 0.0
        for t in range(3):
            s = s + base[r][c] * factor(r, c, t)
        allCells.append([round(s / 3, 2), r, c])
for i in range(len(allCells)):
    for j in range(len(allCells) - 1 - i):
        if allCells[j][0] < allCells[j + 1][0]:
            tmp = allCells[j]
            allCells[j] = allCells[j + 1]
            allCells[j + 1] = tmp

lon0 = grid["lonMin"]
lat0 = grid["latMin"]
size = grid["cellSize"]
print("=== 网格热点(时间均值最高的 3 格)===")
for i in range(3):
    cellInfo = allCells[i]
    lon = round(lon0 + size * (cellInfo[2] + 0.5), 3)
    lat = round(lat0 + size * (cellInfo[1] + 0.5), 3)
    print("  行", cellInfo[1], "列", cellInfo[2], " 中心 (", lon, ",", lat, ") 时间均值", cellInfo[0])
print()

# ---------- 第 7 步:结论 ----------
print("=== 结论 ===")
print("1. 原始", len(rows), "条,丢弃", missing, "条缺失记录,剔除 1 条 pm25=999 异常值,最终", len(final), "条")
print("2. 不清理就统计,pm25 均值会从", round(mean_of(finalPm), 2), "被抬到", round(naiveMean, 2))
print("3. 城市里污染最重的是", hotCity, "(", round(hotVal, 2), "),最轻的是", coldCity, "(", round(coldVal, 2), ")")
print("4. 网格热点集中在西南片区(行 1-3、列 3),和 L37 里「一直高」的结论一致")
print("5. 限制: 样本仅", len(final), "条、跨 5 个月、每城 2-3 条,只能作方法演示,不足以支撑结论")
```

运行结果:

```text
表头: date,city,temp,pm25,rain
原始记录: 16 条

丢弃(字段为空): 2023-01-07 北京
丢弃(字段为空): 2023-02-05 上海
清洗缺失值后剩余: 14 条

=== 直接用 3 倍标准差(错误示范)===
均值 129.71  标准差 250.93  上限 882.49

剔除异常值: 2023-04-03 成都 pm25 = 999.0
干净数据 pm25 均值 62.85  标准差 19.87  3 倍上限 122.47
→ 对比:干净数据的标准差 19.87 ,混进 999 后被撑到 250.93
最终可用记录: 13 条

=== 清洗前后对比 ===
清洗前均值: 129.71  清洗后均值: 62.85  相差: 66.87

=== 空间聚合:按城市 ===
城市      条数   平均pm25   平均气温
北京       3      87.33      -1.87
上海       2      51.5      8.05
广州       3      38.0      23.3
成都       2      60.5      19.0
哈尔滨       3      72.33      15.27

PM2.5 最高: 北京 87.33    PM2.5 最低: 广州 38.0

=== 网格热点(时间均值最高的 3 格)===
  行 2 列 3  中心 ( 115.175 , 39.125 ) 时间均值 146.47
  行 3 列 3  中心 ( 115.175 , 39.175 ) 时间均值 132.29
  行 1 列 3  中心 ( 115.175 , 39.075 ) 时间均值 130.66

=== 结论 ===
1. 原始 16 条,丢弃 2 条缺失记录,剔除 1 条 pm25=999 异常值,最终 13 条
2. 不清理就统计,pm25 均值会从 62.85 被抬到 129.71
3. 城市里污染最重的是 北京 ( 87.33 ),最轻的是 广州 ( 38.0 )
4. 网格热点集中在西南片区(行 1-3、列 3),和 L37 里「一直高」的结论一致
5. 限制: 样本仅 13 条、跨 5 个月、每城 2-3 条,只能作方法演示,不足以支撑结论
```

### 动手练习

1. 把物理上限 500 改成 100,重新运行,看会不会误删正常记录(比如 102)并说明为什么这个阈值定错了。
2. 加一步「时间聚合」:按月份(取日期的前 7 个字符)分组,打印每个月的平均 pm25。
3. 把 999 改成 300,重新运行,观察 3σ 规则还能不能把它抓出来 —— 体会「阈值被污染」的临界点。
4. 给结论加第 6 条:写出你希望补充哪些数据(比如更多城市、更长时段)才能让结论更可靠。

### 随堂检测

**1. CSV 里的缺失值 split 之后是什么?**

- A. 0
- B. 长度为 0 的空字符串
- C. None
- D. NaN

<details><summary>答案与解析</summary>

**答案:B**。CSV 是纯文本,缺失就是两个逗号挨着,split(",") 会给出一个空字符串。它不是 None 也不是 0,所以判断方式是「strip 之后长度是不是 0」。

</details>

**2. float("") 会怎么样?**

- A. 抛 ValueError,要用 try/except 接住
- B. 返回 0
- C. 返回空字符串
- D. 返回 None

<details><summary>答案与解析</summary>

**答案:A**。空字符串不能转成数字,Python 会抛 ValueError。如果不接住,程序会直接崩在第一个脏数据上,后面的数据一条都处理不了。真实项目里更常见的做法是 pandas 的 to\_numeric(errors="coerce") 把它变成 NaN。

</details>

**3. 数据里已经有一个 999 时,直接用「均值 ± 3 倍标准差」找异常值的问题是什么?**

- A. 均值和标准差都被 999 抬高了,阈值失去意义
- B. 标准差会变成负数
- C. 999 一定不会被抓出来
- D. 这个方法只能用于气温

<details><summary>答案与解析</summary>

**答案:A**。999 让标准差从 19.87 涨到 250.93,阈值随之被撑大。这一次它碰巧还是卡住了 999(上限 882),但如果异常值只有 300,它就会被放过去。正确顺序是先按领域规则(量程上限)或中位数 + MAD 剔除明显错误值,再在干净数据上算统计量。

</details>

**4. 为什么清洗前要先把空值行丢掉,而不是留着一起算均值?**

- A. 没有区别
- B. 留着会占内存
- C. 丢掉能提高精度
- D. 空字符串无法参与计算,留着会直接报错或把统计量带偏

<details><summary>答案与解析</summary>

**答案:D**。空值既不能做加法也不能转 float,留着要么报错要么被迫填一个假值。而无论填 0 还是填均值,都会改变最终的均值与标准差,进而影响异常值判定的阈值。

</details>

**5. 一份只有 16 条记录、跨 5 个月、每城 2–3 条的分析报告,结论应该怎么写?**

- A. 把样本复制多份凑大数据量
- B. 直接下结论说北京全年污染最重
- C. 用 999 当作北京的极端污染证据
- D. 只写「方法演示」并明确列出样本量的限制

<details><summary>答案与解析</summary>

**答案:D**。样本量和时间跨度不足以支撑任何城市级结论(北京那 3 条还都在 1 月,冬季本来就偏高)。诚实地写出限制是分析工作的一部分;把异常值当证据、或人为放大样本,都是数据造假。

</details>


---

# 速查卡

### ① 输出与输入

| 写法 | 说明 |
|---|---|
| `print("hi")` | 输出字符串 |
| `print(a, b)` | 输出多个值,默认空格分隔 |
| `print(x, end="")` | 不换行 |
| `print(f"{x:>5}", f"{p:.2f}")` | 对齐 / 保留小数 |
| `input("提示")` | 读入一行,结果**永远是字符串** |

### ② 类型与转换

| 写法 | 说明 |
|---|---|
| `int(x) float(x) str(x) bool(x)` | 类型转换 |
| `type(x)` | 查看类型 |
| `int("18") → 18` | 字符串转整数 |
| `int("3.5") → 报错` | 要先 float("3.5") 再 int() |

### ③ 字符串

| 写法 | 说明 |
|---|---|
| `f"你好{name}"` | f-string 插值(推荐) |
| `s[0]  s[-1]` | 首字符 / 末字符 |
| `s[1:4]` | 切片,含头不含尾 |
| `len(s)` | 长度 |
| `s.upper() lower() strip()` | 大小写 / 去空格 |
| `s.split(",")` | 按分隔符切成列表 |
| `",".join(list)` | 把列表拼成字符串 |
| `s.replace("a","b")` | 替换(返回新字符串) |

### ④ 列表 / 字典

| 写法 | 说明 |
|---|---|
| `nums = [1, 2, 3]` | 列表:有序,按下标取 |
| `nums.append(x)` | 尾部追加 |
| `nums.pop() / remove(x)` | 弹出末尾 / 删除指定值 |
| `nums.sort()` | 原地排序 |
| `sum(nums) max(nums) min(nums)` | 求和 / 最大 / 最小 |
| `d = {"k": 1}` | 字典:键值对 |
| `d["k"] / d.get("k", 默认)` | 取值 / 安全取值 |
| `for k, v in d.items():` | 同时遍历键和值 |
| `x in nums / "k" in d` | 是否存在 |

### ⑤ 流程控制

| 写法 | 说明 |
|---|---|
| `if cond: ...` | 条件(冒号 + 缩进 4 空格) |
| `elif cond: / else:` | 否则如果 / 否则 |
| `for i in range(5):` | 0,1,2,3,4 |
| `for x in list:` | 遍历元素 |
| `while cond:` | 条件为真就一直做 |
| `break / continue` | 跳出循环 / 跳过本次 |
| `and or not` | 与 / 或 / 非 |
| `== != > < >= <=` | 比较(相等是两个等号) |

### ⑥ 函数

| 写法 | 说明 |
|---|---|
| `def f(a, b=1):` | 定义,含默认值参数 |
| `return value` | 返回结果(不写返回 None) |
| `f(3) / f(3, 4)` | 调用 |
| `def f(*args)` | 可变参数:任意多个位置参数打包成元组 |
| `作用域` | 函数内赋值 = 局部变量 |

### ⑦ 类

| 写法 | 说明 |
|---|---|
| `class Dog:` | 定义类(模具) |
| `def __init__(self, name):` | 构造函数 |
| `self.name = name` | 属性 |
| `def bark(self):` | 方法(第一参数必须是 self) |
| `obj = Dog("旺财")` | 创建对象 |
| `def __str__(self):` | print 对象时显示的内容 |

### ⑧ 文件与异常

| 写法 | 说明 |
|---|---|
| `f = open("a.txt", "w")` | 写入(会清空!) |
| `f = open("a.txt", "a")` | 追加 |
| `f.read() / f.readlines()` | 读全部 / 读成列表 |
| `f.write("x\n")` | 写一行(自己加换行符) |
| `with open("a.txt", encoding="utf-8") as f:` | 推荐写法:离开缩进块自动关闭 |
| `f.close()` | 关闭(真实环境推荐 with) |
| `try: ... except ValueError as e:` | 兜住错误 |
| `finally:` | 无论成败都执行 |

### ⑨ 常见报错速查

| 写法 | 说明 |
|---|---|
| `NameError` | 变量没定义 / 拼错 |
| `TypeError` | 类型不匹配(字符串 + 数字、参数个数不对) |
| `ValueError` | int("abc") 这类:类型对、值不合法 |
| `IndexError` | 列表下标越界 |
| `KeyError` | 字典没这个键 |
| `ZeroDivisionError` | 除以 0 |
| `IndentationError` | 缩进不一致 / 该缩进没缩进(少了冒号报的是 SyntaxError) |
| `AttributeError` | 对象没有这个属性或方法 |


---

# 附录 A · 校验方法与修改记录

**校验方法**:从原网页提取全部 32 关的 129 段 Python 代码,分别在 ① 网页自带的 JavaScript 版 Python 解释器 和 ② 标准 CPython 3.13 中运行,逐段比对输出;再逐关核对讲解文字、代码注释、练习题和测验答案里引用的数字与结论是否与真实运行结果一致。聚类、DBSCAN、莫兰指数等算法另用 scikit-learn / numpy 独立计算交叉核对。

**修改原则**:以标准 Python 的真实行为为准;网页模拟器特有的限制(不支持 with / set / 元组比较、报错为中文、sort 按字符串比较等)一律改成标准 Python 的写法与说法;只改错误和不一致之处,不改动课程结构与教学思路。

**L01**

- 〔适配〕去掉「网页内置解释器 / 右上角运行按钮」等网页专属说明,改为本地 Python 3 的学习方式。

**L02**

- 〔代码〕code2 里 9.9 \* 3 在真实 Python 输出 29.700000000000003,补充 round() 并注释浮点误差。
- 〔内容〕原文说 "18" + "1" 会导致 TypeError,不对:字符串加字符串是拼接;TypeError 来自字符串加数字。已改正。

**L05**

- 〔适配〕「解释器超过 12 万步自动停止」是网页模拟器行为,真实 Python 没有;改为 Ctrl + C 中断。

**L07**

- 〔测验〕第 1 题解析没有提到 -1 也能取到 30,且选项「-3 也可以」表述含糊;已改正。

**L08**

- 〔代码〕原注释称「模拟器不支持 with」,真实 Python 应优先用 with;主代码改为 with 写法,所有 open() 补 encoding="utf-8"(避免 Windows 中文乱码),按行读取改为 for line in f。

**L09**

- 〔适配〕「本模拟器只内置 math/random/time」改为标准库与第三方库(pip 安装)的说明。

**L11**

- 〔适配〕真实 Python 的报错是英文的,删去「解释器已翻译成中文」的说法,补充读报错的示例。

**L12**

- 〔代码〕level() 返回的 "优秀 " 带多余空格,导致等级统计字典的键变成 '优秀 ';去掉多余空格(L04/L05/L10/L11 同类空格一并清理)。

**L13**

- 〔代码〕分箱公式原为 (lon + 115) // 5 \* 5,得到 190、230 这种毫无地理意义的箱号,与讲解「116.4 → 115」矛盾;改为 int(lon // 5 \* 5)。
- 〔内容〕「用错 / 会让箱号变成 35.0」的说法不准确,并补充「浮点数 // 结果仍是浮点」这一真实 Python 行为。
- 〔测验〕最后一题解析称「112 会变成 115」,实际 112 // 5 \* 5 = 110;举例「117 不取更近的」也不成立(117 本来就更靠近 115)。已改正。

**L14**

- 〔代码〕打印标签「没找到广州呢」与实际查询的「不存在的城市」不符;删去网页私有库 ts.pairwise;测验解析改为真实报错文字。
- 〔内容〕原卡片称「元组不能比大小、不能排序」(网页模拟器的限制),真实 Python 支持按字典序比较和排序;卡片重写。

**L15**

- 〔代码〕讲解提到「主代码里的 find\_max、count\_if」,但原代码并没有这两个函数;已补上。

**L16**

- 〔内容〕表格里的例子 5.upper() 在真实 Python 中是 SyntaxError(5. 被当成小数),不是 AttributeError;已改为 x = 5; x.upper()。
- 〔适配〕「报错是中文、会列出现有键/合法下标」是网页模拟器的行为,改为真实 Python 的报错内容;注释 # 50 改为实际输出 50.0。

**L17**

- 〔代码〕注释「比第 6 位 "9" < "1"?」有误:第 6 个字符是 "0" 对 "1"。
- 〔代码〕原文称「解释器不支持 set」,真实 Python 有 set;保留字典版原理讲解,新增 set 标准写法示例。
- 〔内容〕删除重复的一段讲解(同一意思写了两遍)。
- 〔内容〕「坑一」原例 "2021-1" > "2021-10" 为 True 是错的(实际为 False);「坑二」原文给出的错误结果与实际计算不符;已用可验证的例子重写。

**L18**

- 〔代码〕原代码用网页私有的 tensor 模块(import tensor as ts),在真实 Python 中 ModuleNotFoundError;全部改写为 numpy / pandas。shape 写法改为 (8,);分组由「按城市」(每组 1 行,无意义)改为按大区。

**L22**

- 〔内容〕交叉引用「下一幕 L23」改为 L24(预测在 L24);pandas 2.2+ 中 resample("Y") 已弃用,改为 "YE";年均值改用 len() 而非硬写 12(与本幕自己的警示一致);测验解析不再用选项字母。

**L24**

- 〔代码〕原「移动平均(前 3 个月)」在测试期前 3 个月实际只用了 0~2 个值(第 1 个月直接拿上月值),与方法名不符;改为始终用最近 3 个已知月(含训练区末尾),MAE 数值随之更新。

**L23**

- 〔内容〕公式中的 x̄(x 平均值)全部丢失了上横线,写成了 Σ(x−x) 等无意义式子,已补回;删去不存在的「推导见本幕末尾」与乱码「『」;示例数据改用本幕实际算出的年均气温;主代码误差表表头有「城市」却没打印城市名,已补上。

**L26**

- 〔代码〕讲解说「用混淆矩阵衡量」,但示例与主代码只算了准确率;补上混淆矩阵计算。主代码中跳过自身的做法其实是留一法,标题改正。「准确率、精确率、召回率三者合起来叫 F1」有误,F1 只是精确率与召回率的调和平均。

**L28**

- 〔内容〕引言「L15 用了准确率」应为 L26;公式里丢失的「≤」「≈」补回;第 1 题题干 96% 与「95 个负类」不自洽(永远答负类正好 95%),已改正;代码里硬写的 /50.0、\*1.0 改为按实际样本数计算。

**L29**

- 〔内容〕sklearn 1.4 起 n\_init 默认 "auto"(不再是 10);交叉引用「L18 的肘部法」应为 L30;「DBSCAN 的簇中心是真实样本点」不成立(DBSCAN 没有中心);迭代骨架示例原本没有任何输出,补了打印。

**L30**

- 〔代码〕DBSCAN 示例原本只循环打印「eps = … 时对比一下」,没有任何计算,注释里的结果无从验证;改为可运行的手写 DBSCAN(结果已与 sklearn.cluster.DBSCAN 逐一核对一致)。轮廓系数补上单点簇记 0 的惯例;交叉引用 L17 改为 L29。
- 〔代码〕【重要】原手写 k-means 只从一个起点出发,k = 2、4、5 时陷入很差的局部最优(出现只有 1 个站的簇),肘部法「k=3 处拐弯」和轮廓系数「k=3、4 打平」都是这个假象造成的(用 scikit-learn 多次初始化核对,k=2 的 inertia 应为 2332.35 而不是 2863.13)。改为多起点(每个站点轮流当起点、取最优),相应地重写了肘部法与轮廓系数的结论。

**L31**

- 〔代码〕示例称「忘转弧度时根号里会出现负数」并给了一个自相矛盾的算例(输出 0.9115 为正数);事实上 haversine 公式对任意弧度值都满足 0 ≤ a ≤ 1,不会报错——这恰恰是此类错误难发现的原因。已改正说明并删去错误算例。
- 〔代码〕主代码注释「这个解释器的 sort() 对数字按字符串比」是网页模拟器的缺陷,真实 Python 直接 pairs.sort() 即可;末段「纬度差相同的两组城市」并不成立(北京-石家庄纬差 1.86°,上海-杭州约 0.96°),改为「经度差 1 度在不同纬度的距离」;投影卡片中 CGCS2000、EPSG:4490 的表述有误(4490 是经纬度坐标,不是投影),已改正。

**L33**

- 〔代码〕「典型点结果」原本是 5 行写死的 print,改为真正用 bbox 计算;缓冲区椭圆方向、sjoin\_nearest 参数写法更正;「兰州 →」空输出改为明确提示。

**L35**

- 〔代码〕局部莫兰示例原来只打印「同号邻居会得到正的局部值」(对负偏差的格子也这么说),没有真正计算;改为真实计算 Ii 并分类。公式里丢失的 x̄ 补回。
- 〔代码〕【重要】原「置换检验」只是把展平后的网格整体平移 37 格,空间结构几乎没变,打乱后 I = 0.7969 与原值 0.8013 几乎一样,输出却写着「打乱后接近 0」——结论与结果自相矛盾。改为真正的随机置换检验(199 次,固定种子)并给出伪 p 值。Gi\* 原代码只加邻居、不含自己,实际算的是 Gi 而非 Gi\*,已改为含自身。

**L32**

- 〔代码〕时间差原来只取小时位(int(split(":")[0])),「11:30」会被当成 11 点,与本幕测验「必须用时间戳算时间差」及练习题相矛盾;新增 to\_hours() 计入分钟。全程平均速度原来除以段数(隐含每段 1 小时),改为总距离 / 总时长。movingpandas 写法更正;代码标题 L24 改为 L32。

**L37**

- 〔内容〕原文把行 0~5 叫「左上 / 西北」,但同一段代码把行号换算成纬度时却把行 0 当成最南端(lat = latMin + (r+0.5)·size),南北自相矛盾;统一采用代码与数据集(lonMin/latMin 为左下角)的约定:行 0 在南,并加了约定说明卡片。片区名、四片区标签相应改正;均值改用 len(vals);MAU → MAUP。

**L38**

- 〔代码〕s04 只跳过 pm25 为空的行,与主代码(任一字段为空即丢弃)口径不同,导致同一份数据算出两个标准差(242.86 / 250.93);统一口径,并把写死的「19.87 → 250.93」改为实时计算。交叉引用 L13/L25/L26 更正为 L18/L37;「左上片区」按网格约定改为西南片区。

**L25**

- 〔结构〕L25 与 L37 标题、正文几乎完全相同(L37 多一段四片区汇总),属于重复关卡;删除 L25,统一保留在 L37。

**速查**

- 〔内容〕去掉「本模拟器不支持 \*args」;IndentationError 不包括「少了冒号」(那是 SyntaxError);补充 with open 写法。


# 附录 B · 网页附带工具库 minialgo.py 的校验

原网页还内嵌了一个约 1500 行的教学算法库 minialgo.py(课程代码本身没有调用它)。把其中的函数逐一与 numpy / scikit-learn 的结果对照:

- 距离与统计:`euclid`、`manhattan`、`haversine`、`mean`、`std`、`cov`、`pearson`、`median`、`quantile` —— 结果一致。
- 回归与分类:`linreg_fit`、`linreg_r2` 与 `np.polyfit` 一致;`knn_predict`、`confusion_matrix`、`precision_recall_f1`、`accuracy` 与 sklearn 一致。
- 聚类:`silhouette` 与 `sklearn.metrics.silhouette_score` 一致;`dbscan` 在 eps = 1.5 / 2.0 / 2.5 / 3.0 下的簇数与噪声点数与 `sklearn.cluster.DBSCAN` 完全一致;`kmeans` 为单起点确定性初始化,可能停在局部最优(这是算法特性,不是错误)。
- **发现并修复 1 处错误**:`morans_i` 的结果被放大了 n / k 倍 —— 权重已按行标准化(W = n),代码却又乘了 n / (邻居总数),而且方差已经除过 n。50 个站点、k = 4 时原函数返回 5.75(莫兰指数不可能这么大),正确值是 0.46(已用 numpy 按定义独立计算核对)。
- **补充说明 1 处**:`gd_linreg` 在 x 未标准化(如气温 0~30)时,默认学习率 0.05 会发散成 inf,已在函数说明里注明「先标准化或调小学习率」。

修复后的 minialgo.py 随讲义一并提供。
