fn function() {
    println!("this is outside function");
}

mod my {
    pub fn indirect_call() {
        print!("call my::indirect_call, that\n>");
        function();
        {
            use cool::function as root_cool_function;
            print!(">");
            root_cool_function();
        }
        {
            use self::cool::function as my_cool_function;
            print!(">");
            my_cool_function();
        }
        {
            use super::function as root_function;
            print!(">");
            root_function();
        }
    }

    fn function() {
        println!("call my::function");
    }

    mod cool {
        pub fn function() {
            println!("call my::cool::function");
        }
    }
}

mod cool {
    pub fn function() {
        println!("this is cool::function");
    }
}

mod test {
    pub mod test2 {
        #[allow(dead_code)]
        pub fn function() {
            println!("this is test::test2::function");
        }

        #[allow(dead_code)]
        pub fn test3() {
            use super::super::function as fff;
            fff();
            {
                use self::function as myfff;
                myfff();
            }
        }
    }
    #[allow(dead_code)]
    pub fn function() {
        println!("this is test::function");
    }
}

fn main() {
    my::indirect_call();
    test::test2::test3();
}
