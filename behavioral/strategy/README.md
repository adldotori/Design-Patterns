# Strategy Pattern

https://refactoring.guru/design-patterns/strategy

> ### 객체의 행동(알고리즘)을 컴포넌트화

### 적용 상황

- 런타임에서 객체 안의 알고리즘을 변경하고 싶을 때
- 여러 객체들끼리 행동 방식만 다를 때
- 클래스 안에 있는 데이터와 알고리즘의 분리(isolation)

### 장점

- 런타임에서 행동 변경 가능
- 알고리즘의 디테일 분리
- OCP: 새로운 알고리즘 추가 시 OCP 만족

### 단점

- 알고리즘 개수가 적거나 변경할 일이 적을 때 무의미함
- 클라이언트가 strategy 간의 차이를 알아야 함

### 타 패턴과의 관계

- Bridge, State, Strategy는 모두 association을 기반으로 한 구조를 가지고 있다. 그러나 이 3개는 전부 다른 문제를 푼다.
- TODO: Command
- TODO: Decorator
- TODO: Template Method
- TODO: State
