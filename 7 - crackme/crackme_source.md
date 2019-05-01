```java
// Array that defines the charset/alphabet 
charset = [abc…zABC…Z0123…9-];
// Array of indexes used to check the characters after the '-' symbol
my_index_array = [52,61,3, … ,11,50,25];

// Preliminary check on the flag
function global_check(flag){
	ris = 1;
	// Explicit check on some chars
	if( flag[3] == '{' && flag[36] == '}' && flag[18] == '-' && strncmp(flag, "flg", 3) ){
		// Loop to check that every char between the '{ … }' is in the charset  
		for(i = 4; i <= 35 && ris; i++){
			// Check the presence of the 'flag[i]' char into the 'charset' array
			ptr = strchr(charset, flag[i]);
			if (ptr == NULL){
				ris = 0;
			}
		}
	}else{
		ris = 0;
	}
	return ris;
}

// Check characters between '{' and '-'
function check_fisrt_part(flag){
	ris = 0;
	// Explicit checks on some chars and some operation between couples of 4 symbols. Remember that the hex chars are written in little endianness, so at the end you’ll need to write them 'backward'
	if( flag[4] == 'N' && flag[5] == 'x' && flag[6:10] == 'U2wR' && (flag[10:14] - flag[6:10] == "27FA3AF0") && ("713DD282" == ((XOR flag[6:10], flag[10:14]) + flag[14:18]) ){
		ris = 1;
	}
	return ris;
}

// Check characters between '-' and '}'
function check_second_part(flag){
	ris = 1;
	// Loop to analyze each char that is in between the  '-' and '}' symbols
	for(i = 0; i <=16 && ris; i++){
		// Explicit check
		if(flag[i+19] != charset[my_index_array[i]]){
			ris = 0;
		}
	}
	return ris; 
}

// Error function
function error(){
	print("Wrong flag! FORMAT …");
	exit(1);
}

// Function that aggregates the result of the 'check_fisrt_part' and 'check_second_part' methods
function check_full_flag(flag){
	ris = 0;
	if( check_fisrt_part(flag) && check_second_part(flag) ){
		ris = 1;
	}
	return ris;
}

// Main function
function main(){
	print("Insert the flag");
	// Read from standard input the 'flag'
	scanf("%63s", flag);
	if( strlen(flag) == 37 ){
		// Call the previous functions to check the inserted flag
		if(global_check(flag) && check_full_flag(flag)){
			print("Correct!")
		} else {
			error();
		}
	} else {
		error();
	}
}
```
