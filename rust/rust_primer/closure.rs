// 静态分发
fn call_clourse<T>(f: T) -> i32
    where T: Fn(i32) -> i32
{
    f(1)
}

//动态分发
fn call_clourse2<T>(f: &T) -> i32
    where T: Fn(i32) -> i32
{
    f(1)
}

fn add_one(x: i32) -> i32 {
    x + 1
}

fn factory() -> Box<Fn(i32) -> i32> {
    let num = 5;
    Box::new(move |x| x + num)
}

fn main() {
    let c1 = |x| x + 1;
    let c2 = |x: i32| x + 1;
    let c3 = |x: i32| -> i32 { x + 1 };
    println!("{}", c1(1));
    println!("{}", c2(1));
    println!("{}", c3(1));

    println!("{}", call_clourse(|x| x + 1));
    println!("{}", call_clourse(add_one));
    println!("{}", call_clourse(&|x| x + 1));
    println!("{}", call_clourse2(&add_one));
    let f = factory();
    println!("{}", f(1));
}
