<h1>信息检索实验1 -- 爬虫入门</h1>
<h2>目录结构</h2>
**1.**

​	主函数是spider.py，爬取了https://www.zhihu.com/question/412799877/answer/1523203315页面的文字和图片信息。

**2.**

​	save_svg.py是被调函数，用来下载保存svg图像，可选择保存为PNG格式。

**3.**

​	svg2png.py展示了如何利用cairosvg库，将svg图像转化为png图像。

**4.**

​	由于windows下的cairosvg需要的dll库有一些未解决的小问题，所以在根目录下列出了spider.py脚本用到的dll库。其余在https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer中下载安装后的bin目录中。（已有的dll库也来自bin目录下）

**5.**

​	为查看方便，将`./img`和`./text`分别设为存放图像和文字的文件夹。



<h2>运行结果</h2>

- 在Spyder中运行后应如下图所示

![1603271327201](E:\IRlabs\spider01-v2\effect.png)

- img和text文件夹已经包含运行后结果



时间: 2020.10.21