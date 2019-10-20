# SJTU CTF 2019 Write-up

## Crypto
### babyblock
It’s obvious that this encryption use the same key and a plaintext-dependent VI every time.
First of all, we may brute force sum of the flag plaintext string. Refer to `brute_force_message.py` to see how it works. This script generates a bash script to send request to server with strings of different sum. With the condition that ciphertext begins with `0ops{`, if we observe any reply that has the same first five bytes with ciphertext of the encrypted flag, we can obtain the sum of the original plaintext. In this case it is `2740`.
Then we may obtain characters in the flag one by one. Refer to `decrypt.py` for details. The program generates plaintext to be encrypted on server, then it asks for ciphertext. With the equation that `cipher ^ plain = cipher_payload ^ plain_payload`, we can obtain the flag in less than 30 steps.
### babylcg
First of all we need to solve work of proof. This can be easily done with brute force. Refer to `work.py` for details.
Then we may solve the challenge one by one.
Challenge 0 is easy. Just copy-paste the LCG algorithm.
For challenge 1, with equation that `m * x + c = next_x (mod p)`, we may obtain `c` with `c = next_x - m * x (mod p)`.
For challenge 2,
```
a1 = m * a0 + c (mod p)
a2 = m * a1 + c
a3 = m * a2 + c 
```
Hence, `a2 - a1 = m * (a1 - a0)`, we may obtain that `m = (a2 - a1) * (a1 - a0)^-1`
Therefore, `c` can be obtained with the method described in challenge 1.
For challenge 3, we should solve an equation. [THERE SHOULD BE A REFERENCE]. Refer to `challenge_3.py` for implementation.
### babyrsa
For p and q in this RSA algorithm, we assume that
```
p = 10^256 * a + b
q = 10^256 * b + a
```
Therefore,
```
n = p * q = 10^512 * ab + 10^256 * (a + b) + ab
```
As both a, b < 10^256, we can obtain `a*b`, and then obtain `a + b`. As a, b are known, we may obtain p, q. Then we can decrypt the ciphertext with standard RSA methods.
### CRC Forgery
As plaintext, CRC and CRC algorithm are known, we may backtrack the missing 64 bits.
Let `cipher_msg = 00...00 + CRC`, `plain_msg = message + const`
At the i-th iteration of CRC algorithm, the `length - i` bits haven’t been altered. Therefore, we may do the reverse algorithm. For current reverse iteration, if `cipher_msg[(i+64) bit] != plain_msg[(i+64) bit]`, then this bit should be flipped at i-th iteration. XOR cipher message with poly until we obtain what the missing bits should be before calculating CRC of the remaining bits `blank_after_bits`.
Then we calculate CRC from beginning to the missing blanks. We obtain what the missing blanks look like after calculating previous bits. We assume that value to be `blank_before_bits`
It’s obvious that `blank_after_bits ^ blank_before_bits = blank_bits`. Then we obtain the result.
### Mixed Cipher
From the Python script we observe that this encryption does two things. First of all, mapping each character to other character, aka. CAESAR encryption. Then, it XOR each byte with a key stream, where key is a constant size.
Therefore, we may first guess key length. As key and message are visible characters, we can brute force different key length. We enumerate: 1. Stride 2. Every position of the key 3. Possible character of key in this position. The correct combination should render the plaintext in visible characters. After several trials, we found that key length is 29.
Then we just guess the key. Fortunately, the key is not a random string. After determining some characters, we may fill the blanks according to the generated `mappings.txt`, just like what we did in high school entrance examination. Then we obtain the key.
Now we’re left with a CAESAR-encrypted ciphertext. With some online tools we can easily obtain the result. [REFERENCE]
## Reverse
### snake
It is easily observed that this is a Python byte-code file. Just decompile it, we get a function with a lot of if statements. Follow logic of the conditions to construct the flag.
### chaos
It seems that the ELF binary is corrupted, so we can’t decompile it with Ghidra. Attach gdb to the process, it seems that it’s running something like CAESAR cipher. Find where the input, ciphertext and encryption rule are on stack. Then write a simple program to decrypt it.
### triblock
The encryption is hidden in 3 parts: INIT, FIN and main function. Decompile it with Ghidra. We obtain the flag in two steps.
First, reversing the encryption method in main. We can easily guess what do some of the functions do, such as `generate_key_from_string`, `encrypt` and `reverse`. Then analyze what the ciphertext is. From INIT function and ELF binary we may reverse what ciphertext is in memory. Then brute force the plaintext. It turned out to be `this_is_not_flag`.
Then we do the second part of the reversing in FIN. Indeed this part of code will never be executed. As encrypt is stateful, which means that what we’ve encrypted last time will affect what we obtain this time, we must run decrypt on phase 1 plaintext to preserve the original program flow. Then it’s easy brute force the plain text with the same method.
## Web
## basic_web
Just look at the source code.
## ezxxe
XXE exploitation with Java. Note that `flag` is a directory.
## Message board
Just a kind of XSS. Build a server, brute force the md5, and let the admin visit. Then you get the flag.
But there’s another problem. `view.php` explicitly cleared the cookie. Then XSS Audit came to help. [REFERENCE]. By constructing an URL to disable clearing flag scripts, we obtain the flag on our server.
## Misc
### anti-hack11
Never reinvent the wheel. Just download a Chrome extension to solve the captcha, and modify it to run on CTF server. You may refer to `anti-hack11.diff`. [REFERENCE]
### anti-hack10
Use volidity to analyze the core dump. [REFERENCE] Flag is in memory region of `mspaint.exe`. Use GIMP to view the memory as raw image. Adjust the width and the flag will be shown. [REFERENCE]
### sqlmap yibasuo
The `sqlmap` utility guess what’s inside the database one character by one. With Wireshark filter `http.request_in`, we can see all request sent by `sqlmap`. Then find `!=` in HTTP POST form. In this way we obtain the flag.
### weird logo
With `pngcheck` we find there’re hidden data at the end of the image. That’s a zip file in reverse byte order. Then we can get a QR code from the image by bit-and 1 lowest bit in pixels of each channel. Refer to `weird_logo.py`. [REFERENCE] Scanning the QR code we obtain the password of the zip file.
### animal
Just pickle with latest protocol of Python pickle. Here I use a special way to construct the payload automatically.
### dog
For the first layer of encryption, there’s no password indeed. Use `ZipCenOp.jar` to remove the password.
For the second layer, there’re base32 encoded password at the end of the file.
Then use `cat * > all.jpg` to get the image. Use binwalk to extract another zip. From EXIF data we obtain the password of the zip.
Finally brute force the password with john. It turns out to be a 8-digit number.
