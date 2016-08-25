fn function() {
    println!("call 'function()'");
}

mod my {
    #[allow(dead_code)]
    fn private_function() {
        println!("call my 'function()'");
    }

    pub fn function() {
        println!("call mu 'function()'");
    }

    pub mod nested {
        #[allow(dead_code)]
        fn private_function() {
            println!("call my nested 'function()'");
        }

        pub fn function() {
            println!("call my nested 'function'");
        }
    }

    mod private_mod {
        #[allow(dead_code)]
        pub fn function() {
            println!("call private mod is no");
        }
    }
}

fn main() {
    function();
    my::function();
    my::nested::function();
    //my::private_mod::function();
}
