Doxygen
==========

为其他编程语言生成文档的工具。

Doxygen 安装
--------------

.. code-block:: bash

    Ubuntu: sudo apt install doxygen
    msys2:  pacman -S mingw-w64-x86_64-doxygen

生成配置文件
-------------

运行 `doxygen -g Doxyfile` 来生成配置；

.. code-block:: bash

    doxygen -g Doxyfile

使用 `doxygen Doxyfile` 执行配置文件，生成文档

.. code-block:: bash

    doxygen Doxyfile

Doxyfile 配置注解
-------------------

一般要手动指定的配置项：

.. code-block:: bash

    PROJECT_NAME        = "My Project"
    INPUT               = src include
    OUTPUT_DIRECTORY    = "docs"
    RECURSIVE           = YES

常用部分示例：

.. code-block:: bash

    # 项目名称
    PROJECT_NAME           = "My Project"
    # 项目版本
    PROJECT_NUMBER         = "1.0"
    # 输出目录
    OUTPUT_DIRECTORY       = "docs"
    # 需要生成的文件和目录
    INPUT                  = src include
    # 希望排除某些子目录（例如测试目录）
    EXCLUDE_PATTERNS      = */tests/*
    # 递归搜索需要生成的目录
    RECURSIVE              = YES
    # 生成HTML文档
    GENERATE_HTML          = YES
    # 生成LaTeX文档，用于打印
    GENERATE_LATEX         = YES
    # 生成XML文件
    GENERATE_XML           = YES
    # 生成PDF文档（需要配置LaTeX）
    GENERATE_RTF           = NO
    # 解析注释中的\file命令
    EXTRACT_ALL            = YES
    # 解析文件中的注释
    EXTRACT_PRIVATE        = YES
    # 解析类中的注释
    EXTRACT_STATIC         = YES
    # 包含简短描述
    SHOW_INCLUDE_FILES     = YES
    # 包含目录结构
    SHOW_GROUPED_MEMB_INC  = YES
    # 显示复杂的继承关系图
    HAVE_DOT               = YES
    #  DIA_PATH               = "/usr/bin/" # 指定了 Graphviz 工具的 dot 程序的路径
    GENERATE_TREEVIEW      = YES
    # 使用HTML的帮助服务器框架
    USE_HTAGS              = YES
    # 设置HTML文档的标题
    HTML_TITLE             = "My Project Documentation"
    # 设置HTML文档的脚注
    FOOTER                  = "Copyright © My Company"
    # 设置HTML文档的字体大小
    HTML_FONTSIZE          = +2
    # 包含源代码文件
    SHOW_FILES             = YES
    # 显示每个文件的最后修改日期
    SHOW_LAST_MODIFIED_BY   = YES
    # 显示每个文件的 CVS/SVN/... 版本信息
    SHOW_USE_FILES         = YES
    # 警告如果未文档化的成员超过一定比例
    WARN_IF_UNDOCUMENTED   = YES
    # 警告如果文档覆盖率低于一定比例
    WARN_DOC_ERROR          = YES

常用的指令
-----------

官网示例：

.. code-block:: c

    /*! \fn int open(const char *pathname,int flags)
        \brief Opens a file descriptor.
    
        \param pathname The name of the descriptor.
        \param flags Opening flags.
    */

常用的指令：

.. note:: 

    使用 `'\\'` 和 `'@'` 都可以，建议使用 `'@'` ，因为 `'\\'` 可能会和转义字符冲突。

.. code-block:: c

   /**
    *
    * @file 档案的批注说明
    * @author 作者的信息
    * @see 参考项
    * @brief 求和
    * @param 参数说明
    * @date 日期
    * @version 版本号
    * @note 注解，可以是详细的注解
    * @remarks 备注事项（remaks）
    * @attention 注意事项(attention)
    * @warning 警告信息
    * @return 后面接函数传回值的说明
    * @retval 传回值说明主要用于函式说明中
    * @bug 缺陷描述
    * @todo 待办事项
    *
    */

