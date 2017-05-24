use std::ops::Add;

fn add<T: Add<T, Output = T>>(a: T, b: T) -> T {
    a + b
}

#[derive(Debug)]
struct Point {
    x: i32,
    y: i32,
}

impl Add for Point {
    type Output = Point;
    fn add(self, p: Point) -> Point {
        Point {
            x: self.x + p.x,
            y: self.y + p.y,
        }
    }
}

#[derive(Debug)]
struct GenericPoint<T: Add<T, Output = T>> {
    x: T,
    y: T,
}

impl<T: Add<T, Output = T>> Add for GenericPoint<T> {
    type Output = GenericPoint<T>;
    fn add(self, p: GenericPoint<T>) -> GenericPoint<T> {
        GenericPoint {
            x: self.x + p.x,
            y: self.y + p.y,
        }
    }
}

fn main() {
    println!("{}", add(2u8, 3u8));
    let p1 = Point { x: 1, y: 2 };
    let p2 = Point { x: 2, y: 3 };
    //println!("{:?}", p1 + p2); //Point { x: 3, y: 5 }
    println!("{:?}", add(p1, p2)); //Point { x: 3, y: 5 }

    let gp1 = GenericPoint { x: 1.2, y: 2.3 };
    let gp2 = GenericPoint { x: 3.4, y: 4.5 };
    println!("{:?}", add(gp1, gp2)); //GenericPoint { x: 4.6, y: 6.8 }
}
