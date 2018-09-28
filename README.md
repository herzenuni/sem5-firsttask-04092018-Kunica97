*Данное задание выполнено. Проверить работоспособность кода можно по ссылке https://repl.it/@kunica_devica/040918-first*

## Задача 1

Напишите программу, в которой пользователь вводит число от 0 до 9 включительно, а программа выводит название введённого числа, а если второй входной аргумент ```type``` имеет значение ```bin```, ```oct```,```hex```, то функция преобразует это число в бинарную, восьмеричную или шестнадцатеричную форму. Предусмотреть проверку корректности введённого пользователем значения.
При реализации должны использоваться декораторы (но можно обойтись и без них). 
Предусмотрите обработку исключительных ситуаций. 
Напишите тесты с использованием assert.

## Задача 2

На основе созданного в рамках лабораторного занятия 1 программного кода напишите фрагмент кода (класс) для обработки исключительных ситуаций, которые могут возникнуть в процессе выполнения кода.

1. напишите класс для обработки исключений RangeException, для обработки исключения, которое возникает в ситуации, когда вводится число не из описанного в условии диапазона;
2. напишите класс для обработки исключений ConvertTypeException, для обработки исключения, которое возникает в ситуации, когда пользователь выбрал тип не из списка обозначенного в условии задачи.

## Самостоятельная работа 
*в процессе*

Для программы, сделанной в рамках лабораторной работы 1 и 2, реализуйте с использованием механизма декораторов (предпочтительно) или без него (в этом случае будет необходимо использовать еще один аргумент) функционал для сохранения истории вычислений функции в файл. 

При записи в файл предусмотреть вероятность возникновения исключительных ситуаций и создать собственный класс или классы для обработки исключительных ситуаций при записи в файл.

