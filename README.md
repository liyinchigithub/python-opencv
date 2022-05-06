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
python  main.py
```



# 参考：

https://github.com/opencv/opencv





