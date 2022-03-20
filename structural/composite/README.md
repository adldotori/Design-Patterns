# Composite Pattern

https://refactoring.guru/design-patterns/composite

> ### 리눅스폴더구조처럼 객체 간의 트리구조 표현 시 사용

- 리눅스 폴더 구조, 디자인 툴의 컴포넌트들, 회사 계급 체계과 같은 tree structure 를 표현할 때 사용함
- 각 class들이 모두가 똑같은 인터페이스를 구현하고 instance는 재귀적으로 그 안에 포함된 instance의 메소드들을 콜하고 통합함
- component라는 interface가 존재하고 리프 노드가 실제로 이를 실행하는 역할을 함. 그 사이의 모든 노드들은 composite라는 노드로 이뤄지며 component라는 타입의 원소들을 포함함. 리프일 수도 있고 같은 composite일 수도 있음.
- leaf와 composite이 거의 유사한 역할을 할 때 사용하는 것을 추천.

### 적용 상황

- 트리 같은 객체 구조 표현
- 클라이언트가 단순한 원소와 복잡한 원소를 똑같이 처리하게 하고 싶을 때

### 장점

- 복잡한 트리구조를 사용하기 쉽게 할 수 있다. 다형성과 재귀를 사용함.
- OCP: 기존의 코드를 깨지 않고 새로운 타입을 추가할 수 있음.

### 단점

- composite와 leaf의 기능이 너무 다를 때 같은 인터페이스로 구현하는 것이 어려움
