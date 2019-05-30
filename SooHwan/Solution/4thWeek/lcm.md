* 주차 : 4주차
* 문제명 : N개의 최소공배수
* 링크 :  https://programmers.co.kr/learn/courses/30/lessons/12953
* 사용언어 : C++,python3
* 자체평점(5점 만점) : 1.5/5
  
  ---

* 풀이

N개의 수의 최소 공배수는 다음과 같이 재귀적으로 정의된다.

    > lcm(a[1]..a[n]) = lcm(lcm(a[1]..a[n-1]),a[n])

lcm과 gcd는 유클리드 호제법으로 쉽게 구현이 가능하므로, 이를 이용해 구현하면 된다.

  