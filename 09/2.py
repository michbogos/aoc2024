def parse_cnt(cnt):
    disk, spaces, files = [], [], []
    for i, c in enumerate(cnt):
        if i % 2:
            spaces.append((int(c), len(disk)))
        else:
            files.append((int(i//2), int(c), len(disk)))
        disk += [-1 if i % 2 else int(i//2) for _ in range(int(c))]
    return disk, spaces, files


with open("../inputs/09.txt") as f:
    cnt = f.readline()
    disk, spaces, files = parse_cnt(cnt)
    while files:
        fid, flen, fidx = files.pop()

        for i, (slen, sidx) in enumerate(spaces):
            if fidx < sidx:
                break
            if slen >= flen:
                disk[fidx:fidx + flen] = [-1] * flen
                disk[sidx:sidx + flen] = [fid] * flen
                if slen > flen:
                    spaces[i] = (slen - flen, sidx+flen)
                else:
                    spaces.pop(i)
                break
    print(sum(disk[i] * i for i in range(len(disk)) if disk[i] > 0))
