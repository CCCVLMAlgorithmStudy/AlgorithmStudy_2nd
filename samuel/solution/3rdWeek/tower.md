# tower
* 주차 : 3주차
* 문제명 : 탑
* 링크 : https://programmers.co.kr/learn/courses/30/lessons/42588
* 사용언어 : Python
* 자체평점(5점 만점) : 2/5
 
  —

* 풀이
주어진 리스트의 오른쪽에서 왼쪽으로 전파를 송신하므로 리스트를 reverse하여 풀거나 for문을 역으로 감소시키는 것으로 문제 해결할 수 있다.
heights의 길이만큼 answer 리스트를 0으로 초기화한다.
for문을 전체길이에서 -1로 감소시키며 0까지 비교하기 위해 range함수에서 전체길이 len(heights)-1 에서 -1까지 반복한다.기준이 되는 탑[i]과 비교하는 탑[j]을 비교하여 비교하는 탑이 크면 answer[i]에 j+1 (리스트가 0부터 시작하므로) 입력하고 for문을 빠져나감(break)
반복하여 입력하고 answer 리스트 반환