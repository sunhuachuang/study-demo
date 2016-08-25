struct Point {
    x: i32,
    y: i32,
    z: i32,
}

fn main() {
    let mut point = Point {
        x: 0,
        y: 0,
        z: 0,
    };

    {
        let borrow_point = &point;
        let anthor_point = &point;

        println!("point: {}, {}, {}", point.x, borrow_point.y, anthor_point.z);
        //let mut_borrow   = &mut point;
    }

    {
        let mut_borrow = &mut point;
        mut_borrow.z = 5;
    }

    println!("point: {}, {}, {}", point.x, point.y, point.z);
}
