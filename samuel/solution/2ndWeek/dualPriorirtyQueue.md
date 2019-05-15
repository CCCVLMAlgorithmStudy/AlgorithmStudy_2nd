# dualPriorityQueue
* 주차 : 2주차
* 문제명 : 이중우선순위 큐
* 링크 : https://programmers.co.kr/learn/courses/30/lessons/42628
* 사용언어 : Python
* 자체평점(5점 만점) : 2/5
 
  —

* 풀이

For 문에서 매개변수 리스트의 요소에 “I”혹은 “D” 포함되었는지 검색한 뒤, I가 포함되었으면 arr 리스트에 추가.
추가할 때, i[2:] 로 문자열의 3번째(0, 1, 2의 3번째) 위치부터 끝자리까지 정수형으로 변환하여 추가한다.
“D”의 경우 arr 리스트가 비었는지 확인하고 비어있으면 continue 로 for문의 다음 요소를 검색한다. 
이후 2가지 방법으로 풀었다.

- [ ] List Sort 방법 - dualPriority_listSort
arr 리스트가 비어있지 않으면 리스트를 정렬한 후 리스트 요소가 “D 1”인지 검색하고 맞으면 리스트의 끝요소인 최대값을 제거(pop()) 아니면(“D -1”)  리스트를 reverse() 하고 pop()하여 최소값을 제거하고 다음 요소로 넘어간다.

- [ ] Max 값, Min 비교하는 방법 - dualPriority_MaxMin
arr 리스트가 비어있지 않으면 arr 리스트의 Max 값과 Min 값을 각 변수 Max와 Min에 저장하고 리스트 요소가 “D 1” 이면 Max 값 제거 “D -1”이면 Min 값 제거하고 다음 요소로 넘어간다.