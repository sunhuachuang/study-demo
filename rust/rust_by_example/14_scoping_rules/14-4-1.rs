fn main() {
    let (x, y) = (4, 5);

    print_refs(&x, &y);

    failed_borrow();
}

fn print_refs<'a, 'b>(x: &'a i32, y: &'b i32) {
    println!("x:{} , y:{}", x, y);
}

fn failed_borrow<'a>() {
    let _x = 2;
}
