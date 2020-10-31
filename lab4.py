import re
import time

input = open('josnviewer.io (1).json', 'r', encoding='utf-8')
output = open('timetable.yaml', 'w', encoding='utf-8')

start_time = time.perf_counter()
strings = input.read().split('\n')
for i in range(len(strings)):
    if '{' in strings[i]:
        strings[i] = re.sub('[-{}/[,]', ' ', strings[i])
        strings[i + 1] = re.sub(r'"(\w*)"', r'-  \1', strings[i+1])
        strings[i + 1] = re.sub(r'"([\s\S]*)"', r"'\1'", strings[i+1])
        output.write('\n')
        output.write(strings[i])
    else:
        if ':' in strings[i]:
            strings[i] = re.sub(r'"(\w*)"', r'   \1', strings[i])
            strings[i] = re.sub(r'"(\b[0-9].*[0-9]\b)"', r"'\1'", strings[i])
            strings[i] = re.sub('[{}/["",]', '', strings[i])
            output.write('\n')
            output.write(strings[i])
            continue
print(time.perf_counter() - start_time)