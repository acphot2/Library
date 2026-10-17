class SegmentTreeMax:
    def __init__(self, init_val):
        """
        初期化
        init_val: リスト（初期の値）
        """
        n = len(init_val)
        self.ide_ele = -float('inf')  # 最大値クエリの単位元（比較に影響しない最小値）
        
        # 要素数を2のべき乗に切り上げる
        self.num = 1 << (n - 1).bit_length()
        self.tree = [self.ide_ele] * (2 * self.num)
        
        # 葉に値を設定する
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        
        # 2段目以降のノードを構築する
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = max(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        """
        k番目の要素を x に更新する（0-indexed）
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            k >>= 1
            self.tree[k] = max(self.tree[2 * k], self.tree[2 * k + 1])

    def query(self, l, r):
        """
        [l, r) の区間最大値を取得する（0-indexed、rは含まない）
        """
        res = self.ide_ele
        l += self.num
        r += self.num
        
        while l < r:
            if l & 1:
                res = max(res, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                res = max(res, self.tree[r])
            l >>= 1
            r >>= 1
        return res


#==================================================
    
# 初期データ
data = [1, 3, 5, 2, 7, 6, 4]
seg = SegmentTreeMax(data)

# 1. 区間 [1, 4) の最大値を取得（インデックス1, 2, 3 の要素: 3, 5, 2）
print(seg.query(1, 4))  # 出力: 5

# 2. インデックス3の値を 10 に更新
seg.update(3, 10)  # data[3] が 10 になる

# 3. 再び区間 [1, 4) の最大値を取得（インデックス1, 2, 3 の要素: 3, 5, 10）
print(seg.query(1, 4))  # 出力: 10


#==================================================

class SegmentTreeMin:
    def __init__(self, init_val):
        """
        初期化（区間最小値用）
        init_val: リスト（初期の値）
        """
        n = len(init_val)
        self.ide_ele = float('inf')  # 最小値クエリの単位元（比較に影響しない無限大）
        
        # 要素数を2のべき乗に切り上げる
        self.num = 1 << (n - 1).bit_length()
        self.tree = [self.ide_ele] * (2 * self.num)
        
        # 葉に値を設定する
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        
        # 2段目以降のノードを構築する（minに変更）
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = min(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        """
        k番目の要素を x に更新する（0-indexed）
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            k >>= 1
            self.tree[k] = min(self.tree[2 * k], self.tree[2 * k + 1])

    def query(self, l, r):
        """
        [l, r) の区間最小値を取得する（0-indexed、rは含まない）
        """
        res = self.ide_ele
        l += self.num
        r += self.num
        
        while l < r:
            if l & 1:
                res = min(res, self.tree[l])  # max から min に変更
                l += 1
            if r & 1:
                r -= 1
                res = min(res, self.tree[r])  # max から min に変更
            l >>= 1
            r >>= 1
        return res


#==================================================

# 初期データ
data = [5, 2, 8, 1, 9, 3]
seg = SegmentTreeMin(data)

# 1. 区間 [1, 4) の最小値を取得（インデックス1, 2, 3 の要素: 2, 8, 1）
print(seg.query(1, 4))  # 出力: 1

# 2. インデックス3の値を 10 に更新（data[3] が 1 から 10 になる）
seg.update(3, 10)

# 3. 再び区間 [1, 4) の最小値を取得（インデックス1, 2, 3 の要素: 2, 8, 10）
print(seg.query(1, 4))  # 出力: 2

#==================================================

class SegmentTreeSum:
    def __init__(self, init_val):
        """
        初期化（区間総和用）
        """
        n = len(init_val)
        self.ide_ele = 0  # 総和の単位元は 0
        
        # 要素数を2のべき乗に切り上げる
        self.num = 1 << (n - 1).bit_length()
        self.tree = [self.ide_ele] * (2 * self.num)
        
        # 葉に値を設定する
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        
        # 2段目以降のノードを構築する（足し算に変更）
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, k, x):
        """
        k番目の要素を x に更新する（0-indexed）
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            k >>= 1
            self.tree[k] = self.tree[2 * k] + self.tree[2 * k + 1]

    def query(self, l, r):
        """
        [l, r) の区間総和を取得する（0-indexed、rは含まない）
        """
        res = self.ide_ele
        l += self.num
        r += self.num
        
        while l < r:
            if l & 1:
                res += self.tree[l]  # max から += に変更
                l += 1
            if r & 1:
                r -= 1
                res += self.tree[r]  # max から += に変更
            l >>= 1
            r >>= 1
        return res


#==================================================
# 初期データ
data = [1, 2, 3, 4, 5]
seg = SegmentTreeSum(data)

# 1. 区間 [1, 4) の総和を取得（インデックス1, 2, 3 の要素: 2 + 3 + 4）
print(seg.query(1, 4))  # 出力: 9

# 2. インデックス2の値を 10 に更新（data[2] が 3 から 10 になる）
seg.update(2, 10)

# 3. 再び区間 [1, 4) の総和を取得（インデックス1, 2, 3 の要素: 2 + 10 + 4）
print(seg.query(1, 4))  # 出力: 16


