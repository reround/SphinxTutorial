视频、音频
============

.. note::

    ``.. video::`` 标签没有 ``muted`` 就不能 ``autoplay`` ， 但是有 ``muted`` 就是静音。


视频
------

安装插件
~~~~~~~~~

.. code-block:: bash

    pip install sphinxcontrib-video


导入
~~~~~~~~~

.. code-block:: python

    extensions = [
        ...
        "sphinxcontrib.video",  # 视频支持
        ...
    ]

属性
~~~~~~~~~

.. csv-table:: Optional Attributes
    :header: Attribute, value, Description

    ``:alt:``,``str``,Specify the text to write when the video cannot be displayed
    ``:autoplay:``,,Specifies that the video will start playing as soon as it is ready
    ``:nocontrols:``,,Specifies that video controls should not be displayed (such as a play/pause button etc).
    ``:height:``,``int``,Sets the height of the video player in pixels (ignored if relative width is used)
    ``:loop:``,,Specifies that the video will start over again, every time it is finished
    ``:muted:``,,Specifies that the audio output of the video should be muted
    ``:poster:``,``str``, Specifies an image url to be shown while the video is downloading, or until the user hits the play button
    ``:preload:``,``str``,"Specifies if and how the author thinks the video should be loaded when the page loads. Can only be values from ``['auto', 'metadata', 'none']``"
    ``:width:``,``int``\ [``%``\ ], Sets the width of the video player in pixels or relative to the page's width if a percentage
    ``:class:``,``str``, Set extra class to the video html tag
    ``:playsinline:``,,Specifies that the video will play in-line (instead of full-screen) on small devices.


.. code-block:: rst

    .. video:: ../_static/video/video.mp4
        :playsinline:
        :nocontrols:
        :muted:
        :autoplay:
        :loop:
        :width: 100%

.. video:: ../_static/video/video.mp4
    :playsinline:
    :nocontrols:
    :muted:
    :autoplay:
    :loop:
    :width: 100%

    示例视频


音频
-----

.. warning::

    音频文件不能有 `:nocontrols:` 属性，否则不会播放。

    编译时会有警告，但不影响使用。

.. note:: 

    推荐宽度 800px，高度 40px。


.. code-block:: rst

    可以使用
        :width: 800
        :height: 40
    自定义宽高。

    .. video:: ../_static/video/xx.wav
        :playsinline:
        :autoplay:
        :loop:
        :width: 800
        :height: 40


.. video:: ../_static/video/xx.wav
    :playsinline:
    :autoplay:
    :loop:
    :width: 800
    :height: 40

    示例音频
