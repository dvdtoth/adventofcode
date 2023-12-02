use std::fs::File;
use std::io::Read;

// Iterate through each line of a file
// For each line as a string, identify the first and last digit present and add them together and add to the sum
// If a single digit is present, double it and add it to the sum
// Return the sum
fn main() {
    let mut sum = 0;
    let mut file = File::open("input").unwrap();
    let mut contents = String::new();
    file.read_to_string(&mut contents).unwrap();
    for line in contents.lines() {
        let mut digits = Vec::new();
        for c in line.chars() {
            if c.is_digit(10) {
                digits.push(c.to_digit(10).unwrap());
            }
        }
        if digits.len() != 0 {
            let  first = digits.first().unwrap();
            let  last = digits.last().unwrap();
            let  line_num = first.to_string() + &last.to_string();
            sum += line_num.parse::<u32>().unwrap();
        }
    }
    println!("{}", sum);
}