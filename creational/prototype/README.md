# Prototype Pattern

https://refactoring.guru/design-patterns/prototype

> ### 코드에 대한 의존성 없이 존재하는 객체를 그대로 복사

- 모든 클래스에 대해 clone 메소드를 전부 구현
- 어떤 클래스로 생성된 객체여도 clone 메소드를 통해 복사할 수 있도록 함.

### 적용 상황

- concrete 클래스의 구현 방식과 의존성 없이 복사하고 싶을 때
- configuration 을 토대로 복잡하게 생성하지 않고 기존에 있던 객체를 복사하여 편하게 사용하고 싶을 때

### 장점

- concrete 클래스와 상관없이 복사 가능
- 반복적인 객체 초기화 대신 pre-built 된 프로로타입 복사를 이용하여 편하게 객체 생성 가능
- 복잡한 객체를 편하게 생성

### 단점

- 순환 참조가 있는 복잡한 객체 복사는 어려움
