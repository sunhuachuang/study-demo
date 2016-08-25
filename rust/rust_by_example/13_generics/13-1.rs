#![allow(unused_variables)]
struct T;
struct S(T);
struct SGen<T>(T);

fn die_regular(s: S) {}

fn die_generic_specialized_t(s: SGen<T>) {}

fn die_generic_specialized_i32(s: SGen<i32>) {}

fn die_generic<T>(s: SGen<T>) {}

fn main() {
    die_regular(S(T));
    die_generic_specialized_t(SGen(T));
    die_generic_specialized_i32(SGen(6));

    die_generic::<char>(SGen('a'));
    die_generic(SGen('c'));
}
