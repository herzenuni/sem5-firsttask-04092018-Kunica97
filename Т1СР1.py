class WriteFileError(Exception):
  def __init__(self, error_message="File error"):
    self.error_message = error_message

  def __str__(self):
    return self.error_message
    
class RangeException(Exception):
  def __init__(self, error_message="Число не из нужного диапазона"):
    self.error_message = error_message
  
  def __str__(self):
    return self.error_message

class ConvertTypeException(Exception):
  def __init__(self, error_message="Тип системы счисления не из списка"):
    self.error_message = error_message

  def __str__(self):
    return self.error_message

def logger(a, b):
  try:
    with open('log.txt', 'a') as file:
      file.write("Введенные данные: "+ str(a) + "," + str(b) + " ответ " + str(ss(a,b)) + "\n")
  except:
    raise WriteFileError

def ss(a, b):
  if b == 'bin':
    a = bin(a)
  elif b == 'oct':
    a = oct(a)
  elif b == 'hex':
    a = hex(a)
  string = str(a)[2:]
  return string

def name(a):
  if a == 0:
    return('Ноль');
  elif a == 1:
    return('Один');
  elif a == 2:
    return('Два');
  elif a == 3:
    return('Три');
  elif a == 4:
    return('Четыре');
  elif a == 5:
    return('Пять');
  elif a == 6:
    return('Шесть');
  elif a == 7:
    return('Семь');
  elif a == 8:
    return('Восемь');
  elif a == 9:
    return('Девять');


while True:
  print('Введите число и систему счисления:')
  try:
    a = int(input())
    if a > 9 or a < 0:
      raise RangeException
  except (TypeError, ValueError):
    print('Это символ!')
    continue
  else:
    break

b = input()
if b == 'bin' or b == 'oct' or b == 'hex':
  print('Ответ: ',ss(a, b))
  print('Вы ввели: ', name(a))
else: 
  raise ConvertTypeException

logger(a,b)
