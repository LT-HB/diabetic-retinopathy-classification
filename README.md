# 视网膜病变图像分类

## 前言
* 数据集
```
├── datasets: 所有训练以及测试图像文件夹
     ├──Retinopathy_grade_0: 
     ├──Retinopathy_grade_1: 
     ├──Retinopathy_grade_2:
     └──Retinopathy_grade_3:
```
* 使用txt_annotation.py生成图片的标签和路径
* 图像处理后的数据可以根据 图片预处理.ipynb 获取，HOG处理使用了skimage
* 深度学习的训练权重以及用于分类算法的特征提取权重，以及经过均衡化后的剪裁的原始
  图片，对比度拉伸图片，高斯模糊图片 链接：https://pan.baidu.com/s/11Va0YdixrJ4d3tJ6XbI9_A 
  提取码：lt66 
