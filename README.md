# SphinxTutorial

Sphinx教程（SphinxTutorial ）

这是一篇Sphinx教程，主要介绍Sphinx的基本用法。

目的是为了帮助读者更好地了解Sphinx，并能够更好地使用Sphinx。

里面的内容是参考网上的教程，并结合自己的理解进行整理、补充。

希望对读者有所帮助。

> “基础语法”、“中级语法”、“Sphinx标记结构”三节来自 [rst-tutorial-elinpf](https://rst-tutorial-elinpf.readthedocs.io/en/latest/) (https://rst-tutorial-elinpf.readthedocs.io/en/latest/)


## 编译本文依赖 (Compile this .rst file requirements)

本文依赖如下：

```bash
pip install sphinx # 安装sphinx
pip install sphinx-rtd-theme sphinx-book-theme # 常用主题
pip install sphinxcontrib-video # 视频播放
pip install sphinxcontrib-plantuml # 绘制UML图
pip install myst-parser # 支持markdown
pip install sphinx-design # 美化主题
```

```text
sphinx_advance/graphviz 需要安装 graphviz
sphinx_advance/plantuml 需要安装 java 和 plantuml.jar
```

编译命令

```bash
# Makefile 文件目录下
make html
```

生成后的文件目录结构如下：

```text
|-- build
|   |-- doctrees
|   |-- html
|   |   |-- _static
|   |   |-- _templates
|   |   |-- index.html   <-- 主页
|   |   |-- ...
|   |-- ...
|-- source/
|-- conf.py
|-- Makefile
|-- README.md

```
