st=set()

st.add(10)
st.add(30)
st.update([30,20,40])
print(st)

st.remove(40)
st.discard(20)
print(st)

a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))
