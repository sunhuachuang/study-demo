fn main() {
    let mut _integer = 5;

    {
        let _ref_interger = &_integer;
       //_integer = 4;
    }

   _integer = 4;
}
