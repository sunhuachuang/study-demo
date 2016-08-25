//unit struct
struct Nil;

//tuple struct
struct Pair(i32, f64);

//generate like C struct
struct Point {
    x: f64,
    y: f64,
}

//structs can be reused as another fields in other struct
#[allow(dead_code)]
struct Rectangle {
    p1: Point,
    p2: Point,
}

fn main() {
    let point: Point = Point{ x: 0.3, y: 4.5};

    println!("first: {},{}", point.x, point.y);

    //descript Point
    let Point {x: my_x, y: my_y } = point;

    let _rectangle = Rectangle {
        p1: Point { x: my_x, y: my_y },
        p2: point,
    };

    //println!("{:?}", _rectangle);

    let _nil = Nil;

    let pair = Pair(1, 0.1);

    let Pair(integer, decimal) = pair;

    println!("pair contains {:?} and {:?}", integer, decimal)
}
