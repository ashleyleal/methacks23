<?php
// Get the user input value from the request body
$userInput = file_get_contents('php://input');

// Open the text file for writing
$file = fopen("user_input.txt","a");

// Write the user input value to the text file
fwrite($file,$userInput."\n");

// Close the text file
fclose($file);
?>
