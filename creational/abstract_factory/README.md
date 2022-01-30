# Abstract Factory Pattern

https://refactoring.guru/design-patterns/abstract-factory

> ### 관련된 objects의 집단 생성을 위한 inteface 제공

- 객체의 스타일이 명시적으로 존재하며 스타일이 다른 객체를 동시에 생성하지 않아야 할 때 사용
- 총 4가지의 파트로 구성됨.

  1. Abstract Products
     - product 의 추상화 클래스
  2. Concrete Products
     - abstract product class를 상속받는 클래스
  3. Abstract Factory
     - abstract product 객체를 생성하는 추상 팩토리 클래스
  4. Concrete Factories
     - abstract factory class를 상속받아 concrete product 객체를 생성하는 팩토리 클래스

- Client 는 abstract factory class를 사용하며 내부 구현 방식과는 무관하게 동작가능하도록 함
- 객체간의 호환성이 항상 보장됨. (mac button 과 window checkbox가 동시에 생성되지 않음)
- builder 패턴은 복잡한 객체들을 생성하는데 집중하나 abstract factory 패턴은 관련된 객체간의 생성에 특화

### 장점

- 생성되는 여러 객체 간의 호환성이 보장됨
- concrete product class와 client 코드의 decoupling
- product creation code를 한 곳에서만 사용 (SRP)
- new type product 쉽게 추가 가능 (OCP)

### 단점

- 새로운 인터페이스와 클래스가 많이 생성되어 코드 구조가 복잡해질 수 있음
