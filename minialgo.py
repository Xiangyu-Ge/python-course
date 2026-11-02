# -*- coding: utf-8 -*-
# ============================================================================
# minialgo.py  --  迷你机器学习 / 空间分析算法库（纯 Python 教学工具箱）
# ============================================================================
#
# 【这是什么】
#   这是一个"零依赖"的教学算法库。里面的距离计算、线性回归、梯度下降、
#   KNN 分类、K-Means 聚类、DBSCAN、莫兰指数、Getis-Ord Gi* 等算法，
#   全部只用最基础的语法实现：变量、if、for、while、def、class、
#   列表(list)、字典(dict)、元组(tuple) 和 math 模块。
#
# 【为什么不用现成的库】
#   因为本学习页面运行的是自研的纯 Python 解释器（不是 CPython），
#   它不支持列表推导式、lambda、map/filter、*args、生成器、装饰器、
#   也不支持 numpy / pandas。所以这里的每一行代码都是"能被读懂"的写法，
#   你完全可以跟着注释把算法逻辑一行一行看明白。
#
# 【怎么用】
#   把这个文件整体粘到代码框最前面（或者在编辑器里把它当作"预置工具箱"），
#   然后直接调用函数即可。例如：
#
#       print(euclid((0, 0), (3, 4)))                 # 输出 5.0
#       print(haversine(116.4, 39.9, 121.5, 31.2))    # 北京到上海约 1067 公里
#       model = linreg_fit([1, 2, 3, 4], [3, 5, 7, 9])
#       print(linreg_predict(model, 10))              # 输出 21.0
#       print(knn_predict([[0, 0], [1, 1]], ['A', 'B'], [0.1, 0.2]))   # 输出 A
#       result = kmeans([[0, 0], [0, 1], [9, 9], [9, 8]], 2)
#       print(result['centroids'], result['labels'], result['inertia'])
#
# 【几条约定】
#   1. 点统一用 [x, y] 或 (x, y) 表示，里面放两个数就行。
#   2. 坐标顺序是 (经度 lon, 纬度 lat)，经度在前、纬度在后。
#   3. 所有函数都不修改传进来的原始列表，需要"新的"就返回新列表。
#   4. 结果是确定性的：同一个输入永远得到同一个输出。
#      只有 split_train_test 会打乱顺序，而它由你传入的 seed 完全决定。
#   5. 随机数是自己写的线性同余伪随机（LCG），种子固定时可复现。
#   6. 空列表、只有一个元素、全部相等、k 比样本还大……这些边界情况
#      都做了处理，函数不会崩溃。
#
# 【函数总览】
#   距离与几何 : euclid / manhattan / haversine / bbox_contains / bbox_center
#                min_max_scale / zscore
#   回归       : mean / std / cov / pearson / linreg_fit / linreg_predict
#                linreg_r2 / gd_linreg / gd_history / mse / mae
#   分类       : knn_predict / knn_proba / split_train_test / confusion_matrix
#                accuracy / precision_recall_f1 / logistic_fit / logistic_predict
#                logistic_proba / sigmoid
#   聚类       : kmeans / kmeans_elbow / kmeans_history / dbscan / silhouette
#   时空分析   : spatial_lag / morans_i / local_morans / getis_ord
#                grid_centroids / buffer_circle / trajectory_speed
#                trajectory_length
#   工具       : train_test_report / describe / median / quantile / histogram
#                normalize_points
#
# ============================================================================

import math


# ============================================================================
# 第 0 部分：内部小工具（外部也可以直接调用，但主要是给上面那些函数用的）
# ============================================================================

def _copy_list(values):
    """把列表浅复制一份，避免函数改动到调用者传进来的原始数据。"""
    result = []
    for i in range(len(values)):
        result.append(values[i])
    return result


def _sorted_copy(values):
    """返回排好序的新列表，不改变传入列表的顺序。"""
    result = _copy_list(values)
    result.sort()
    return result


def _mean_of(values):
    """内部用的平均值，空列表返回 0.0。"""
    n = len(values)
    if n == 0:
        return 0.0
    total = 0.0
    for i in range(n):
        total = total + values[i]
    return total / n


def _l2_distance(p1, p2):
    """内部用的普通欧氏距离，比公开的 euclid() 更少做类型检查，跑得更快。"""
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    return math.sqrt(dx * dx + dy * dy)


def _nearest_indices(coords, k):
    """内部函数：给每个点找出 k 个最近邻居的下标。

    返回一个列表，第 i 个元素是第 i 个点的邻居下标列表。
    点的坐标相同、距离一样时，按下标从小到大取，保证结果确定。
    """
    n = len(coords)
    neighbors = []
    for i in range(n):
        # pairs 里每项是 [距离, 下标]，用"距离优先、下标其次"排序
        pairs = []
        for j in range(n):
            if j == i:
                continue
            pairs.append([_l2_distance(coords[i], coords[j]), j])
        pairs.sort()
        row = []
        limit = k
        if limit > len(pairs):
            limit = len(pairs)
        for t in range(limit):
            row.append(pairs[t][1])
        neighbors.append(row)
    return neighbors


def _lcg(seed):
    """内部函数：自己写的线性同余伪随机数发生器，返回一个"下一个随机数"的函数。

    原理：x = (a * x + c) mod m，这是最古老的伪随机算法之一，好处是
    完全可复现——同样的种子，永远得到同样的数列。
    这里的函数返回 0.0 <= r < 1.0 的浮点数（不会返回恰好 1.0）。
    """
    state = [int(seed) % 2147483647]
    if state[0] <= 0:
        state[0] = state[0] + 2147483646

    def next_rand():
        # 取模前先缩小，避免在不同语言里出现整数溢出的差异
        state[0] = (1103515245 * (state[0] % 65536) + 12345 + 65536 * ((1103515245 * (state[0] // 65536)) % 32768)) % 2147483647
        return state[0] / 2147483647.0

    return next_rand


# ============================================================================
# 第 1 部分：距离与几何
# ============================================================================

def euclid(p1, p2):
    """二维欧氏距离（直线距离）：点用 (x, y) 或 [x, y]。"""
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    return math.sqrt(dx * dx + dy * dy)


def manhattan(p1, p2):
    """二维曼哈顿距离：只沿横竖方向走，"横着走多远 + 竖着走多远"。"""
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def haversine(lon1, lat1, lon2, lat2):
    """球面距离（公里）：把地球当成半径 6371.0088 公里的球，算两点大圆距离。"""
    r = 6371.0088
    # 角度转弧度
    rad_lon1 = math.radians(lon1)
    rad_lat1 = math.radians(lat1)
    rad_lon2 = math.radians(lon2)
    rad_lat2 = math.radians(lat2)
    dlon = rad_lon2 - rad_lon1
    dlat = rad_lat2 - rad_lat1
    a = math.sin(dlat / 2.0) * math.sin(dlat / 2.0) + math.cos(rad_lat1) * math.cos(rad_lat2) * math.sin(dlon / 2.0) * math.sin(dlon / 2.0)
    # 数值误差可能让 a 稍微大于 1，开方前先夹到 [0, 1]
    if a < 0.0:
        a = 0.0
    if a > 1.0:
        a = 1.0
    c = 2.0 * math.asin(math.sqrt(a))
    return r * c


def bbox_contains(bbox, lon, lat):
    """判断一个经纬度点是否落在矩形框内：bbox = [minLon, minLat, maxLon, maxLat]。"""
    if len(bbox) < 4:
        return False
    if lon < bbox[0] or lon > bbox[2]:
        return False
    if lat < bbox[1] or lat > bbox[3]:
        return False
    return True


def bbox_center(bbox):
    """求矩形框的中心点，返回 [lon, lat]。"""
    if len(bbox) < 4:
        return [0.0, 0.0]
    return [(bbox[0] + bbox[2]) / 2.0, (bbox[1] + bbox[3]) / 2.0]


def min_max_scale(values):
    """最小-最大归一化：把一组数线性压到 0~1，返回新列表；全部相等时全给 0.5。"""
    n = len(values)
    if n == 0:
        return []
    lo = values[0]
    hi = values[0]
    for i in range(n):
        if values[i] < lo:
            lo = values[i]
        if values[i] > hi:
            hi = values[i]
    result = []
    span = hi - lo
    for i in range(n):
        if span == 0:
            result.append(0.5)
        else:
            result.append((values[i] - lo) / span)
    return result


def zscore(values):
    """标准化（z-score）：(x - 平均值) / 标准差，返回新列表；标准差为 0 时全给 0.0。"""
    n = len(values)
    if n == 0:
        return []
    mean_value = _mean_of(values)
    # 这里用总体标准差（除以 n），让 z 分数的平方和刚好等于 n
    total = 0.0
    for i in range(n):
        d = values[i] - mean_value
        total = total + d * d
    sd = math.sqrt(total / n)
    result = []
    for i in range(n):
        if sd == 0:
            result.append(0.0)
        else:
            result.append((values[i] - mean_value) / sd)
    return result


# ============================================================================
# 第 2 部分：回归（从平均数、标准差一路做到梯度下降）
# ============================================================================

def mean(values):
    """求算术平均值；空列表返回 0.0。"""
    return _mean_of(values)


def std(values):
    """样本标准差（除以 n-1，用来估计总体波动）；元素少于 2 个时返回 0.0。"""
    n = len(values)
    if n < 2:
        return 0.0
    mean_value = _mean_of(values)
    total = 0.0
    for i in range(n):
        d = values[i] - mean_value
        total = total + d * d
    return math.sqrt(total / (n - 1))


def cov(xs, ys):
    """协方差（除以 n-1）：衡量 x 和 y 是同涨同跌还是此消彼长。"""
    n = len(xs)
    if len(ys) < n:
        n = len(ys)
    if n < 2:
        return 0.0
    mx = 0.0
    my = 0.0
    for i in range(n):
        mx = mx + xs[i]
        my = my + ys[i]
    mx = mx / n
    my = my / n
    total = 0.0
    for i in range(n):
        total = total + (xs[i] - mx) * (ys[i] - my)
    return total / (n - 1)


def pearson(xs, ys):
    """皮尔逊相关系数 r（-1 到 1）：任一方向标准差为 0 时返回 0.0。"""
    n = len(xs)
    if len(ys) < n:
        n = len(ys)
    if n < 2:
        return 0.0
    mx = 0.0
    my = 0.0
    for i in range(n):
        mx = mx + xs[i]
        my = my + ys[i]
    mx = mx / n
    my = my / n
    sxy = 0.0
    sxx = 0.0
    syy = 0.0
    for i in range(n):
        dx = xs[i] - mx
        dy = ys[i] - my
        sxy = sxy + dx * dy
        sxx = sxx + dx * dx
        syy = syy + dy * dy
    if sxx == 0 or syy == 0:
        return 0.0
    return sxy / math.sqrt(sxx * syy)


def linreg_fit(xs, ys):
    """一元线性回归的最小二乘解，返回 [斜率, 截距]。"""
    n = len(xs)
    if len(ys) < n:
        n = len(ys)
    if n == 0:
        return [0.0, 0.0]
    mx = 0.0
    my = 0.0
    for i in range(n):
        mx = mx + xs[i]
        my = my + ys[i]
    mx = mx / n
    my = my / n
    sxy = 0.0
    sxx = 0.0
    for i in range(n):
        dx = xs[i] - mx
        sxy = sxy + dx * (ys[i] - my)
        sxx = sxx + dx * dx
    if sxx == 0:
        # 所有 x 都一样，画不出一条斜线，只能返回"水平线"
        return [0.0, my]
    slope = sxy / sxx
    intercept = my - slope * mx
    return [slope, intercept]


def linreg_predict(model, x):
    """用回归模型算预测值，model 就是 [斜率, 截距]。"""
    if len(model) < 2:
        return 0.0
    return model[0] * x + model[1]


def linreg_r2(xs, ys, model):
    """决定系数 R²：越接近 1 说明直线拟合得越好；总波动为 0 时返回 0.0。"""
    n = len(xs)
    if len(ys) < n:
        n = len(ys)
    if n == 0:
        return 0.0
    my = 0.0
    for i in range(n):
        my = my + ys[i]
    my = my / n
    ss_tot = 0.0
    ss_res = 0.0
    for i in range(n):
        pred = linreg_predict(model, xs[i])
        ss_tot = ss_tot + (ys[i] - my) * (ys[i] - my)
        ss_res = ss_res + (ys[i] - pred) * (ys[i] - pred)
    if ss_tot == 0:
        return 0.0
    return 1.0 - ss_res / ss_tot


def mse(actual, pred):
    """均方误差：先把每个误差平方，再取平均（对大误差惩罚更重）。"""
    n = len(actual)
    if len(pred) < n:
        n = len(pred)
    if n == 0:
        return 0.0
    total = 0.0
    for i in range(n):
        d = actual[i] - pred[i]
        total = total + d * d
    return total / n


def mae(actual, pred):
    """平均绝对误差：误差取绝对值再取平均（单位跟原数据一样，好解释）。"""
    n = len(actual)
    if len(pred) < n:
        n = len(pred)
    if n == 0:
        return 0.0
    total = 0.0
    for i in range(n):
        total = total + abs(actual[i] - pred[i])
    return total / n


def gd_linreg(xs, ys, lr=0.05, epochs=200):
    """梯度下降法求线性回归，返回 [斜率, 截距]（lr 是学习率，epochs 是迭代轮数）。

    注意：x 的数值较大时（比如气温 0~30），默认 lr=0.05 会发散成 inf。
    这时先把 x 标准化（zscore / min_max_scale），或者把 lr 调小（如 0.001）。
    """
    result = gd_history(xs, ys, lr, epochs)
    if len(result) == 0:
        return [0.0, 0.0]
    last = result[len(result) - 1]
    return [last[0], last[1]]


def gd_history(xs, ys, lr=0.05, epochs=200):
    """梯度下降的"损失下降轨迹"：每一步返回 [斜率, 截距, mse]，可以画成动画。

    斜率 m 的更新方向是 2 * 平均(x * 误差)，截距 b 的更新方向是 2 * 平均(误差)。
    """
    n = len(xs)
    if len(ys) < n:
        n = len(ys)
    m = 0.0
    b = 0.0
    history = []
    if n == 0 or epochs <= 0:
        return history
    for step in range(epochs):
        # 1) 先算当前模型的平均误差
        sum_err = 0.0
        sum_x_err = 0.0
        for i in range(n):
            err = (m * xs[i] + b) - ys[i]
            sum_err = sum_err + err
            sum_x_err = sum_x_err + err * xs[i]
        grad_m = 2.0 * sum_x_err / n
        grad_b = 2.0 * sum_err / n
        # 2) 沿着梯度的反方向走一小步（lr 控制步子大小）
        m = m - lr * grad_m
        b = b - lr * grad_b
        # 3) 记下这一步的模型和它的均方误差
        pred = []
        for i in range(n):
            pred.append(m * xs[i] + b)
        history.append([m, b, mse(ys, pred)])
    return history


# ============================================================================
# 第 3 部分：分类（KNN、逻辑回归、评价指标）
# ============================================================================

def knn_predict(X_train, y_train, x_query, k=3):
    """K 近邻分类：找最近的 k 个训练样本投票，票数相同时取较小的标签。"""
    n = len(X_train)
    if len(y_train) < n:
        n = len(y_train)
    if n == 0:
        return None
    if k <= 0:
        k = 1
    # 1) 算出查询点到每个训练点的距离
    pairs = []
    for i in range(n):
        pairs.append([_l2_distance(x_query, X_train[i]), i])
    # 2) 距离从小到大排序（距离相同时按下标，保证结果确定）
    pairs.sort()
    limit = k
    if limit > n:
        limit = n
    # 3) 前 k 个邻居投票
    counts = {}
    for t in range(limit):
        label = y_train[pairs[t][1]]
        if label in counts:
            counts[label] = counts[label] + 1
        else:
            counts[label] = 1
    # 4) 找出票王；票数相同时用"较小的标签"，让结果可复现
    best_label = None
    best_count = -1
    labels = []
    for label in counts:
        labels.append(label)
    labels = sorted(labels)
    for i in range(len(labels)):
        label = labels[i]
        if counts[label] > best_count:
            best_count = counts[label]
            best_label = label
    return best_label


def knn_proba(X_train, y_train, x_query, k=3):
    """K 近邻的"投票比例"：返回 {标签: 占比}，可以当作粗略概率用。"""
    n = len(X_train)
    if len(y_train) < n:
        n = len(y_train)
    if n == 0:
        return {}
    if k <= 0:
        k = 1
    pairs = []
    for i in range(n):
        pairs.append([_l2_distance(x_query, X_train[i]), i])
    pairs.sort()
    limit = k
    if limit > n:
        limit = n
    counts = {}
    for t in range(limit):
        label = y_train[pairs[t][1]]
        if label in counts:
            counts[label] = counts[label] + 1
        else:
            counts[label] = 1
    result = {}
    labels = []
    for label in counts:
        labels.append(label)
    labels = sorted(labels)
    for i in range(len(labels)):
        label = labels[i]
        result[label] = counts[label] / limit
    return result


def split_train_test(X, y, ratio=0.7, seed=42):
    """按比例切分训练集/测试集，返回 [X_train, X_test, y_train, y_test]。

    打乱顺序用的是自写的线性同余伪随机，种子固定时每次切分结果完全一样。
    """
    n = len(X)
    if len(y) < n:
        n = len(y)
    if n == 0:
        return [[], [], [], []]
    # 1) 先准备好一个"索引洗牌"算法（Fisher-Yates 洗牌）
    index = []
    for i in range(n):
        index.append(i)
    rand = _lcg(seed)
    i = n - 1
    while i > 0:
        pick = int(rand() * (i + 1))
        if pick > i:
            pick = i
        if pick < 0:
            pick = 0
        tmp = index[i]
        index[i] = index[pick]
        index[pick] = tmp
        i = i - 1
    # 2) 计算切点，保证训练集和测试集都不为空（只要样本够多）
    n_train = int(n * ratio)
    if n_train < 1:
        n_train = 1
    if n_train > n - 1:
        n_train = n - 1
    if n == 1:
        n_train = 1
    X_train = []
    X_test = []
    y_train = []
    y_test = []
    for t in range(n):
        pos = index[t]
        if t < n_train:
            X_train.append(X[pos])
            y_train.append(y[pos])
        else:
            X_test.append(X[pos])
            y_test.append(y[pos])
    return [X_train, X_test, y_train, y_test]


def confusion_matrix(y_true, y_pred, labels):
    """混淆矩阵：返回 {"labels": [...], "matrix": [[...], ...]}，行是真值、列是预测。"""
    label_list = _copy_list(labels)
    size = len(label_list)
    # 先把标签映射成 0,1,2... 方便定位表格单元格
    position = {}
    for i in range(size):
        position[label_list[i]] = i
    matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(0)
        matrix.append(row)
    n = len(y_true)
    if len(y_pred) < n:
        n = len(y_pred)
    for t in range(n):
        true_label = y_true[t]
        pred_label = y_pred[t]
        if true_label in position and pred_label in position:
            r = position[true_label]
            c = position[pred_label]
            matrix[r][c] = matrix[r][c] + 1
    return {"labels": label_list, "matrix": matrix}


def accuracy(y_true, y_pred):
    """准确率：预测对的样本数占总样本数的比例；没有样本时返回 0.0。"""
    n = len(y_true)
    if len(y_pred) < n:
        n = len(y_pred)
    if n == 0:
        return 0.0
    correct = 0
    for i in range(n):
        if y_true[i] == y_pred[i]:
            correct = correct + 1
    return correct / n


def precision_recall_f1(y_true, y_pred, label):
    """针对某个标签算精确率、召回率、F1，返回 [精确率, 召回率, F1]。"""
    n = len(y_true)
    if len(y_pred) < n:
        n = len(y_pred)
    tp = 0
    fp = 0
    fn = 0
    for i in range(n):
        is_true = y_true[i] == label
        is_pred = y_pred[i] == label
        if is_true and is_pred:
            tp = tp + 1
        elif is_pred and not is_true:
            fp = fp + 1
        elif is_true and not is_pred:
            fn = fn + 1
    if tp + fp == 0:
        precision = 0.0
    else:
        precision = tp / (tp + fp)
    if tp + fn == 0:
        recall = 0.0
    else:
        recall = tp / (tp + fn)
    if precision + recall == 0:
        f1 = 0.0
    else:
        f1 = 2.0 * precision * recall / (precision + recall)
    return [precision, recall, f1]


def sigmoid(z):
    """S 形函数 1/(1+e^-z)：把任意实数压到 0~1 之间，逻辑回归的核心。"""
    # 防止 e 的指数太大导致溢出，先把 z 夹在 [-60, 60]
    if z < -60.0:
        z = -60.0
    if z > 60.0:
        z = 60.0
    return 1.0 / (1.0 + math.exp(-z))


def logistic_fit(X, y, lr=0.1, epochs=300):
    """逻辑回归训练（X 是二维特征），返回 [w1, w2, b]；内部自动做了标准化。"""
    n = len(X)
    if len(y) < n:
        n = len(y)
    if n == 0:
        return [0.0, 0.0, 0.0]
    # 1) 先算每一列的平均值和标准差（用于标准化，让梯度下降更稳）
    sum1 = 0.0
    sum2 = 0.0
    for i in range(n):
        sum1 = sum1 + X[i][0]
        sum2 = sum2 + X[i][1]
    mean1 = sum1 / n
    mean2 = sum2 / n
    var1 = 0.0
    var2 = 0.0
    for i in range(n):
        d1 = X[i][0] - mean1
        d2 = X[i][1] - mean2
        var1 = var1 + d1 * d1
        var2 = var2 + d2 * d2
    sd1 = math.sqrt(var1 / n)
    sd2 = math.sqrt(var2 / n)
    if sd1 == 0:
        sd1 = 1.0
    if sd2 == 0:
        sd2 = 1.0
    # 2) 在标准化后的空间里跑梯度下降
    w1 = 0.0
    w2 = 0.0
    b = 0.0
    for step in range(epochs):
        g1 = 0.0
        g2 = 0.0
        gb = 0.0
        for i in range(n):
            z1 = (X[i][0] - mean1) / sd1
            z2 = (X[i][1] - mean2) / sd2
            p = sigmoid(w1 * z1 + w2 * z2 + b)
            err = p - y[i]
            g1 = g1 + err * z1
            g2 = g2 + err * z2
            gb = gb + err
        w1 = w1 - lr * g1 / n
        w2 = w2 - lr * g2 / n
        b = b - lr * gb / n
    # 3) 把系数换算回原始特征尺度，这样预测函数可以直接吃原始坐标
    coef1 = w1 / sd1
    coef2 = w2 / sd2
    intercept = b - w1 * mean1 / sd1 - w2 * mean2 / sd2
    return [coef1, coef2, intercept]


def logistic_proba(model, x):
    """逻辑回归预测"属于第 1 类"的概率（0~1 之间）。"""
    if len(model) < 3:
        return 0.5
    return sigmoid(model[0] * x[0] + model[1] * x[1] + model[2])


def logistic_predict(model, x):
    """逻辑回归分类结果：概率大于等于 0.5 判为 1，否则判为 0。"""
    if logistic_proba(model, x) >= 0.5:
        return 1
    return 0


# ============================================================================
# 第 4 部分：聚类（K-Means、DBSCAN、轮廓系数）
# ============================================================================

class KMeans:
    """K-Means 聚类器：反复"分配点 -> 更新中心"，直到中心不再移动。

    用法：
        km = KMeans(2, seed=7)
        km.fit(X)
        print(km.centroids)   # 每个簇的中心
        print(km.labels)      # 每个点属于哪个簇
        print(km.inertia)     # 簇内平方和，越小说明簇越紧凑
    """

    def __init__(self, k=2, seed=7, max_iter=100):
        """初始化：记下要聚几类、随机种子和最大迭代次数。"""
        self.k = k
        self.seed = seed
        self.max_iter = max_iter
        self.centroids = []
        self.labels = []
        self.inertia = 0.0
        self.iters = 0
        self.history = []

    def __str__(self):
        """打印这个对象时，用一行字概括它的状态，方便调试。"""
        return "KMeans(k=" + str(self.k) + ", iters=" + str(self.iters) + ", inertia=" + str(round(self.inertia, 4)) + ")"

    def _point_dist(self, p1, p2):
        """算一个点到另一个点的距离（内部用，避免重复做参数检查）。"""
        return _l2_distance(p1, p2)

    def _init_centroids(self, X):
        """挑 k 个初始中心：先随机选一个点，之后每次选"离已有中心最远"的点。

        这种"最远点"策略比纯随机更稳，而且完全确定（只依赖种子选的第一个点）。
        """
        n = len(X)
        rand = _lcg(self.seed)
        first = int(rand() * n)
        if first >= n:
            first = n - 1
        centers = [X[first]]
        while len(centers) < self.k:
            # 找出离现有中心最远的点，把它当作下一个中心
            best_index = 0
            best_dist = -1.0
            for i in range(n):
                near = -1.0
                for c in range(len(centers)):
                    d = self._point_dist(X[i], centers[c])
                    if near < 0 or d < near:
                        near = d
                if near > best_dist:
                    best_dist = near
                    best_index = i
            # 万一所有点都已经被选过，就随机补一个不同的点
            candidate = X[best_index]
            duplicate = False
            for c in range(len(centers)):
                if centers[c][0] == candidate[0] and centers[c][1] == candidate[1]:
                    duplicate = True
            if duplicate:
                pick = int(rand() * n)
                if pick >= n:
                    pick = n - 1
                candidate = X[pick]
            centers.append(candidate)
        return centers

    def _assign(self, X, centers):
        """把每个点分配到离它最近的中心，返回标签列表。"""
        labels = []
        for i in range(len(X)):
            best = 0
            best_dist = -1.0
            for c in range(len(centers)):
                d = self._point_dist(X[i], centers[c])
                if best_dist < 0 or d < best_dist:
                    best_dist = d
                    best = c
            labels.append(best)
        return labels

    def _centers_of(self, X, labels, centers):
        """根据当前分配结果重新计算每个簇的中心（也就是簇内所有点的平均位置）。"""
        new_centers = []
        for c in range(len(centers)):
            # 累加这个簇里所有点的横纵坐标
            sum_x = 0.0
            sum_y = 0.0
            count = 0
            for i in range(len(X)):
                if labels[i] == c:
                    sum_x = sum_x + X[i][0]
                    sum_y = sum_y + X[i][1]
                    count = count + 1
            if count == 0:
                # 这个簇一个点都没有，保留原来的中心，不让它消失
                new_centers.append([centers[c][0], centers[c][1]])
            else:
                new_centers.append([sum_x / count, sum_y / count])
        return new_centers

    def _inertia_of(self, X, labels, centers):
        """簇内平方和：每个点到它所属中心的距离平方之和，越小越紧凑。"""
        total = 0.0
        for i in range(len(X)):
            c = labels[i]
            dx = X[i][0] - centers[c][0]
            dy = X[i][1] - centers[c][1]
            total = total + dx * dx + dy * dy
        return total

    def _changed(self, old_centers, new_centers):
        """判断中心是否还在移动（移动距离超过一个极小值就算变了）。"""
        if len(old_centers) != len(new_centers):
            return True
        for c in range(len(old_centers)):
            dx = old_centers[c][0] - new_centers[c][0]
            dy = old_centers[c][1] - new_centers[c][1]
            if math.sqrt(dx * dx + dy * dy) > 1e-9:
                return True
        return False

    def fit(self, X):
        """在点集 X 上完成一次完整的 K-Means 聚类，返回自己（方便链式调用）。"""
        n = len(X)
        self.centroids = []
        self.labels = []
        self.inertia = 0.0
        self.iters = 0
        self.history = []
        if n == 0:
            return self
        # 要分的簇数不能超过点数
        if self.k > n:
            self.k = n
        if self.k < 1:
            self.k = 1
        max_iter = self.max_iter
        if max_iter < 1:
            max_iter = 1
        centers = self._init_centroids(X)
        labels = self._assign(X, centers)
        for step in range(max_iter):
            new_centers = self._centers_of(X, labels, centers)
            new_labels = self._assign(X, new_centers)
            # 逐帧动画需要中心点和标签，所以每一步都存一份（深复制，防止后续修改覆盖旧帧）
            snapshot_centers = []
            for c in range(len(centers)):
                snapshot_centers.append([centers[c][0], centers[c][1]])
            snapshot_labels = _copy_list(labels)
            self.history.append([snapshot_centers, snapshot_labels])
            self.iters = step + 1
            # 中心不再移动就提前收工
            stop = not self._changed(centers, new_centers)
            centers = new_centers
            labels = new_labels
            if stop:
                break
        self.centroids = centers
        self.labels = labels
        self.inertia = self._inertia_of(X, labels, centers)
        return self


def kmeans(X, k, seed=7, max_iter=100):
    """K-Means 聚类，返回 {"centroids": 中心, "labels": 标签, "inertia": 簇内平方和, "iters": 轮数}。"""
    result = {"centroids": [], "labels": [], "inertia": 0.0, "iters": 0}
    n = len(X)
    if n == 0:
        return result
    if k > n:
        k = n
    if k < 1:
        k = 1
    if seed < 1:
        seed = 1
    if max_iter < 1:
        max_iter = 1
    # 1) 选初始中心
    centers = []
    rand = _lcg(seed)
    first = int(rand() * n)
    if first >= n:
        first = n - 1
    centers.append([X[first][0], X[first][1]])
    while len(centers) < k:
        # 每一步都挑"离已有中心最远"的那个点作为新中心
        best_index = 0
        best_dist = -1.0
        for i in range(n):
            near = -1.0
            for c in range(len(centers)):
                dx = X[i][0] - centers[c][0]
                dy = X[i][1] - centers[c][1]
                d = dx * dx + dy * dy
                if near < 0 or d < near:
                    near = d
            if near > best_dist:
                best_dist = near
                best_index = i
        centers.append([X[best_index][0], X[best_index][1]])
    # 2) 反复"分配点 -> 重算中心"
    labels = []
    for i in range(n):
        labels.append(0)
    iters = 0
    for step in range(max_iter):
        # 2.1 分配：每个点找最近的中心
        new_labels = []
        for i in range(n):
            best = 0
            best_dist = -1.0
            for c in range(len(centers)):
                dx = X[i][0] - centers[c][0]
                dy = X[i][1] - centers[c][1]
                d = dx * dx + dy * dy
                if best_dist < 0 or d < best_dist:
                    best_dist = d
                    best = c
            new_labels.append(best)
        # 2.2 更新：每个簇的中心改成簇内点的平均位置
        new_centers = []
        for c in range(len(centers)):
            sum_x = 0.0
            sum_y = 0.0
            count = 0
            for i in range(n):
                if new_labels[i] == c:
                    sum_x = sum_x + X[i][0]
                    sum_y = sum_y + X[i][1]
                    count = count + 1
            if count == 0:
                new_centers.append([centers[c][0], centers[c][1]])
            else:
                new_centers.append([sum_x / count, sum_y / count])
        # 2.3 看中心是否还在动
        moved = False
        for c in range(len(centers)):
            dx = centers[c][0] - new_centers[c][0]
            dy = centers[c][1] - new_centers[c][1]
            if math.sqrt(dx * dx + dy * dy) > 1e-9:
                moved = True
        centers = new_centers
        labels = new_labels
        iters = step + 1
        if not moved:
            break
    # 3) 算簇内平方和
    inertia = 0.0
    for i in range(n):
        c = labels[i]
        dx = X[i][0] - centers[c][0]
        dy = X[i][1] - centers[c][1]
        inertia = inertia + dx * dx + dy * dy
    result["centroids"] = centers
    result["labels"] = labels
    result["inertia"] = inertia
    result["iters"] = iters
    return result


def kmeans_elbow(X, k_max=6, seed=7):
    """肘部法则：对 k = 1,2,...,k_max 各跑一次聚类，返回 [[k, inertia], ...]。"""
    n = len(X)
    result = []
    if k_max < 1:
        return result
    limit = k_max
    if limit > n:
        limit = n
    if limit < 1:
        return result
    for k in range(1, limit + 1):
        model = kmeans(X, k, seed, 100)
        result.append([k, model["inertia"]])
    return result


def kmeans_history(X, k, seed=7):
    """K-Means 的逐帧过程：返回每一步的 [centroids, labels]，用来做动画。"""
    n = len(X)
    if n == 0:
        return []
    if k > n:
        k = n
    if k < 1:
        k = 1
    if seed < 1:
        seed = 1
    # 初始中心：跟 kmeans() 用同样的规则，保证两者结果一致
    centers = []
    rand = _lcg(seed)
    first = int(rand() * n)
    if first >= n:
        first = n - 1
    centers.append([X[first][0], X[first][1]])
    while len(centers) < k:
        best_index = 0
        best_dist = -1.0
        for i in range(n):
            near = -1.0
            for c in range(len(centers)):
                dx = X[i][0] - centers[c][0]
                dy = X[i][1] - centers[c][1]
                d = dx * dx + dy * dy
                if near < 0 or d < near:
                    near = d
            if near > best_dist:
                best_dist = near
                best_index = i
        centers.append([X[best_index][0], X[best_index][1]])
    frames = []
    labels = []
    for i in range(n):
        labels.append(0)
    for step in range(100):
        # 分配
        new_labels = []
        for i in range(n):
            best = 0
            best_dist = -1.0
            for c in range(len(centers)):
                dx = X[i][0] - centers[c][0]
                dy = X[i][1] - centers[c][1]
                d = dx * dx + dy * dy
                if best_dist < 0 or d < best_dist:
                    best_dist = d
                    best = c
            new_labels.append(best)
        # 更新
        new_centers = []
        for c in range(len(centers)):
            sum_x = 0.0
            sum_y = 0.0
            count = 0
            for i in range(n):
                if new_labels[i] == c:
                    sum_x = sum_x + X[i][0]
                    sum_y = sum_y + X[i][1]
                    count = count + 1
            if count == 0:
                new_centers.append([centers[c][0], centers[c][1]])
            else:
                new_centers.append([sum_x / count, sum_y / count])
        moved = False
        for c in range(len(centers)):
            dx = centers[c][0] - new_centers[c][0]
            dy = centers[c][1] - new_centers[c][1]
            if math.sqrt(dx * dx + dy * dy) > 1e-9:
                moved = True
        centers = new_centers
        labels = new_labels
        # 存一帧（深复制，避免后面的修改影响到已经存下的帧）
        frame_centers = []
        for c in range(len(centers)):
            frame_centers.append([centers[c][0], centers[c][1]])
        frame_labels = _copy_list(labels)
        frames.append([frame_centers, frame_labels])
        if not moved:
            break
    return frames


def dbscan(X, eps, min_pts):
    """DBSCAN 密度聚类，返回 {"labels": 标签, "n_clusters": 簇数, "n_noise": 噪声数}。

    核心思想：一个点周围 eps 范围内如果有至少 min_pts 个点（含自己），
    它就是"核心点"；核心点能互相连成一片，就连成一个簇；连不上的算噪声（标签 -1）。
    """
    n = len(X)
    labels = []
    for i in range(n):
        labels.append(-2)  # -2 表示"还没看过"，-1 表示噪声，0/1/2... 表示簇编号
    result = {"labels": labels, "n_clusters": 0, "n_noise": 0}
    if n == 0:
        result["labels"] = []
        return result
    if min_pts < 1:
        min_pts = 1
    if eps < 0:
        eps = 0.0
    # 1) 预先算好每个点的邻居（包括自己）和它的"半径内点数"
    neighbors = []
    for i in range(n):
        row = []
        for j in range(n):
            if _l2_distance(X[i], X[j]) <= eps:
                row.append(j)
        neighbors.append(row)
    # 2) 逐个点处理：是核心点就往外"长"出一个簇
    cluster_id = 0
    for i in range(n):
        if labels[i] != -2:
            continue
        if len(neighbors[i]) < min_pts:
            labels[i] = -1  # 不是核心点，先当噪声（后面可能被别的簇收编）
            continue
        # 从点 i 出发，做一次区域生长
        labels[i] = cluster_id
        queue = []
        for t in range(len(neighbors[i])):
            queue.append(neighbors[i][t])
        head = 0
        while head < len(queue):
            j = queue[head]
            head = head + 1
            # 半径内的点，如果之前被判成噪声，现在收编进这个簇
            if labels[j] == -1:
                labels[j] = cluster_id
            if labels[j] != -2:
                continue
            labels[j] = cluster_id
            # j 自己也是核心点的话，把它的邻居也拉进来一起长
            if len(neighbors[j]) >= min_pts:
                for t in range(len(neighbors[j])):
                    queue.append(neighbors[j][t])
        cluster_id = cluster_id + 1
    # 3) 统计噪声个数
    n_noise = 0
    for i in range(n):
        if labels[i] == -1:
            n_noise = n_noise + 1
    result["labels"] = labels
    result["n_clusters"] = cluster_id
    result["n_noise"] = n_noise
    return result


def silhouette(X, labels):
    """平均轮廓系数（-1 到 1，越大说明聚类分得越开）；无法计算时返回 0.0。

    对每个点：a = 它到同簇其他点的平均距离，b = 它到最近的其他簇的平均距离，
    单点分数 = (b - a) / max(a, b)。最后对所有点取平均。
    """
    n = len(X)
    if len(labels) < n:
        n = len(labels)
    if n < 2:
        return 0.0
    # 统计有哪些簇（忽略噪声 -1）
    cluster_ids = []
    for i in range(n):
        c = labels[i]
        if c == -1:
            continue
        if c not in cluster_ids:
            cluster_ids.append(c)
    if len(cluster_ids) < 2:
        return 0.0
    scores = []
    for i in range(n):
        if labels[i] == -1:
            continue
        # a：同簇平均距离
        sum_same = 0.0
        count_same = 0
        for j in range(n):
            if j != i and labels[j] == labels[i]:
                sum_same = sum_same + _l2_distance(X[i], X[j])
                count_same = count_same + 1
        # b：最近的其他簇的平均距离
        best_other = -1.0
        for c in range(len(cluster_ids)):
            other = cluster_ids[c]
            if other == labels[i]:
                continue
            sum_other = 0.0
            count_other = 0
            for j in range(n):
                if labels[j] == other:
                    sum_other = sum_other + _l2_distance(X[i], X[j])
                    count_other = count_other + 1
            if count_other > 0:
                avg_other = sum_other / count_other
                if best_other < 0 or avg_other < best_other:
                    best_other = avg_other
        if count_same == 0 or best_other < 0:
            # 这个簇只有自己一个点，或者没有别的簇，算不出轮廓，跳过
            continue
        a = sum_same / count_same
        b = best_other
        biggest = a
        if b > biggest:
            biggest = b
        if biggest == 0:
            scores.append(0.0)
        else:
            scores.append((b - a) / biggest)
    if len(scores) == 0:
        return 0.0
    total = 0.0
    for i in range(len(scores)):
        total = total + scores[i]
    return total / len(scores)


# ============================================================================
# 第 5 部分：时空分析（空间权重、莫兰指数、Getis-Ord、网格、轨迹）
# ============================================================================

def spatial_lag(values, coords, k=4):
    """空间滞后：每个点取它 k 个最近邻居的平均值（不含它自己）。"""
    n = len(values)
    if len(coords) < n:
        n = len(coords)
    if n == 0:
        return []
    if k < 1:
        k = 1
    neighbors = _nearest_indices(coords, k)
    result = []
    for i in range(n):
        row = neighbors[i]
        if len(row) == 0:
            result.append(float(values[i]))
        else:
            total = 0.0
            for t in range(len(row)):
                total = total + values[row[t]]
            result.append(total / len(row))
    return result


def morans_i(values, coords, k=4):
    """全局莫兰指数：衡量"相邻的点数值是否相似"，返回 [I, E_I]。

    I > 0 说明高值与高值扎堆（空间聚集），I  0 说明随机分布，
    I < 0 说明高值与低值相邻（空间分散）。E_I 是随机情况下的期望值。
    """
    n = len(values)
    if len(coords) < n:
        n = len(coords)
    if n < 2:
        return [0.0, 0.0]
    if k < 1:
        k = 1
    mean_value = _mean_of(values)
    # 1) 离差
    z = []
    for i in range(n):
        z.append(values[i] - mean_value)
    variance = 0.0
    for i in range(n):
        variance = variance + z[i] * z[i]
    variance = variance / n
    if variance == 0:
        # 所有值都一样，谈不上"聚集"，直接返回 0
        return [0.0, -1.0 / (n - 1)]
    # 2) 邻居表，权重按"每行和为 1"处理（每个邻居权重 1/k）
    neighbors = _nearest_indices(coords, k)
    s0 = 0.0
    for i in range(n):
        s0 = s0 + len(neighbors[i])
    if s0 == 0:
        return [0.0, -1.0 / (n - 1)]
    # 3) 分子：每个点与它邻居平均值的"同步程度"
    numerator = 0.0
    for i in range(n):
        row = neighbors[i]
        if len(row) == 0:
            continue
        lag_total = 0.0
        for t in range(len(row)):
            lag_total = lag_total + z[row[t]]
        numerator = numerator + z[i] * (lag_total / len(row))
    # 行标准化后权重总和 W = n,公式 I = (n / W) * Σ z_i * lag_i / Σ z_i² 化简为
    # Σ z_i * lag_i / Σ z_i²。注意 variance 已经除过 n,所以分母要乘回 n。
    i_value = numerator / (variance * n)
    expected = -1.0 / (n - 1)
    return [i_value, expected]


def local_morans(values, coords, k=4):
    """局部莫兰指数：每个点的 Ii 值列表，用来找"热点"和"冷点"具体在哪。"""
    n = len(values)
    if len(coords) < n:
        n = len(coords)
    if n < 2:
        return []
    if k < 1:
        k = 1
    mean_value = _mean_of(values)
    z = []
    for i in range(n):
        z.append(values[i] - mean_value)
    variance = 0.0
    for i in range(n):
        variance = variance + z[i] * z[i]
    variance = variance / n
    if variance == 0:
        result = []
        for i in range(n):
            result.append(0.0)
        return result
    neighbors = _nearest_indices(coords, k)
    result = []
    for i in range(n):
        row = neighbors[i]
        if len(row) == 0:
            result.append(0.0)
            continue
        lag_total = 0.0
        for t in range(len(row)):
            lag_total = lag_total + z[row[t]]
        lag = lag_total / len(row)
        result.append(z[i] * lag / variance)
    return result


def getis_ord(values, coords, k=4):
    """Getis-Ord Gi* 近似值：每个点的局部热点统计量，值越大越像"高值聚集区"。"""
    n = len(values)
    if len(coords) < n:
        n = len(coords)
    if n < 2:
        return []
    if k < 1:
        k = 1
    mean_value = _mean_of(values)
    total = 0.0
    for i in range(n):
        d = values[i] - mean_value
        total = total + d * d
    variance = total / n
    if variance == 0:
        result = []
        for i in range(n):
            result.append(0.0)
        return result
    sd = math.sqrt(variance)
    neighbors = _nearest_indices(coords, k)
    result = []
    for i in range(n):
        row = neighbors[i]
        # Gi* 的权重包含自己，所以分子是"自己 + 邻居"的和
        lag_total = values[i]
        for t in range(len(row)):
            lag_total = lag_total + values[row[t]]
        w = len(row) + 1
        numerator = lag_total - mean_value * w
        denominator = sd * math.sqrt((n * w - w * w) / (n - 1))
        if denominator == 0:
            result.append(0.0)
        else:
            result.append(numerator / denominator)
    return result


def grid_centroids(lon_min, lat_min, cell_size, rows, cols):
    """生成规则网格的中心点：返回 rows*cols 个 [lon, lat]，按行优先排列。"""
    result = []
    if rows < 1 or cols < 1:
        return result
    half = cell_size / 2.0
    for r in range(rows):
        for c in range(cols):
            result.append([lon_min + c * cell_size + half, lat_min + r * cell_size + half])
    return result


def buffer_circle(lon, lat, radius_km, n=12):
    """近似缓冲区：以 (lon, lat) 为圆心、radius_km 为半径，返回圆周上 n 个点。"""
    result = []
    if n < 1:
        return result
    # 纬度方向：1 度约 111.32 公里；经度方向要除以 cos(纬度)，越靠两极越"窄"
    dlat = radius_km / 111.32
    cos_lat = math.cos(math.radians(lat))
    if cos_lat < 0:
        cos_lat = -cos_lat
    if cos_lat < 1e-9:
        cos_lat = 1e-9
    dlon = radius_km / (111.32 * cos_lat)
    for i in range(n):
        angle = 2.0 * math.pi * i / n
        result.append([lon + dlon * math.cos(angle), lat + dlat * math.sin(angle)])
    return result


def trajectory_speed(coords, times):
    """轨迹分段速度（公里/小时）：times 是每个点的小时数，返回每个点的速度。

    因为 n 个点只有 n-1 段，所以结果长度和点一样，第一个位置用 0.0 表示"起点没有速度"。
    """
    n = len(coords)
    if len(times) < n:
        n = len(times)
    if n == 0:
        return []
    result = [0.0]
    for i in range(1, n):
        dt = times[i] - times[i - 1]
        if dt == 0:
            result.append(0.0)
            continue
        d = haversine(coords[i - 1][0], coords[i - 1][1], coords[i][0], coords[i][1])
        result.append(d / dt)
    return result


def trajectory_length(coords):
    """轨迹总长度（公里）：把所有相邻点之间的距离加起来。"""
    n = len(coords)
    if n < 2:
        return 0.0
    total = 0.0
    for i in range(1, n):
        total = total + haversine(coords[i - 1][0], coords[i - 1][1], coords[i][0], coords[i][1])
    return total


# ============================================================================
# 第 6 部分：通用工具（统计描述、分位数、直方图、坐标归一化）
# ============================================================================

def train_test_report(X_train, y_train, X_test, y_test, k=3):
    """切分之后一次性看效果：返回 {"accuracy": 准确率, "predictions": 预测标签列表}。"""
    predictions = []
    for i in range(len(X_test)):
        predictions.append(knn_predict(X_train, y_train, X_test[i], k))
    acc = accuracy(y_test, predictions)
    return {"accuracy": acc, "predictions": predictions}


def median(values):
    """中位数：排序后正中间的那个数，偶数个时取中间两个的平均；空列表返回 0.0。"""
    n = len(values)
    if n == 0:
        return 0.0
    data = _sorted_copy(values)
    middle = n // 2
    if n % 2 == 1:
        return float(data[middle])
    return (data[middle - 1] + data[middle]) / 2.0


def quantile(values, q):
    """分位数：q 取 0~1（0.5 就是中位数），用线性插值；空列表返回 0.0。"""
    n = len(values)
    if n == 0:
        return 0.0
    if q < 0:
        q = 0.0
    if q > 1:
        q = 1.0
    data = _sorted_copy(values)
    if n == 1:
        return float(data[0])
    pos = q * (n - 1)
    low = int(pos)
    if low >= n - 1:
        return float(data[n - 1])
    frac = pos - low
    return data[low] + (data[low + 1] - data[low]) * frac


def describe(values):
    """一组数据的描述统计：返回 {"n","min","max","mean","std","median"}。"""
    n = len(values)
    if n == 0:
        return {"n": 0, "min": 0.0, "max": 0.0, "mean": 0.0, "std": 0.0, "median": 0.0}
    data = _sorted_copy(values)
    return {
        "n": n,
        "min": float(data[0]),
        "max": float(data[n - 1]),
        "mean": _mean_of(values),
        "std": std(values),
        "median": median(values)
    }


def histogram(values, bins=10):
    """直方图分组：返回 [[下界, 上界, 计数], ...]，可直接拿去画柱状图。"""
    n = len(values)
    result = []
    if n == 0 or bins < 1:
        return result
    lo = values[0]
    hi = values[0]
    for i in range(n):
        if values[i] < lo:
            lo = values[i]
        if values[i] > hi:
            hi = values[i]
    if hi == lo:
        # 所有数一样，就造一个把数据罩住的小区间
        lo = lo - 0.5
        hi = hi + 0.5
    width = (hi - lo) / bins
    for b in range(bins):
        result.append([lo + b * width, lo + (b + 1) * width, 0])
    for i in range(n):
        # 算这个数落在第几组；最大的那个数归到最后一组，避免越界
        position = int((values[i] - lo) / width)
        if position >= bins:
            position = bins - 1
        if position < 0:
            position = 0
        result[position][2] = result[position][2] + 1
    return result


def normalize_points(points):
    """把一批点整体缩放到 0~1 的方框里，方便在画布上作图（保持形状不变形）。"""
    n = len(points)
    if n == 0:
        return []
    min_x = points[0][0]
    max_x = points[0][0]
    min_y = points[0][1]
    max_y = points[0][1]
    for i in range(n):
        if points[i][0] < min_x:
            min_x = points[i][0]
        if points[i][0] > max_x:
            max_x = points[i][0]
        if points[i][1] < min_y:
            min_y = points[i][1]
        if points[i][1] > max_y:
            max_y = points[i][1]
    span_x = max_x - min_x
    span_y = max_y - min_y
    # 用两个方向里较大的跨度做同一个比例，这样点的相对形状不会被拉扁
    span = span_x
    if span_y > span:
        span = span_y
    if span == 0:
        # 所有点重合在一起，统一放到画布中间
        result = []
        for i in range(n):
            result.append([0.5, 0.5])
        return result
    result = []
    for i in range(n):
        x = (points[i][0] - min_x) / span
        y = (points[i][1] - min_y) / span
        result.append([x, y])
    return result
