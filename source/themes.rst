
sphinx-book-theme 主题
=======================

主题教程：
https://sphinx-book-theme.readthedocs.io/en/latest/index.html

.. code-block:: python

    html_theme = "sphinx_book_theme"
    html_logo = "_static/imgs/sphinx-logo.svg"
    html_title = "Sphinx Tutorial"

中文搜索
----------

中文搜索功能依赖 jieba 库，需要额外安装：

.. code-block:: bash

    pip install jieba

其它的主题
-------------

可以先到 Sphinx 的官网

https://sphinx-themes.org/


https://sphinxthemes.com/
查看。

.. code-block:: bash

    # 安裝 主题命令
    # conf.py 设置主题 配置

    pip install sphinx-rtd-theme
    html_theme = "sphinx_rtd_theme"

    pip install mpl-sphinx-theme
    html_theme = "mpl-sphinx-theme"

    pip install cloud-sptheme
    html_theme = 'cloud'

    pip install piccolo-theme
    html_theme = 'piccolo_theme'

    pip install sphinx-documatt-theme
    html_theme = 'sphinx_documatt_theme'

    pip install sphinx-wagtail-theme
    extensions.append("sphinx_wagtail_theme")
    html_theme = 'sphinx_wagtail_theme'

    pip install sphinx
    html_theme = 'nature'

    pip install sphinx-book-theme
    html_theme = "sphinx_book_theme"

