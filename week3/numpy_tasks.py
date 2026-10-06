import numpy as np

def task_l1():
    v = np.arange(10, 50)
    print("Original:", v)
    print("Reversed:", v[::-1])

def task_l2():
    a = np.random.random((5, 5))
    print(a)
    print("Min:", a.min(), "Max:", a.max())

def task_l3():
    a = np.random.random((5, 5))
    a_min, a_max = a.min(), a.max()
    normalized = (a - a_min) / (a_max - a_min)
    print(normalized)

def task_l4():
    a = np.random.randint(0, 10, (5, 3))
    b = np.random.randint(0, 10, (3, 2))
    result = a @ b
    print("A:\n", a, "\nB:\n", b, "\nA @ B:\n", result)

def task_l5():
    today = np.datetime64('today', 'D')
    yesterday = today - np.timedelta64(1, 'D')
    tomorrow = today + np.timedelta64(1, 'D')
    print("Yesterday:", yesterday, "Today:", today, "Tomorrow:", tomorrow)

def task_l6():
    a = np.random.uniform(0, 10, 5)
    print("Original:", a)
    print("astype(int):", a.astype(int))
    print("np.floor:", np.floor(a))
    print("np.trunc:", np.trunc(a))
    print("a - a%1:", a - a % 1)
    print("np.int_(a):", np.int_(a))

def task_l7():
    dtype = [('position', [('x', float), ('y', float)]),
             ('color', [('r', int), ('g', int), ('b', int)])]
    points = np.zeros(3, dtype=dtype)
    points[0] = ((1.0, 2.0), (255, 0, 0))
    points[1] = ((3.5, 4.5), (0, 255, 0))
    points[2] = ((5.0, 6.0), (0, 0, 255))
    print(points)
    print("First point x:", points[0]['position']['x'])


def task_r1():
    def gen():
        for i in range(10):
            yield i * i
    arr = np.fromiter(gen(), dtype=int)
    print(arr)

def task_r2():
    a = np.random.randint(0, 2, 5)
    b = np.random.randint(0, 2, 5)
    print("A:", a, "B:", b)
    print("Equal:", np.array_equal(a, b))

def task_r3():
    points = np.random.random((100, 2))
    diff = points[:, np.newaxis, :] - points[np.newaxis, :, :]
    dist = np.sqrt((diff ** 2).sum(axis=-1))
    print("Distance matrix shape:", dist.shape)
    print("Sample distances (first 3x3):\n", dist[:3, :3])

def task_r4():
    a = np.random.randint(0, 10, (4, 5)).astype(float)
    result = a - a.mean(axis=1, keepdims=True)
    print("Original:\n", a, "\nRow-mean subtracted:\n", result)

def task_r5(n=1):
    a = np.random.randint(0, 10, (5, 3))
    print("Original:\n", a)
    sorted_a = a[a[:, n].argsort()]
    print(f"Sorted by column {n}:\n", sorted_a)

def task_r6():
    a = np.random.randint(0, 10, (4, 4))
    print(a)
    print("Rank:", np.linalg.matrix_rank(a))

def task_r7():
    a = np.ones((16, 16), dtype=int)
    block_sum = a.reshape(4, 4, 4, 4).sum(axis=(1, 3))
    print("Block sums (4x4 blocks):\n", block_sum)


if __name__ == '__main__':
    for name, fn in list(globals().items()):
        if name.startswith('task_') and callable(fn):
            print(f"\n-> {name}")
            fn()