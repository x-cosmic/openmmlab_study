# 目标检测任务实践
## 1、学习笔记

https://bbs.csdn.net/topics/615951096?spm=1001.2014.3001.6377

## 2、训练
训练过程

<img src="https://github.com/x-cosmic/openmmlab_study/blob/main/assignment04/pictures/trainval.png" width = "80%">

## 3、测试
测试结果

<img src="https://github.com/x-cosmic/openmmlab_study/blob/main/assignment04/pictures/test.png" width = "80%">

## 4、 预测
输出时自己重新设置了颜色显示方案：
```python
color_map = {
        0: (128, 128, 128),  # 背景
        1: (255, 0, 0),      # 西瓜红瓤
        2: (34,139,34),      # 西瓜外壳
        3: (144,238,144),    # 西瓜白皮
        4: (0, 0, 0),        # 西瓜黑籽
        5: (255, 255, 255),  # 西瓜白籽
    }
```
第一张图, 测试数据中的图

<img src="https://github.com/x-cosmic/openmmlab_study/blob/main/assignment04/pictures/Figure_1.png" width = "80%">


第二张图，New Bing 生成的图 生成的图光影和自然图有些不同

<img src="https://github.com/x-cosmic/openmmlab_study/blob/main/assignment04/pictures/Figure_2.png" width = "80%">



