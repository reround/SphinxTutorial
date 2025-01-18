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
    'sphinx-mathjax-offline'，# 离线公式支持
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

# plotmatlab 输出图像设置
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
