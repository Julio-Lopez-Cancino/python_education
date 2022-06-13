st = open('st.txt', 'w')
st.write('Hi from Python!')
st.close()


#with open Python will automatically close the file

with open('st2.txt','w') as f:
    f.write('Here\'s another example')
