## HyperLPR Python

### 介绍

一个简单的中文车牌识别Python实现。

### 前言

之前有个HyperLPR的C++项目，其识别效果并不是很好，编译存在一定困难。在结合了一些近年来OCR、场景文字检测论文等论文，使用Python简单的实现了一下。

### 特性

+ 单张720p 识别时间在单核Intel 2.2G CPU(MBP2015 15inch)不低于 140ms。比EasyPR单核识别速度快近10倍左右的时间。
+ 识别率在EasyPR数据集上0-error达到70.2% 1-error识别率达到 89.6%
+ 单线程平均检测时间在EasyPR数据集在保持在160ms以下。基于adaboost检测方法在实时性、召回率、准确率上都不逊于MSER方法。检测recall和easyPR持平。
+ 代码框架简单，总代码不到1k行。

### 缺点

+ 代码较为简单，存在BUG
+ 在大角度下（大于-+15度）下不能取得良好的定位效果，后续会有解决方案。
+ 目前仅能识别标准蓝牌

### 注意事项

本项目仅仅用于研究和测试，请勿用于商业



### 依赖

+ Keras + Theano backend (Tensorflow data order)
+ Theano
+ Numpy
+ Scipy
+ OpenCV
+ scikit-image


### 模型
由于涉及到商业用途，目前开源的检测模型存在一定数量的误检，可通过级联判断模型来减少误检。



### 识别样张

![1](/res/2.png)

![1](/res/1.png)

![3](/res/3.png)

![5](/res/5.png)

![6](/res/6.png)

![8](/res/8.png)

![7](/res/7.png)

![10](/res/10.png)



### 识别样张

##### Anthor

+ Jack Yu

