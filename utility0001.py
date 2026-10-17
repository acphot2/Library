# 20261015
# 区間被覆問題
# test



class Interval:
    """区間を表すクラス"""
    def __init__(self, start, end, label=None):
        self.start = start
        self.end = end
        self.label = label  # 区間の名前やID（任意）

    def __repr__(self):
        label_str = f", label='{self.label}'" if self.label is not None else ""
        return f"Interval({self.start}, {self.end}{label_str})"


def solve_interval_cover(target_start, target_end, intervals):
    """
    ターゲット区間 [target_start, target_end] を最小の区間数で被覆する関数。

    Parameters:
        target_start (int/float): カバーしたい範囲の開始点
        target_end (int/float): カバーしたい範囲の終了点
        intervals (list of Interval): 利用可能な区間のリスト

    Returns:
        list of Interval: 最小被覆を構成する区間のリスト（カバー不可能な場合は空リスト）
    """
    # 開始点の昇順、同じ開始点なら終了点の降順でソート
    sorted_intervals = sorted(intervals, key=lambda x: (x.start, -x.end))

    selected = []
    current_end = target_start
    n = len(sorted_intervals)
    i = 0

    while current_end < target_end:
        best_interval = None
        max_end = current_end

        # 現在のカバー範囲の開始時点（current_end）以下で始まり、
        # 最も遠くまで届く（endが最大の）区間を探す
        while i < n and sorted_intervals[i].start <= current_end:
            if sorted_intervals[i].end > max_end:
                max_end = sorted_intervals[i].end
                best_interval = sorted_intervals[i]
            i += 1

        # 新たに範囲を広げられない場合はカバー不可能
        if best_interval is None or max_end <= current_end:
            return []

        selected.append(best_interval)
        current_end = max_end

    return selected

#==================================================


# 上記のコードをインポート、または同じファイルに記述
# from interval_cover import Interval, solve_interval_cover

# 1. ターゲット範囲の設定（例: 0 から 10 までをカバーしたい）
target_start = 0
target_end = 10

# 2. 利用可能な区間のリストを作成
available_intervals = [
    Interval(0, 3, "A"),
    Interval(1, 5, "B"),
    Interval(3, 8, "C"),
    Interval(4, 9, "D"),
    Interval(8, 10, "E"),
    Interval(2, 4, "F")
]

# 3. 求解
result = solve_interval_cover(target_start, target_end, available_intervals)

# 4. 結果の出力
if result:
    print(f"最小被覆に必要な区間数: {len(result)}")
    print("選択された区間:")
    for iv in result:
        print(f"  - {iv}")
else:
    print("指定された範囲を完全にカバーすることは不可能です。")