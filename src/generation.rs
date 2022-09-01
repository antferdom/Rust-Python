pub fn has_close_elements(numbers: Vec<f64>, threshold: f64) -> bool {
    for idx in 0..numbers.len() {
        for idx2 in 0..numbers.len() {
            if idx != idx2 {
                let distance = (numbers[idx] - numbers[idx2]).abs();
                if distance < threshold {
                    return true;
                }
            }
        }
    }

    return ;
}