import numpy as np

#using window=15. If not, change all 15 and 30 below as needed

entity = []
context = []
with open("raw", 'r') as f:
    flag = 0
    con = ["unk" for _ in range(30)]
    for line in f:
        a = line.split()
        if flag==0:
            entity.append(a)
            con = ["unk" for _ in range(30)]
        elif flag==1:
            for i in range(min(15, len(a))):
               con[2*i] = a[-i-1]
        else:
            for i in range(min(15, len(a))):
                con[2*i+1] = a[i]
            context.append(con)
        flag = (flag+1) %3
print(entity)
print(np.array(entity))

print(context)
print(np.array(context))
# np.save("entity.npy", np.array(entity))
# np.save("context.npy", np.array(context))
'''

[['Albert', 'Einstein'], ['Nobel', 'Prize', 'in', 'Physics']]
[list(['Albert', 'Einstein']) list(['Nobel', 'Prize', 'in', 'Physics'])]
[['Professor', 'is', 'unk', 'a', 'unk', 'German', 'unk', 'scientist', 'unk', 'unk', 'unk', 'unk', 'unk', 'unk', 'unk', 'unk', 'unk', 'unk', 'unk', 'unk', 'unk', 'unk', 'unk', 'unk', 'unk', 'unk', 'unk', 'unk', 'unk', 'unk'], ['1921', 'for', 'the', 'his', 'received', 'services', 'He', 'to', 'unk', 'theoretical', 'unk', 'physics', 'unk', 'unk', 'unk', 'unk', 'unk', 'unk', 'unk', 'unk', 'unk', 'unk', 'unk', 'unk', 'unk', 'unk', 'unk', 'unk', 'unk', 'unk']]
[['Professor' 'is' 'unk' 'a' 'unk' 'German' 'unk' 'scientist' 'unk' 'unk'
  'unk' 'unk' 'unk' 'unk' 'unk' 'unk' 'unk' 'unk' 'unk' 'unk' 'unk' 'unk'
  'unk' 'unk' 'unk' 'unk' 'unk' 'unk' 'unk' 'unk']
 ['1921' 'for' 'the' 'his' 'received' 'services' 'He' 'to' 'unk'
  'theoretical' 'unk' 'physics' 'unk' 'unk' 'unk' 'unk' 'unk' 'unk' 'unk'
  'unk' 'unk' 'unk' 'unk' 'unk' 'unk' 'unk' 'unk' 'unk' 'unk' 'unk']]

'''
