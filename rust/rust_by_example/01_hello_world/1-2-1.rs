#[derive(Debug)]
struct Structure(i32);

#[derive(Debug)]
struct Deep(Structure);

fn main() {
    println!("{:?} days", 365);

    println!("{1:?} {0:?} is the {c:?}",
             "a",
             "b",
             c = "ab"
             );

    println!("{:?} will be print", Structure(3));

    println!("{:?} will also be print", Deep(Structure(7)));
}
