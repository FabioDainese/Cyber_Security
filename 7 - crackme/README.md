# Introduction
This challenge was designed to familiarize with the [*IDA*](https://www.hex-rays.com/products/ida/index.shtml) software, a professional tool for program analysis (11<sup>th</sup> February 2019).

# Challenge Description
This challenge consists to reverse engineer the [`'crackme'`](crackme) program using the *IDA* disassembler and the *GDB* debugger in order to analyze the behavior of the various functions such that we can reconstruct the correct *FLAG*.

The *crackme* program basically checks if the input string, inserted by the user, meets some requirements in order to be considered a valid flag or not (there's only one possible *flag*). So to reconstruct the *flag* we’ll just need to follow the flow of the program and compose the *flag* step-by-step so that the program does not end in any error state.

* [Crackme](crackme) (e38570a4f85c527481b060402545294ca195dd0c6e2c20014659dff8b201743e sha256sum)

# Solution
You can find in the [*crackme_source.md*](crackme_source.md) file (well commented) a full pseudo-code reconstruction of the program!

***

Thanks to the *IDA* disassembler we can clearly see that once the input string is inserted, i.e. the *flag*, the program checks that it’s `37` characters long, otherwise it will go into an error state and prints `"wrong flag"`.

After that the program calls a function that returns `1` if and only if the string contains at the beginning the sequence of characters `flg{` , the character `}` at the end, the character `-` in the 18<sup>th</sup> position (array starts from `0`) and all characters between `{` and `}` are part of a charset that has been defined (`charset = [0-9a-zA-Z-]`). If the previous function does not returns `1`, it means that has returned `0`, the program will go into an error state and prints `"wrong flag"`. From these preliminary checks we can see that the correct *flag* has to be of the form `flg{ ... - ... }` (where instead of `...` there will be some specific characters).

Then the program will analyze the various characters included between the two curly braces by calling two functions, the first one will check all the characters before the `'-'` (first part), meanwhile the second one will check all the remaining characters (second part).

The first of these functions will return `1` if and only if:

* `flag[4] == "N"` (the first character after the `{` symbol);
* `flag[5] == "x"` (the next char);
* `flag[6:10] == "U2wR"` (the characters included between the 6<sup>th</sup> and the 9<sup>th</sup> position, 10<sup>th</sup> not included <— 4 chars)
* `flag[10:14] - flag[6:10] == "27FA3AF0"` (This means: `flag[10:14] = "27FA3AF0" + flag[6:10]`. The outcome of this operation, in hexadecimal, results to be `"7A716D45"` that transformed into ASCII is equals to `"Emqz"`);
* `(( XOR flag[6:10], flag[10:14] ) + flag[14:18] ) == "713DD282"` (This means: `flag[14:18] = "713DD282" - (XOR flag[6:10], flag[10:14]) = "713DD282" - "28065F10" = "49377372"` that transformed into ASCII is equals to `"rs7I"`).

Meantime the second function uses the support of two pre-defined arrays to check the correctness of the characters. The first array is the one that defines the charset (`[0-9a-zA-Z-]`) and the second one is an array containing indexes (to get these indexes you’ll just need to convert the hex characters into integers).
The function uses a loop to scroll all characters from the 19<sup>th</sup> position (immediately after `'-'`) until the end and at each cycle/iteration it checks that the `flag[i+19]` character is equal to `charset[my_index_array[i]]` (the `'i'` index goes from `0` up to `16`). 

So to retrieve this second part of the *flag* we can use this simple script in python:

```python
charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-"
for i in [0x34,0x3D,0x03,0x0D,0x2C,0x2E,0x15,0x01,0x0C,0x18,0x26,0x26,0x15,0x2B,0x0B,0x32,0x19]:
	print(charset[i], end="")
```

If one, or more, of those previous conditions/comparison are not satisfied, the functions will return `0` and the program will end up by printing an error message, otherwise it will return `1` and prints the message `"Correct"` (correct *flag*) and terminate its execution.

**N.B.** All the characters specified in hexadecimal base are written in little endianness, so at the end to get the correct *flag* you’ll have to remember to write them down in the reverse order (backward).
