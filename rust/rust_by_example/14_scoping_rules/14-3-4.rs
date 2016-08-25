#[derive(Clone, Copy)]
struct Point { x: i32, y:i32 }

fn main() {
    let c = "y";

    let ref ref_c1 = c;
    let ref_c2     = &c;

    println!("c1 eq c2 ? {}", *ref_c1 == *ref_c2);

    let point = Point { x: 0, y: 0 };

    let _copy_of_x = {
        let Point { x: ref ref_to_x, y: _ } = point;
        *ref_to_x
    };

    let mut mutable_point = point;
    {
        let Point {x: _, y: ref mut mut_ref_to_y } = mutable_point;
        *mut_ref_to_y = 1;
    }

    println!("point: {}, {}", point.x, point.y);
    println!("mutable_point: {}, {}", mutable_point.x, mutable_point.y);
    let tuple = (Box::new(5u32), 3u32);

    println!("tuple is {:?}", tuple);
}
