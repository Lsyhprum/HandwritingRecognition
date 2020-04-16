# gnt 处理

[CASIA Online and Offline Chinese Handwriting Databases](http://www.nlpr.ia.ac.cn/databases/handwriting/Offline_database.html)

[CASIA-HWDB脱机手写汉字数据集以及申请表下载](https://www.jianshu.com/p/980e2528e8fe)

[TensorFlow与中文手写汉字识别](https://blog.csdn.net/czq7511/article/details/72725635/)

# 训练

Expected more than 1 value per channel when training, got input size torch.Size([1, 300])

模型中用了batchnomolization，训练中用batch训练的时候，应该是有单数，比如dataset的总样本数为17,你的batch_size为8,就会报这样的错误。