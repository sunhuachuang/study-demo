fn main() {
    println!("{}", factorial(5));
    println!("{}", factorial2(6));
}

fn factorial(n: i32) -> i32 {
    if n == 1 {
        return 1;
    } else {
        return n * factorial(n-1);
    }
}

fn factorial2(n: i32) -> i32 {
    return fact_iter(1, 1, n);
}

fn fact_iter(product: i32, counter: i32, maxn: i32) -> i32 {
    if counter > maxn {
        return product;
    } else {
        return fact_iter(product*counter, counter+1, maxn);
    }
}
