---
slideOptions:
  transition: slide
  spotlight:
    enabled: false
---

# REGEX FOR BEGINNERS

##### And bullies

---

### Why use regex

* speed up text manipulation
  * find stuff quickly
  * replace stuff quickly
* make everyone jealous

----

`/^(?=.*(\[Rep SG:[^\]]*\]))(?=.*(\[Rep CR:[^\]]*\]))(?=.*(\[Rep TY:[^\]]*\])).*$/`

---

### Standard text search

X => X

---

<span style="font-family: mono;">
blastimir

blast you bleeding blastimir!
</span>

----

<span style="font-family: mono;">
<span style="color:green;">b</span>lastimir

<span style="color:green;">b</span>last you bleeding blastimir!
</span>

----

<span style="font-family: mono;">
<span style="color:green;">bl</span>astimir

<span style="color:green;">bl</span>ast you bleeding blastimir!
</span>

----

<span style="font-family: mono;">
<span style="color:green;">bla</span>stimir

<span style="color:green;">bla</span>st you bleeding blastimir!
</span>

----

<span style="font-family: mono;">
<span style="color:green;">blas</span>timir

<span style="color:green;">blas</span>t you bleeding blastimir!
</span>

----

<span style="font-family: mono;">
<span style="color:green;">blast</span>imir

<span style="color:green;">blast</span> you bleeding blastimir!
</span>

----

<span style="font-family: mono;">
<span style="color:green;">blasti</span>mir

<span style="color:green;">blast</span><span style="background-color:red;">&nbsp;</span>you bleeding blastimir!
</span>

----

<span style="font-family: mono;">
<span style="color:green;">b</span>lastimir

blast you <span style="color:green;">b</span>leeding blastimir!
</span>

----

<span style="font-family: mono;">
<span style="color:green;">bla</span>stimir

blast you <span style="color:green;">bl</span><span style="background-color:red;">e</span>eding blastimir!
</span>

----

<span style="font-family: mono;">
<span style="color:green;">b</span>lastimir

blast you bleeding <span style="color:green;">b</span>lastimir!
</span>

----

...

----

<span style="font-family: mono;">
<span style="color:green;">blastimir</span>

blast you bleeding <span style="color:green;">blastimir</span>!
</span>

---

### Problem

<span style="font-family: mono;">
<span style="color:green;">blast</span>

<span style="color:green;">blast</span> you bleeding <span style="color:green;">blast</span>imir!
</span>

----

### ~~Standard text search~~

---

### Regex Syntax

X =/= X

`[ ] \ ^ $ . | ? * + ( ) { }`

----

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

----

<!-- .slide: data-transition="none" data-transition-speed="fast" -->

```diff
 drink
 drank
 drunk
 drek
 drinking
 drunkard
 antidrink
```

#### &nbsp;

----

<!-- .slide: data-transition="none" data-transition-speed="fast" -->

```diff
+drink
 drank
 drunk
 drek
+drinking
 drunkard
+antidrink
```

#### `drink`

----

<!-- .slide: data-transition="none" data-transition-speed="fast" -->

```diff
+drink
+drank
 drunk
 drek
+drinking
 drunkard
+antidrink
```

#### `dr[ia]nk`

----

<!-- .slide: data-transition="none" data-transition-speed="fast" -->

```diff
+drink
+drank
+drunk
 drek
+drinking
+drunkard
+antidrink
```

#### `dr[iau]nk`

----

<!-- .slide: data-transition="none" data-transition-speed="fast" -->

```diff
+drink
+drank
+drunk
 drek
 drinking
 drunkard
+antidrink
```

#### `dr[iau]nk\b`

----

<!-- .slide: data-transition="none" data-transition-speed="fast" -->

```diff
+drink
+drank
+drunk
 drek
 drinking
 drunkard
 antidrink
```

#### `\bdr[iau]nk\b`

---

### Example 2

Filter files

----

<!-- .slide: data-transition="none" data-transition-speed="fast" -->

```diff
 german.jpg
 midget.png
 bondage.jpeg
 definitelyajpg.rar
 nudes.jpg.zip
 rtfm.txt
 send_nudes.eml
 goaway.tar.gz
```

#### &nbsp;

----

<!-- .slide: data-transition="none" data-transition-speed="fast" -->

```diff
+german.jpg
 midget.png
 bondage.jpeg
+definitelyajpg.rar
+nudes.jpg.zip
 rtfm.txt
 send_nudes.eml
 goaway.tar.gz
```

#### `jpg`

----

<!-- .slide: data-transition="none" data-transition-speed="fast" -->

```diff
+german.jpg
 midget.png
 bondage.jpeg
 definitelyajpg.rar
+nudes.jpg.zip
 rtfm.txt
 send_nudes.eml
 goaway.tar.gz
```

#### `\.jpg`

----

<!-- .slide: data-transition="none" data-transition-speed="fast" -->

```diff
+german.jpg
 midget.png
 bondage.jpeg
 definitelyajpg.rar
 nudes.jpg.zip
 rtfm.txt
 send_nudes.eml
 goaway.tar.gz
```

#### `\.jpg$`

----

<!-- .slide: data-transition="none" data-transition-speed="fast" -->

```diff
+german.jpg
 midget.png
+bondage.jpeg
 definitelyajpg.rar
 nudes.jpg.zip
 rtfm.txt
 send_nudes.eml
 goaway.tar.gz
```

#### `\.jpe?g$`

----

<!-- .slide: data-transition="none" data-transition-speed="fast" -->

```diff
+german.jpg
+midget.png
+bondage.jpeg
 definitelyajpg.rar
 nudes.jpg.zip
 rtfm.txt
 send_nudes.eml
 goaway.tar.gz
```

#### `\.(jpe?g)|(png)$`

---

### Example 3

Looking for drunk campaigns

----

<!-- .slide: data-transition="none" data-transition-speed="fast" -->

```diff
 Campaign: drink
 Campaign: drink too much
 Campaign: #69
 Campaign: #666
 Not a Campaign: oops
 Your mom is a Campaign
 Campaign: 666
 Campaign:
```

#### &nbsp;

----

<!-- .slide: data-transition="none" data-transition-speed="fast" -->

```diff
+Campaign: drink
+Campaign: drink too much
+Campaign: #69
+Campaign: #666
+Not a Campaign: oops
+Your mom is a Campaign
+Campaign: 666
+Campaign:
```

#### `Campaign`

----

<!-- .slide: data-transition="none" data-transition-speed="fast" -->

```diff
+Campaign: drink
+Campaign: drink too much
+Campaign: #69
+Campaign: #666
+Not a Campaign: oops
 Your mom is a Campaign
+Campaign: 666
+Campaign:
```

#### `Campaign:`

----

<!-- .slide: data-transition="none" data-transition-speed="fast" -->

```diff
+Campaign: drink
+Campaign: drink too much
+Campaign: #69
+Campaign: #666
 Not a Campaign: oops
 Your mom is a Campaign
+Campaign: 666
+Campaign:
```

#### `^Campaign:`

----

<!-- .slide: data-transition="none" data-transition-speed="fast" -->

```diff
 Campaign: drink
 Campaign: drink too much
 Campaign: #69
 Campaign: #666
 Not a Campaign: oops
 Your mom is a Campaign
 Campaign: 666
+Campaign:
```

#### `^Campaign:$`

----

<!-- .slide: data-transition="none" data-transition-speed="fast" -->

```diff
+Campaign: drink
+Campaign: drink too much
 Campaign: #69
 Campaign: #666
 Not a Campaign: oops
 Your mom is a Campaign
+Campaign: 666
 Campaign:
```

#### `^Campaign: \w+`

----

<!-- .slide: data-transition="none" data-transition-speed="fast" -->

```diff
+Campaign: drink
 Campaign: drink too much
 Campaign: #69
 Campaign: #666
 Not a Campaign: oops
 Your mom is a Campaign
+Campaign: 666
 Campaign:
```

#### `^Campaign: \w+$`

----

<!-- .slide: data-transition="none" data-transition-speed="fast" -->

```diff
+Campaign: drink
+Campaign: drink too much
 Campaign: #69
 Campaign: #666
 Not a Campaign: oops
 Your mom is a Campaign
+Campaign: 666
 Campaign:
```

#### `^Campaign:( \w+){1}`

----

<!-- .slide: data-transition="none" data-transition-speed="fast" -->

```diff
+Campaign: drink
 Campaign: drink too much
 Campaign: #69
 Campaign: #666
 Not a Campaign: oops
 Your mom is a Campaign
+Campaign: 666
 Campaign:
```

#### `^Campaign:( \w+){1}$`

----

<!-- .slide: data-transition="none" data-transition-speed="fast" -->

```diff
 Campaign: drink
+Campaign: drink too much
 Campaign: #69
 Campaign: #666
 Not a Campaign: oops
 Your mom is a Campaign
 Campaign: 666
 Campaign:
```

#### `^Campaign:( \w+){3}`

----

<!-- .slide: data-transition="none" data-transition-speed="fast" -->

```diff
+Campaign: drink
+Campaign: drink too much
 Campaign: #69
 Campaign: #666
 Not a Campaign: oops
 Your mom is a Campaign
+Campaign: 666
 Campaign:
```

#### `^Campaign:( \w+)+`

----

<!-- .slide: data-transition="none" data-transition-speed="fast" -->

```diff
+Campaign: drink
+Campaign: drink too much
+Campaign: #69
+Campaign: #666
 Not a Campaign: oops
 Your mom is a Campaign
+Campaign: 666
+Campaign:
```

#### `^Campaign:( \w+)*`

----

<!-- .slide: data-transition="none" data-transition-speed="fast" -->

```diff
 Campaign: drink
 Campaign: drink too much
 Campaign: #69
 Campaign: #666
 Not a Campaign: oops
 Your mom is a Campaign
+Campaign: 666
 Campaign:
```

#### `^Campaign: \d+`

----

<!-- .slide: data-transition="none" data-transition-speed="fast" -->

```diff
 Campaign: drink
 Campaign: drink too much
+Campaign: #69
+Campaign: #666
 Not a Campaign: oops
 Your mom is a Campaign
+Campaign: 666
 Campaign:
```

#### `^Campaign: .\d+`

----

<!-- .slide: data-transition="none" data-transition-speed="fast" -->

```diff
 Campaign: drink
 Campaign: drink too much
+Campaign: #69
+Campaign: #666
 Not a Campaign: oops
 Your mom is a Campaign
 Campaign: 666
 Campaign:
```

#### `^Campaign: #\d+`

----

<!-- .slide: data-transition="none" data-transition-speed="fast" -->

```diff
 Campaign: drink
 Campaign: drink too much
+Campaign: #69
+Campaign: #666
 Not a Campaign: oops
 Your mom is a Campaign
+Campaign: 666
 Campaign:
```

#### `^Campaign: #?\d+`

---

### Example 4

Duplicate words

----

<!-- .slide: data-transition="none" data-transition-speed="fast" -->

```diff
 That is not a test.
+That is not not a test.
+This is a test.
+This is is a test.
```

#### `(\w+)\s\1`

----

<!-- .slide: data-transition="none" data-transition-speed="fast" -->

```diff
 That is not a test.
+That is not not a test.
 This is a test.
+This is is a test.
```

#### `(\b\w+\b)\s\1`

---

### Scary Example 5

Password validation

----

<!-- .slide: data-transition="none" data-transition-speed="fast" -->

##### `^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$`

----

<!-- .slide: data-transition="none" data-transition-speed="fast" -->

```plaintext
^               <- start of string
(?=.*[A-Za-z])
(?=.*\d)
[A-Za-z\d]
{8,}
$
```

----

<!-- .slide: data-transition="none" data-transition-speed="fast" -->

```plaintext
^
(?=.*[A-Za-z])  <- positive lookahead: find a character
(?=.*\d)
[A-Za-z\d]
{8,}
$
```

----

<!-- .slide: data-transition="none" data-transition-speed="fast" -->

```plaintext
^
(?=.*[A-Za-z])
(?=.*\d)        <- positive lookahead: find a digit
[A-Za-z\d]
{8,}
$
```

----

<!-- .slide: data-transition="none" data-transition-speed="fast" -->

```plaintext
^
(?=.*[A-Za-z])
(?=.*\d)
[A-Za-z\d]      <- find a character or a digit
{8,}
$
```

----

<!-- .slide: data-transition="none" data-transition-speed="fast" -->

```plaintext
^
(?=.*[A-Za-z])
(?=.*\d)
[A-Za-z\d]
{8,}            <- repeat previous expression
$                     *at least* 8 times
```

----

<!-- .slide: data-transition="none" data-transition-speed="fast" -->

```plaintext
^
(?=.*[A-Za-z])
(?=.*\d)
[A-Za-z\d]
{8,}
$               <- end of string
```

---

### Finite State Machines

* Every regular expression is a finite state machine!

----

<!-- .slide: data-transition="none" data-transition-speed="fast" -->

```plaintext
\.(jpe?g)|(png)
```

![state-machine-images](https://github.com/dsimidzija/presentations/raw/master/assets/images/state-machine-images.png)

----

<!-- .slide: data-transition="none" data-transition-speed="fast" -->

```plaintext
^(a|b)c*d+$
```

![state-machine2](https://github.com/dsimidzija/presentations/raw/master/assets/images/state-machine2.png)

----

<!-- .slide: data-transition="none" data-transition-speed="fast" -->

### FSM graph for:

```plaintext
\bdr[iau]nk\b
```


# ?

---

### Further points

* Many more options than presented
* Start simple
* Use https://regex101.com/

---

### T.Hanks

![T.Hanks](https://i.imgur.com/xn9uaPX.jpg)
