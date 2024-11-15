graphviz 绘图
===============

安装 graphviz
---------------

.. code-block:: bash

    # Ubuntu
    sudo apt-get install graphviz
    # msys2
    pacman -S mingw-w64-x86_64-graphviz

安装完成后, 在命令行中输入 `dot -V` 来验证是否安装成功.

修改项目配置文件
------------------

修改项目配置文件 conf.py , 在其中开启 graphviz 插件并设置一些相关的参数:

.. code-block:: python

    # 通过配置开启graphviz插件
    extensions = ['sphinx.ext.graphviz']

    # 设置graphviz_dot路径
    graphviz_dot = 'dot'
    # 设置graphviz_dot_args的参数, 这里设置了默认字体支持中文
    graphviz_dot_args = ["-Gfontname=SimHei", "-Nfontname=SimHei", "-Efontname=SimHei"]
    # 输出格式, 默认png，这里使用svg矢量图
    graphviz_output_format = 'svg'

    # -Gfontname=Georgia：这个参数设置了整个图形（包括节点和边）的默认字体为Georgia。这意味着，除非你为节点或边指定了不同的字体，否则它们都将使用Georgia字体。
    # -Nfontname=Georgia：这个参数专门设置了节点（Node）的字体为Georgia。
    # -Efontname=Georgia：这个参数专门设置了边（Edge）的字体为Georgia。

这里 `graphviz_dot` 的值是 `dot` , 为了不把绝对路径写到配置文件中, 防止其他人的路径不一样, 所以这里要求 `dot` 这个程序在环境变量中, 能够直接使用.

画图
在 Sphinx 文档中使用 `.. graphviz::` 段来插入图片, 可以在文档中直接使用 dot 语言或者使用 dot文档.

Example:

.. code-block:: rst

    .. graphviz::

        digraph abc{
            a;
            b;
            c;
            d;

            a -> b;
            b -> d;
            c -> d;
        }

或者使用一个dot文档:

.. code-block:: rst

    .. graphviz::external.dot



graphviz 语法
===============

.. graphviz:: 

    digraph G{
    rankdir = LR
    {rank="same"; B; C; E} 
    {rank="same"; A; AF; F} 

    S1 [shape=point ]
    A [shape=box]
    B [shape=point ]
    C [shape=point ]
    AF [shape=point  label="F to A"]
    D [shape=box]
    E [shape=box]
    S2 [shape=point ]

    S1 -> A [style=dashed]
    A -> B [dir=none]
    B -> D 
    B -> C [dir=none]
    C -> E

    F -> E [dir=back]
    A -> AF [dir=back style=dashed]
    AF -> F [dir=none style=dashed]
    S2 -> F [dir=back style=dashed]
    }


.. graphviz:: 

    digraph G {
        A -> B;
        B -> C;
        C -> D;
        D -> A;
    }

.. graphviz:: 

    graph FF{
        rankdir=LR;
        size=4
        node[shape=record style=filled]
        vscode--{IDE 编程效率 外观}
        IDE--Julia
        编程效率--{Codeium Codelf}
        外观--{主题 background Power_Mode[label="Power Mode"]}
        主题--{颜色主题 图标主题}
        title[shape=egg label="VS Code插件" style=wedged]
    }

.. graphviz:: 

    digraph G {
        splines=polyline;
        nodesep=.05;
        rankdir=LR;
        node [shape=record,width=.1,height=.1];

        node0 [label = "<f0> |<f1> |<f2> |<f3> |<f4> |<f5> |<f6> | ",height=2.5];
        node [width = 1.5];
        node1 [label = "{<n> n14 | 719 |<p> }"];
        node2 [label = "{<n> a1 | 805 |<p> }"];
        node3 [label = "{<n> i9 | 718 |<p> }"];
        node4 [label = "{<n> e5 | 989 |<p> }"];
        node5 [label = "{<n> t20 | 959 |<p> }"] ;
        node6 [label = "{<n> o15 | 794 |<p> }"] ;
        node7 [label = "{<n> s19 | 659 |<p> }"] ;

        node0:f0 -> node1:n;
        node0:f1 -> node2:n;
        node0:f2 -> node3:n;
        node0:f5 -> node4:n;
        node0:f6 -> node5:n;
        node2:p -> node6:n;
        node4:p -> node7:n;
    }


.. graphviz:: 
    
    digraph CentralPmr {  
        fontname="Helvetica";
        shape=box;
        node[shape=box];
        graph [splines=ortho]

        sg  [label="TTD storage group for\nthe logged values"]
        vc  [label="Value catalogue"]
        tc1 [label="Time catalogoue (1)"]
        tc2 [label="Time catalogoue (2)"]
        sv_ [shape=point,width=0.01,height=0.01];
        sv  [label=""]
        ie  [shape=none, label="Initiating event"]
        c1  [shape=none, label="The set of values, defined\nby the value catalogue, which\nare freezed out of the TTD\nstorage group of the actual log."]
        c2  [shape=none, label="Time catalogue defining\nat what time around the\ninitiating event values\nshould be collected."]
        sgf [shape=record, label="{<f0> 1|2|3|4|..}|{ | | | | }"]

        sg  -> sv_ [penwidth=4, dir=none];
        sv_ -> sv -> tc2 [penwidth=4]
        sv  -> sgf:f0 [penwidth=4]
        {vc, tc1}  -> sg
        c1  -> sv [style=dashed, arrowhead="open"];

        {rank=min;  ie} 
        {rank=same; sg c1}
        {rank=same; vc sgf}
        {rank=max;  rc2}
    }

.. graphviz:: 

    digraph CentralPmr {  
        fontname="Helvetica";
        shape=box;
        node[shape=box];
        // graph [splines=ortho]

        sg [label="TTD storage group for\nthe logged values", width = 2.5]
        sv [label="", width = 2]
        ie [ shape=none, label="Initiating event", fontsize = 18 ]
        c1 [ shape=none, label="The set of values, defined\nby the value catalogue, which\nare freezed out of the TTD\nstorage group of the actual log." ]

        sgf[shape=box, margin=0, label=<
        <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4">
            <TR>
                <TD BORDER="0" COLSPAN="2">TTD storage group for<BR/>PMR freezed values</TD>
            </TR>
            <TR>
                <TD PORT="f1">1</TD>
                <TD BORDER="0" ROWSPAN="6">The set of<BR/>values is<BR/>stored in<BR/>the TTD<BR/>storage<BR/>group</TD>
            </TR>
            <TR>
                <TD>2</TD>
            </TR>
                    <TR>
                <TD>3</TD>
            </TR>
                    <TR>
                <TD>4</TD>
            </TR>
                    <TR>
                <TD>-</TD>
            </TR>
            <TR>
                <TD>-</TD>
            </TR>
            <TR>
                <TD BORDER="0" COLSPAN="2">Up to nine freezing areas<BR/>for defined central PMR</TD>
            </TR>
        </TABLE>>]; 

        TTD [shape=none, margin=0, label=<
        <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="12">
            <TR>
                <TD PORT="f1">Value catalogue</TD>
            </TR>
            <TR>
                <TD BORDER="0"></TD>
            </TR>
            <TR>
                <TD PORT="f2">Time catalogue (1)</TD>
            </TR>
            <TR>
                <TD BORDER="0">Time catalogue defining<BR/>at what time around the<BR/>initiating event values<BR/>should be collected</TD>
            </TR>
            <TR>
                <TD PORT="f3">Time catalogue (2)</TD>
            </TR>
        </TABLE>>]; 


        connector_1[ shape = point height = 0 width = 0 margin = 0 ]
        ie -> connector_1[ style = dotted, arrowhead = none ];
        { rank = same; connector_1 c1 }
        connector_1 -> c1[ style = invis, minlen = 4 ];
        c1 -> sv[ style = dashed, arrowhead = open ];
        connector_2[ shape = point height = 0 width = 0 margin = 0 ]
        connector_1 -> connector_2[ style = dotted ];
        { rank = same; sg connector_2 sv }
        sg -> connector_2[ minlen = 3, penwidth = 4, arrowhead = none ];
        connector_2 -> sv[ minlen = 3, penwidth = 4 ];

        sg:sw -> TTD:f1:nw[ weight = 5 ];
        sg:w -> TTD:f2:w;
        sv:sw -> TTD:f3:e[ penwidth = 4 ];
        sv:sw -> sgf:f1:w[ penwidth = 4 ];

        node[ shape = plaintext ];
        leg2[ label = "Data flow" ];
        leg4[ label = "Reference" ];
        leg6[ label = "Comment" ];

        node [ shape = point height = 0 width = 0 margin = 0 ];
        leg1 leg3 leg5

        TTD:sw -> leg1[ style = invis ];

        { rank = same; leg1 leg2 leg3 leg4 leg5 leg6 }
        edge[ minlen = 2 ];
        leg1 -> leg2[ penwidth = 4 ];
        leg3 -> leg4[ style = dotted ];
        leg5 -> leg6[ style = dashed, arrowhead = open ];
    }


.. graphviz::
    :caption: ccc
    :name: sss
    :align: center

    digraph CentralPmr {  
        rankdir=LR; // 设置图的方向为从左到右
        start_port [ shape = point height = 0 width = 0 margin = 0 ];
        coupler [shape = box label = "耦合器"];
        BPD [shape = box label = "平衡探测器"];
        loop_filter [shape = box label = "环形滤波器" ];
        local_laser [shape = box label = "本振激光器"];
        port_1 [shape = point height = 0 width = 0 margin = 0 ];
        port_2 [shape = point height = 0 width = 0 margin = 0 ];

        {rank="same"; BPD; loop_filter} 
        {rank="same"; coupler; local_laser}

        start_port -> coupler[style=dashed label=<&phi;<sub>ML</sub>>];
        coupler -> BPD[style=dashed];
        BPD -> loop_filter [label="拍频信号"];
        BPD -> port_2 [label="拍频信号"];
        local_laser -> loop_filter [dir=back];
        coupler -> local_laser [dir=back style=dashed  label=<&phi;<sub>LO</sub>>];
        port_1 -> local_laser [dir=back label="本振光" style=dashed];
    }
