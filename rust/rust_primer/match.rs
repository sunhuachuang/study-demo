#[allow(unused_variables)]
fn main() {
    let tuple: (i32, String) = (1, String::from("hello"));
    let point: (i32, i32) = (1, 2);

    let (x2, _) = tuple;
    println!("{:?}", tuple);

    match tuple {
        ref t => println!("{:?}", t), //ref 引用，而不move掉
    }

    println!("{:?}", tuple);

    let (x, y) = tuple;
    let (x1, y1) = point;

    //println!("{:?}", tuple); point had moved, and not copy
    println!("{:?}", point);

    let x = 10;

    match x {
        e @ 1...9 | e @ 10...20 => println!("got {}", e),
        _ => println!("no"),
    }

    let y = 10;
    let yy = false;

    //no
    match y {
        ref e @ 9 | ref e @ 10 if yy => println!("got {}", e),
        _ => println!("no"),
    }

    println!("{}", y);
}
