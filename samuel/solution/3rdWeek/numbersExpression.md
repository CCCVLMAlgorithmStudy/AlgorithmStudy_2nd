# numbersExpression
* 주차 : 3주차
* 문제명 : 숫자의 표현
* 링크 : https://programmers.co.kr/learn/courses/30/lessons/12924
* 사용언어 : Python
* 자체평점(5점 만점) : 1/5
 
  —

* 풀이
1부터 n까지  자연수부터. n까지의 합중 n과 같은 값이 몇가지나 있는지 세는 문제.
2중 for문으로 첫번째 for문은 1부터 n까지 두번째 for문은 i부터 n까지 하나씩 sum 변수에 더해서 n과 비교하여 같은 값이면 횟수(answer)에서 1을 더하고 첫번째 for문으로, n을 넘어가면 바로 첫번째 for문으로 돌아가서 sum 값을 초기화한 후 반복 작업한다.