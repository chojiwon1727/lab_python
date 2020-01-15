import math
from collections import Counter, defaultdict
from typing import NamedTuple, Any
import matplotlib.pyplot as plt
import numpy as np


# NamedTuple을 상속받는 클래스 선언
class Candidate(NamedTuple):
    level: str
    lang: str
    tweets: bool
    phd: bool
    result: bool = None


def uncertainty(p):
    """
    0 <= p <= 1
    확률 p = 0이면, 항상 사건이 발생하지 않는다(불확실성 0)
    확률 p = 1이면, 항상 사건이 발생한다(불확실성 0)
    확률이 0과 1사이면, 사건이 발생할 수도, 발생하지 않을 수도 있다(불확실성 있음)
    """
    return -p * math.log(p, 2)


def entropy(class_probability):
    """
    주어진 확률(class_probability)의 리스트에 대해서 엔트로피를 계산
    entropy = sum(i) [uncertainty(p_i)] = -p_1 * log(p_1) -p_2 * log(p_2) -...
    """
    ent = 0
    for p in class_probability:
        if p != 0:                           # -> 만약 p=0이면 log(p)를 계산할 때 Error가 발생하기 때문
            ent += uncertainty(p)
    return ent


def binary_entropy(p):
    """
    사건이 일어날 확률 p, 사건이 일어나지 않을 확률(1-p)
    entropy = -p * log(p) -(1-p) * log(1-p)
    """
    return uncertainty(p) + uncertainty(1-p)


def class_probability(labels):
    total_count = len(labels)
    counts = Counter(labels)
    # probability = []
    # for count in counts.values():
    #     p = count / total_count
    #     probability.append(p)
    probability = [count/total_count for count in counts.values()]
    return probability


def partition_by(dataset, attr_name):
    """
    NamedTuple들의 리스트로 이루어진 dataset을
    NamedTuple의 특정 attribute로 partitioning
    """
    partitions = defaultdict(list)      # key값이 없으면 key값을 만들어서 추가해주고, key값이 있으면 바로 추가 -> list를 value로 갖는 dict
    for sample in dataset:
        key = getattr(sample, attr_name)    # 해당 attr_name(ex, level)의 값(ex, senior, mid, junior)을 찾아서
        partitions[key].append(sample)      # 그 값을 dict의 key로 사용해서 sample을 저장
    return partitions


def partition_entropy_by(dataset, attr_name, label_name):
    """
    attr_name(ex, level)으로 분리된 각 파티션에서
    label_name(ex, 'Senior', 'Mid', 'Junior')의 엔트로피를 각각 계산하고
    파티션 내에서의 엔트로피 * 파티션의 비율들의 합을 리턴
    """
    # 1) 파티션 나눔
    partitions = partition_by(dataset, attr_name)

    # 2) 클래스(레이블 - 합격여부, result) 별 확률을 계산하기 위해서 레이블들의 리스트 생성
    labels = []
    for partition in partitions.values():
        values = []
        for sample in partition:
            selection_result = getattr(sample, label_name)
            values.append(selection_result)
        labels.append(values)

    # 3) 각 파티션이 차지하는 비율을 계산하고, 각 파티션에서의 엔트로피에 그 비율을 곱해줌
    total_count = sum(len(label) for label in labels)
    ent = 0
    for label in labels:
        class_prob = class_probability(label)
        part_ent = entropy(class_prob)
        ent += part_ent * (len(label) / total_count)
    return ent


class Leaf(NamedTuple):     # Leaf는 NamedTuple을 상속받는 class
    value: Any     # value는 합격, 불합격, setosa등과 같은 문자가 올 수도 있고, 0, 1과 같은 숫자가 올 수도 있어서 Any


class Split(NamedTuple):
    attribute: str    # 트리에서 가지(branch)가 나눠지는 기준
    subtree: dict


def predict(model, sample):
    """ sample을 model(의사결정나무)에 적용했을 때 예측결과 리턴 """
    if isinstance(model, Leaf):    # isinstance(object, class) : 파라미터로 받은 object가 해당 class의 인스턴스이면 True 리턴
        return model.value       # model이 leaf타입이면, leaf가 가지고 있는 value(값)  리턴
    subtree_key = getattr(sample, model.attribute)     # ex, sample(candidate 한명)에서 'level' 찾아서 값('Senior') 꺼내기
    print('subtree_key:', subtree_key)

    subtree = model.subtree[subtree_key]     # attribute에서 찾은 값(subtree_key)를 가지고 해당 key의 subtree로 내려감
    return predict(subtree, sample)          # predict함수를 다시 반복하면서 Leaf이면 Leaf의 값(합격, 불합격)을 출력하고 - if문의 return
                                             # 만약 subtree가 Leaf가 아니라 Split이면 다시 아래 과정을 반복 - predict함수의 최종 return


def build_tree(dataset, by_splits, target):
    """
    1) target의 개수(True, False)를 셈 -> Counter객체 생성 (ex, {True: __, False: __}이면 len은 2

    2) Counter의 length가 1이거나 by_split이 빈 리스트가 되면 Leaf를 생성하고 종료
       (Counter의 length가 1이면 dataset의 모든 sample들이 하나의 target값을 갖는다는 의미)
       (by_split이 빈 리스트가 되는 것은 트리의 depth가 깊어져서 더 이상 나눌 수 없는 경우)

    3)  Counter의 length가 1이 아니라면 partition을 나눌 수 있음
        by_split의 각 변수별 entropy를 계산해서 root에 사용할 변수 선택
       - entropy 최소값(min)을 갖는 변수를 찾을 때
         min(최소값찾고싶은 변수, key=정렬기준)의 key파라미터에는 정렬기준이 들어가는데,
         이 key값에는 파라미터가 1개만 들어갈 수 있어서
         partition_entropy_by 함수(파라미터 3개)를 바로 쓸 수 없음
         따라서 partition_entropy_by 함수를 대신 할 수 있는
         다른 내부 함수(wrapper 함수, helper 함수)를 만들어서
         파라미터를 1개만 줘도 실행할 수 있게 만들어야 함

    4) entropy 최소값을 주는 변수(3에서 선택된 변수)로 partition 만들기
    5) 4)에서 선택한 변수를 제외한 나머지 변수들로 subtree 만들어서 Split()객체 리턴하기

    :param dataset: 의사결정 트리를 만들고싶은 data set
    :param by_splits: 가지 나눌 기준(변수, attribute)
    :param target: data의 label(class, target)
    :return:
    """
    print('\n>>> Building Tree...')
    print(f'dataset({len(dataset)}) = {dataset}')
    print(f'by_splits = {by_splits}, \ntarget = {target}')

    # 1)
    target_counts = Counter(getattr(sample, target) for sample in dataset)
    print('target_counts : ', target_counts)
    print('================')

    # 2)
    if len(target_counts) == 1:
        # dict의 keys()가 리턴하는 타입은 리스트가 아니어서 인덱스 연산자([])를 사용할 수 없어서 먼저 리스트로 만들어준 것
        keys = list(target_counts.keys())     # [k for k in target_count.keys()]와 동일
        result = keys[0]      # True 또는 False
        leaf = Leaf(result)
        print('leaf:', leaf)
        return leaf

    if not by_splits:    # list가 if문에 사용될때 원소가 있으면 True, 없으면 False
        return Leaf(list(target_counts.keys())[0])

    # 3)
    def splitted_entropy(split_attr):
        result = partition_entropy_by(dataset, split_attr, target)

        print(f'{split_attr}_splitted entropy : {result}')
        return result

    best_splitter = min(by_splits, key=splitted_entropy)
    print('================')
    print('best_splitter:', best_splitter)

    # 4)
    partitions = partition_by(dataset, best_splitter)
    print('partitions:', partitions)       # partition에서의 key(senior, mid, junior)별로 5)에서 subtree생성

    # 5)
    new_split = [x for x in by_splits if x != best_splitter]        # branch 기준 리스트에서 선택된 변수 제외
    print(f'by_splits : {by_splits} / 선택된 변수 제외한 by_splits : {new_split}')

    # partitions.items()하면 key(ex, senior, mid, junior)와 value(ex, [Candidate(level= , lang= , ...), Candidate[], ..], ...)
    subtree = {k: build_tree(subset, new_split, target) for k, subset in partitions.items()}
    return Split(best_splitter, subtree)





if __name__ == '__main__':
    candidates = [Candidate('Senior', 'Java', False, False, False),
                  Candidate('Senior', 'Java', False, False, False),
                  Candidate('Mid', 'Python', False, False, True),
                  Candidate('Junior', 'Python', False, False, True),
                  Candidate('Junior', 'R', True, False, True),
                  Candidate('Junior', 'R', True, True, False),
                  Candidate('Mid', 'R', True, True, True),
                  Candidate('Senior', 'Python', False, False, False),
                  Candidate('Senior', 'R', True, False, True),
                  Candidate('Junior', 'Python', True, False, True),
                  Candidate('Senior', 'Python', True, True, True),
                  Candidate('Mid', 'Python', False, True, True),
                  Candidate('Mid', 'Java', True, False, True),
                  Candidate('Junior', 'Python', False, True, False)]

    # uncertainty 함수의 그래프 그리기
    x_points = np.linspace(0.0001, 1, 100)
    y_points = [uncertainty(p) for p in x_points]
    plt.plot(x_points, y_points)
    plt.title('y = -p * log(p)')
    plt.xlim(0.0)
    plt.ylim(0.0)
    plt.show()

    # binary entropy 함수 그래프
    x_points = np.linspace(0.0001, 0.9999, 100)
    y_points = [binary_entropy(p) for p in x_points]
    plt.plot(x_points, y_points)
    plt.title('binary entropy')
    plt.axvline(x=0.5, color='0.5')
    plt.xlim(0.0)
    plt.ylim(0.0)
    plt.show()

    # entropy 함수 테스트
    rain_prob = [1, 0]
    ent = entropy(rain_prob)
    print('entropy = ', ent)

    rain_prob = [0.5, 0.5]
    ent = entropy(rain_prob)
    print('entropy = ', ent)

    rain_prob = [0.9, 0.1]
    ent = entropy(rain_prob)
    print('entropy = ', ent)

    # class_probability 함수 테스트
    level = ['Junior', 'Mid', 'Senior', 'Junior']
    cls_prob = class_probability(level)
    print(cls_prob)

    # partition_by 테스트
    partition_by_level = partition_by(candidates, 'level')
    print(f'partition_by_level : {partition_by_level}')

    partition_by_tweets = partition_by(candidates, 'tweets')
    print(f'partition_by_tweets : {partition_by_tweets}')

    # partition_entropy_by 함수를 이용해서 각 attribute별 entropy계산
    ent_level = partition_entropy_by(candidates, 'level', 'result')
    print(f'entropy partitioned by level : {ent_level}')

    ent_lang = partition_entropy_by(candidates, 'lang', 'result')
    print(f'entropy partitioned by lang : {ent_lang}')

    ent_tweets = partition_entropy_by(candidates, 'tweets', 'result')
    print(f'entropy partitioned by tweets : {ent_tweets}')

    ent_phd = partition_entropy_by(candidates, 'phd', 'result')
    print(f'entropy partitioned by phd : {ent_phd}')

    # Leaf와 Split calss를 이용한 의사결정트리
    # 1)
    hire_tree = Split(
        'level',                                                              # branch나누는 기준
        {'Senior': Split('tweets', {True: Leaf(True), False: Leaf(False)}),   # sub-tree
         'Mid': Leaf(True),                                                   # leaf(합격)
         'Junior': Split('phd', {True: Leaf(False), False: Leaf(True)})       # sub-tree
         }
    )

    # 2)
    # hire_tree2 = Split(
    #     'lang',
    #     {'Java': Split('level', {'Senior': Leaf(False), 'Mid': Leaf(True)}),
    #      'Python': Split('level', {'Senior': Split(), 'Mid': Leaf(True), 'Junior': Split()}),
    #      'R': Split('level',{'Senior': Leaf(True), 'Mid': Leaf(True), 'Junior': Split()})}
    # )

    candidate1 = Candidate('Senior', 'Java', False, False, False)
    result = predict(hire_tree, candidate1)
    print('result :', result)

    candidate2 = Candidate('Mid', 'Python', False, False, True)
    result = predict(hire_tree, candidate2)
    print('result :', result)
    print()

    build_tree = build_tree(candidates, ['level', 'lang', 'tweets', 'phd'], 'result')
    print()
    print(build_tree)

