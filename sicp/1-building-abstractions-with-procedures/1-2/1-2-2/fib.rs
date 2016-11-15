fn main() {
    println!("{}", fib_recursive(6));
    println!("{}", fib_iteration(6));
}

fn fib_recursive(n: i32) -> i32 {
    if (n == 0) || (n == 1) {
        return n;
    } else {
        return fib_recursive(n-1) + fib_recursive(n-2);
    }
}

fn fib_iteration(n: i32) -> i32 {
    fn fib_iter(a: i32, b: i32, count: i32) -> i32 {
        if count == 0 {
            return b;
        } else {
            return fib_iter(a+b, a, count-1);
        }
    }

    return fib_iter(1, 0, n);
}
