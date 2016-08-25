pub fn public_function() {
    println!("called rary publif function");
}

fn private_function() {
    println!("called rary private function");
}

pub fn indirect_access() {
    println!("call rary indirect access, that\n>");
    private_function();
}
