pyAutoDoc
===========

python 自动文档生成

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
