use std::sync::Arc;

fn make_counter() ->  Box< FnMut()-> Arc<i32>> {
    let mut count:Arc<i32> = Arc::new(0);
    Box::new(move || -> Arc<i32> {
        *Arc::make_mut(&mut count) += 1;
        let count = count.clone();
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
