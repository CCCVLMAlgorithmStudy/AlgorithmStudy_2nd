* 주차 : 4주차
* 문제명 : 구명보트
* 링크 :  https://programmers.co.kr/learn/courses/30/lessons/42885
* 사용언어 : C++,python3
* 자체평점(5점 만점) : 2/5
  
  ---

* 풀이

보트 인원이 2명으로만 제한되어 있기 때문에 보트 수를 줄이려면 최대한 보트의 한계에 가깝께 사람을 태워야 한다.

1. 몸무게가 담긴 배열을 오름차순으로 정렬한다.
2. 커서를 두개 만들어 각각 맨 앞과 맨 뒤로 초기화한다. 앞을 가리키는 커서를 minC,뒤를 가리키는 커서를 maxC라 하자
3. 매 반복마다 두개의 커서가 가리키는 값을 더해 한계보다 큰 지 검사한다.
4. 한계보다 작을 경우, minC를 한 칸 전진시키고 maxC를 한 칸 후퇴시킨다. 이후 답을 하나 증가 시킨다.
5. 한계보다 클 경우는 maxC만 한 칸 후퇴시킨다. 이후 답을 하나 증가 시킨다.
6. maxC와 minC가 같을 경우, minC를 하나 증가 시키고 답을 하나 증가 시킨다.
7. 3.~6.의 과정을 minC \< maxC 일 때 까지 반복한다. 

시간 복잡도는 배열 전체를 한번만 순회하므로 O(n)
