# Flyweight Pattern

https://refactoring.guru/design-patterns/flyweight

> ### 여러 객체 간의 공유 메모리 적용

- 여러 객체들 간의 공유 정보들을 캐싱하여 메모리 절약함
- 게임처럼 사양이 중요한 곳에서 많이 사용됨
- 객체의 고유 특성(intrinsic state)은 객체에 저장하고 외부 환경에 따라 변하는 특성(extrinsic state)은 따로 저장함
- Context(모든 상태 포함)클래스에서 객체의 고유 특성(공유 가능한 부분)들만 Flyweight클래스로 저장함.
- Flyweight 객체는 Flyweight Factory에서 캐싱됨. 기존에 있으면 찾아주고 없으면 추가.

### 적용 상황

- 정해진 RAM을 훨씬 넘는 객체를 지원해야 하는 경우에 사용
- Flyweight 객체의 intrinsic state는 변경되어서는 안됨

### 장점

- RAM 절약

### 단점

- RAM 을 절약하는 대신 CPU가 많이 사용됨

### 타 패턴과의 관계

- Composite 패턴에서 메모리 절약하기 위해 Flyweight 사용함
- Flyweight는 엄청나게 많은 작은 객체를 표현한다면, Facade는 엄청나게 큰 서브시스템을 단 하나의 객체로 표현함
- Flyweight는 Singleton과 유사함.
  - 첫번째 차이점. 싱글톤은 하나의 객체만을 Flyweight는 여러 intrinsic state 가질 수 있음
  - 두번째 차이점. 싱글톤은 수정가능. Flyweight은 수정불가능.
