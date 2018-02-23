# REGEX FOR BEGINNERS

##### And bullies

---

### Why use regex

* speed up text manipulation
    * find stuff quickly
    * replace stuff quickly
* make everyone jealous

+++

`/^(?=.*(\[Rep SG:[^\]]*\]))(?=.*(\[Rep CR:[^\]]*\]))(?=.*(\[Rep TY:[^\]]*\])).*$/`

---

### Standard text search

X => X

---

blastimir

blast you bleeding blastimir!

+++

<span style="color:green;">b</span>lastimir

<span style="color:green;">b</span>last you bleeding blastimir!

+++

<span style="color:green;">bl</span>astimir

<span style="color:green;">bl</span>ast you bleeding blastimir!

+++

<span style="color:green;">bla</span>stimir

<span style="color:green;">bla</span>st you bleeding blastimir!

+++

<span style="color:green;">blas</span>timir

<span style="color:green;">blas</span>t you bleeding blastimir!

+++

<span style="color:green;">blast</span>imir

<span style="color:green;">blast</span> you bleeding blastimir!

+++

<span style="color:green;">blasti</span>mir

<span style="color:green;">blast</span><span style="background-color:red;">&nbsp;</span>you bleeding blastimir!

+++

<span style="color:green;">b</span>lastimir

blast you <span style="color:green;">b</span>leeding blastimir!

+++

<span style="color:green;">bla</span>stimir

blast you <span style="color:green;">bl</span><span style="background-color:red;">e</span>eding blastimir!

+++

<span style="color:green;">b</span>lastimir

blast you bleeding <span style="color:green;">b</span>lastimir!

+++

...

+++

<span style="color:green;">blastimir</span>

blast you bleeding <span style="color:green;">blastimir</span>!

---

### Problem

<span style="color:green;">blast</span>

<span style="color:green;">blast</span> you bleeding <span style="color:green;">blast</span>imir!

+++

### ~~Standard text search~~

---

### Regex Syntax

X =/= X

`[ ] \ ^ $ . | ? * + ( ) { }`

+++

```plaintext
[...] => one of
\d    => number
A-Z   => any uppercase char
a-z   => any lowercase char
\t    => tab
\n    => line feed
...
```

---

### Simple example

Looking for:

> drink drank drunk

Not interested in:

> drinking drunkard antidrink

---

### Standard search

* multiple searches (drink, drank, drunk)
* false positives

---

### Regex

* one search to rule them all

&darr;

+++

```plaintext
drink
drank
drunk
drek
drinking
drunkard
antidrink
```

@[1,5,7](`drink`)
@[1-2,5,7](`dr[ia]nk`)
@[1-3,5-7](`dr[iau]nk`)
@[1-3,7](`dr[iau]nk\b`)
@[1-3](`\bdr[iau]nk\b`)

---

### Example 2

Filter files

+++

```plaintext
german.jpg
midget.png
bondage.jpeg
definitelyajpg.rar
nudes.jpg.zip
rtfm.txt
send_nudes.eml
goaway.tar.gz
```

@[1,4,5](`jpg`)
@[1,5](`\.jpg`)
@[1](`\.jpg$`)
@[1,3](`\.jpe?g$`)
@[1-3](`\.(jpe?g)|(png)$`)

---

### Example 3

Looking for drunk campaigns

+++

```plaintext
Campaign: drink
Campaign: drink too much
Campaign: #69
Campaign: #666
Not a Campaign: oops
Your mom is a Campaign
Campaign: 666
Campaign:
```

@[1-8](`Campaign`)
@[1-5,7-8](`Campaign:`)
@[1-4,7-8](`^Campaign:`)
@[8](`^Campaign:$`)
@[1-2,7](`^Campaign: \w+`)
@[1,7](`^Campaign: \w+$`)
@[1-2,7](`^Campaign:( \w+){1}`)
@[1,7](`^Campaign:( \w+){1}$`)
@[2](`^Campaign:( \w+){3}`)
@[1-2,7](`^Campaign:( \w+)+`)
@[1-4,7-8](`^Campaign:( \w+)*`)
@[7](`^Campaign: \d+`)
@[3-4,7](`^Campaign: .\d+`)
@[3-4](`^Campaign: #\d+`)
@[3-4,7](`^Campaign: #?\d+`)

---

### Example 4

Duplicate words

+++

```plaintext
That is not a test.
That is not not a test.
This is a test.
This is is a test.
```

@[2-4](`(\w+)\s\1`)
@[2,4](`(\b\w+\b)\s\1`)

---

### Scary Example 5

Password validation

+++

`^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$`

+++

```plaintext
^
(?=.*[A-Za-z])
(?=.*\d)
[A-Za-z\d]
{8,}
$
```

@[1](start of string)
@[2](positive lookahead: find a character)
@[3](positive lookahead: find a digit)
@[4](find a character or a digit)
@[5](repeat previous expression *at least* 8 times)
@[6](end of string)

---

### Further points

* Many more options than presented
* Start simple
* Use https://regex101.com/

---

### T.Hanks

![T.Hanks](https://i.imgur.com/xn9uaPX.jpg)
