import numpy as np
a1=([1,2,3,4,5])
a2=([[1,2,3],
     [4,5,6],
     [7,8,9]])
a3 = ([[[1,2,3],[4,5,6],[7,8,9]],
       [[1,2,3],[4,5,6],[7,8,9]],
       [[1,2,3],[4,5,6],[7,8,9]]])
print(np.zeros(10)) # 모든 요소를 0으로 초기화
print(np.ones(10)) # 모든 요소를 1로 초기화
print(np.ones((3,3)))
print(np.full((3,3),1.25)) # 모든 요소를 지정한 값으로 초기화
print(np.eye(3)) # 주대각선의 원소가 모두 1이고 나머지 원소는 모두 0인 정사각 행렬
print(np.tri(3)) # 삼각행렬 형성
print(np.empty(10)) # 초기화되지 않은 배열 생성
print(np.zeros_like(a1)) # 지정된 배열과 shape가 같은 행렬 생성
print(np.ones_like(a2))
print(np.full_like(a3,10))
print(np.arange(0,30,2)) # 정수 범위로 배열 생성 (몇부터(범위), 몇까지, 특정간격으로)
print(np.linspace(0,1,5)) # 범위 내에서 균등간격의 배열 생성 (몇부터(범위), 몇까지, 특정개수로 균등 분할)
print(np.logspace(0.1,1,10)) # 범위 내에서 균등간격으로 로그 스케일로 배열 생성
# 랜덤값으로 배열 형성
# seed : 난수발생을 위한 시드(seed)지정
# permutation : 순서를 임의로 바꾸거나 임의의 순열 반환
# shuffle : 리스트나 배열의 순서를 뒤섞음
# random : 랜덤한 수의 배열 생성
# rand : 균등분포에서 표본 추출
# randint : 주어진 최소/최대 범위의 난수 추출
# randn : 표준편차가 1, 평균값 0인 정규분표의 표본 추출
# binomial : 이항분포에서 표본 추출
# normal : 정규분포 (가우시안)에서 표본 추출
# beta : 베타분포에서 표본 추출
# chisquare : 카이제곱분포에서 표본 추출
# gamma : 감파분포에서 표본 추출
# uniform : 균등 (0,1) 분포에서 표본 추출
print(np.random.random((3,3)))
print(np.random.randint(0,10,(3,3)))