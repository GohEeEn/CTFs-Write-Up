# Space Snack

## Category

misc

## Write Up

### Task 1

__Given__ :

```text
Vg nccrnef lbh unq jung vg gnxrf gb fbyir gur svefg pyhr
Jryy Qbar fcnpr pnqrg
pgs{Lbh_sbhaq_gur_ebg}
Npprff pbqr cneg 1: QO 
```

__Decoded__ (ROT13) :

```text
It appears you had what it takes to solve the first clue
Well Done space cadet
ctf{You_found_the_rot}
Access code part 1: DB
```

### Task 2

__Given__ :

```text
Jhlzhy ulcly dhz clyf nvvk ha opkpun tlzzhnlz.
jam{Aol_vul_aybl_zhshk}
jvkl whya: NW
```

__Decoded__ (Caesar Cipher, rotation=7) :

```text
Caesar never was very good at hiding messages.
ctf{The_one_true_salad}
code part: GP
```

### Task 3

__Given__ :

```text
RXZlbiAgaW4gc3BhY2Ugd2UgbGlrZSB0aGUgYnV0dGVyeSBiaXNjdXQgYmFzZS4gY3Rme0lfbGlrZV90aGVfYnV0dGVyeV9iaXNjdWl0X2Jhc2V9IC4gQWNjZXNzIHBhcnQgMzogWEQ=
```

Decoded (Base64) :

```text
Even  in space we like the buttery biscut base. ctf{I_like_the_buttery_biscuit_base} . Access part 3: XD
```

### Task 4

__Given__ :

```text
.. -. ... .--. . -.-. - --- .-. / -- --- .-. ... . / .-- --- ..- .-.. -.. / -... . / .--. .-. --- ..- -.. / --- ..-. / -.-- --- ..- .-. / . ..-. ..-. --- .-. - ... .-.-.- / -.-. - ..-. ---... ... .--. .- -.-. . -.. .- ... .... ..--- ----- ..--- .---- / .- -.-. -.-. . ... ... / -.-. --- -.. . ---... / .--- --...
```

__Decoded__ (Morse Code) :

```text
INSPECTORMORSEWOULDBEPROUDOFYOUREFFORTS.CTF:SPACEDASH2021ACCESSCODE:J7
```

### Task 5

Docker container will never named `boring_wozniak`, because of the logic (line 844 to 846) in 
file [names-generator.go](https://github.com/moby/moby/blob/c90254c7464cac5c56e7ab9e6b1857c119d5d263/pkg/namesgenerator/names-generator.go) from the source code

### Task 6

__Given__ the PIN generation algorithm :

```c
int generatePin() {
    srand(time(0));
    return rand();
}
```

and also the required timezone be __UTC__

By adjusting the seeding long integer to `UTC +0:00` (check [here](https://www.epochconverter.com/timezones)), you should be able to get the correct PIN (see `task6.c`)

### Task 7

__Given__ :

```text
* ****  * * * *** ***  **    *  *  * ****  * ** *  ** ***  ** ***  ** * *  *   ** *     *  * ** *  *   ** *     *   **  *   *****  **** *  ***  *  ** * *     * 
```

__Decoded__ 1 (Substitution : * -> 0, and ' ' -> 1) :

```text
0100001101010100010001100111101101101000011010010110010001100100011001010110111001011111011010010110111001011111011100110111000001100001011000110110010101111101
```

__Decoded__ 2 (8-bit binary with no delimiter) :

```text
CTF{hidden_in_space}
```

## Flags

1. ctf{You_found_the_rot}
2. ctf{The_one_true_salad}
3. ctf{I_like_the_buttery_biscuit_base}
4. CTF:SPACEDASH2021
5. ctf{boring_wozniak}
6. 1376299761
7. CTF{hidden_in_space}

## References

- [Cyberchef](https://gchq.github.io/CyberChef/) [Task 1,3,4,7]
- [Caesar Cipher Brute-Force Decoder](https://www.dcode.fr/caesar-cipher) [Task 2]
- <https://medium.com/peptr/why-boring-wozniak-will-never-be-generated-as-a-container-name-in-docker-763b755f9e2a> [Task 5]
- [EPOCH timezone checker](https://www.epochconverter.com/timezones) [Task 6]
- [About time_t struct in C](https://en.cppreference.com/w/c/chrono/time_t) [Task 6]
- [About timegm function in C](https://www.man7.org/linux/man-pages/man3/timegm.3.html) [Task 6]
