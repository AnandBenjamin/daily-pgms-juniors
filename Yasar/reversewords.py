#Program to reverse a string word by word



class Reverse:
       def reverse_words(self,string):
              return " ".join(reversed(string.split(" ")))

a=Reverse()
string=input()
print(a.reverse_words(string))


