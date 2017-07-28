# coding=utf-8

from hashlib import md5
from struct import unpack_from
from bisect import bisect_left

ITEMS = 100000
NODES = 100
node_stat = [0 for i in range(NODES)]


def _hash(value):
    k = md5(str(value)).digest()
    ha = unpack_from(">I", k)[0]
    return ha

ring = []
hash2node = {}

for n in range(NODES):
    h = _hash(n)
    ring.append(h)
    ring.sort()
    hash2node[h] = n

# insert item
# 1.generate ring
# 2.get item hash
# 3.ring pos
# 4.node stat ++
for item in range(ITEMS):
    h = _hash(item)
    n = bisect_left(ring, h) % NODES
    node_stat[hash2node[ring[n]]] += 1

_ave = ITEMS / NODES
_max = max(node_stat)
_min = min(node_stat)

# 数据分布明显不均匀，是因为ring上的节点实际在环上的区间大小不一造成的。
print("Ave: %d" % _ave)
print("Max: %d\t(%0.2f%%)" % (_max, (_max - _ave) * 100.0 / _ave))
print("Min: %d\t(%0.2f%%)" % (_min, (_ave - _min) * 100.0 / _ave))
