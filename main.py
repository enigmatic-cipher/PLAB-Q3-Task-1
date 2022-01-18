"""
Given a string as input. Clean the string by removing all occurrence of character '#'.
Input-> "#global#"
Output-> New String=global
"""
st = "#global#"
ln = len(st)
str = ""
for i in range(1,ln):
  ch = st[i]
  if (ch != "#"):
    str = str + ch
print(f"New String:{str}")
