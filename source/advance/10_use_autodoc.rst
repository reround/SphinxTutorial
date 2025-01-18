.. _topics-10_use_autodoc:

使用 autodoc 自动生成文档
==========================

.. note::

   本节内容基于 Sphinx 1.0.7

Sphinx 可以从 Python 模块中自动生成文档。这个功能被称为 autodoc，它是 Sphinx 的一个扩展。autodoc 可以从模块中提取文档字符串，然后将它们转换为 reStructuredText 格式，最后将它们嵌入到 Sphinx 文档中。

.. note::

   autodoc 仅支持 Python 2.3 及以上版本。

在 ``conf.py`` 中启用 autodoc 扩展::

   extensions = ['sphinx.ext.autodoc']

.. note::

    你可以在 ``conf.py`` 中启用多个扩展，只要将它们放在 ``extensions`` 列表中即可。

::

    .. autoclass:: net_inspect.domain.Cluster
        :members:
        :undoc-members:

可用参数：

.. code-block::

   :members: 显示类的所有成员
   :undoc-members: 显示未被文档化的成员
   :show-inheritance: 显示继承关系
   :inherited-members: 显示继承的成员
   :private-members: 显示私有成员
   :special-members: 显示特殊成员
   :exclude-members: 排除成员
   :member-order: 指定成员排序方式
   :noindex: 不生成索引

