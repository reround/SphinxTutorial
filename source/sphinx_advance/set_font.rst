设置字体
==========

设置字体为宋体。

.. code-block:: python

    # conf.py

    html_css_files = ['custom.css']

.. code-block:: css

    /* _static/custom.css */

    body {
        font-family: 'SimSun', serif;
    }

.. note::

    确保 custom.css 文件位于你的 Sphinx 项目中的 _static 文件夹下。

.. rubric:: 写个脚本到 conf.py 自动生成 custom.css 文件

.. code-block:: python
    
    # conf.py

    if not os.path.exists("_static/custom.css"):
        with open("_static/custom.css", "w", encoding="utf-8") as f:
            custom_css = """
    body {
        font-family: 'SimSun', serif;
    }
            """
            f.write(custom_css)