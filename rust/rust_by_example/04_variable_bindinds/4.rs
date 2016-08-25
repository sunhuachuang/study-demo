fn main() {
    let an_integer = 1u32;
    let a_boolean = true;
    let unit = ();

    let copied_integer = an_integer;

    println!("int:{}, bool:{}, unit:{:?}, copied:{}", an_integer, a_boolean, unit, copied_integer);

    let _unused = "aaa";
}
