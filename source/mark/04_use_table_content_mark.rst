.. _topics-04_use_table_content_mark:

==========
表内容标记
==========

.. glossary::

   environment
      A structure where information about all documents under the root is
      saved, and used for cross-referencing.  The environment is pickled
      after the parsing stage, so that successive runs only need to read
      and parse new and changed documents.

   source directory
      The directory which, including its subdirectories, contains all
      source files for one Sphinx project.

.. rubric:: rst 语法

.. code-block:: rst

   .. glossary::

      environment
         A structure where information about all documents under the root is
         saved, and used for cross-referencing.  The environment is pickled
         after the parsing stage, so that successive runs only need to read
         and parse new and changed documents.

      source directory
         The directory which, including its subdirectories, contains all
         source files for one Sphinx project.


.. glossary::

   term 1
   term 2
      Definition of both terms.

.. rubric:: rst 语法

.. code-block:: rst

   .. glossary::

      term 1
      term 2
         Definition of both terms.


.. productionlist::
   try_stmt: try1_stmt | try2_stmt
   try1_stmt: "try" ":" `suite`
            : ("except" [`expression` ["," `target`]] ":" `suite`)+
            : ["else" ":" `suite`]
            : ["finally" ":" `suite`]
   try2_stmt: "try" ":" `suite`
            : "finally" ":" `suite`

.. rubric:: rst 语法

.. code-block:: rst
      
   .. productionlist::
      try_stmt: try1_stmt | try2_stmt
      try1_stmt: "try" ":" `suite`
               : ("except" [`expression` ["," `target`]] ":" `suite`)+
               : ["else" ":" `suite`]
               : ["finally" ":" `suite`]
      try2_stmt: "try" ":" `suite`
               : "finally" ":" `suite`

