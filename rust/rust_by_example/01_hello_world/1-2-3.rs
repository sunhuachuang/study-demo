use std::fmt::{self, Formatter, Display};

struct City {
    name: &'static str,
    lat: f32,
    lon:f32,
}

impl Display for City {
    fn fmt(&self, f: &mut Formatter) -> fmt::Result {
        let lat_c = if self.lat >= 0.0 { 'N' } else { 'S' };
        let lon_c = if self.lon >= 0.0 { 'E' } else { 'W' };

        write!(f, "{}: {:.3}du{} {:.3}du{}",
               self.name, self.lat.abs(), lat_c, self.lon.abs(), lon_c
               )
    }
}

/* { : }
? -> Debug
o -> Octal(八进制)
b -> Binary(二进制)
p -> Pointer(指针)
x -> LowerHex
X -> UpperHex
e -> LowerExp
E -> UpperExp
*/
fn main() {
    for city in [
        City { name: "A", lat:53.23456, lon:-6.764221 },
        City { name: "B", lat:64.2, lon:4.3 },
        City { name: "C", lat:-90.34, lon:-2.76 },
    ].iter() {
        println!("{}", *city);
    }
}
