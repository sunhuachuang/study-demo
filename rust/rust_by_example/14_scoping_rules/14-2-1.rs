fn main() {
    let immut_box = Box::new(5i32);

    println!("{}", immut_box);

    let mut mut_box = Box::new(5i32);

    println!("{}", mut_box);

    *mut_box  = 6;

    println!("{}", mut_box);
}
