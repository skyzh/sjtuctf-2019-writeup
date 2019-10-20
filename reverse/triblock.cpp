#include <iostream>
#include <algorithm>

using namespace std;

char key[] = "welcome_to_0ops!";


unsigned char answer[] = {
        0xE4, 0x15, 0x57, 0x4,
        0xC5, 0xB1, 0xAA, 0x52,
        0xAE, 0xC9, 0x80, 0xB3,
        0x58, 0x95, 0xFF, 0x7E
};

unsigned char answer_2[] = {
        0xA8, 0x58, 0xCB, 0x76,
        0xC5, 0xC9, 0x17, 0x62,
        0x7F, 0xD5, 0x45, 0x36,
        0xA1, 0x49, 0x60, 0x32
};

void initialize() {
    int i = 0;
    while (i < 0x10) {
        key[i] = key[i] ^ 7;
        i = i + 1;
    }
}

using byte = unsigned char;
using uint = unsigned int;

void generate_key(char *key, char *key_store) {
    int iVar1;
    uint uVar2;
    int local_18;
    int ch;
    int i;

    local_18 = 0;
    ch = 0;
    while (ch < 0x100) {
        key_store[ch] = (char) ch;
        ch = ch + 1;
    }
    i = 0;
    while (i < 0x100) {
        iVar1 = (uint) (byte) key_store[i] + local_18 + (int) key[i % 0x10];
        uVar2 = (uint) (iVar1 >> 0x1f) >> 0x18;
        local_18 = (iVar1 + uVar2 & 0xff) - uVar2;
        swap(key_store[i], key_store[local_18]);
        i = i + 1;
    }
}


void decrypt(char *key_store, char *cipher, char *message) {
    int i;
    int j;
    unsigned long k;

    i = 0;
    j = 0;
    k = 0;
    while (k < 0x10) {
        i = i + 1U & 0xff;
        j = (uint) (byte) key_store[i] + j & 0xff;
        swap(key_store[i], key_store[j]);
        message[k] = cipher[k] ^ key_store[(byte) (key_store[j] + key_store[i])];
        k = k + 1;
    }
    return;
}


int phase_1() {
    initialize();
    char key_store[0x100];
    char message[0x100] = {0};
    char plain_text[0x100] = {0};
    for (int i = 0; i < 0x10; i++) {
        char key_backup[0x100];
        for (int j = 0; j < 0x100; j++) {
            generate_key(key, key_store);
            plain_text[i] = j;
            decrypt(key_store, plain_text, message);
            if ((unsigned char) message[i] == answer[0x10 - i - 1]) {
                cout << j << " " << (char) j << "    ";
                break;
            }
        }
        cout << endl;
    }
    cout << plain_text << endl;
    return 0;
}

int main() {
    char phase1_plain_text[] = "this_is_not_flag";
    char key_store[0x100];
    char message[0x100] = {0};
    char plain_text[0x100] = {0};
    initialize();
    generate_key(key, key_store);
    decrypt(key_store, phase1_plain_text, message);
    for (int i = 0; i < 0x10; i++) phase1_plain_text[i] ^= key[i];
    for (int i = 0; i < 0x10; i++) {
        char key_backup[0x100];
        for (int j = 0; j < 0x100; j++) {
            memcpy(key_backup, key_store, sizeof(key_store));
            plain_text[i] = j;
            decrypt(key_backup, plain_text, message);
            if ((unsigned char) message[i] == answer_2[0x10 - i - 1]) {
                cout << char(j ^ key[i]);
                break;
            }
        }
    }
    cout << message << endl;
    return 0;
}
