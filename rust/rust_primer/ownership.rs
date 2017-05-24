use std::marker::Copy;

#[derive(Copy, Clone, Debug)]
struct Point {
    x: i32,
    y: bool,
}

#[derive(Debug)]
struct CopyPoint {
    x: i32,
    y: bool,
}

impl Copy for CopyPoint {}

impl Clone for CopyPoint {
    fn clone(&self) -> CopyPoint {
        CopyPoint {
            x: self.x,
            y: self.y,
        }
    }
}

fn main() {

    let s = String::from("string");
    let ss = s;
    println!("{}", ss);
    //println!("{}", s); // //s被move, 绑定被销毁

    //s = String::from("sss"); //不可以重新赋值
    let s = String::from("sss"); //可以重新生成并绑定
    println!("{}", s);

    let i = 3i32;
    let ii = i;
    println!("{}", i); //copy属性 基本数据类型(Primitive Types)均实现了Copy特性
    println!("{}", ii);


    let p1 = Point { x: 1, y: true };
    let p2 = p1;
    println!("{:?}", p1);
    println!("{:?}", p2);

    let cp1 = CopyPoint { x: 1, y: false };
    let cp2 = cp1;
    println!("{:?}", cp1);
    println!("{:?}", cp2);

    let m = 1;
    let some_clourse = move |x: i32| m + x;
    let y = some_clourse(1);
    println!("{}", m); //实现了copy
    println!("{}", y);

    let mut ms = String::from("sss");
    let ms_clourse = move |x: char| {
        ms.push(x);
        ms
    };
    let my = ms_clourse('s');
    println!("{:?}", my);
    //println!("{:?}", ms); 已经move

    let mut ms = String::from("sss");
    {
        let mut ms_clourse = |x: char| ms.push(x);
        ms_clourse('s');
    }
    println!("{:?}", ms); //"ssss"

    let x = 1;
    let y = &x; //引用与借用
    println!("{}, {}", x, y);

    let mut x = 1;
    {
        let y: &mut i32 = &mut x;
        *y += 1;
    }
    println!("{}", x); //2

    let mut x = 1;

    let y = &mut x;
    *y += 1;
    //println!("{}", x); //2 可变借用尚未归还, 不可使用
    let x = 1;
    let y = &x;
    println!("{}, {}", x, y); //不可变借用, 无需归还, 还可以使用

    println!("{}", get_bigger(1, 2)); //copy
    println!("{}", foo("aaa", "bbb")); //带生命周期的引用
    println!("{}", foo2("aaa", "bbb")); //带生命周期的引用
    println!("{}", foo3("aaa"));
    println!("{}", foo4("aaa"));

    let ls = LifeStruct { x: &1u8 };
    println!("{:?}", ls);
    ls.print_x();
    ls.add_some(&5u8);
}

fn get_bigger(x: i32, y: i32) -> i32 {
    if x > y { x } else { y }
}

fn foo<'a>(x: &'a str, y: &'a str) -> &'a str {
    if true { x } else { y }
}

//返回值的生命周期应该是 所有参数生命周期的交集中的子集
fn foo2<'a, 'b: 'a>(x: &'a str, y: &'b str) -> &'a str {
    if true { x } else { y }
}

#[allow(unused_variables)]
fn foo3<'a>(x: &'a str) -> &'static str {
    "aaaa"
}

#[allow(unused_variables)]
fn foo4<'a, 'b: 'a>(x: &'b str) -> &'a str {
    let x: &'a str = "aaa";
    x
}

//实际的struct的Lifetime应该是所有field Lifetime交集的子集
#[derive(Debug)]
struct LifeStruct<'a> {
    x: &'a u8,
}

//前一个<'a>是参数&self的生命周期, 后一个<'a>是LifeStruct的特性限制
impl<'a> LifeStruct<'a> {
    fn print_x(&self) {
        println!("{}", self.x);
    }
}

impl<'a, 'b> LifeStruct<'a> {
    fn add_some(&'a self, n: &'b u8) -> &'a u8 {
        println!("{}", n + 1);
        self.x
    }
}
