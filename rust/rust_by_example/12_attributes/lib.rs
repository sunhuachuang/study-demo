//this is a library
#![crate_type = "lib"]
#![crate_name = "rary"]

pub fn public_function() {
    println!("call rary's public function");
}

fn private_function() {
    println!("call rary's private functuon");
}

pub fn indirect_access() {
    println!("call rary's indirect access and that: >");
    private_function();
}
