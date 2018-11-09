### python 四则运算
{
#### print 打印
luoyadong@u:~/python_study$ python3
Python 3.7.0 (default, Jun 28 2018, 13:15:42) 
[GCC 7.2.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> print('Hello world')
Hello world
>>> print('Hello wrold!')
Hello wrold!
>>> print('Spam and eggs')
Spam and eggs
>>> pirnt('Spam and eggs')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'pirnt' is not defined
>>> print('Spam and eggs')
Spam and eggs

#### 加减乘除
>>> 2 + 2
4
>>> 1.98 + 2.98
4.96
>>> 1.98 + 2.97
4.95
>>> 8 * 8 - 9
55
>>> 2 * (3 + 4)
14
>>> 10 /2
5.0
>>> 10 /2 
5.0
>>> 10 / 2
5.0
>>> 10 / 2.
5.0
>>> 10 / 2
5.0
>>> -7
-7
>>> (-7 + 2) * (-4)
20

#### >, < >= ,<=
>>> my_boolean = True
>>> my_boolean
True
>>> 2 == 3
False
>>> "Hello" == 'Hello'
True
>>> "Hello" = 'Hello'
  File "<stdin>", line 1
SyntaxError: can't assign to literal
>>> "Hello" == 'Hello'
True
>>> 1 != 1
False
>>> 1 != 2
True
>>> "elevn" != "seven"
True
>>> 2 != 10
True
>>> 7 < 5
False
>>> 7 > 5
True
>>> 10 < 10
False
>>> 10 <= 10
True
>>> 9 >= 9.0
True
>>> "abc" > "ABC"
True
>>> "abc" >= "ABC"
True

#### 除0报错
>>> 11 / 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>> 44 / 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero

#### float 值
>>> 3 / 4
0.75
>>> 9.87654
9.87654
>>> 9.87654000
9.87654
>>> 9.87654300
9.876543

#### bug
>>> 1 / 3
0.3333333333333333
>>> 1 / 3
0.3333333333333333
>>> 1 / 3
0.3333333333333333
>>> 1 / 3
0.3333333333333333

#### float 两个操作数可以都是浮点数或者一个是浮点数一个整形，两个整型默认也是float
>>> 3 /4 
0.75
>>> 3.14 /4
0.785
>>> 3.4 / 3. 2
  File "<stdin>", line 1
    3.4 / 3. 2
             ^
SyntaxError: invalid syntax
>>> 3.4 / 3.2
1.0625
>>> 4 + 3.33
7.33

#### 幂操作 
>>> 2 ** 2
4
>>> 2 ** 5
32
>>> 2 ** 3
8
>>> 9 ** (1/2)
3.0
>>> 2 ** 3 ** 2
512
>>> 2 ** 2 ** 2
16
>>> 2 ** 8
256

#### 商和余数的计算
>>> 20 // 6
3
>>> 1.25 % 0.5
0.25
>>> 20 % 6
2
>>> 

}

### strings 字符串
{
	string: 
		one of the basic types in Python that store text
	A string is created by entering text between two single or double quotation marks.

>>> "Python is fun!"
'Python is fun!'
>>> 'Always look on the bright side of life'
'Always look on the bright side of life'
>>> 'Brian\'s mother: He\'s not the Messiah. He\'s a very naughty boy!'
"Brian's mother: He's not the Messiah. He's a very naughty boy!"
>>> "Brian's mother: He's not the Messiah. He's a very naughty boy!"
"Brian's mother: He's not the Messiah. He's a very naughty boy!"
>>> "\"say\" Hello world!"
'"say" Hello world!'
>>> '"say" Hello world'
'"say" Hello world'
>>> "\""
'"'
>>> """Customer: Good morning.
...     Owner: Good morning, Sir. Welcome to the National Cheese Emporium."""
'Customer: Good morning.\n\tOwner: Good morning, Sir. Welcome to the National Cheese Emporium.'

### string operations
{

#### string add string
>>> "Spam" + 'eggs'
'Spameggs'
>>> print("First string" + "," + "second string")
First string,second string
>>> "2" + "2"
'22'
>>> 1 + '2' + '3' + '4'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'

#### string * int
>>> print("spam" * 3)
spamspamspam
>>> 4 * '2'
'2222'
>>> "17" * "87"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'str'
>>> 'pythonisfun' * 7.0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'float'

### string * 0
>>> 'zero' * 0
''
>>> 'zero' * 1
'zero'
>>> 'zero' * 2
'zerozero'

}

}

### input/output
{
	
#### output
{
	print()
}

#### input
{
>>> input("Enter something please:")
Enter something please:This is what
'This is what'
>>> input("Enter something please:")
Enter something please:This is what\nthe user enters!
'This is what\\nthe user enters!'
}

}

### type conversion
{
#### string to int/float
{
>>> int("2") + int("3")
5
>>> float(intput("Enter a number:")) + float(input("Enter another number:"))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'intput' is not defined
>>> float(input("Enter a number:")) + float(input("Enter another number:"))
Enter a number:40
Enter another number:2
42.0
>>> int(input("Enter a number:")) + int(input("Enter another number:"))
Enter a number:40
Enter another number:2
42
>>> float("210" * int(input("Enter a number:")))
Enter a number:2
210210.0

}

}

### variables
{
```
	variables can be ressigned as many times as you want.
	In python, variables don't have specific types, so you can assign a string to a variable, and later assign an interger to the same variable.
```
	```
	However, it is not good practice. To avoid mistakes, try to avoid overwriting the same variable with different data types.
	```
#### variable names
{
>>> this_is_a_normal_name = 7
>>> 123abc = 7
  File "<stdin>", line 1
    123abc = 7
         ^
SyntaxError: invalid syntax
>>> _abc123 = 7
>>> spaces are not allowed
  File "<stdin>", line 1
    spaces are not allowed
             ^
SyntaxError: invalid syntax

```Python is a case sensitive programming language.Thus, Lastname and latstname are two different variable names in Python.
```
}

#### del variables
{
>>> foo = "a string"
>>> foo
'a string'
>>> bar
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'bar' is not defined
>>> del foo
>>> foo
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'foo' is not defined
}

}

