# 文档

[myst-parser](https://myst-parser.readthedocs.io/en/latest/)
https://myst-parser.readthedocs.io/en/latest/

[sphinx-markdown 扩展教程](https://sphinx-book-theme.readthedocs.io/en/latest/tutorials/get-started.html)
https://sphinx-book-theme.readthedocs.io/en/latest/tutorials/get-started.html

# 安装与配置

```{rubric} 安装

```

```bash
pip install myst-parser
pip install sphinx-design
```

```{rubric} 配置

```

```python
# conf.py

extensions = [
"myst_parser",
"sphinx_design",
]
```

# 引用

> Here's my quote, it's pretty neat.
> I wonder how many lines I can create with
> a single stream-of-consciousness quote.
> I could try to add a list of ideas to talk about.
> I suppose I could just keep going on forever,
> but I'll stop here.

# 引文

```{epigraph}
Here's my quote, it's pretty neat.
I wonder how many lines I can create with
a single stream-of-consciousness quote.
I could try to add a list of ideas to talk about.
I suppose I could just keep going on forever,
but I'll stop here.

-- Author, Source
```

# 超链接

[My website](https://www.example.com)

# 表格

| Column 1 | Column 2 | Column 3 |
| -------- | -------- | -------- |
| Row 1,1  | Row 1,2  | Row 1,3  |
| Row 2,1  | Row 2,2  | Row 2,3  |
| Row 3,1  | Row 3,2  | Row 3,3  |

# 脚注

Here's a footnote[^1].

[^1]: This is the footnote content.

# 边栏

```{sidebar} 侧边栏标题
侧边栏内容
```

````{sidebar} **My sidebar title**
```{note}
Here is my sidebar content, it is pretty cool!
```
![](../_static/imgs/sphinx-logo.png)
````

sphinx_book_theme + myst_parser + sidebar

sphinx_book_theme + myst_parser + sidebar

sphinx_book_theme + myst_parser + sidebar

sphinx_book_theme + myst_parser + sidebar

sphinx_book_theme + myst_parser + sidebar

sphinx_book_theme + myst_parser + sidebar

sphinx_book_theme + myst_parser + sidebar

sphinx_book_theme + myst_parser + sidebar

sphinx_book_theme + myst_parser + sidebar

sphinx_book_theme + myst_parser + sidebar

sphinx_book_theme + myst_parser + sidebar

sphinx_book_theme + myst_parser + sidebar

# 页边

```{margin} Look, some margin content!
On wider screens, this content will pop out to the side!
```

````{margin} **Notes in margins**
```{note}
Wow, a note with an image in a margin!
![](../_static/imgs/sphinx-logo.png)
```
````

sphinx_book_theme + myst_parser + margin

sphinx_book_theme + myst_parser + margin

sphinx_book_theme + myst_parser + margin

sphinx_book_theme + myst_parser + margin

sphinx_book_theme + myst_parser + margin

sphinx_book_theme + myst_parser + margin

sphinx_book_theme + myst_parser + margin

sphinx_book_theme + myst_parser + margin

sphinx_book_theme + myst_parser + margin

# 图片

## image

![My image](../_static/imgs/sphinx-logo.png)

## figure

### margin-caption figure

```{figure} ../_static/imgs/sphinx-logo.png
---
width: 60%
figclass: margin-caption
alt: My figure text
name: myfig5
---
figclass: margin-caption
```

We can reference the figure with {ref}`this reference <myfig5>`. Or a numbered reference like
{numref}`myfig5`.

### margin figure

```{figure} ../_static/imgs/sphinx-logo.png
---
figclass: margin
alt: My figure text
name: myfig4
---
figclass: margin
```

sphinx_book_theme + myst_parser + figure + margin

sphinx_book_theme + myst_parser + figure + margin

sphinx_book_theme + myst_parser + figure + margin

sphinx_book_theme + myst_parser + figure + margin

sphinx_book_theme + myst_parser + figure + margin

# 数学公式

```{math}
:label: My label

\nabla^2 f =
\frac{1}{r^2} \frac{\partial}{\partial r}
\left( r^2 \frac{\partial f}{\partial r} \right) +
\frac{1}{r^2 \sin \theta} \frac{\partial f}{\partial \theta}
\left( \sin \theta \, \frac{\partial f}{\partial \theta} \right) +
\frac{1}{r^2 \sin^2\theta} \frac{\partial^2 f}{\partial \phi^2}
```

And here is a really long equation with a label!

```{math}
:label: My label 2

\nabla^2 f =
\frac{1}{r^2} \frac{\partial}{\partial r}
\left( r^2 \frac{\partial f}{\partial r} \right) +
\frac{1}{r^2 \sin \theta} \frac{\partial f}{\partial \theta}
\left( \sin \theta \, \frac{\partial f}{\partial \theta} \right) +
\frac{1}{r^2 \sin^2\theta} \frac{\partial^2 f}{\partial \phi^2}
\nabla^2 f =
\frac{1}{r^2} \frac{\partial}{\partial r}
\left( r^2 \frac{\partial f}{\partial r} \right) +
\frac{1}{r^2 \sin \theta} \frac{\partial f}{\partial \theta}
\left( \sin \theta \, \frac{\partial f}{\partial \theta} \right) +
\frac{1}{r^2 \sin^2\theta} \frac{\partial^2 f}{\partial \phi^2}
```

You can add a link to equations like the one above {eq}`My label` and {eq}`My label 2`.

# 代码块

```{code-block} python
:name: mycode
:linenos:
:emphasize-lines: 1,3


def my_function(x, y):
    """
    This is a function that multiplies two numbers.

    :param x: The first number.
    :param y: The second number.
    :return: The product of x and y.
    """
    return x * y
```

# 标签页

``````{tab-set}
`````{tab-item} rST
````rst
.. admonition:: A sidebar admonition!
    :class: sidebar note

    Some sidebar content.
````
`````
`````{tab-item} Markdown
````md
```{admonition} A sidebar admonition!
:class: sidebar note
Some sidebar content.
```
````
`````
``````

# 代码块

```python
print("Hello, world!")
```

# admonition

属性：

`:class: full-width`

```{admonition} 自定义!
自定义内容
```

```{note}
<!-- :class: full-width -->
note
```

```{tip}
<!-- :class: full-width -->
tip
```

```{hint}
<!-- :class: full-width -->
hint
```

```{attention}
<!-- :class: full-width -->
attention
```

```{caution}
<!-- :class: full-width -->
caution
```

```{important}
<!-- :class: full-width -->
important
```

```{warning}
<!-- :class: full-width -->
note
```

```{danger}
<!-- :class: full-width -->
danger
```

```{error}
<!-- :class: full-width -->
error
```

# 绘图

## plantuml

```{plantuml}
@startuml
help themes
@enduml
```

# test

```{video} ../_static/video/video.mp4
:width: 500
<!-- :nocontrols: -->
<!-- :loop: -->
:autoplay:
```

[ ] 未完成
[x] 已完成
