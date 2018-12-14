# Course: Data Structure , Author:Nazia Sharmin, assignment:Lab7,instructor:Professor-Diego Aguirre,
# T.A.:.Anindita Nath, date of last modification:12/13/2018, purpose of program:
#In this lab we use Edit Distance by using dynamic programming.

def Editdistance(st1, st2, l, n):
    # If first string is empty, the only option is to
    # insert all characters of second string into first
    if l == 0:
        return n

        # If second string is empty, the only option is to
    # remove all characters of first string
    if n == 0:
        return l


    if st1[l - 1] == st2[n - 1]:
        return Editdistance(st1, st2, l - 1, n - 1)

        # If last characters are not same, consider all three
    # operations on last character of first string, recursively
    # compute minimum cost for all three operations and take
    # minimum of three values.
    return 1 + min(Editdistance(st1, st2, l, n - 1),  # Insert
                   Editdistance(st1, st2, l- 1, n),  # Remove
                   Editdistance(st1, st2, l - 1, n - 1)  # Replace
                   )
st1 = "miners"
st2 = "iner"
print(Editdistance(st1, st2, len(st1), len(st2)))