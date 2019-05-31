# lifeboat
* 주차 : 4주차
* 문제명 : 구명보트
* 링크 : https://programmers.co.kr/learn/courses/30/lessons/42885
* 사용언어 : Python
* 자체평점(5점 만점) : 3/5
 
  —

* 풀이
구명보트를 최대 2명씩 탈 수 있으므로, 가장 가벼운 사람과 가장 무거운 사람을 비교하여 무게 제한보다 작으면 같이 타고 가고 아니면 혼자 타고 갈 수 있다. People 을 sort 하여 가장 작은 값(맨 앞_0부터)과 가장 큰 값(맨 뒤_people의 길이)을 비교하여 무게보다 작으면 비교 값을 서로 이동하고 아니면 맨 뒤 값만 이동하며(값을 바꾸며) answer(보트의 수)를 증가시킨다.
뒤의 기준값(j)이 앞의 기준값(i)보다 같거나 커지면 반복문을 종료한다.