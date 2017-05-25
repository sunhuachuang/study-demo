use std::time;
use std::collections::HashMap;

/// vec 不同于 array
/// O(1)随机访问, O(1)尾部增加删除
/// Vec<T> T的size是固定的,对于不固定的,可以用box包裹,使得其变成固定的指针大小
fn main() {
    let mut v: Vec<i32> = Vec::new();
    v.push(1);
    let mut v2 = (0..5).collect::<Vec<i32>>();
    v2.push(1);

    let mut v = vec![1, 2, 3];
    v.pop();
    println!("{:?}", v);
    let vv = vec![0; 10]; //[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    println!("{:?}", vv);

    //从迭代器生成
    let mut vvv: Vec<_> = (1..5).collect();
    println!("{:?}", vvv); //[1, 2, 3, 4]

    //不用下标访问
    println!("{}", vvv[1]);
    println!("{}", vvv[2usize]);

    //推荐使用 返回 Option<T> => Some() or None
    println!("{:?}", vvv.get(1)); //Some(2)
    println!("{:?}", vvv.get(4)); //None
    println!("{:?}", vvv.get_mut(2));

    //引用
    for i in &vvv {
        println!("{}", i);
    }

    for i in vvv.into_iter() {
        println!("{}", i);
    }

    //println!("{:?}", vvv); 所有权已经转移

    //test push效率
    let mut vt: Vec<usize> = vec![];
    push_1m(&mut vt, 5_000_000);

    //预先分配内存, 效率高
    let mut vt: Vec<usize> = vec![];
    vt.reserve(5_000_000);
    push_1m(&mut vt, 5_000_000);

    //HashMap
    let mut hash = HashMap::new();
    hash.insert("sun", 123);
    hash.insert("hua", 234);

    if hash.contains_key("sun") {
        println!("got sun: {:?}, all: {}", hash.get("sun"), hash.len()); //got sun: Some(123), all: 2
    }

    hash.remove("sun");

    let mut hash2 = HashMap::new();
    for c in "孙华闯孙华闯孙a".chars() {
        let counter = hash2.entry(c).or_insert(0);
        *counter += 1;
    }
    println!("{:?}", hash2);
}

fn push_1m(v: &mut Vec<usize>, total: usize) {
    let e = time::SystemTime::now();

    for i in 1..total {
        v.push(i);
    }

    let ed = time::SystemTime::now();
    println!("time: {:?}", ed.duration_since(e).unwrap());
}
