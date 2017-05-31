use std::rc::Rc;
use std::sync::Arc;
use std::thread;

/// Rc 单线程
/// Arc 多线程

/// 多个对象使用同一个对象
struct Owner {
    name: String,
}

struct Gradget {
    id: i32,
    owner: Rc<Owner>,
}

fn main() {
    let five = Rc::new(5);
    let five2 = five.clone();
    let five3 = five.clone();
    println!("{}, {}, {}", five, five2, five3);

    let f = Rc::new(5);
    let weak_f = Rc::downgrade(&f);
    let strong_f: Option<Rc<_>> = weak_f.upgrade();
    println!("{:?}, {:?}", weak_f, strong_f); //(Weak), Some(5)

    let numbers: Vec<_> = (0..100u32).collect();
    let shared_numbers = Arc::new(numbers);

    for i in 0..10 {
        let child_numbers = shared_numbers.clone();

        thread::spawn(move || {
                          let local_numbers = &child_numbers[..];
                          println!("{}: {:?}", i, local_numbers[i]);
                      });
    }

    let own: Rc<Owner> = Rc::new(Owner { name: String::from("sun") });
    let g1 = Gradget {
        id: 1,
        owner: own.clone(),
    };
    let g2 = Gradget {
        id: 2,
        owner: own.clone(),
    };
    drop(own);

    println!("Gadget {} owned by {}", g1.id, g1.owner.name);
    println!("Gadget {} owned by {}", g2.id, g2.owner.name);
}
