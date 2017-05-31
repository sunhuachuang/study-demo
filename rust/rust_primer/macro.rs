macro_rules! create_function {
    ($func_name: ident) => (
        fn $func_name() {
            println!("function: {:?} is calling.", stringify!($func_name));
        }
    )
}

//repetition
macro_rules! vector {
    ($($x: expr), *) => {
        {
            let mut tmp_vec = Vec::new();
            $(tmp_vec.push($x);)*;
            tmp_vec
        }
    }
}

//recursion
macro_rules! find_min{
    ($x: expr) => ($x);
    ($x: expr, $($y: expr), +) => (
        std::cmp::min($x, find_min!($($y), +))
    )
}

//hygienic Macro
macro_rules! create_x {
    () => {
        let x = 10;
        println!("{}", x);
    }
}

// 宏与函数处于不同的命名空间
fn create_function() {
    println!("call create function fn");
    let a = vector![1, 2, 3];
    println!("{:?}", a);
}


//#[macro_export]
//#[macro_use]

fn main() {
    create_function!(foo);
    foo();
    create_function();
    println!("{}", find_min!(1u32));
    println!("{}", find_min!(1u32 + 3, 3u32));
    println!("{}", find_min!(1u32 + 1, 3u32, 2u32 * 2, 1));

    create_x!();
    //println!("{}", x); x is not defined
}
