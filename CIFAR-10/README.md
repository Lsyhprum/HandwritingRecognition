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