pyAutoDoc
===========

python 自动文档生成
-------------------

#. `extensions` 中添加 `sphinx.ext.autodoc` ；
#. 添加需要生成文档的模块的路径；

    .. code-block:: python

        import os, sys
        sys.path.insert(0, os.path.abspath("/path/to/module"))

#. 编写 `rst` 文件；

    .. code-block:: rst

        .. automodule:: stools.Ssignal
            :members:

    :members:
        默认为 `None` 。如果设置为 `all` ，则会列出模块中的所有成员（函数、类、变量等）。也可以指定一个成
        员列表，只显示这些成员。

    :undoc-members:
        
        默认为 `False` 。如果设置为 `True` ，则会包含那些没有文档字符串的成员。

    :show-inheritance:
        
        默认为 `True` 。如果设置为 `True` ，则在类文档中显示继承关系。

    :inherited-members:
        
        默认为 `False` 。如果设置为 `True` ，则会列出从基类继承的成员。

    :exclude-members:
        
        允许你指定一个或多个成员名称，这些成员将不会被包括在文档中。

    :special-members:
        
        默认为 `True` 。如果设置为 `False` ，则不会显示特殊方法（如 `__init__` 、 `__repr__` 等）。

    :imported-members:
        
        默认为 `False` 。如果设置为 `True` ，则会显示从其他模块导入的成员。

    :private-members:
        
        默认为 `False` 。如果设置为 `True` ，则会显示私有成员。

    :member-order:
        
        默认为 `bysource` 。可以设置为 `bysource` 、 `alphabetic` 或 `groupwise` ，以控制成员的排序方式。

    :synopsis:
        
        用于为模块提供一个简短的描述，这个描述会出现在模块文档的顶部。

    :module-synopsis:
        
        类似于 `:synopsis:` ，但专门用于模块。

    :platform:
        
        描述模块支持的平台。

    :toctree:
        
        用于指定生成的文档应该包含在哪个文档树（ `toc-tree` ）中。

    :noindex:
        
        如果设置为 `True` ，则该模块不会出现在索引中。

    :dedent:
        
        默认为 `4` 。指定模块文档字符串中的缩进数量，用于格式化。

    :lineno-match:
        
        默认为 `True` 。如果设置为 `True` ，则会尝试匹配源代码中的行号。


自动生成文档
------------

参考 : https://blog.csdn.net/lixiaomei0623/article/details/120530642

配置
^^^^^^^

.. code-block:: python

    # ./source/conf.py

    import os
    import sys
    sys.path.insert(0, os.path.abspath('../../src'))

    extensions = [
        'sphinx.ext.autodoc',
        'sphinx.ext.napoleon',
        'sphinx.ext.doctest',
        'sphinx.ext.intersphinx',
        'sphinx.ext.todo',
        'sphinx.ext.coverage',
        'sphinx.ext.mathjax',
    ]

.. code-block:: bash

    # pwd : ./source/
    sphinx-apidoc -o source ../src/

实例
------

有一下项目：

.. code-block:: text

    doc/
    | |- build/
    | |- source/
    | |- make.bat
    | |- Makefile
    src/
    | |- numpy.py
    | |- google.py
    | |- ...

google.py
^^^^^^^^^^^
.. code-block:: python

    # -*- coding: utf-8 -*-
    '''Google注释风格
    详情见 `Google注释风格指南`_
    .. _Google注释风格指南:
    https://google.github.io/styleguide/pyguide.html
    '''
    
    
    class GoogleStyle:
        '''Google注释风格
        用 ``缩进`` 分隔，
        适用于倾向水平，短而简单的文档
        Attributes:
            dividend (int or float): 被除数
            name (:obj:`str`, optional): 该类的命名
        '''
    
        def __init__(self, dividend, name='GoogleStyle'):
            '''初始化'''
            self.dividend = dividend
            self.name = name
    
        def divide(self, divisor):
            '''除法
            Google注释风格的函数，
            类型主要有Args、Returns、Raises、Examples
            Args:
                divisor (int):除数
            Returns:
                除法结果
            Raises:
                ZeroDivisionError: division by zero
            Examples:
                >>> google = GoogleStyle(divisor=10)
                >>> google.divide(10)
                1.0
            References:
                除法_百度百科  https://baike.baidu.com/item/%E9%99%A4%E6%B3%95/6280598
            '''
            try:
                return self.dividend / divisor
            except ZeroDivisionError as e:
                return e

numpy.py
^^^^^^^^^^^

.. code-block:: python
 
    """NumPy注释风格
    详情见 `NumPy注释风格指南`_
    .. _NumPy注释风格指南:
    https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard
    """
    
    class NumpyStyle:
        '''Numpy注释风格
        用 ``下划线`` 分隔，
        适用于倾向垂直，长而深的文档
        Attributes
        ----------
        multiplicand : int
            被乘数
        name : :obj:`str`, optional
            该类的命名
        '''
    
        def __init__(self, multiplicand, name='NumpyStyle'):
            '''初始化'''
            self.multiplicand = multiplicand
            self.name = name
    
        def multiply(self, multiplicator):
            '''乘法
            Numpy注释风格的函数，
            类型主要有Parameters、Returns
            Parameters
            ----------
            multiplicator :
                乘数
            Returns
            -------
            int
                乘法结果
            Examples
            --------
            >>> numpy = NumpyStyle(multiplicand=10)
            >>> numpy.multiply(10)
            100
            '''
            try:
                if isinstance(multiplicator, str):
                    raise TypeError('Division by str')
                else:
                    return self.multiplicand * multiplicator
            except TypeError as e:
                return e

reStructredText.py
^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    # -*- coding: utf-8 -*-
    
    class ReStructuredTextStyle:
        '''reStructuredText风格
        用 ``冒号`` 分隔，
        PyCharm默认风格
        :arg augend: 被加数
        :type augend: int
        '''
    
        def __init__(self, augend, name='ReStructuredTextStyle'):
            '''初始化'''
            self.augend = augend
            self.name = name
    
        def add(self, addend):
            '''加法
            reStructuredText风格的函数，
            类型主要有param、type、return、rtype、exception
            :param addend: 被加数
            :type addend: int
            :returns: 加法结果
            :rtype: :obj:`int` or :obj:`str`
            :exception TypeError: Addition by str
            >>> reStructredText = ReStructuredTextStyle(augend=10)
            >>> reStructredText.add(10)
            20
            '''
            try:
                if isinstance(addend, str):
                    raise TypeError('Addition by str')
                else:
                    return self.augend + addend
            except TypeError as e:
                return e
