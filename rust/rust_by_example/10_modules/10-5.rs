mod my;

fn function() {
    println!("this is outside function");
}
fn main() {
    my::function();
    function();
}
