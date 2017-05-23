#![feature(inclusive_range_syntax)]
fn main() {
    let a1 = 5;
    let a2: i32 = 5;
    assert_eq!(a1, a2);

    let b1: u32 = 5;
    //assert_eq!(a2, b1); //mismatch types
    println!("{}, {}, {}", a1, a2, b1);

    let mut m1: f64 = 1.0;
    println!("{}", m1); //warning: value assigned to `m1` is never read

    m1 = 3.0;
    println!("{}", m1);

    let b2 = 4.0f32;
    println!("{}", b2);

    //int
    /*
     * 不可变大小
     * u8 (无符号) i8 (有符号)
     * u16        i16
     * u32        i32 (默认)
     * u64        i64
     *
     * 可变大小
     * usize     isize
     *
     * 浮点数
     * f32 (默认)  f64
     */









    let f1 = 0.2;
    let f2 = 0.2f32;
    assert_eq!(f1, f2);

    let f3 = 0.1;
    if f1 + f3 == 0.3 {
        println!("0.1 + 0.2 == 0.3");
    } else {
        println!("0.1 + 0.2 != 0.3");
    }

    // let 模式匹配表达式
    let (a, b) = (1, 2);
    println!("a: {}, b: {}", a, b);

    let (t, mut f): (bool, bool) = (true, false);
    println!("t: {}, f: {}", t, f);

    f = !f;
    assert_eq!(t, f);

    // 内置原生类型
    /*
     * bool        布尔类型: true, false
     * char        字符类型: 单个unicode字符, 存储为4个字节
     * int(float)  数值类型: 有符号整数, 无符号整数，浮点数
     * str(String) 字符串类型: 底层为不定长类型str, 常用其切片 &str(&'static str) 和 堆分配 String, 切片静态不可变。String可变
     * array       数组类型: 同类型固定大小 [T; N]
     * slice       切片类型: 引用数组的部分, 不需要拷贝 &[T]
     * tuple       元组类型: 固定大小有序列表，类型不统一，可以通过解构和索引获取值
     * pointer     指针类型: 最底层裸指针 *const T 和 *mut T, 解引用必须放到unsafe中
     * function    函数类型: 实质是个函数指针
     *             元类型: (), 唯一值 ()
     */










    let t = true;
    let f: bool = false;
    assert_eq!(t, !f);

    let c = 'c';
    println!("{}", c as i32);

    let x = 123_456;
    assert_eq!(x, 123456);
    let xx: f64 = 1.23e+2;
    //let zero = z.abs_sub(123.4);
    let bin = 0b1111_0000;
    let oct = 0o7320_1546;
    let hex = 0xf23a_b09;
    println!("{}, {}, {}, {}", xx, bin, oct, hex);

    let str = "hello";
    let sstr: &'static str = "hello";
    assert_eq!(str, sstr);
    let mut string = str.to_string();
    string += " world!";
    println!("{}, {}", str, string);

    let arr = [1, 2, 3, 4, 5];
    println!("arr1: {:?}, {}", arr, arr[1]);
    let arr2 = [0; 10];
    println!("{:?}, arr1.slice: {:?}, {:?}",
             arr2,
             &arr[1..3],
             &arr[1...3]); //#![feature(inclusive_range_syntax)]
    // arr1: [1, 2, 3, 4, 5], 2
    // [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], arr1.slice: [2, 3], [2, 3, 4]

    let tup = (1, "hello");
    let (_, say) = tup;
    println!("{}, tuple.1 : {}", say, tup.1);

    let x = 5;
    let raw = &x as *const i32;
    let points_at = unsafe { *raw };
    println!("{}", points_at);

    fn foo(x: i32) -> i32 {
        return x * 2;
    }

    let bar: fn(i32) -> i32 = foo;
    println!("{}", bar(3));

    /*
     * 单字节字符 b'a', b'hello', 原始字符串r#"hello"#
     * 使用 & 将string 转化为 &str很廉价，反之to_string, 涉及内存分配，不廉价
     * 动态数组 vec!
     * 不多于32个元素的数组和不多于12个元素的元组，传值自动复制
     */
    type Point = (i32, i32);
    let p: Point = (1, 2);
    println!("{:?}", p);

    let s = "hello".to_string();
    use_str(&*s); //string to &str

    let say = "我很好".to_string();
    for i in say.as_bytes() {
        println!("{}", i);
    }

    for i in say.chars() {
        println!("{}", i);
    }

    println!("{:?}", say.chars().nth(2));
}

fn use_str(s: &str) {
    println!("{}", s);
}
