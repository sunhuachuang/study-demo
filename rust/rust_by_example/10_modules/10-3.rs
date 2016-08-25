use my::test::function as inside_function;

fn function() {
    println!("this is outside funciton");
}

mod my {
    pub mod test {
        pub fn function() {
            println!("this is inside function");
        }
    }
}

fn main() {
    function();

    println!("start a block");
    {
        function();
        my::test::function();
    }
    println!("next block");
    {
        use my::test::function;
        function();
    }
    println!("end block");

    inside_function();
}
