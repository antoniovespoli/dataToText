"""

COMPUTE VARIABILITY SCORE

A = set()
filename = "WeatherGov/1. Corpus/All.text"

with open(filename) as f:
    content = f.readlines()

content = [x.strip() for x in content] 

for line in content:
    new_line = ''.join([i for i in line if not i.isdigit()])
    A.add(new_line)

print(len(A)/len(content))
    
"""

import pyter

target_file = "target.txt"
hyp_file = "hypotheses.txt"
#target_file = "Corpus/Test.text"
#hyp_file = "GeneratedData/Retrieval_test.txt"

with open(target_file) as f:
    target = f.readlines()

with open(hyp_file) as f:
    hyp = f.readlines()

target = [x.strip() for x in target] 
hyp = [x.strip() for x in hyp] 

target_numbers_only = []
for line in target:
    new_line = [int(s) for s in line.split() if s.isdigit()]
    target_numbers_only.append(new_line)

hyp_numbers_only = []
for line in hyp:
    new_line = [int(s) for s in line.split() if s.isdigit()]
    hyp_numbers_only.append(new_line)

tot = 0
for i in range(len(target)):
    if target_numbers_only[i] != [] and hyp_numbers_only[i] != []:
        tot += pyter.ter(target_numbers_only[i], hyp_numbers_only[i])
        #print(pyter.ter(target_numbers_only[i], hyp_numbers_only[i]))

#print("SUPER TOTAL")
print(tot/len(target))