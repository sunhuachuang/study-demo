#include <iostream>
#include <algorithm>

using namespace std;

/**
 * 两种方法
 * 1. 重载 == <
 * 2. 自定义 Pred fn 比较函数
 */

/**
 * 1.不变序列算法
 *   不会改变容器或对象
 *   适用于顺序容器于关联容器
 *   时间复杂度通常是O(n) 遍历
 * min 两个对象 min(iterator a, iterator b, Pred fn)
 * max
 * min_element 区间
 * max_element
 * for_each
 * count
 * count_if
 * *find
 * find_if
 * find_end 在区间里面查找另一个区间最后一次出现的位置
 * find_first_of 在区间里面查找第一个出现在另一个容器中的元素
 * adjacent_find 在区间里面查找第一次出现连续两个相等元素的位置
 * search 在区间查找另一个区间第一次出现的位置
 * search_n 在区间查找第一次出现等于某值的连续n个元素
 * equal 判断两区间是否相等
 * mismatch 逐个比较两个区间的元素，返回第一次不相等的位置
 * lexicographical_compare 按字典比较两个区间的大小
 */

/**
 * 2. 变值算法
 *    改变区间或目标区间的值
 *    不能作用于关联容器，只能用于顺序容器
 * for_each() 1中的是产生新的值， 2中的是改变该值
 * *copy 复制到别处
 * copy_backward 复制到别处, 目标区间从后往前copy
 * transform 讲一个区间的元素变形后拷贝到另一个区间
 * swap_ranges 交换两个区间的内容
 * fill 填充区间
 * fill_n 用某个值替换区间的n个元素
 * generate 用某个操作的结果填充区间
 * generate_n
 * replace 将区间中的某个值替换为另一个值
 * replace_if
 * replace_copy 将区间的值拷贝到另一个区间， 拷贝到另一个区间的值是修改后的值
 * replace_copy_if
 */

/**
 * 3. 删除算法
 *    删除容器中的某些元素
 *    删除不会使得容器元素减少 （元素向前移动， 最后的空位置维持原来的值不变）
 *    只能作用于顺序容器， 不能作用于关联容器
 *    算法复杂度通常为 O(n)
 * remove
 * remove_if
 * remove_copy 拷贝区间到另一个区间， 等于某个值的元素不拷贝
 * remove_copy_if
 * unique 删除容器中连续相等的元素， 只留下一个
 * unique_copy 拷贝区间到另一个区间， 连续相等的元素只拷贝一个
 */

/**
 * 4. 变序算法
 *    改变元素位置， 不改变元素值
 *    只能作用于顺序容器， 不能作用于关联容器
 *    算法复杂度通常为 O(n)
 * *reverse 颠倒区间元素顺序
 * reverse_copy 颠倒后的区间copy到另一区间，原区间不变
 * rotate 将区间循环左移
 * rotate_copy 收尾相接旋转后的copy到另一区间，原区间不变
 * *next_permutation 将区间改为下一个排列
 * *prev_permutation 将区间改为上一个排列
 * *random_shuffle 随机打乱
 * partition 把区间满足条件的移到左边，不满足的移动右边
 * stable_partition 原来的先后次序不变
 */

/**
 * 5. 排序算法 => 快排
 *    复杂度通常为 O(nlog(n))
 *    随机访问迭代器， 不适用于关联容器于list
 * *sort
 * stable_sort 相等元素的相对次序
 * partial_sort 部分排序，直到最小的n的元素就位
 * partial_sort_copy
 * nth_element 部分排序， 使得第n小的元素，比它小的在前面，大的在后面
 */

/**
 * 6. 有序区间算法
 *    排好顺序的区间， 需要随机访问迭代器
 *    不适用于关联容器与list
 * *binary_search 判断区间是否包含某个元素 O(log(n))
 * includes 判断一个区间中的元素是否都在另一个区间中
 * *lower_bound 查找最后一个不小于某值的元素
 * *upper_bound 查找第一个大于某值的元素
 * *equal_range 同时获取 lower_bound 与 upper_bound
 * merge 合并两个有序区间到第三个区间
 * set_union 并集copy到第三区间
 * set_intersection 交集copy到第三区间
 * set_difference 差集copy到第三区间
 * set_symmetric_difference 对称差集copy到第三区间 （并集 - 交集）
 * inplace_merge 将两个有序区间原地合并成一个有序区间
 */

int main() {

}
