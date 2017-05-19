use std::cell::Cell;

struct Person {
    name: &'static str,
    age: Cell<u8>,
}

impl Person {
    fn new(name: &'static str, age: u8) -> Person {
        Person {
            name: name,
            age: Cell::new(age),
        }
    }

    //self，允许实现者移动和修改对象，对应的闭包特性为FnOnce。默认无法再次使用.
    //&self，既不允许实现者移动对象也不允许修改，对应的闭包特性为Fn。
    //&mut self，允许实现者修改对象但不允许移动，对应的闭包特性为FnMut
    fn say(&self) {
        println!("hello {}, age: {}", self.name, self.age.get());
    }

    fn one_year(&mut self) {
        self.age.set(self.age.get() + 1);
    }

    fn another(self) -> Person {
        self.age.set(self.age.get() + 1);
        return self;
    }
}

fn main() {
    println!("{}", add(1, 2));
    //let x: i32 = diverges();
    //thread 'main' panicked at 'This function never returns', func_method.rs:15
    //note: Run with `RUST_BACKTRACE=1` for a backtrace.

    let num = 5;
    let plus_num = |x: i32| x + num;
    println!("{}", plus_num(1));

    let mut mn = 5;
    {
        let mut change_num = move |x: i32| {
            //copy
            mn += x;
            println!("{}", mn); //6
        };

        change_num(1);
        println!("{}", mn); //5
    }

    println!("{}", mn); //5

    let transform: fn(i32) -> i32 = add_one;
    let f0 = add_one(2i32) * 2;
    let f1 = apply(add_one, 2);
    let f2 = apply(transform, 2);
    println!("{}, {}, {}", f0, f1, f2); //6, 6, 6

    let closure = |x: i32| x + 1;
    let c0 = closure(2) * 2;
    let c1 = apply(closure, 2);
    let c2 = apply(|x: i32| x + 1, 2);
    println!("{}, {}, {}", c0, c1, c2); //6, 6, 6

    let box_fn = factory(1);
    let b0 = box_fn(2) * 2;
    let b1 = (*box_fn)(2) * 2;
    let b2 = (&box_fn)(2) * 2;
    println!("{}, {}, {}", b0, b1, b2); //6, 6, 6

    let add_num = &(*box_fn);
    let translate: &Fn(i32) -> i32 = add_num;
    let z0 = add_num(2) * 2;
    let z1 = apply(add_num, 2);
    let z2 = apply(translate, 2);
    println!("{}, {}, {}", z0, z1, z2); //6, 6, 6

    //lambda vs closure
    //lambda  只能取到调用时候的环境变量
    //closure 能保持住定义时候的环境变量
    let p1 = Person {
        name: "sun",
        age: Cell::new(20u8),
    };
    p1.say();

    let mut p2 = Person::new("hua", 20u8);
    p2.one_year();
    p2.say();

    let p3 = Person::new("s", 20u8);
    let p4 = p3.another(); //another variable
    //p3.say(); cannot use again
    p4.say();
}

fn add(x: i32, y: i32) -> i32 {
    x + y
}

#[allow(dead_code)]
fn diverges() -> ! {
    panic!("This function never returns");
}

fn add_one(x: i32) -> i32 {
    x + 1
}

fn apply<F>(f: F, y: i32) -> i32
    where F: Fn(i32) -> i32
{
    f(y) * y
}

fn factory(x: i32) -> Box<Fn(i32) -> i32> {
    Box::new(move |y| x + y)
}
