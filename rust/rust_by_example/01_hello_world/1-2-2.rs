use std::fmt;

#[derive(Debug)]
struct MinMax(i64, i64);

impl fmt::Display for MinMax {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "({}, {})", self.0, self.1)
    }
}

#[derive(Debug)]
struct Point2 {
    x: f64,
    y: f64,
}

impl fmt::Display for Point2 {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "({}, {})", self.x, self.y)
    }
}

fn main() {
    let minmax = MinMax(0, 14);

    println!("display: {}", minmax);
    println!("debug: {:?}", minmax);

    let big_range = MinMax(-300, 300);
    let smail_range = MinMax(-1, 1);

    println!("{big} is big_range, {smail} is smail_range", big = big_range, smail= smail_range);

    let point = Point2{x: 2.7, y: 3.3};

    println!("display: {}", point);
    println!("debug: {:?}", point);
}
