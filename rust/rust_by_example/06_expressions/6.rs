fn main() {
    let x  = 5u32;

    let y = {
        let x_squared = x * x;
        let x_cube = x_squared * x;
        x_cube + x_squared + x
    };

    let z = {
        2 * x;
    };

    println!("x:{:?}", x);
    println!("y:{:?}", y);
    println!("z:{:?}", z);
}
