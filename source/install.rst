
安装
=====

参考：https://zhuanlan.zhihu.com/p/384863296

    
.. note:: 

    完善功能所需的扩展库

    .. code-block:: bash

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



安装sphinx
----------

.. code-block:: bash

    pip install sphinx
    pip install -i https://pypi.tuna.tsinghua.edu.cn/simple sphinx # 使用镜像


创建sphinx项目
--------------

.. code-block:: bash

    sphinx-quickstart 

然后会有如下的输出，需要根据提示输入项目名称、作者、版本号、语言等信息

.. code-block:: text

    ...
    ...
    > Separate source and build directories (y/n) [n]: y  <--------这里选y表示编译的文件单独放在build中

    The project name will occur in several places in the built documentation.
    > Project name: SphinxDemo     <--------这里输入项目的名称
    > Author name(s): xxpcb        <--------这里输入作者
    > Project release []: v1.0     <--------这里输入版本号

    ...
    ...
    For a list of supported codes, see
    https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language.
    > Project language [en]: zh_CN   <--------这里输入语音（中文简体）
    ...
    ...


项目文件结构
--------------

.. code-block:: text
        
    SphinxDemo
    |- Makefile
    |- cmd.bat
    |- make.bat
    |- source
    |   |- conf.py
    |   |- _static
    |   |- _templates
    |   |- index.rst
    |- _build
        |- html
        |- doctrees

这里先简单说明一下各个文件的作用：

.. code-block:: text
        
    build：生成的文件的输出目录
    source: 存放文档源文件
    _static：静态文件目录，比如图片等
    _templates：模板目录
    conf.py：进行 Sphinx 的配置，如主题配置等
    index.rst：文档项目起始文件，用于配置文档的显示结构
    cmd.bat：这是自己加的脚本文件（里面的内容是‘cmd.exe’）,用于快捷的打开 windows 的命令行
    make.bat：Windows 命令行中编译用的脚本
    Makefile：编译脚本，make 命令编译时用

导出文件
--------

导出 HTML
~~~~~~~~~

.. code-block:: bash

    make html

导出pdf
~~~~~~~~~~


#. 安装texlive

    在清华大学开源软件镜像站下载镜像文件：

    https://mirrors.tuna.tsinghua.edu.cn/CTAN/systems/texlive/Images/texlive2018-20180414.iso


#. 生成pdf
   
.. code-block:: bash

    make latexpdf


安装 autobuild 工具
--------------------

快速开始
~~~~~~~~~~~~

上面使用 make html 的方式编译，编译完后需要打开 html 文件来查。

还有一种 HTTP 服务的方式，可以在浏览器器中通过 ip 地址来查看，该方式需要安装自动 build 工具：

.. code-block:: bash

    pip install -i https://pypi.tuna.tsinghua.edu.cn/simple sphinx-autobuild

然后使用如下编译指令进行编译

.. code-block:: bash

    sphinx-autobuild source build/html

然后可以到浏览器中，输入 `127.0.0.1:8000` 查看效果。

设置 ip 地址和端口号
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    sphinx-autobuild source build/html --host=0.0.0.0 --port=8000

在局域网内的任何设备上，通过浏览器访问http://<您的服务器IP地址>:8000即可查看文档。

.. code-block:: bash

    sphinx-autobuild source build/html --host=0.0.0.0 --port=8000 --open-browser

这将在服务启动后自动在默认浏览器中打开文档的主页

更改样式主题
---------------

上面的测试效果，使用的是默认的主题 alabaster，
如果想安装其它的主题，
可以先到 Sphinx 的官网

https://sphinx-themes.org/


https://sphinxthemes.com/
查看。

这里选用一个较为常用的主题 Read the Docs，安装这个主题首先需要在 python 中进行安装，命令如下：

.. code-block:: bash

    pip install -i https://pypi.tuna.tsinghua.edu.cn/simple sphinx_rtd_theme

然后修改 `conf.py` 文件，找到 `html_theme` 字段，修改为

.. code-block:: bash

    #html_theme = 'alabaster'
    html_theme = 'sphinx_rtd_theme'

然后重新编译，查看效果。



支持 markdown
--------------


Sphinx 默认只支持 reST 格式的文件，reST 的使用语法介绍见：

https://zh-sphinx-doc.readthedocs.io/en/latest/rest.html

安装 markdown 支持工具
~~~~~~~~~~~~~~~~~~~~~~~~

如果相要使用 markdown 格式的文档，还要安装 markdown 支持工具，命令如下：

.. code-block:: bash

    pip install -i https://pypi.tuna.tsinghua.edu.cn/simple recommonmark

若要使用 markdown 的表格，还要安装：

.. code-block:: bash

    pip install -i https://pypi.tuna.tsinghua.edu.cn/simple sphinx_markdown_tables

然后，还要修改 conf.py 文件，找到 extensions 字段，修改为:

.. code-block:: bash

    #extensions = [
    #]
    extensions = ['recommonmark','sphinx_markdown_tables']

注：支持 markdown 后，文档文件可以使用 markdown 格式，但文档的配置文件 index.rst 还要使用 reST 格式

修改文档显示结构
-----------------

index 文件分析
~~~~~~~~~~~~~~~~

修改文档结构，需要修改 index.rst 文件，首先来看一下这个文件中的内容：

.. code-block:: rst

    .. SphinxDemo documentation master file, created by
    sphinx-quickstart on Sat Jun 26 17:56:51 2021.
    You can adapt this file completely to your liking, but it should at least
    contain the root `toctree` directive.
    
    Welcome to SphinxDemo's documentation!
    ======================================
    
    .. toctree::
    :maxdepth: 2
    :caption: Contents:
    
    
    
    Indices and tables
    ==================
    
    * :ref:`genindex`
    * :ref:`modindex`
    * :ref:`search`

- 两个点 `..` +空格+后面的文本，代表注释（网页上不显示）
- 等号线 `====` +上一行的文本，代表一级标题
- `.. toctree::` 声明的一个树状结构（Table of Content Tree）
- `:maxdepth: 2` 表示页面的级数最多显示两级
- `:caption: Contents:` 用于指定标题文本（可以不要）
- 最下面的 3 行是索引和搜索链接（可以先不用管）

修改 index 文件
~~~~~~~~~~~~~~~~

修改 soure 文件夹下的 index.rst 文件,，这里表示添加了一个 Cpp 目录，然后 Cpp 目录下，链接的又一个 index 文件

.. code-block:: rst

    .. toctree::
    :maxdepth: 3
    :caption: Contents:

    Cpp/index

然后新建 `Cpp` 文件夹，并在该文件夹内新建若干个子类文件夹和一个 `index.rst` 文件。
然后编辑 `soure/Cpp` 文件夹里的 `index.rst` 文件，这里表示该目录级别下，又包含了 3 个子目录，子目录中再次通过 `index` 文件来描述子目录中的文档结构：

.. code-block:: rst

    C++知识
    =================================

    .. toctree::
    :maxdepth: 2

    01设计模式/index
    02数据结构/index
    03多线程/index

然后再进入各个子文件夹，添加 `markdown`格式的文档和 `index.rst` 文件

`soure/Cpp/01` 设计模式中的 `index.rst` 文件内容如下，这里表示管理了 2 个文档

.. code-block:: rst

    设计模式
    =================================

    .. toctree::
    :maxdepth: 1

    01单例模式
    02工厂方法模式

然后就可以编译，查看效果了。

整个目录结构如下：

.. code-block:: text

    - source
        |- index.rst
        |- Cpp
            |- index.rst
            |- 01设计模式
                |- index.rst
                |- 01单例模式.md
                |- 02工厂方法模式.md
            |- 02数据结构
                |- index.rst
                |- 01数组.md
                |- 02链表.md
            |- 03多线程
                |- index.rst
                |- 01线程.md
                |- 02锁.md


项目托管到 `gitee`
以上的操作，只能在本地的浏览器查看文档，若想让所有人都能看到，需要部署到 `ReadtheDocs` 展示，在部署之前，要把代码托管到代码托管平台，这里选用 `gitee` ，国内使用速度快。

先到 `gitee` 上（ `https://gitee.com/` ）建立一个公开的仓库，然后将本地项目文件上传即可，如我是建立一个名为 `SphinxDemo` 的仓库。

在上传文件之前，先自己写一个 `.gitignore` 文件，用于指示编辑的文件（ `build` 目录）不上传到代码仓库， `.gitignore` 文件内容如下：

.. code-block:: bash

    build/

然后使用就是在本地的项目文件夹内使用基本的 git 指令来将文件上传到仓库：

.. code-block:: bash

    git init
    git add -A
    git commit -m "first commit"
    git remote add origin https://gitee.com/xxpcb/sphinx-demo.git
    git push -u origin master


项目常用配置模板
-----------------
   
我的常用 `conf.py` 文件

.. code-block:: python

    # Configuration file for the Sphinx documentation builder.
    #
    # For the full list of built-in configuration values, see the documentation:
    # https://www.sphinx-doc.org/en/master/usage/configuration.html

    # -- Project information -----------------------------------------------------
    # https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

    import os, sys

    project = "Notes"
    copyright = "2024, shun"
    author = "shun"
    release = "1.0.0"

    # -- General configuration ---------------------------------------------------
    # https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
    sys.path.append(os.path.abspath("sphinxext"))
    extensions = [
        "sphinx.ext.mathjax",  # 数学公式支持
        "sphinx.ext.graphviz",  # graphviz 图形支持
        "sphinxcontrib.plantuml",  # plantuml 图形支持
        "matplotlib.sphinxext.plot_directive",  # matplotlib 绘图
        # "breathe", # doxygen 注释支持
        "sphinxcontrib.video",  # 视频支持
        # "sphinx.ext.autodoc", # 自动生成 API 文档
        "myst_parser",  # markdown 解析器
        "sphinx_design",
        "sphinx.ext.todo",
    ]
    todo_include_todos = True

    # plot_formats = [("png", 80), ("hires.png", 200), "pdf"]
    # plot_formats = [("hires.png", 200), ("png", 80), "pdf"]
    # plot_html_show_formats = False

    templates_path = ["_templates"]
    exclude_patterns = []

    language = "zh_CN"

    # -- Options for HTML output BEGIN-------------------------------------------------
    # https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

    # html_theme = "sphinx_rtd_theme"
    html_theme = "sphinx_book_theme"
    html_logo = "_static/imgs/sphinx-logo.svg"
    html_title = "Sphinx Tutorial"
    html_css_files = ["custom.css"]  # 自定义css文件
    html_static_path = ["_static"]
    numfig = True  # 允许图片自动编号
    # -- Options for HTML output END-------------------------------------------------


    # -- Options for graphviz output BEGIN---------------------------------------------
    # 设置graphviz_dot路径
    graphviz_dot = "dot"
    # 设置graphviz_dot_args的参数, 这里设置了默认字体
    # graphviz_dot_args = ["-Gfontname=Georgia", "-Nfontname=Georgia", "-Efontname=Georgia"]
    graphviz_dot_args = ["-Gfontname=SimHei", "-Nfontname=SimHei", "-Efontname=SimHei"]
    # 输出格式, 默认png，这里使用svg矢量图
    graphviz_output_format = "svg"
    # -- Options for graphviz output END---------------------------------------------


    # -- Options for plantuml output BEGIN---------------------------------------------
    plantuml_output_format = "svg"  # 可选，控制输出图片格式
    plantuml = r"java -jar D:\jar\plantuml.jar"  # 可选，指定 plantuml.jar 路径
    # -- Options for plantuml output END---------------------------------------------


    # -- Options for breathe output BEGIN---------------------------------------------
    # breathe_projects = {"demo": "path/to/doxygen/xml"}  # 项目名称和doxygen生成的xml文件路径
    # breathe_default_project = "demo"
    # -- Options for breathe output END---------------------------------------------


    # -- Options for LaTeX output BEGIN---------------------------------------------
    latex_documents_theme = "manual"  # 文档主题
    # latex_documents_theme = "howto"  # 文档主题
    latex_elements = {
        "classoptions": "openany",  # 章节之间不分页，针对于 "manual"， 不知道原因没用
    }
    out_put_file_name = "SphinxNote{}.tex".format(release)  # 文件名
    put_put_file_title = "SphinxNote"  # 文件标题名
    latex_engine = "xelatex"  # 使用 xelatex
    latex_documents = [
        (
            "index",
            out_put_file_name,
            put_put_file_title,
            author,
            latex_documents_theme,
        ),
    ]

    mathjax3_config = {
        # 启用 MathJax 支持的 公式自动编号
        "TeX": {
            "extensions": ["amsmath"],
        }
    }

    # \singlespacing         % 单倍行距
    # \onehalfspacing        % 1.5倍行距
    # \doublespacing         % 双倍行距
    latex_elements = {
        "preamble": r"""
        \usepackage[UTF8, scheme = plain]{ctex}
        \setcounter{tocdepth}{1} %目录编号深度
        \setcounter{secnumdepth}{1} % 章节编号深度
        \usepackage{amsmath}  % 引入 amsmath 包以支持公式编号
        \usepackage{indentfirst} % 首行缩进
        \setlength{\parindent}{2em} % 首行缩进 2 字符
        \usepackage{setspace}  %行距
        \onehalfspacing        % 1.5倍行距
    
        """,
        "fontpkg": r"""
            \usepackage{fontspec}
            \setmainfont{SimSun}  % 设置主字体为宋体
            \setsansfont{SimHei}  % 可选：设置无衬线字体为黑体
            \setmonofont{Courier New}  % 可选：设置等宽字体
        """,
        "figure_align": "H",
    }
    latex_logo = "_static/imgs/sphinx-logo.png"  # 自定义 logo

    # -- Options for LaTeX output END---------------------------------------------


    # -- 设置字体 ---------------------------------------------
    # 判断 _static/custom.css 文件是否存在，不存在则创建
    if not os.path.exists("_static/custom.css"):
        with open("_static/custom.css", "w", encoding="utf-8") as f:
            custom_css = """
    body {
        font-family: 'SimSun', serif;
    }
            """
            f.write(custom_css)

    # -- 设置字体 ---------------------------------------------
