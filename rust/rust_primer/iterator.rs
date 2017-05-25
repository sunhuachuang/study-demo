use std::collections::HashMap;

fn main() {
    let v: Vec<_> = (0..5).collect();
    let v2 = (0..5).collect::<Vec<_>>();
    println!("{:?}, {:?}", v, v2);

    //fold vs reduce fold可以指定初始值
    let x = (0..5).fold(1u8, |x, y| {
        println!("{}, {}", x, y); //x is sum, y is next value
        x + y
    });
    println!("{}", x);

    for i in (0..5).map(|x| x + 1) {
        println!("{}", i);
    }

    for i in (0..5).filter(|x| x % 2 == 0) {
        println!("{}", i);
    }

    let v = vec![1, 2, 3, 4, 5, 6];

    let vv = v.iter().cloned().take(2).collect::<Vec<_>>();
    println!("{:?}", vv); //[1, 2]

    let vvv: Vec<_> = v.iter().cloned().skip(2).collect();
    println!("{:?}", vvv); //[3, 4, 5, 6]

    //多余的舍弃
    let z1 = vec!["sun", "hua", "chuang", "test"];
    let z2 = vec![1, 2, 3];
    let z: HashMap<_, _> = z1.iter().zip(z2.iter()).collect();
    println!("{:?}", z);

    for (i, j) in z2.iter().enumerate() {
        println!("{}: {}", i, j);
    }
}
