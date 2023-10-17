use std::fmt;

struct StringFlatHashTable{
    table_size: i32,
    indexed_values: Vec<&str>,
    key_hash_size: i32
};

trait StringHash{
    fn new(data: Vec<(&str, &str)>, table_size: usize, key_hash_size: usize) -> Self;
    fn hash_key(key_str: $str, key_hash_size: usize) -> usize;
    fn add_value(value: &str, source_indexed_values: &mut Vec<&str>) -> &Vec<&str>;
};

impl fmt::Display for StringFlatHashTable{
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "StringFlatHashTable(table_size: {}, indexed_table: {:?}, key_hash_size: {})",
               self.table_size, self.indexed_table, self.key_hash_size)
    }
}

impl StringHash for StringFlatHashTable {
    fn new(data: Vec<(&str, &str)>, table_size: usize, key_hash_size: usize) -> Self{
        data
    };
    fn hash_key(key_str: $str, key_hash_size: usize) -> usize;
    fn add_value(value: &str, source_indexed_values: &mut Vec<&str>) -> &Vec<&str>;
}