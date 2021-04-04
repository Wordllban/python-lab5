import re
from collections import defaultdict

def find_log_lines():
    mar_9 = re.compile( r'(^.*09\/Mar\/2004:((21:10:((4[4-9])|' \
                        r'(5[0-9])))|((21:[1-5][1-9])|' \
                        r'(2[2-3]:[0-5][0-9])):[0-5][0-9]) .*\] \".*\" ([1-5][0-9][0-9]) .*)')

    mar_10 = re.compile(r'(^.*10\/Mar\/2004:.*\] \".*\" ([1-5][0-9][0-9]).*)')

    mar_11 = re.compile(r'(^.*11\/Mar\/2004:(((([0-1][0-8]:[0-5][0-9])|' \
                        r'(19:[0-1][0-9])|(19:2[0-8])|(19:29:[0-1][0-9])):[0-5][0-9])|' \
                        r'(19:29:2[0-8])).*\] \".*\" ([1-5][0-9][0-9]) .*)')

    statuses = defaultdict(int)

    file = open('access_log')

    for line in file:
        for match in re.finditer(mar_9, line):
            statuses[match.group(10)] += 1
        for match in re.finditer(mar_10, line):
            statuses[match.group(2)] += 1
        for match in re.finditer(mar_11, line):
            statuses[match.group(10)] += 1
    file.close()
    return statuses


if __name__ == '__main__':
    print(find_log_lines())
