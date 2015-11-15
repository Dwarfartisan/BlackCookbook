
fn make_counter() ->  Box< FnMut()-> i32> {
    let mut count = 0;
    Box::new(move || -> i32 {
        count += 1;
        return count;
    })
}

fn main() {
   let mut counter1 = make_counter();
   let mut counter2 = make_counter();
   let c = counter1();
   println!("counter 1 count: {}", c);
   println!("counter 1 count: {}", counter1());
   println!("counter 2 count: {}", counter2());
   println!("counter 1 count: {}", counter1());
   println!("counter 2 count: {}", counter2());
   println!("counter 2 count: {}", counter2());
   println!("counter 1 count: {}", counter1());
   println!("counter 2 count: {}", counter2());
   println!("counter 1 count: {}", counter1());
   println!("counter 1 count: {}", counter1());
}
