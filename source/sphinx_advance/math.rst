数学表达式渲染方式
====================


配置插件
----------


Sphinx提供了两种数学表达式的渲染方式 ( 二选一 ):

`'sphinx.ext.imgmath'` : 通过 LaTex 渲染成图片( png 或 svg ).

`'sphinx.ext.mathjax'` : 通过 MathJax 渲染.

配置 `conf.py` ,


.. code-block:: python

    extensions = [
    ...
    'sphinx.ext.mathjax',
    ...
    ]

    mathjax3_config = {
        "TeX": {
            "extensions": ["amsmath"],
        }
    }

如果想更改，可以注释掉 `'sphinx.ext.mathjax'`, ， 并添加 `'sphinx.ext.imgmath'`, 即可.

然后，我们就可以在 html 里面编写基于 LaTeX 的数学表达式了，行间数学表达式格式如下：

.. code-block:: rst

    .. math::

        E = mc^2


渲染效果

    .. math::

        E = mc^2

行内数学表达式格式如下：

.. code-block:: rst

    质能方程 :math:`E = mc^2` 。

渲染效果

    质能方程 :math:`E = mc^2` 。

`MathJax` 的路径
-------------------

此外, 你还需要配置 `MathJax` 的路径 `mathjax_path` , Sphinx默认使用 `MathJax CDN` 提供的 JS 文件。 Sphinx默认使用的 `MathJax` 的路径值为 `https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML` 。 但在某些情况下可能无法使用， 可能是 `https` 安全协议的问题, 改成 `http` 即可, 即设置配置文件 `conf.py` 中的

.. code-block:: python

    # conf.py
    mathjax_path = 'https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML'

当然你也可以使用本地的MathJax, 参考 `Installing Your Own Copy of MathJax` , 到 `MathJax <https://github.com/mathjax/MathJax/archive/master.zip>`_ 下载 MathJax包  (约34.1MB) 并解压放到 “ `_static` ” 目录, 然后设置路径, 即在 `conf.py` 文件中添加代码:

公式编号与引用
---------------


.. code-block:: rst

    .. math::
        :label: eq1

        E = mc^2

    公式 :eq:`eq1` 是一个质能方程。

渲染效果

    .. math::
        :label: eq1

        E = mc^2

    公式 :eq:`eq1` 是一个质能方程。