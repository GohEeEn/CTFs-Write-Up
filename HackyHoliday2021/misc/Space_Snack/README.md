# Space Snack

Find the answers to the treasure hunt to gain access to the cake in the space cafe.

## Category

misc

## Write Up

### Task 1 - Roten to the core (20 points)

You find a roten apple next to a piece of paper with 13 circles on and some text. What's the message?

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

### Task 2 - The roman space empire (25 points)

You find a page with a roman insignia at the top with some text what could it mean?

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

__NOTE__ : Caesar the 1st roman empiral is the reason of this cipher naming, since he used it in his personal correspondance

### Task 3 - The space station that rocked (25 points)

You hear the heavy base line of 64 speakers from the next compartment. you walk in and the song changes to writing's on the wall, there is some strange code painted on the wall what could it mean?

__Given__ :

```text
RXZlbiAgaW4gc3BhY2Ugd2UgbGlrZSB0aGUgYnV0dGVyeSBiaXNjdXQgYmFzZS4gY3Rme0lfbGlrZV90aGVfYnV0dGVyeV9iaXNjdWl0X2Jhc2V9IC4gQWNjZXNzIHBhcnQgMzogWEQ=
```

__Decoded__ (Base64) :

```text
Even  in space we like the buttery biscut base. ctf{I_like_the_buttery_biscuit_base} . Access part 3: XD
```

### Task 4 - What the beep is that? (25 points)

You hear beeps on the radio, maybe someone is trying to communicate? Flag format: CTF:XXXXXX

__Given__ :

```text
.. -. ... .--. . -.-. - --- .-. / -- --- .-. ... . / .-- --- ..- .-.. -.. / -... . / .--. .-. --- ..- -.. / --- ..-. / -.-- --- ..- .-. / . ..-. ..-. --- .-. - ... .-.-.- / -.-. - ..-. ---... ... .--. .- -.-. . -.. .- ... .... ..--- ----- ..--- .---- / .- -.-. -.-. . ... ... / -.-. --- -.. . ---... / .--- --...
```

__Decoded__ (Morse Code) :

```text
INSPECTORMORSEWOULDBEPROUDOFYOUREFFORTS.CTF:SPACEDASH2021ACCESSCODE:J7
```

### Task 5 - The container docker (25 points)

You are now in the space cafe, the cake is in the container that should not be here. You can see random names on all the containers. What will Docker never name a container? Note: Please enter it as ctf{full_name}

__Answer__

Docker container will never named `boring_wozniak`, because of the logic (line 844 to 846) in file [names-generator.go](https://github.com/moby/moby/blob/c90254c7464cac5c56e7ab9e6b1857c119d5d263/pkg/namesgenerator/names-generator.go) from the source code

### Task 6 - There might be more cake (50 points)

They ate then cake and left a note with a secret algorithm to unlock the cake treasury. We saw it happening at exactly January 1, 2030 11:23:45 AM... are you the visionary that can figure out the PIN code?

__Given__ the PIN generation algorithm :

```c
int generatePin() {
    srand(time(0));
    return rand();
}
```

and also the required timezone be __UTC__

By adjusting the seeding long integer to `UTC +0:00` (check [here](https://www.epochconverter.com/timezones)), you should be able to get the correct PIN (see `task6.c`)

### Task 7 - Stars in space (30 points)

The treasury consists of cake hidden on stars in space.

__Given__ :

```text
* ****  * * * *** ***  **    *  *  * ****  * ** *  ** ***  ** ***  ** * *  *   ** *     *  * ** *  *   ** *     *   **  *   *****  **** *  ***  *  ** * *     * 
```

__Decoded__ 1 (Substitution : * = 0, and ' ' = 1) :

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
- [Why boring wozniak will never be generated as a container name in docker](https://medium.com/peptr/why-boring-wozniak-will-never-be-generated-as-a-container-name-in-docker-763b755f9e2a)
- [EPOCH timezone checker](https://www.epochconverter.com/timezones) [Task 6]
- [About time_t struct in C](https://en.cppreference.com/w/c/chrono/time_t) [Task 6]
- [About timegm function in C](https://www.man7.org/linux/man-pages/man3/timegm.3.html) [Task 6]
