#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <openssl/sha.h>

// #define PWDBUFFER 50
#define PWDBUFFER 20
#define HASHSIZE 32
#define FLAGSIZE 128

int main(void) {
	FILE *file;
	unsigned char flag[FLAGSIZE];
	unsigned char correct_hash[HASHSIZE] = {
		0x71, 0xa9, 0x86, 0xaa, 0xf6, 0x26, 0xbf, 0xb8, 0x05, 0x90, 0xb1, 0xac, 0x93, 0x74, 0x5d, 0x25, 0x79, 0xba, 0xf0, 0xa7, 0xaa, 0x98, 0xd1, 0x66, 0xc4,0x04, 0xb8, 0xf5, 0x75, 0x77, 0xae, 0x88
	};
	unsigned char computed_hash[HASHSIZE];
	unsigned char password[PWDBUFFER];

	printf("Insert your password: ");
	scanf("%49s", password);
	printf("%s\n",password);
	SHA256(password, strlen((char *)password), computed_hash);
	if(memcmp(computed_hash, correct_hash, HASHSIZE) == 0) {
		printf("CORRECT PASSWORD!\n");
		file = fopen("flag", "r");
		if(file != NULL) {
			fscanf(file, "%s", flag);
			fclose(file);
			printf("Flag: %s\n", flag);
		} else {
			printf("Error while opening the flag file\n");
		}
	} else {
		printf("WRONG PASSWORD!\n");
	}
	fflush(stdout);

	return 0;
}

