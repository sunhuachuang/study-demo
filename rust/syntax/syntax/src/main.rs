fn main() {
    /*
    let mut x = 5;
    let (m, n) = (2 ,3);
    let x: i32 = 5；
    x = 10;
    println!("Hello, world!{}", x);
     */
    print_number(9);
    print_sum(2,3);
    let y: i32 = add_one(3);
    println!("y= {}", y);
    //let mut m = 5;
    let m = 5;
    //let n = (m = 6);
    let t = true;
    let c = 'c';
    let mut a = [0;4];
    a[1] = 3;
    let astr = ["aa", "bb", "cc"];//数组中的字符用双引号
    let tuples = (12, "abc", true);
    let tuples0 = tuples.0;
    fn _function(x: i32) -> i32 {x}
    let __function: fn(i32) -> i32 = _function;
    println!("m:{}, t:{}, c:{}", m, t, c);
    println!("a len:{}, one is {}", a.len(), a[1]);
    println!("astr: {}, {}, {}", astr[0], astr[1], astr[2]);
    println!("tuples: {} and {} and {}",tuples0, tuples.1, tuples.2 );
    //ifrust(7);
    //if_number(7);
    //for_test(5);
    //while_test();
    enumerate_range();
    loop_test();
    loop_if_test();
}

//参数必须有类型
fn print_number(x:i32) {
    println!("x is: {}", x);
}

fn print_sum(x:i32, y:i32) {
    println!("x+y={}", x+y);
}

fn add_one(x:i32) -> i32 {
    x+1//返回值最后不能加;
}

//if
fn ifrust(x: i32) {
    if x == 5 {
        println!("number is 5");
    } else if x == 6 {
        println!("number is 6");
    } else {
        println!("no number");
    }
}

fn if_number(x: i32) {
    let y = if x ==5 {10} else {15};
    println!("y: {}", y);
}

fn for_test(x: i32) {
    for y in 1..x {//不包括上限值
        println!("y: {}", y);
    }
}

fn while_test() {
    let mut x = 5;
    let mut done = false;
    while !done {
        x += x - 3;
        println!("while:x:{}", x);

        if x%5 == 0 {
            done = true;
        }
    }
}

fn enumerate_range() {
    for (i, j) in (6..9).enumerate() {//i表示循环的次数
        println!("i:{}, j={}", i, j);
    }
}

fn loop_test() {
    let mut x = 5;
    loop {
        x += x - 3;
        println!("loop-x:{}", x);
        if x%5 == 0 { break; }
    }
}

fn loop_if_test() {
    'outer: for x in 0..10 {
        'inner: for y in 0..10 {
            if x%2 == 0 { continue 'outer; }
            if y%2 == 0 { continue 'inner; }
            println!("x:{}, y:{}", x, y);
        }
    }
}
