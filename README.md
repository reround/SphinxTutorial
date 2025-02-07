# SphinxTutorial

Sphinx教程（SphinxTutorial ）

> 这是一篇Sphinx教程，主要介绍Sphinx的基本用法。 \\
> 目的是为了帮助读者更好地了解Sphinx，并能够更好地使用Sphinx。 \\
> 里面的内容是参考网上的教程，并结合自己的理解进行整理、补充。 \\
>
> 可能电脑上环境不齐全，提供一个 Release 版本参考。

希望对读者有所帮助。

> “基础语法”、“中级语法”、“Sphinx标记结构”三节来自 [rst-tutorial-elinpf](https://rst-tutorial-elinpf.readthedocs.io/en/latest/)
> 对其中的语法进行了补充和修改，并添加了一些自己的理解。


## 编译本文依赖 (Compile this .rst file requirements)

本文依赖如下：

```bash
pip install sphinx # 安装sphinx
pip install sphinx-rtd-theme sphinx-book-theme # 常用主题
pip install sphinx-autobuild # 自动编译
pip install sphinxcontrib-video # 视频播放
pip install sphinxcontrib-plantuml # 绘制UML图
pip install myst-parser # 支持markdown
pip install sphinx-design # 美化主题
pip install breathe # 为其他语言生成文档
pip install jieba # 中文搜索
pip install sphinx-mathjax-offline # 离线公式

...
```

```python
# 章节：sphinx_advance/graphviz 需要安装 graphviz
# 章节：sphinx_advance/plantuml 需要安装 java 和 plantuml.jar
# 并将 graphviz 和 java 添加到环境变量中
# 并修改 source/config.py 中的 plantuml ，指定 plantuml.jar 的路径

# 上面的安装包自行获取。太占空间了，就不上传了。

plantuml = r"java -jar D:\jar\plantuml.jar"
```

编译命令

```bash
# 在项目目录下
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


[介绍](./doc/introduce.md)
