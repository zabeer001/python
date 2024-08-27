<?php
// Function to check if a number is prime
function isPrime($num) {
    if ($num <= 1) {
        return false;
    }
    if ($num <= 3) {
        return true;
    }
    if ($num % 2 == 0 || $num % 3 == 0) {
        return false;
    }
    for ($i = 5; $i * $i <= $num; $i += 6) {
        if ($num % $i == 0 || $num % ($i + 2) == 0) {
            return false;
        }
    }
    return true;
}

// Input array
$array = [10, 7, 13, 22, 17, 18, 29];

// Filtering primes
$prime_array = array_filter($array, 'isPrime');

// Print the result
print_r($prime_array);
?>
