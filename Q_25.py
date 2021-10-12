word = '''this is a paragraph which is written just for the purpose of providing content 
to let the average word length be calculated
'''
total=1
res = len(word.split())
print(str(res))
for w in range(1,res):
    total +=w
average=total/res
print(average)
