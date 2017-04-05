##### array slice map
1. array 定义时候带有具体的长度, slice　不带长度
1. array 传值拷贝, slice　是传引用, map 也是传引用
1. slice map 使用前必须初始化, make

##### new make
1. make 作用于内置的数据结构 slice map channel, 分配内存空间并且给其初始化一个值
1. new 作用于结构体,　分配内存并返回该内存的指针

##### for
for 循环代替 for, while, 通过range可循环array, slice, map

##### function
1. 多返回值
1. 指针传递
1. defer延迟语句
1. panic and recover
