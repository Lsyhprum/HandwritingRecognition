# LeNet-5

![]()

## LeNet-5 结构

* 输入层 

32*32*1

* 卷积层

filter深度 6  
filter大小 5*5 
padding 2
步长 s = 1

输出 28*28*6

* 池化层

filter 2*2
步长 s = 2
padding 0

输出 14*14*6

* 卷积层

filter深度 16  
filter大小 5*5 
padding 0 
步长 s = 1

输出 10*10*16

* 池化层

filter 2*2
步长 s = 2
padding 0

输出 5*5*16

flatten 400

* fc

neuron 120

* fc 84

* 输出层

softmax

## 性质

* 7层网络，可训练层 5

* LeNet-5 60000 参数

* 高度、宽度在缩小，channel 增加

