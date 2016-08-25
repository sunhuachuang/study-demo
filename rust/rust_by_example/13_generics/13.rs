struct T;

// it use 'T'
struct Single(T);

//it is generics
struct SingleGen<T>(T);

fn main() {
    let _s = Single(T);

    let _char: SingleGen<char> = SingleGen('a');

    let _t = SingleGen(T);

    let _i32 = SingleGen(6);
}
