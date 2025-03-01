.. _topics-05_use_display_code_mark:

========
显示代码
========

.. note:: 我们可以在配置文件指定highlight_langeuage="c,python"

使用codeblock
=============

.. code-block:: c

    #include<stdio.h>
    int main()
    {
        printf("%s\n","aaaa");
        return 0;
    }

.. rubric:: rst 语法

.. code-block:: rst

    .. code-block:: c

        #include<stdio.h>
        int main()
        {
            printf("%s\n","aaaa");
            return 0;
        }


显示行号
========

.. code-block:: c
    :linenos:

    #include<stdio.h>
    int main()
    {
        printf("%s\n","aaaa");
        return 0;
    }

.. rubric:: rst 语法
    
.. code-block:: rst

    .. code-block:: c
        :linenos:

        #include<stdio.h>
        int main()
        {
            printf("%s\n","aaaa");
            return 0;
        }

突出特定行
==========

.. code-block:: python
   :emphasize-lines: 3,5

   def some_function():
       interesting = False
       print 'This line is highlighted.'
       print 'This one is not...'
       print '...but this one is.'

.. rubric:: rst 语法

.. code-block:: rst
    
    .. code-block:: python
    :emphasize-lines: 3,5

    def some_function():
        interesting = False
        print 'This line is highlighted.'
        print 'This one is not...'
        print '...but this one is.'


引用一个文件
============

.. literalinclude:: test.py
   :encoding: utf-8
   :language: python
   :emphasize-lines: 1,3-5
   :linenos:
   :lines: 1-5,9-

.. rubric:: rst 语法

.. code-block:: rst

    .. literalinclude:: test.py
    :encoding: utf-8
    :language: python
    :emphasize-lines: 1,3-5
    :linenos:
    :lines: 1-5,9-

diff2个文件
===========

.. literalinclude:: test.py
   :diff: test2.py

.. rubric:: rst 语法

.. code-block:: rst

    .. literalinclude:: test.py
    :diff: test2.py