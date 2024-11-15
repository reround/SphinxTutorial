
include
=========

`.. include::` 可以实现文档间的包含，类似于 `c` 语言中的 `.h` 文件，语法如下：

.. code-block:: rst

    .. include:: /path/to/file

如果同级标题内容太多，就可以分开写在不同的文件中，然后在当前文件中使用 `.. include::` 指令包含。