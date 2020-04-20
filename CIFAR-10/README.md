transforms.Normalize 为什么要归一化、标准化

fc 前记得 flatten

测试集、训练集、验证集 10% 80% 10%

output_shape = (image_shape-filter_shape+2*padding)/stride + 1

in
out
kernel_size
stride
padding=1

输出形状 print(x.size())


ResNet https://blog.csdn.net/sunqiande88/article/details/80100891

https://blog.csdn.net/winycg/article/details/86709991

降采样 max_pool / conv stride = 2


MobileNet

https://www.bilibili.com/video/BV1RJ411d7sF?from=search&seid=3184848541177549540

https://blog.csdn.net/winycg/article/details/86662347