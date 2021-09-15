# Mobile One

The one true mobile app.

## Difficulty

Easy (50 points)

## Writeup

1. By using `strings` and `grep` CLI tool, we are able to find the flag directly from the given APK file
2. The full command `strings <FULL_FILE_NAME> | grep "<STRING>"` is basically

    - `strings` returns all the readable characters found within the given file (FULL_FILE_NAME)
    - `|` pipes all the output to the 2nd part
    - `grep` will search for the given STRING within all the piped output

### Flag

flag{strings_grep_and_more_strings}

### References

- ref1
