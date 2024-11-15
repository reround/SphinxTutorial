用 Doxygen、Sphinx 与 Breathe 创建文档
=======================================

Breathe
--------
.. code-block:: bash

    pip install breathe


`Sphinx` 与 `Breathe`
------------------------

`Sphinx` 目前的『市场』占有率非常高，因为它有免费的文档托管 `Read the Docs` ，支持线上预览以及版本历史等，由此大多数的 `Python` 文档都是选择它来生成文档的。

对的，你没听错，一开始它确实是为了 `Python` 文档而出现的，后来也逐渐支持其它语言，包括 `C/C++` ，只是， `Doxygen` 与 `Sphinx` 不能直接关联，即 `Sphinx` 不能直接使用 `Doxygen` 生成的内容来生成 `Sphinx` 文档，它还需要一个插件来做适配，Breathe 就是为了连接 `Doxygen` 与 `Sphinx` 而生。

`Sphinx` 默认的解析文档是 `reStructureText`，你可以认为是高级版本的 `Markdown` ，也就是比它功能更强大。当然，你也可以使用 `Markdown` 来写文档，它有一个专门的插件来做这件事。


#. 将 `Doxygen` 中的 `GENERATE_XML` 设置为 `YES` ，生成 `xml` 文件 ；
#. 确保 `Breathe` 在 `Python path` 内；
#. 不在的话，需要在 `conf.py` 内加上 `sys.path.append("/path/to/breathe/")` ；
#. 配置 `conf.py` 文件：

    #. 为 `extensions` 添加 `breathe` ；
    #. 设置 `breathe_projects = {"myproject": "/path/to/doxygen/xml"}` ；
    #. 设置 `breathe_default_project = "myproject"` ；

#. 翻阅 breathe 的 quickstart 文档，我们可以看到有下面命令可以使用，在 `rst` 文件中使用 `doxygen` 指令：

    .. code-block:: rst

        .. doxygenfile::      文件
        .. doxygenindex::     索引
        .. doxygenfunction::  函数
        .. doxygenstruct::    结构体
        .. doxygenenum::      枚举类型
        .. doxygentypedef::   typedef 类型定义
        .. doxygenclass::     类


-----

以下未验证：
==============

CMake 配置
------------

终于来到了 `CMake` 环节，我们该如何把上述的复杂步骤结合起来？

`CMake` 提供了很简单的 `doxygen_add_docs` ，通过简单配置，你就能生成 `Doxygen` 文档：

.. code-block:: cmake
        
    find_package(Doxygen REQUIRED)

    # 这里只是举例，其它 Doxygen 配置加上 `DOXYGEN_` 前缀即可
    set(DOXYGEN_GENERATE_HTML YES)
    set(DOXYGEN_EXTRACT_ALL YES)
    set(DOXYGEN_BUILTIN_STL_SUPPORT YES)

    doxygen_add_docs(doxygen_docs "${PROJECT_SOURCE_DIR}/src")

那么 `Sphinx` 呢？我找到一个现成可以用的： `cmake-sphinx` ，但是需要修改一部分，大体上这里的功能可以完全满足我们的使用。

.. code-block:: cmake

    # 别忘了生成 XML，同时可以去掉上面的 DOXYGEN_GENERATE_HTML
    set(DOXYGEN_GENERATE_XML YES) 

    find_package(Sphinx REQUIRED COMPONENTS breathe)
    set(SPHINX_VERSION ${PROJECT_VERSION})
    set(SPHINX_LANGUAGE zh_CN)
    sphinx_add_docs(
    docs
    BREATHE_PROJECTS
    doxygen_docs
    BUILDER
    html
    SOURCE_DIRECTORY
    .)

然后，在编译目录下，打开 `docs/docs/index.html` 就能看到美观的文档了。

Ref
Clear, Functional C++ Documentation with Sphinx + Breathe + Doxygen + CMake
首发于 Github issues: https://github.com/xizhibei/blog/issues/139 ，欢迎 Star 以及 Watch
