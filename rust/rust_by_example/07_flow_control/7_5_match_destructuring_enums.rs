#[allow(dead_code)]
#[derive(Debug)]

enum Color {
    Red,
    Blue,
    Green,
    RGB(u32, u32, u32),
    HSV(u32, u32, u32),
    HSL(u32, u32, u32),
    CMY(u32, u32, u32),
    CMYK(u32, u32, u32, u32),
}

fn main() {
    let color = Color::RGB(122, 17, 40);
    println!("what color is it?");

    match color {
        Color::Red    => println!("the color is red"),
        Color::Blue   => println!("the color is blue"),
        Color::Green  => println!("the color is green"),
        Color::RGB(r, g, b) => println!("red:{}, greeb{}, blue{}", r, g, b),
        Color::HSV(h, s, v) => println!("hue{}, saturation{}, value{}", h, s, v),
        Color::HSL(h, s, l) => println!("hue{}, saturation{}, lightness{}", h, s, l),
        Color::CMY(c, m, y) => println!("cyan{}, meganta{}, yellow{}", c, m, y),
        Color::CMYK(c, m, y, k) => println!("cyan{}, meganta{}, yellow{}, key{}", c, m, y, k),
    }
}
