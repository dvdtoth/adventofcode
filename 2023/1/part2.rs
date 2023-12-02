use std::collections::HashMap;
use std::fs::File;
use std::io::Read;

// Iterate through each line of a file
// For each line identify the first and last digit present. Concatenate them and add to the sum.
fn main() {
    let digitmap = HashMap::from([
        ("eight", 8),
        ("zero", 0),
        ("one", 1),
        ("two", 2),
        ("three", 3),
        ("four", 4),
        ("five", 5),
        ("six", 6),
        ("seven", 7),
        ("nine", 9),
    ]);

    let mut sum = 0;
    let mut file = File::open("input").unwrap();
    let mut contents = String::new();
    file.read_to_string(&mut contents).unwrap();
    for line in contents.lines() {
      

        let mut digits = Vec::new();
        // Iterate through the subscring character by character and if there's a match from digitmap, add it to the digits vector
        // watch out for overlapping words
        // let mut output = String::new();
        let mut i = 0;
        while i < line.len() {
            for (key, value) in &digitmap {
                if line[i..].starts_with(key) {
                    digits.push(value);
                }
            }

            // there's surely a nicer way to do this
            if line[i..].starts_with("0") {
                digits.push(&0);
            } else if line[i..].starts_with("1") {
                digits.push(&1);
            } else if line[i..].starts_with("2") {
                digits.push(&2);
            } else if line[i..].starts_with("3") {
                digits.push(&3);
            } else if line[i..].starts_with("4") {
                digits.push(&4);
            } else if line[i..].starts_with("5") {
                digits.push(&5);
            } else if line[i..].starts_with("6") {
                digits.push(&6);
            } else if line[i..].starts_with("7") {
                digits.push(&7);
            } else if line[i..].starts_with("8") {
                digits.push(&8);
            } else if line[i..].starts_with("9") {
                digits.push(&9);
            }
            i += 1;
        }


        if digits.len() != 0 {
            let first = digits.first().unwrap();
            let last = digits.last().unwrap();
            let line_num = first.to_string() + &last.to_string();
            sum += line_num.parse::<u32>().unwrap();
        }
    }
    println!("{}", sum);
}
