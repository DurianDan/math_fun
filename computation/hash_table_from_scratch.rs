use std::fmt;

struct StringFlatHashTable {
    table_size: i32,
    buckets: Vec<String>,
    key_hash_size: i32,
}

trait StringHash {
    fn new(table_size: usize, key_hash_size: usize) -> Self;
    fn hash_key(&self, key_str: &str) -> i32;
    fn insert(&mut self, key: &str, value: &str) -> i32;
    fn lookup(&self, key: &str) -> &str;
}

impl fmt::Display for StringFlatHashTable {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "StringFlatHashTable(table_size: {}, buckets: {:?}, key_hash_size: {})",
               self.table_size, self.buckets, self.key_hash_size)
    }
}

impl StringHash for StringFlatHashTable {
    fn new(table_size: usize, key_hash_size: usize) -> Self {
        let buckets = Vec::with_capacity(table_size);
        StringFlatHashTable {
            table_size: table_size as i32,
            buckets,
            key_hash_size: key_hash_size as i32,
        }
    }

    fn insert(&mut self, key: &str, value: &str) -> i32 {
        self.buckets[self.hash_key(key)] = value.to_owned();
        0
    }

    fn lookup(&self, key: &str) -> &str {
        &self.buckets[self.hash_key(key) as usize]
    }

    fn hash_key(&self, key_str: &str) -> i32 {
        let slice = key_str.get(0..self.key_hash_size);
        let mut sum_ascii = 0;
        for char in slice.chars() {
            sum_ascii += char as u8
        }
        return (sum_ascii % self.table_size as u8) as i32;
    }
}

fn main() {
    let mut test_table = StringFlatHashTable::new(100, 4);
    test_table.insert("ok", "ok1");
    println!("{}", test_table.lookup("ok")); // Should print "ok1"
}
