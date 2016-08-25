fn create_box() {
    let _function_box = Box::new(3i32);
}

fn main() {
    let _box_int = Box::new(5i32);
    {
        let _shirt_box = Box::new(13i32);
    }

    for _ in 0u32..1000 {
        create_box();
    }
}
