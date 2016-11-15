fn main() {
    println!("{:?}", sabs(-3)); //3
    println!("{:?}", mabs(-4)); //4
    println!("{:?}", orabs(-5)); //5
}

fn sabs(x: i32) -> i32 {
    if x < 0 {
        - x
    } else {
        x
    }
}

//wait for later i don't know Infinity.
fn mabs(x: i32) -> i32 {
    match x {
        0       => 0,
        -10...0 => -x,
        0...10 => x,
        _       => x,
    }
}

fn orabs(x: i32) -> i32 {
    if x == 0 || x > 0 {
        x
    } else {
        -x
    }
}
