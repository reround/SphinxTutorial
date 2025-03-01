.. _topics-06_use_others:

========
其他标记
========

字段标记
========

:fieldname: name
:fieldname: age
:fieldanme: getAge()

.. rubric:: rst 语法

.. code-block:: rst

  :fieldname: name
  :fieldname: age
  :fieldanme: getAge()

csv表格
========

.. csv-table:: Frozen Delights!
   :header: "Treat", "Quantity", "Description"
   :widths: 15, 10, 30

   "Albatross", 2.99, "On a stick!"
   "Crunchy Frog", 1.49, "If we took the bones out, it wouldn't be
   crunchy, now would it?"
   "Gannet Ripple", 1.99, "On a stick!"

.. rubric:: rst 语法

.. code-block:: rst

  .. csv-table:: Frozen Delights!
    :header: "Treat", "Quantity", "Description"
    :widths: 15, 10, 30

    "Albatross", 2.99, "On a stick!"
    "Crunchy Frog", 1.49, "If we took the bones out, it wouldn't be
    crunchy, now would it?"
    "Gannet Ripple", 1.99, "On a stick!"


csv表格引用一个csv文件的
=========================

.. csv-table:: Frozen Delights!
   :header: "Treat", "Quantity", "Description"
   :widths: 15, 10, 30
   :file: test.csv
   :encoding: utf-8
   :align: left

.. rubric:: rst 语法

.. code-block:: rst

  .. csv-table:: Frozen Delights!
    :header: "Treat", "Quantity", "Description"
    :widths: 15, 10, 30
    :file: test.csv
    :encoding: utf-8
    :align: left
    
.. note:: 如果引用一个互联网的csv文件，使用url替换file即可


listtable表格
===============

.. list-table:: Frozen Delights!
   :widths: 15 10 30
   :header-rows: 1

   * - Treat
     - Quantity
     - Description
   * - Albatross
     - 2.99
     - On a stick!
   * - Crunchy Frog
     - 1.49
     - If we took the bones out, it wouldn't be
       crunchy, now would it?
   * - Gannet Ripple
     - 1.99
     - On a stick!

.. rubric:: rst 语法

.. code-block:: rst

  .. list-table:: Frozen Delights!
    :widths: 15 10 30
    :header-rows: 1

    * - Treat
      - Quantity
      - Description
    * - Albatross
      - 2.99
      - On a stick!
    * - Crunchy Frog
      - 1.49
      - If we took the bones out, it wouldn't be
        crunchy, now would it?
    * - Gannet Ripple
      - 1.99
      - On a stick!
      