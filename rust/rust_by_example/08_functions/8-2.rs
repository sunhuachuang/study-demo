fn main() {
    fn function             (i: i32) -> i32 { i+1 }
    let closure_annotated = |i: i32| -> i32 { i+1 };
    let closure_inferred  = |i     |          i+1  ;

    let i = 1;
    println!("funcion: {}", function(i));
    println!("annotated: {}", closure_annotated(i));
    println!("inferred: {}", closure_inferred(i));

    let one = || 1;
    println!("one is {}", one());

    let professor_x = "hello,world";
    let print = || println!("professor name is {}", professor_x);
    print();
}
