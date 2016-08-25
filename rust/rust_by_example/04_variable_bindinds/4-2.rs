fn main() {
    let long_live = 32;

    {
        let short_live = "a";
        println!("short:{}", short_live);
        let long_live = "shadowing";
        println!("shadow:{} ", long_live);
    }

    println!("long_live:{}", long_live);

    let long_live = "aaa";

    println!("shadow: {}", long_live);
}
