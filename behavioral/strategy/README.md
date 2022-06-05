# Strategy Pattern

https://refactoring.guru/design-patterns/strategy

> ### 객체의 행동(알고리즘)을 컴포넌트화

- 객체의 행동(알고리즘)을 strategy라는 클래스로 분리하여 객체에 행동을 주입시키는 구조
- 객체의 행동 방식이 다양할 때 이를 컴포넌트화하여 쉽게 변경가능함
- 클라이언트는 Dependency Injection을 통해 context가 concrete strategy에 의존하지 않도록 함
- 일반적으로 client가 concrete를 몰라도 되나 strategy에서는 concrete class를 정확히 알고 있어야 함

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

- Bridge, Strategy, State는 모두 association을 기반으로 한 구조를 가지고 있다.
  - 구조적인 관점: bridge가 기본이며 strategy는 거기서 client가 concrete implementation을 의존하며, state는 하나 더 나아가 concrete implementation이 abstraction까지 의존한다.
  - 역할의 관점: bridge는 2개의 인터페이스 연결, strategy는 객체의 행동 변경, state는 객체의 state에 따른 행동 변경이다.
- TODO: Command
- TODO: Decorator
- TODO: Template Method
- state는 strategy의 확장판이다. 2개 다 context가 직접 행동하지 않으며 concrete class에게 delegate한다. 그러나 strategy는 concrete class 간의 의존성이 전혀 없으나 state는 자유롭게 서로 변경 가능하도록 한다.
