#![allow(dead_code)]

enum Status {
    Rich,
    Poor,
}

enum Work {
    Civilian,
    Soldier,
}

fn main() {
    use Status::{Poor, Rich};
    use Work::*;

    let status = Poor;
    let work = Civilian;

    match status {
        Rich => println!("this is rich"),
        Poor => println!("this is poor"),
    }

    match work {
        Civilian => println!("this is civilian"),
        Soldier  => println!("this is soldiers"),
    }
}
