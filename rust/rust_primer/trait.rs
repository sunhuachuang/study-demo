use std::fmt::Debug;

trait HasArea {
    fn area(&self) -> f64;
}

#[allow(dead_code)]
struct Circle {
    x: f64,
    y: f64,
    radius: f64,
}

impl HasArea for Circle {
    fn area(&self) -> f64 {
        std::f64::consts::PI * (self.radius * self.radius)
    }
}

#[allow(dead_code)]
#[derive(Debug)]
struct Square {
    x: f64,
    y: f64,
    side: f64,
}

impl HasArea for Square {
    fn area(&self) -> f64 {
        self.side * self.side
    }
}

fn print_area<T: HasArea>(shape: &T) {
    println!("this is shape has area is {}", shape.area());
}

fn multi_trait<T: HasArea, K: HasArea + Debug>(x: &T, y: &K) {
    println!("{}", x.area());
    println!("{:?}", y);
}

fn multi_trait_2<T, K>(x: &T, y: &K)
    where T: HasArea,
          K: HasArea + Debug
{
    println!("{}", x.area());
    println!("{:?}", y);
}

trait Foo {
    fn foo(&self);
    fn bar(&self) {
        println!("call a default bar");
    }
    fn anotherbar() {
        println!("call another default bar");
    }
}

trait FooBar: Foo {
    fn foobar(&self);
}

struct Baz;

impl Foo for Baz {
    fn foo(&self) {
        println!("baz foo");
    }
}

impl FooBar for Baz {
    fn foobar(&self) {
        println!("baz foobar");
    }
}

#[allow(unused_variables)]
fn main() {
    let c = Circle {
        x: 1.0,
        y: 2.0,
        radius: 3.0,
    };

    let s = Square {
        x: 1.0,
        y: 2.0,
        side: 3.0,
    };

    print_area(&c);
    print_area(&s);
    println!("{}, {}", 9 / 10 == 0.9 as i32, 9 / 10); //true, 0 向下取值

    multi_trait(&c, &s);
    multi_trait_2(&c, &s);

    let b = Baz;
    b.foo();
    b.bar();
    b.foobar();

    /** 泛型
     * enum Option<T> {
     *     Some(T),
     *     None,
     * }
     */
    let x: Option<i32> = Some(5);
    let y: Option<f64> = Some(5.1f64);
    println!("{:?}, {:?}", x, y);

    let couple = make_pair("mail", "femail");
    println!("{:?}", couple);

    /**
     * 对于多态函数，存在两种派分 (dispatch) 机制：静态派分和动态派分
     * rust/c++ 采用静态派分, 编译器，用指定类型的特殊函数替换函数调用。
     * go/java 采用动态派分，用interface实现，运行期间，查找虚表(vtable).
     */
    let p1 = Point { x: 0, y: 0 };
    let p2 = Point { x: 0.1, y: 0.2 };
    println!("{:?}, {:?}", p1, p2); //Point { x: 0, y: 0 }, Point { x: 0.1, y: 0.2 }

    let graph = SimpleGraph;
    let object = Box::new(graph) as Box<Graph2<N = Node, E = Edge>>;
}

//generic function
fn make_pair<T, U>(a: T, b: U) -> (T, U) {
    (a, b)
}

//generic struct
#[derive(Debug)]
struct Point<T> {
    x: T,
    y: T,
}

//use generic parameters
trait Graph<N, E> {
    fn has_edge(&self, &N, &N) -> bool;
    fn edge(&self, &N) -> Vec<E>;
}

#[allow(dead_code, unused_variables)]
fn distance<N, E, G: Graph<N, E>>(graph: &G, start: &N, end: &N) -> u32 {
    1u32
}

//use associated types
trait Graph2 {
    type N;
    type E;

    fn has_edge(&self, &Self::N, &Self::N) -> bool;
    fn edges(&self, &Self::N) -> Vec<Self::E>;
}

#[allow(dead_code, unused_variables)]
fn distance2<G: Graph2>(graph: &G, start: &G::N, end: &G::E) -> u32 {
    1u32
}

struct Node;
struct Edge;
struct SimpleGraph;

#[allow(unused_variables)]
impl Graph2 for SimpleGraph {
    type N = Node;
    type E = Edge;

    fn has_edge(&self, n1: &Node, n2: &Node) -> bool {
        true
    }

    fn edges(&self, n: &Node) -> Vec<Edge> {
        let e = Edge;
        vec![e]
    }
}
