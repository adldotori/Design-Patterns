# Bridge Pattern

https://refactoring.guru/design-patterns/bridge

> ### 2가지 클래스들의 집합을 연결

- 독립적인 차원의 집합들이 존재할 때 n x m 클래스를 모두 구현할 수 없음
- 한 클래스를 구현할 때 여러 dim이 필요한 경우 차원 하나를 별도의 클래스 계층으로 추출
- implementation 은 interface + concrete implementation, abstraction 은 부모 클래스, 자식 클래스로 구성
- implementation, abstraction 은 항상 호환 가능하며 이를 통해 상속받는 클래스들 또한 호환 보장
- abstraction 에서 implementation local variable로 갖고 있음

### 적용 상황

- 여러 기능이 있는 모놀리틱 클래스를 나누고 싶을 때
- 독립적인 차원의 클래스로 확장이 필요할 때
- 런타임에서 implementation을 변경해야 할 때

### 장점

- platform-independent한 클래스와 앱을 생성할 수 있음
- 클라이언트 코드는 하이레벨 abstraction 코드와 동작함. 디테일을 몰라도 됨.
- OCP: abstraction, implementation 서로 독립적으로 개발 가능
- SRP: high-level logic은 abstraction에서, 디테일은 implementation에서

### 단점

- 복잡성 증가
