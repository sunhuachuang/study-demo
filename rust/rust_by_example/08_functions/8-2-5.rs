fn create_fn() ->Box<Fn()> {
    let text = "Fn".to_owned();
    Box::new(move || println!("this is {}", text))
}

fn create_fnmut() -> Box<FnMut()> {
    let text = "FnMut".to_owned();
    Box::new(move || println!("this is {}", text))
}

fn main() {
    let fn_plain = create_fn();
    let mut fn_mut   = create_fnmut();

    fn_plain();
    fn_mut();
}
