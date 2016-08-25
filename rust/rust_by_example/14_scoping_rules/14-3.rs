fn destory_box(c: Box<i32>) {
    println!("{} has been destory", c);
}

fn not_destory_box(c: &i32) {
    println!("{} is not be destory", c);
}

fn main() {
    let a = Box::new(5);

    let b = 6;

    not_destory_box(&b);
    not_destory_box(&b);

    {
        let _c = &a;
        //destory_box(a);
    }

    destory_box(a);
}
