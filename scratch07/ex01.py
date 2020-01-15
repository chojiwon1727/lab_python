from math import sqrt

from scratch06.ex06 import normal_cdf, inverse_normal_cdf


def normal_approximation_to_binomial(n,p):
    mu = n*p
    sigma = sqrt(n*p*(1-p))
    return mu, sigma

# 확률 변수가 어떤 구간 안(밖)에 존재할 확률
# P(X <= b), P(X >= a), P(a <= X <=b)  --> 누적확률분포함수를 이용하면 됨!!


# 1)
normal_probability_below = normal_cdf


# 2)
def normal_probability_above(low, mu=0.0, sigma=1.0):
    return 1-normal_cdf(low, mu, sigma)


# 3)
def normal_probability_between(low, high, mu=0.0, sigma=1.0):
    return normal_cdf(high, mu, sigma) - normal_cdf(low, mu, sigma)


# 4) P(X < Low or X > High) : 확률 변수가 특정 범위 밖에 있을 확률(Low < High)
def normal_probability_outside(low, high, mu=0.0, sigma=1.0):
    return 1 - normal_probability_between(low, high, mu, sigma)


# 확률이 주어졌을 때 누적확률이 95%인 x값 찾기(p < 0.05)
# 1)
def normal_upper_bound(prob, mu=0.0, sigma=1.0):
    return inverse_normal_cdf(prob, mu, sigma)


# 2)
def normal_lower_bound(prob, mu=0.0, sigma=1.0):
    return inverse_normal_cdf(1-prob, mu, sigma)


# 3)
def normal_two_sided_bound(prob, mu=0.0, sigma=1.0):
    tail_prob = (1-prob) / 2
    upper_bound = normal_lower_bound(tail_prob, mu, sigma)
    lower_bound = normal_upper_bound(tail_prob, mu, sigma)
    return lower_bound, upper_bound


def two_side_p_value(x, mu=0, sigma=1):
    """양측검정에서 사용하는 p-value"""
    if x >= mu:
        return normal_probability_above(x, mu, sigma) * 2
    else:
        return normal_probability_below(x, mu, sigma) * 2


def estimate_parameters(N, n):
    """
    표본의 평균으로 모집단의 평균과 표준편차 추정해주는 함수
    N: 실험횟수, n: 발견된 횟수
    """
    p = n / N
    sigma = sqrt(p*(1-p)/N)
    return p, sigma


def a_b_test_statistics(N_a, n_a, N_b, n_b):
    p_a, sigma_a = estimate_parameters(N_a, n_a)
    p_b, sigma_b = estimate_parameters(N_b, n_b)
    return (p_b - p_a) / sqrt(sigma_a**2 + sigma_b**2)


if __name__ == '__main__':
    mu, sigma = normal_approximation_to_binomial(1000, 0.5)
    print(f'p=0.5일 때 mu = {mu}, sigma = {sigma}')

    low, high = normal_two_sided_bound(0.95, mu, sigma)
    print(f'low={low}, high={high}')


    beta1 = normal_probability_between(low, high, mu, sigma)
    print('p=0.5인 경우 beta = ', beta1)
    power1 = 1 - beta1
    print('p=0.5인 경우 power = ', power1)
    print()

    mu_1, sigma_1 = normal_approximation_to_binomial(1000, 0.55)
    print(f'p=0.55일 때 mu = {mu_1}, sigma = {sigma_1}')
    beta = normal_probability_between(low, high, mu_1, sigma_1)
    print('p=0.55인 경우 beta = ', beta)
    power = 1 - beta
    print('p=0.55인 경우 power = ', power)
    print()

    mu_2, sigma_2 = normal_approximation_to_binomial(1000, 0.45)
    print(f'p=0.45일 때 mu = {mu_2}, sigma = {sigma_2}')
    beta2 = normal_probability_between(low, high, mu_2, sigma_2)
    print('p=0.45인 경우 beta = ', beta2)
    power2 = 1 - beta2
    print('p=0.45인 경우 power = ', power2)
    print()

    # H0 : p<=1/2,  H1 : p>1/2
    high = normal_upper_bound(0.95, mu, sigma)
    print('유의 수준 5%의 upper bound : ', high)
    beta = normal_probability_below(high, mu_1, sigma_1)
    print('단측검정 beta : ', beta)
    power = 1 - beta
    print('단측검정 power : ', power)
    print()

    # H0 : p>=1/2,  H1 : p<1/2
    low = normal_lower_bound(0.95, mu, sigma)
    print('유의수준 5%의 lower bound : ', low)
    beta = normal_probability_above(low, mu_2, sigma_2)
    print('단측검정 beta : ', beta)
    power = 1 - beta
    print('단측검정 power : ', power)
    print('==============================================')

    # 동전을 1000번 던지는 실험에서 동전의 앞면이 530번 나왔다!
    # H0: p=0.5
    p_value = normal_probability_above(530, mu, sigma) # 단측검정
    print(p_value)

    p_value = two_side_p_value(465, mu, sigma)
    print(p_value)
    print()

    # 동전을 1000번 던져서 525번이 나온 경우 앞면의 확률 p=525/1000=0.525
    p_bar = 525/1000
    mu = p_bar    # 실제 모집단의 평균을 모르기 때문에 모집단의 평균을 표본의 평균으로 대체
    sigma = sqrt(p_bar*(1-p_bar)/1000)     # 표본의 표편으로 모집단의 표편을 추정하므로 n으로 나눠줌
    bounds = normal_two_sided_bound(0.95, mu, sigma)
    print(bounds)

    # 동전을 1000번 던져서 540번 앞면이 나왔을 경우
    p_bar = 540/1000
    mu = p_bar
    sigma = sqrt(p_bar*(1-p_bar)/1000)
    bounds = normal_two_sided_bound(0.95, mu, sigma)
    print(bounds)
    print()

    # A/B Test
    z1 = a_b_test_statistics(1000,200,1000,180)
    print('z1 = ', z1)
    p_value_1 = two_side_p_value(z1)
    print('p_value_1 = ', p_value_1)

    z2 = a_b_test_statistics(1000, 200, 1000, 150)
    print('z2 = ', z2)
    p_value_2 = two_side_p_value(z2)
    print('p_value_2 = ', p_value_2)






