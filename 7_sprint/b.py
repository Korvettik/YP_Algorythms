n = int(input().strip())

def to_minutes(t):
    if '.' in str(t):
        parts = str(t).split('.')
        h = int(parts[0])
        m_str = parts[1]
        if len(m_str) == 1:
            m = int(m_str) * 10
        else:
            m = int(m_str)
            if m_str.startswith('0'):
                m = int(m_str)
        return h * 60 + m
    else:
        return int(t) * 60

def from_minutes(minutes):
    h = minutes // 60
    m = minutes % 60
    if m == 0:
        return str(h)
    else:
        return f"{h}.{m:02d}".rstrip('0').rstrip('.')

lectures = []
for _ in range(n):
    start_str, end_str = input().strip().split()
    start = to_minutes(start_str)
    end = to_minutes(end_str)
    lectures.append((start, end))

# сортируем по времени окончания, а при равенстве - по времени начала
lectures.sort(key=lambda x: (x[1], x[0]))

selected = []
last_end = -1

for start, end in lectures:
    if start >= last_end:
        selected.append((start, end))
        last_end = end

print(len(selected))
for start, end in selected:
    print(f"{from_minutes(start)} {from_minutes(end)}")