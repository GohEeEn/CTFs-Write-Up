# TEASER: su admin

You arrived at the launch platform of SPACE RACE. Teams around you are preparing for the event the best they can by gathering their crew and designing their flag.

At the outset of the camp you notice the Hacky Holidays admin base, you decide to stake-out and see what's happening. After a while you notice that people are only allowed to access the admin base when they show the Hacky Holidays admin flag below.

## Category

web

## Task 1 - Identify yourself (50 points)

Open the [flag designer](https://portal.hackazon.org/#!/flagdesigner) and see if you can hack your way into the admin base.

Note: Only the URL <https://portal.hackazon.org/flagdesigner> and its sub-URLs are part of the teaser challenge.

### Writeup

1. After several testing on each modification available, we can come to a conclusion that the API format for creating the flag be 

```text
/api/flag/flag_pattern/overlay#1/overlay#2/color_1/color_2/color_3/color_overlay#1/color_overlay#2.svg
```

2. Thus, the full API for admin : https://portal.hackazon.org/flagdesigner/api/flag/7/15/9/5/2/4/3/1.svg

## Flags

1. CTF{YOU-HAZ-ADMIN-FLAG}
