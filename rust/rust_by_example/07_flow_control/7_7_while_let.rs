fn main() {
    let mut optional = Some(0);

    while let Some(i) = optional {
        if i > 9 {
            println!("more than 9 quit");
            optional = None;
        } else {
            println!("i is {:?}", i);
            optional = Some(i + 1);
        }
    }
}
