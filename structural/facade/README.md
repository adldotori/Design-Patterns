# Facade Pattern

https://refactoring.guru/design-patterns/facade

> ### 복잡한 클래스의 단순화된 인터페이스 제공

- 복잡한 서브시스템을 몰라도 클라이언트가 사용하기 쉽게 함
- 자유도를 낮춤으로써 사용성을 높임

### 적용 상황

- 복잡한 서브시스템에서 제한적이나 사용하기 쉬운 인터페이스를 제공하고 싶을 때
- 서브시스템을 레이어로 구조화하고 싶을 때 (여러 서브시스템간의 결합도를 낮출 수 있음)

### 장점

- 서브시스템의 복잡도와 사용 난이도를 분리할 수 있음

### 단점

- facade는 God Object(모든 것을 알고 있는 객체로 SRP를 위반함)가 될 수 있음

### 타 패턴과의 관계

- Facade는 존재하는 객체를 위해 새로운 인터페이스 생성을 하나 Adapter는 기존의 인터페이스를 사용가능하게 변경
- Adapter는 한 객체만 wrapping, Facade는 모든 서브시스템을 wrapping함
- Facade에서 서브시스템 객체 생성 방법만 가리고 싶을 경우 Abstract Factory 사용하면 됨
- Flyweight는 엄청나게 많은 작은 객체를 표현한다면, Facade는 엄청나게 큰 서브시스템을 단 하나의 객체로 표현함
- TODO: Mediator
- Facade 객체는 보통 하나로 충분하므로 싱글톤으로도 많이 사용함
- TODO: Proxy
