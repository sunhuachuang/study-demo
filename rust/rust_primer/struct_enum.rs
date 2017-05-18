use std::cell::Cell;

struct Point {
    x: i32,
    y: i32
}

//tuple struct
struct Color(u8, u8, u8);

//newtype
struct Digit(i32);

//unit-like struct
struct None();


//derive(得到,源于) drive(驱动)
#[derive(Default)]
struct Point3d {
    x: i32,
    y: i32,
    z: i32
}

#[derive(Debug)]
struct Changed {
    x: i32,
    y: Cell<i32>
}

#[derive(Debug)]
struct PubField {
    pub x: i32,
    y: i32
}

#[derive(Debug)]
#[allow(dead_code)]
enum Message {
    Quit,
    ChangeColor(i32, i32, i32),
    Move {x: i32, y: i32},
    Write(String)
}

#[allow(unused_variables)]
fn main() {
    let p = Point { x: 1, y: 1 };
    println!("{}, {}", p.x, p.y);

    let black = Color(0, 0, 0);
    let Color(a, b, c) = black;
    println!("{}, {}, {}", a, b, c);

    let v = vec![0, 1, 2];
    let d: Vec<Digit> = v.into_iter().map(Digit).collect();

    for i in d {
        let Digit(a) = i;
        println!("{}", a);
    }

    let n = None();

    //一个包含..的struct可以用来从其它结构体拷贝一些值或者在解构时忽略一些域
    let origin = Point3d::default();
    let point = Point3d { y :1, ..origin };
    let Point3d { x: x0, y: y0, .. } = point;
    println!("{}, {}, {}", origin.x, origin.y, origin.z); //0, 0, 0
    println!("{}, {}, {}", point.x, point.y, point.z); //0, 1, 0
    println!("{}, {}", x0, y0); //0, 1

    let c = Changed { x: 1, y: Cell::new(5) };
    println!("{:?}", c); // Changed { x: 1, y: Cell { value: 5 } }
    c.y.set(7);
    println!("{:?}", c); // Changed { x: 1, y: Cell { value: 7 } }

    let p = PubField { x: 10, y: 1 };
    println!("{:?}", p);

    let m = Message::Move {x: 1, y: 2};
    println!("{:?}", m); //Move { x: 1, y: 2 }
}
