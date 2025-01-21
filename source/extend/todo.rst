
待办事项 todo
===============

添加扩展
--------

.. code:: python

    extensions = [
        "sphinx.ext.todo",
    ]

    todo_include_todos = True


`.. todo::` 指令会创建一个待办事项。

`.. todolist::` 指令会列出当前文档中所有待办事项。

示例
-----

.. todo:: 这是第一项待办事项。

.. todo:: 这是第二项待办事项。


下面是所有待办事项的列表：

.. todolist:: 


.. rubric:: rst 语法

.. code-block:: rst

    .. todo:: 这是第一项待办事项。

    .. todo:: 这是第二项待办事项。


    下面是所有待办事项的列表：

    .. todolist:: 

