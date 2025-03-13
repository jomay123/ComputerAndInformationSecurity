#include <stdio.h>
#include <ctype.h>
#include <string.h>

#define ALPHABET_SIZE 26

int main() {
    char ciphertext[] = "jaran bkncap sdwp ukq wna, bkn oqna#hu pda sknhz se$hh jkp";
    for (int shift = 0; shift < ALPHABET_SIZE; shift++) {
        printf("Shift %d: ", shift);
        
        for (int i = 0; i < strlen(ciphertext); i++) {
            char c = ciphertext[i];

            if (islower(c)) {
                // Decrypt lowercase letters
                char decrypted_char = ((c - 'a' - shift + ALPHABET_SIZE) % ALPHABET_SIZE) + 'a';
                printf("%c", decrypted_char);
            } else if (isupper(c)) {
                // Decrypt uppercase letters
                char decrypted_char = ((c - 'A' - shift + ALPHABET_SIZE) % ALPHABET_SIZE) + 'A';
                printf("%c", decrypted_char);
            } else if (isspace(c)) {
                // Keep spaces
                printf(" ");
            }
            else if (c == ','){
                printf(",");
            }
            // Skip all other special characters
        }
        
        printf("\n");
    }
    
    return 0;
}
