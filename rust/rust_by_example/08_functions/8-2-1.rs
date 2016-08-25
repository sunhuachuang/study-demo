fn main() {
    let color = "green";

    let print = || println!("color: {}",color);

    print();
    print();
    println!("color: {}", color);

    let mut count = 0;

    let mut inc = || {
        count += 1;
        println!("count: {}", count);
    };

    inc();
    inc();

    //let reborrow = &mut count;

    let moveable = Box::new(3);

    let consume = || {
        println!("moveable: {}", moveable);
        drop(moveable);
    };

    consume();

    //consume();
}
