1。需要安装
   numpy(用于矩阵操作)、matplotlib.pyplot(用于绘图)、
   operator(用于提取字典元素)
2。代码构成：分为
   数据搭建部分
   数据切割部分
   构建knn部分
   knn执行部分
共4个部分
    有些部分的注释含有可执    行的plt.scatter等函数    ，取消这些地方的注释可    以看到数据的分布图像。

3。详细介绍：
   knn是一种简单的分类算法，他通过比较距离输入值最近的k个值的标签占比，将占比最大的那个标签作为输入值的预期分类。他最明显的特征不需要函数自己训练参数，而是要求一个认为设定的超参数：k。
   
   代码第4行到第41行：
   数据搭建部分

    在平面内构建了值为1、2、3三种标签的数据
    每个类分别采用正态分布的随机数构成，各数据间有重叠（见图片data_all）
    随机种默认为200，数据总量为600.
   用x*_1、x*_2分别代表横向和纵向，用y*代表数据标签。

   代码第43行到第65行：
   数据切割部分

   先打乱数据的索引
   然后以7：3的比例将数据拆为训练集和测试集(见图片data_test 和data_train)
   最后为了避免计算距离时数据之间因相差过大而扩大误差，对数据的值（x）进行归一化处理。

    代码第67行到第112行：
    构建knn部分
    
     _init_函数：规定了超参数k取3.
     
    train函数：是读入训练集
    
    dist函数：计算两点间距离，这里采用曼哈顿距离（L1距离）
  
    vote函数：实现knn的多数投票机制；利用字典对标签计数，最后输出最大值
    
    predict函数：knn主体，输出预测值Ypred
   
    score函数：评价函数。方法是 比较输入端真值等于估值的次数与真值的总数。
满分为1。

    代码第113行到最后：
    knn执行部分
 
    输出为knn的匹配成功率，完全成功为 1
   
### k = 3 时分数为 0.983 ；
### 分数可能因为随机种的不同（当前为200）或是k的不同（当前为3）而不同