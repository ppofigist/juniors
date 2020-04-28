def solve(lst):
    st = []
    for w in lst:
        if w.isdigit():
            st.append(int(w))
            continue
        y = st.pop()
        x = st.pop()
        if w == '-':
            z = x - y
        elif w == '*':
            z = x * y
        elif w == '+':
            z = x + y
        elif w == '/':
            z = x // y
        st.append(z)
    return st.pop()


lst = input('Ввведите пример ').split()
print(solve(lst))

