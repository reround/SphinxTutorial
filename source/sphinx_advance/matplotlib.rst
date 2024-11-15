
嵌入 Matplotlib 图形
=====================

.. rubric:: 添加扩展

.. code-block:: python
    
    extensions = [
        ...
        "matplotlib.sphinxext.plot_directive",  # matplotlib 绘图
        ...
    ]
    
    # plot_formats 配置生成的图片格式，可以多个，可以单个。默认是 (png，hires.png，pdf)。
    plot_formats = [("hires.png", 200), ("png", 80), "pdf"]
    # 默认情况下，plot_html_show_formats是启用的（设置为True），
    # 这意味着在生成的HTML文档中，每个绘图旁边都会显示一个链接到
    # 高分辨率PNG和PDF文件的链接。这使得用户可以查看更高分辨率的图像或下载PDF版本。
    #设置为False后，即使plot_formats配置了多个格式，
    # 生成的HTML文档中也只会显示默认的PNG图像，而不会显示链接到其他格式的图像的链接。
    plot_html_show_formats = False

Matplotlib 是一个 Python 2D 绘图库，可用于创建各种类型的 2D 图形，包括直方图、散点图、条形图、饼图等。

Matplotlib 图形可以直接嵌入到 Sphinx 文档中，只需使用 ``.. plot::`` 指令，并在指令块中导入 Matplotlib 库和所需的图形函数。

.. warning:: 

    `.. plot::` 不要使用 `:caption:` 进行自动编号，否则以后的 `.. figure:: arg1` 和 `.. plot::` 编号会加一。

    可以使用锚点，但是不能编号了。



.. rubric:: 例子：

.. code-block:: rst

    .. _barfigre:
    .. plot::
        import matplotlib.pyplot as plt
        import numpy as np
        x = np.random.randn(1000)
        plt.hist(x, 20)
        plt.grid()
        plt.title(r'Normal: $\mu=%.2f, \sigma=%.2f$' % (x.mean(), x.std()))
        plt.show()

    .. centered::  图：条形图

    这是条形图 :ref:`图：条形图 <barfigre>`

.. rubric:: 渲染图

.. _barfigre:
.. plot::

    import matplotlib.pyplot as plt
    import numpy as np
    x = np.random.randn(1000)
    plt.hist(x, 20)
    plt.grid()
    plt.title(r'Normal: $\mu=%.2f, \sigma=%.2f$' % (x.mean(), x.std()))
    plt.show()

.. centered::  图：条形图

这是条形图 :ref:`图：条形图 <barfigre>`


