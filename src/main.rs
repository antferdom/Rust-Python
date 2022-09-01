mod generation;

fn main() {
    println!("Hello, world!");

    let mut vec: Vec<f64> = vec![1., 2., 3.];
    let threshold: f64 = 1.5;

    println!("The result is {}", generation::has_close_elements(vec, threshold));

}
