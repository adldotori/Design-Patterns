# Factory Method Pattern

https://refactoring.guru/design-patterns/factory-method

> ### object 생성을 위한 interface 제공

- 모든 생성 디자인 패턴의 시작.
- OOP의 기본이자 코어인 상속에 대한 핵심 디자인 패턴.
- SRP를 위해 object 생성과 object 사용 부분을 분리.
- Product Interface 는 필수이나 Creator Interface 는 때에 따라 다르다.
  1. Product 외부에서 사용해야 하는 메서드가 전부 같은 경우 Creator Interface 필요 X.
  2. Product 외부에서 사용해야 하는 메서드가 다른 경우 Creator Interface 정의 후 Product에 dependent한 Concrete Creator class 구현 필요.
- Creator Interface 가 반드시 abstract class 일 필요는 없다. 모든 Concrete Creator Class 에서 공통적으로 필요한 메서드는 Interface 에서 구현한다.

### 장점

- creator 와 concrete product class 의 decoupling
- product creation responsibilty 와 product using responsibility 분리 (SRP)
- new type product 쉽게 추가 가능 (OCP)

### 단점

- 새로운 하위 클래스가 추가될 경우 클래스가 엄청 많아질 수 있음
