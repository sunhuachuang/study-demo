use std::fmt::{Debug, Display};

fn compare_prints<T: Debug + Display>(t: &T){
    println!("{:?}", t);
    println!("{}", t);
}

fn compare_types<T: Debug, U: Debug>(t: &T, u: &U) {
    println!("{:?}", t);
    println!("{:?}", u);
}

fn main() {
    let string = "worlds";
    let array  = [1, 2, 3];
    let vec    = vec![1, 2, 3];

    compare_prints(&string);
    //compare_prints(&array);not work array cannot display
    compare_types(&array, &vec);
}
