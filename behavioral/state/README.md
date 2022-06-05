# Pattern

https://refactoring.guru/design-patterns/

> ### 객체의 내부 상태 변경에 따라 행동(알고리즘) 변경

- strategy의 확장판
- stateful한 객체에 대해서 사용가능하며 객체의 state에 따라 객체의 행동 방식을 변경함
- strategy 패턴에서 concrete class에서 context로의 의존성이 하나 추가되는데 strategy interface로 인해 순환의존성 문제를 가지지 않음
- 객체의 메소드 하나만을 주입하는 것이 아니라 객체에서 stateful한 모든 메소드에 대해서 concrete state class로 의존성 주입함

### 적용 상황

- stateful한 객체(stateful한 메소드가 존재하는 객체)일 때
- state의 개수가 많을 때
- 클래스 변수의 값에 따른 condition으로 클래스가 오염되었을 때
- 유사한 state 간에 중복 코드가 많을 때 state interface와 concrete state class 사이의 abstract base class를 구현하여 state패턴 적극 사용 가능

### 장점

- SRP: 각 state클래스가 하나의 역할만을 맡음
- OCP: 새로운 state 확장에 열려있음
- 복잡한 state machine을 간단하게 만들 수 있음

### 단점

- state가 몇 개 없거나 변경이 적을 땐 오버엔지니어링일 수 있음

### 타 패턴과의 관계

- Bridge, Strategy, State는 모두 association을 기반으로 한 구조를 가지고 있다.
  - 구조적인 관점: bridge가 기본이며 strategy는 거기서 client가 concrete implementation을 의존하며, state는 하나 더 나아가 concrete implementation이 abstraction까지 의존한다.
  - 역할의 관점: bridge는 2개의 인터페이스 연결, strategy는 객체의 행동 변경, state는 객체의 state에 따른 행동 변경이다.
- state는 strategy의 확장판이다. 2개 다 context가 직접 행동하지 않으며 concrete class에게 delegate한다. 그러나 strategy는 concrete class 간의 의존성이 전혀 없으나 state는 자유롭게 서로 변경 가능하도록 한다.
