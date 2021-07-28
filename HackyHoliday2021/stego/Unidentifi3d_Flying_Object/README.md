# Unidentifi3d_Flying_Object

## Category

stego

## Write-Up

### Task 1

1. Look into the setting config value at the end of the G-code, it turns out that there is a JSON-like metadata for this G-code.
2. By searching online, we can see that the 1st definition name is exactly a model from certain 3D printer brand called GEEETECH

### Task 2

By viewing from the change on layer __88__ to __60__, we can see that the modelling is showing the flag

Flags :

1. geeetech A10M
2. CTF{Flying_saucer}

### References

- [About GEEETECH A10M 3D Printer](https://www.geeetech.com/a10m-mix-color-3d-printer-p-1114.html)
- [G-code Analyzer](https://www.gcodeanalyser.com/) [Task 2]