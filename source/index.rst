.. Notes documentation master file, created by
   sphinx-quickstart on Mon Oct 14 14:22:53 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. _topics-index:

Sphinx Tutorial
================

.. rubric:: myst 和 rst 的对比

::
   
   myst

      tab-set 支持
      支持 {code-cell} , 但是没成功

   rst

      有序列表自增
      属性提示
      扩展语法，如 plot, 和一些扩展属性，如 video.autoplay

      rst 也支持 `.. margin::`， 只不过会语法报错（sphinx_book_theme）

.. note:: 
   
   “基础语法”、“中级语法”、“Sphinx标记结构”三节来自 `rst-tutorial-elinpf <https://rst-tutorial-elinpf.readthedocs.io/en/latest/>`_


.. note:: 
   
   PDF 输出的样式会和 HTML 输出的样式会有差别。

.. toctree::
   :maxdepth: 1
   :caption: 目录:
   :numbered:


   install
   themes
   myst_parser/index
   base/index
   advance/index
   mark/index
   extend/index
   sphinx_advance/index



