#include <math.h>
#include <stdio.h>
#include <string.h>
#include <strings.h>
#include <unistd.h>
#include <stdlib.h>
#include <openssl/sha.h>

#define RED   "\x1B[31m"
#define GRN   "\x1B[32m"
#define YEL   "\x1B[33m"
#define BLU   "\x1B[34m"
#define MAG   "\x1B[35m"
#define CYN   "\x1B[36m"
#define WHT   "\x1B[37m"
#define RST "\x1B[0m"
#define INF  BLU "[" GRN "*" BLU "] "


const char *banner = (
	BLU
	"     WELCOME TO THE \n"
	"          STAR MASS CALCULATOR SERVICE\n\n"
	RST);
const char *cosmos = (
	"                     .                  " YEL "." RST "\n"
	"                     .                  " YEL ";" RST "\n"
	GRN "        *" RST "            :       " YEL "       - --+- -" RST "\n"
	"                *    !           .      " YEL "!" RST "\n"
	"                     |        .         " YEL "." RST "\n"
	"                    _|_         +\n"
	"                  ,  | `.\n"
	"            --- --+-" RED "<#>" RST "-+- ---  --  -\n"
	"  *   '*          `._|_,'\n"
	"                     T\n"
	"        " MAG " * " RST "          |                     *'\n"
	"                     !\n"
	"                     :    " WHT "     . :" RST "\n"
	"                     .    " WHT "   *     " RST "          .\n"
	);
const unsigned char correct_hash[20] = {
	0xdd, 0xb1, 0xed, 0xa7, 0xc7, 0x4d, 0x71, 0xa2, 0x3b, 0x40,
	0x34, 0xcd, 0x43, 0xc3, 0xd5, 0x88, 0x7b, 0x87, 0x45, 0xf6
};

void
readline(char *buf, int size) {
	int i, c;

	i = 0;
	c = getchar();
	while(c != '\n' && c != EOF) {
		if(i<size) {
			buf[i++] = c;	
		}
		c = getchar();
	}
	buf[i] = '\0';
}

void
err(const char *errstr) {
	fprintf(stderr, RED "[!] %s" RST "\n", errstr);
	exit(1);
}

void
calc(void) {
	char name[64], buf[64];
	double lum;

	printf(INF "Name of the star > " RST);
	fflush(stdout);
	readline(name, 63);
	
	printf(INF "Luminosity > " RST);
	fflush(stdout);
	readline(buf, 63);
	lum = strtod(buf, NULL);

	printf(INF "The mass of ");
	printf(name);
	printf(" is %.2lf solar masses" RST "\n", pow(lum, 0.2857));
	fflush(stdout);
}

int
unlock_db(void) {
	unsigned char hash[20];
	char key[32];
	int c, i = 0;

	printf(INF "Insert database key > " RST);
	fflush(stdout);

	c = getchar();
	while(c != '\n') {
		key[i++] = c;
		c = getchar();
	}
	key[i] = '\0';

	SHA1((unsigned char *)key, strlen(key), hash);
	if(memcmp(hash, correct_hash, 20) == 0) {
		return 1;
	} else {
		return 0;
	}
}

void
dumpdb(void) {
	int c;
	FILE *f;

	f = fopen("stars.csv", "r");
	if(f == NULL) {
		err("Error while opening the database");
	}
	while((c = fgetc(f)) != EOF) {
		putchar(c);
	}
	fclose(f);
	fflush(stdout);
}

int
main(void) {
	printf("\n\n%s\n%s", banner, cosmos);
	fflush(stdout);
	calc();
	sleep(3);
	if(unlock_db()) {
		dumpdb();
	} else {
		err("Wrong database key");
	}
	
	return 0;
}
