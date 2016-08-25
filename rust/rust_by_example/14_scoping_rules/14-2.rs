fn destory_box(c: Box<i32>) {
    println!("destory box c is {}", c);
}

fn main() {
    let a = 5u32;
    let b = a;

    println!("a is {}, b is {}", a, b);

    let x = Box::new(5i32);

    let y = x;

    //println!("{:?}", x); x has moved

    destory_box(y);//y has freed

    //println!("{:?}", y);
}
