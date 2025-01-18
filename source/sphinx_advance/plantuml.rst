plantuml 绘图
==============

plantuml安装
------------

jar 包下载
~~~~~~~~~~~~~

摘录：https://bitcat.love/2020/04/18/drawing-graph-with-graphviz-and-plantuml/

PlantUML 是一个开源项目，相比于 Graphviz，它拥有更丰富的绘图功能，而且可以兼容 dot 语法，可以说 Graphviz 是 PlantUML 的一个子集。 且它的绝大部分文档都已经翻译成中文， `官方文档 <https://plantuml.com/zh/>`_ 示例丰富，上手更加容易。

离线版： `/source/_static/docs/` 文件夹中 `离线版 <../_static/docs/PlantUML_Language_Reference_Guide_zh.pdf>`_ 。

PlantUML 并不是一个可执行程序，它是一个 jar 包，需要依赖 JRE (java 运行时环境)。因此它需要使用命令行进行绘图。 同样，它支持命令行参数，例如：指定图片输出格式、输出目录等。下面的命令将会绘制一张 SVG 格式的图片：

.. code-block:: bash

    java -jar /path/to/plantuml.jar file1.puml -TSvg -charset UTF-8

更多的命令行参数可以参考官方的文档 `-Use command line <https://plantuml.com/zh/command-line>`_ 。

    如果想使用 PlantUML 来绘制 dot，需要先安装 Graphviz。

java环境
~~~~~~~~~

首先需要安装java环境，并配置环境变量。

镜像 ： https://repo.huaweicloud.com/java/jdk/

环境变量:

.. code-block:: text

    新建变量名：JAVA_HOME
    变量值：/path/to/jdk

    path环境变量添加：
        %JAVA_HOME%\bin
        %JAVA_HOME%\jre\bin

    新建变量名：ClassPath
    变量值：.;%JAVA_HOME%\lib\dt.jar;%JAVA_HOME%\lib\tools.jar; 

插件安装
~~~~~~~~~

.. code-block:: bash

    pip install sphinxcontrib-plantuml 

配置 Sphinx: 在你的 Sphinx 项目的 conf.py 文件中，你需要添加 'sphinxcontrib.plantuml' 到 extensions 列表中，以启用此插件。

.. code-block:: python
        
    extensions = [
        # 其他已有的扩展...
        'sphinxcontrib.plantuml',
    ]
    
    plantuml_output_format = 'svg'  # 可选，控制输出图片格式
    plantuml = 'java -jar /path/to/plantuml.jar'  # 可选，指定 plantuml.jar 路径

主题
------

可用主题列表
下述网址列出了PlantUML库中的可用主题：

- `PlantUML所有官方主题 <https://the-lum.github.io/puml-themes-gallery>`_
- 在 `the Theme Gallery <https://bschwarz.github.io/puml-themes/gallery.html>`_ 上由 `Brett Schwarz <https://github.com/bschwarz/puml-themes>`_ 制作的一些 `Pluml主题例子 <https://bschwarz.github.io/puml-themes>`_

当然, 你可以用如下命令列出当前plantuml库的自带主题

.. code-block:: rst

    .. plantuml:: 
    
        @startuml
        help themes
        @enduml

.. plantuml:: 

    @startuml
    help themes
    @enduml


一些主题包含某些用以帮助为消息着色的程序，例如：

.. plantuml:: 

    @startuml
    !theme spacelab
    Bob -> Alice :  hello
    Bob <- Alice :  $success("success: hello B.")
    Bob -x Alice :  $failure("failure")
    Bob ->> Alice : $warning("warning")
    @enduml


本地主题
~~~~~~~~~

您可以在本地文件系统上创建自己的主题。您可以在 `duplicate any existing theme <https://github.com/plantuml/plantuml/tree/master/themes>`_ 上面创建一个属于你自己的主题.

默认情况下，主题文件名为 `puml theme foo.puml` 其中 `foo` 是主题的名称。

要调用本地主题，必须使用以下指令：

.. code-block:: rst

    .. plantuml:: 
    
        @startuml
        !theme foo from /path/to/themes/folder
        @enduml

来自互联网的主题
~~~~~~~~~~~~~~~~~~

其他资源库也可以为PlantUML发布主题。

主题文件必须遵循相同的惯例： `puml-theme-foo.puml` 其中 `foo` 是主题的名称。

要使用来自远程资源库的主题，你必须使用以下指令。

.. code-block:: rst

    .. plantuml:: 
    
        @startuml
        !theme amiga from https://raw.githubusercontent.com/plantuml/plantuml/master/themes
        @enduml

plantuml 语法示例，及一些主题示例
====================================
     
.. plantuml:: 

    @startuml
    !theme sunlust
    actor Bob #red
    participant L #99FF99
    @enduml

一些主题包含某些用以帮助为消息着色的程序，例如：

.. plantuml:: 

    @startuml
    !theme amiga
    Bob -> Alice :  hello
    Bob <- Alice :  ("success: hello B.")
    Bob -x Alice :  ("failure")
    Bob ->> Alice : ("warning")
    @enduml


.. plantuml:: 

    @startuml
    !theme sketchy
    actor User as user
    participant "Web Browser互联网" as browser
    participant "Web Server" as server

    user -> browser : accesses
    browser -> server : requests
    server --> browser : responds
    browser --> user : displays
    @enduml

.. plantuml:: 
        
    @startuml
    !theme plain
    Class01 <|-- Class02
    Class03 *-- Class04
    Class05 o-- Class06
    Class07 .. Class08
    Class09 -- Class10
    @enduml

.. plantuml:: 
        
    @startsalt
    !theme reddress-lightorange
    {+
    Login | "MyName "
    Password | "**** "
    [Cancel] | [ OK ]
    }
    @endsalt

.. plantuml:: 
        
    @startuml
    !theme cerulean
    title Point two queries to same activity\nwith `goto`
    start
    if (Test Question?) then (yes)
    'space label only for alignment
    label sp_lab0
    label sp_lab1
    'real label
    label lab
    :shared;
    else (no)
    if (Second Test Question?) then (yes)
    label sp_lab2
    goto sp_lab1
    else
    :nonShared;
    endif
    endif
    :merge;
    @enduml


.. plantuml:: 
        
    @startuml
    !theme cloudscape-design
    object Object01
    object Object02
    object Object03
    object Object04
    object Object05
    object Object06
    object Object07
    object Object08
    Object01 <|-- Object02
    Object03 *-- Object04
    Object05 o-- "4" Object06
    Object07 .. Object08 : some labels
    @enduml