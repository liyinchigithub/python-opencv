# python-opencv


[![python](https://img.shields.io/badge/python-3.7-green.svg)](https://www.python.org/downloads/release/python-374/)
[![opencv](https://img.shields.io/badge/opencv-22.0.4-yellow.svg)](https://opencv.org/releases.html)


人脸识别并保存图片到本地


# 目录说明
* -src                    代码
* --package               顶包
* ---module               模块（package包下的模块）
* ----__init__.py         模块初始化
* -static                 截图保存图片路径
* -logging_init.py        logging 初始化(日志初始化配置，每次触发写入本地文件和控制台)
* -report                 allure生成json、html报告存放位置
* -pytest.ini             pytest单元测试框架配置文件
* -requirements.txt       依赖


# 安装opencv

>https://opencv.org/releases.html

人脸检测器（默认）：haarcascade_frontalface_default.xml

人脸检测器（快速Harr）：haarcascade_frontalface_alt2.xml

人脸检测器（侧视）：haarcascade_profileface.xml

眼部检测器（左眼）：haarcascade_lefteye_2splits.xml

眼部检测器（右眼）：haarcascade_righteye_2splits.xml

嘴部检测器：haarcascade_mcs_mouth.xml

鼻子检测器：haarcascade_mcs_nose.xml

身体检测器：haarcascade_fullbody.xml

人脸检测器（快速LBP）：lbpcascade_frontalface.xml



# 安装tesserocr

## 在Windows下

1.要先下载tesseract，它为tesserocr提供了支持；
tesseract下载地址：https://digi.bib.uni-mannheim.de/tesseract/
打开后，可以看到各种exe的列表，可以随便挑选;
其中文件名中带有dev的为开发版本，不带dev则为稳定版本，例如jb是下载 tesseract-ocr-setup-3.05.01.exe；
![image](https://user-images.githubusercontent.com/19643260/158842943-1826d2c3-9de5-41a6-a09d-2f3ec3b98841.png)

2.下载后双击，一路点击，直到出现下面这个页面
![image](https://user-images.githubusercontent.com/19643260/158842879-a62836ee-c470-4807-ad18-40359a642ab7.png)

这里需要勾选红框里的Additional language data(download)，这个选项是安装OCR识别支持的语言包，这样OCR就可以识别多国语言，然后再一路点击NEXT即可，因为要下载语言包，所以需要点时间，大概10-20分钟左右，跟网速有关，如果不需要支持多国语言的话，也可以不勾选，自由选择

3.打开后，直接搜索chi_sim.traineddata，这个代表的就是中文，下载下来;
然后找到刚刚tesseract安装目录，里面会有一个叫tessdata的目录，直接把刚下载的语言包放到这个目录下即可；

需要说明：默认包含英文字库

![image](https://user-images.githubusercontent.com/19643260/158843311-240aa80c-bbd6-4287-bbb0-604d04988801.png)

4.如何验证tesseract是否安装成功？直接cmd下输入tesseract即可；
成功会直接显示信息;

![image](https://user-images.githubusercontent.com/19643260/158843370-bcb44082-d70c-49bd-a426-41dbd25360e6.png)

5.如果提示'tesseract' 不是内部或外部命令，则是因为没有配置环境变量，手动把tesseract根目录配置到path参数下即可，这块不详细说明；

到此为止，tesseract安装成功啦~

接下来就安装tesserocr，直接pip命令即可：

```shell
pip3 install tesserocr
```

```shell
conda install -c simonflueckiger tesserocr
```
![image](https://user-images.githubusercontent.com/19643260/158843906-5734d77e-05d3-4146-abf3-8f1308f4f5fe.png)

如何验证是否真的安装了？很简单，直接import tesserocr，不报错就说明安装好了；

![image](https://user-images.githubusercontent.com/19643260/158843971-450d759d-e2c1-4561-9f25-9f1c127fa9d9.png)

如果有同学不知道conda这条命令的话，请访问下面的链接，直接搜索scrapy安装，会有介绍conda：
https://juejin.im/post/5afcb91251882565bd257097|

## mac

1.Mac下，首先使用Homebrew 安装ImageMagick 和tesseract库：
```shell
brew install imagemagick
brew install tesseract --language all
```
<img width="564" alt="image" src="https://user-images.githubusercontent.com/19643260/158923056-0eefc142-9c75-4d83-9400-c9e2ca6f0e76.png">

2.安装语言包
```shell
brew install tesseract-lang
```

3.接下来再安装tesserocr即可：
```shell
brew install tesserocr pillow
```

## linux CentOS、Red Hat 

```shell
yum install -y tesseract
yum install -y tesseract-lang
pip3 install tesserocr pillow
```

### Ubuntu、Debian、Deepin

1.安装相关工具
```shell
sudo apt-get install-y tesseract-ocr libtesseract-dev libleptioica-dev
```
2.安装tesserocr
```shell
pip3 install tesserocr pillow
```
3.安装tesseract语言包
```shell
sudo apt-get tesseract-lang
```

# python环境

## 更新pip

```python
pip install --upgrade pip
```

## 创建虚拟目录

```shell
# python -m venv 虚拟环境名称，名称是随意起的
python -m venv tutorial-env
```

## 激活虚拟环境

* 当激活虚拟环境时命令行上会有个虚拟环境名前缀

#### Unix或MacOS上激活虚拟环境
```shell
source tutorial-env/bin/activate
```
#### windows上激活虚拟环境
```shell
tutorial-env\Scripts\activate.bat
```

### 项目依赖安装
```shell
python3.7 -m pip install --upgrade pip
pip install -r requirements.txt
```

* 如果引入其他新的依赖，可以执行冻结第三方库，就是将所有第三方库及版本号保存到requirements.txt文本文件中
```shell
pip freeze > requirements.txt
```
* 如果pip不起作用，可以从pypi上下载最新的源码包(https://pypi.python.org/pypi/)进行安装：
```shell
python setup.py install 
```



## 运行指定用例脚本

```shell
python  
```

## 仅运行指定标志的用例
```shell
# 运行标注@pytest.mark.test的测试用例
pytest -m test
```
## 控制台详细输出

```shell
pytest -v
```

# OCR

OCR,全称叫 Optical Character Recognition，中文翻译叫光学字符识别，是指通过扫描字符，通过其形状将其翻译成电子文本的过程；
一个图形验证码，先使用OCR技术将其转化成电子文本，然后爬虫将识别的结果提交到服务器，便达到自动识别验证码的过程；

```python
import tesserocr
from PIL import Image # pillow
 
#新建Image对象
image = Image.open("3.jpg")
#调用tesserocr的image_to_text()方法，传入image对象完成识别
result = tesserocr.image_to_text(image)
print(result)
```


需要对图片进行额外的处理，如转灰度，二值化等操作；

转灰度处理： 利用Image对象的convert()方法参数传入L，即可将图片转成为灰度图像：

```shell
from PIL import Image # pillow
 
image = Image.open("1.jpg")
image = image.convert('L')
image.show()
```

![image](https://user-images.githubusercontent.com/19643260/158845141-5cde1c4e-2e11-4f71-b989-f96f0d6e34a8.png)

图片成功转灰了；此时我们再校验一下，发现校验还是MEEE，失败；

传入1的后，即可将图片进行二值化处理：

二值化是指将图像上的像素点的灰度值设置为0或255，也就是将整个图片呈现出明显的只有黑和百的视觉效果

```shell
import tesserocr
from PIL import Image
 
image = Image.open("1.jpg")
image = image.convert('1')
image.show()
```

二值化的阈值是可以指定的，上面的方法采用的是默认阈值127；但一般很少直接转换原图，原因如上可看到，错误的更加离谱了；

一般是先将原图转为灰度图像，然后再指定二值化的阈值，代码如下：

```shell

import tesserocr
from PIL import Image #PIL 就是pillow
 
#新建Image对象
image = Image.open("1.jpg")
#进行置灰处理
image = image.convert('L')
#这个是二值化阈值
threshold = 150   
table = []
 
for i in  range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
#通过表格转换成二进制图片，1的作用是白色，不然就全部黑色了
image = image.point(table,"1")
image.show()
result = tesserocr.image_to_text(image)
print(result
```

首先，是把图片置灰处理，灰度图像是一种具有从黑到白256级灰度色阶或等级的单色图像；
对于灰度图像利用阈值得到二值化的图像， 也就是说设定了一个阈值，从0到256，如果灰度图像少于阈值则设置0，大于阈值则设置1，0是黑色，1是白色，这样做，就可以把一个灰度图完全转换二值化图；

原图
![image](https://user-images.githubusercontent.com/19643260/158846047-f2e233bb-7c99-4cce-bab6-8ca4af473420.png)

灰度图
![image](https://user-images.githubusercontent.com/19643260/158846148-d8c17d82-d97c-4991-bcce-427bfdf3ba15.png)

二值图
![image](https://user-images.githubusercontent.com/19643260/158846192-5b360716-0b39-4915-88cf-c64047635ecb.png)


在灰度图上，部分色彩是介于白色跟黑色之间，所以通过设置阈值的方法，把这些中间色彩全部转换成黑色跟白色；

上面把验证码二值图后是长这样的：

![image](https://user-images.githubusercontent.com/19643260/158846279-8215c37f-5e0a-4c01-bbde-5d0dfe5316b7.png)

而校验结果：

![image](https://user-images.githubusercontent.com/19643260/158846338-ad09dc56-1988-4af9-b16e-2a8c2ca03143.png)


有所变化，至少不是MEEE了，那我们继续调，调到一个合适的值;
调了半天，放弃了，原因是这个8，不管怎么调都调不到一个合适的值，一直在S、R、B之间徘徊；

换了个验证码：
![image](https://user-images.githubusercontent.com/19643260/158846522-fcbf94d8-8787-4f97-a58d-21de2033ceca.png)

上面同样的代码，无修改，二值图如下
![image](https://user-images.githubusercontent.com/19643260/158846587-3e48f73c-1e64-45e6-9924-d00f49fbadfe.png)

校验结果：

TODO

实际发现，tesserocr仅能解决实心的验证码，对于空心的验证码，依然束手无策，那怎么办呢？
既然图像识别存在误差，那我们就放弃这条路，而是通过其他的方式来获取这个验证码；
比如直接找到生成这验证码的代码二次转化获取验证码，深度学习训练机器识别；

# 参考：

https://link.zhihu.com/?target=https%3A//blog.csdn.net/qq_42633819/article/details/81191308

https://blog.csdn.net/sinat_38682860/article/details/80636620

https://github.com/opencv/opencv



