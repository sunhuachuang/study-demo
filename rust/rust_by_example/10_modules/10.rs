fn function() {
    println!("call 'function()'");
}

mod my {
    #[allow(dead_code)]
    fn function() {
        println!("call my 'function()'");
    }

    mod nested {
        #[allow(dead_code)]
        fn function() {
            println!("call my nested 'function()'");
        }
    }
}

fn main() {
    function();

    //mod 里面的默认都是private
    //my::function();
}
