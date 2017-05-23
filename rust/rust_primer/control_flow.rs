#[allow(dead_code)]
struct Point {
    x: i32,
    y: i32,
}

#[allow(dead_code)]
enum OptionalInt {
    Value(i32),
    Missing,
}

fn main() {
    let mut x = 5;
    let y = if x == 5 { 10 } else { 5 };
    println!("{}, {}", x, y);

    let z = x = 10;
    println!("{:?}, {:?}", z, x); //(), 10

    //err: let y = (let x = 5);
    //err: let z: i32 = if x == 5 { 10; } else { 15; };

    for i in 0..5 {
        //0, 1, 2, 3, 4
        println!("{}", i);
    }

    for i in [1, 2, 3].iter() {
        println!("{}", i);
    }

    #[allow(unreachable_code)]
    'outer: loop {
        println!("this is outer loop!");

        'inner: loop {
            println!("this is inner loop!");
            break 'outer;
        }

        println!("this will never reached");
    }

    //强大的match表达式
    for day in 1..9 {
        match day {
            6 | 7 => println!("this is weekend ~ :)"),
            d @ 1...5 => println!("this is work day! :(, today is {}", d),
            _ => {
                println!("what is it ?");
            }
        }
    }

    let rx = 5;
    let mut ry = 6;

    match rx {
        ref r => println!("got ref {}", r), //got ref 5
    }

    match ry {
        ref mut r => {
            println!("got mut ref {}", r); //got mut ref 6
            *r = 1;
        }
    }

    println!("{}", ry); //1

    let pair = (0, 0);

    match pair {
        (0, y) => println!("y: {}", y), //y: 0
        (x, 0) => println!("x: {}", x),
        _ => println!("{:?}", pair),
    }

    let p = Point { x: 1, y: 2 };
    match p {
        Point { x, .. } => println!("x is {}", x),
    }

    let o = OptionalInt::Value(5);
    match o {
        OptionalInt::Value(i) if i > 5 => println!("{} > 5", i),
        OptionalInt::Value(..) => println!("it is <= 5"),
        OptionalInt::Missing => println!("got a missing"),
    }

    let number = Some(1);
    let mut number2 = Some(2);

    if let Some(i) = number {
        println!("got number: {}", i);
    } else {
        println!("not got number");
    }

    while let Some(i) = number2 {
        if i > 9 {
            println!("greater than 9");
            number2 = None;
        } else {
            println!("got number2: {}", i);
            number2 = Some(i + 1);
        }
    }

    println!("{:?}", number2);

    for (i, j) in (5..10).enumerate() {
        println!("{}: {}", i, j);
    }

    let lines = "abc
efg
hij"
            .lines();

    for (num, line) in lines.enumerate() {
        println!("{}: {}", num, line);
    }
}
