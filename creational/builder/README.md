# Builder Pattern

https://refactoring.guru/design-patterns/builder

> ### 복잡한 객체를 스텝별로 구성

- 총 4가지의 파트로 구성됨.

  1. Products
     - 실제 생성하고 싶은 객체 클래스
  2. Builder
     - Abstract Builder 클래스로 product 생성하기 위한 추상 빌드 메소드 제공
  3. Concrete Builder
     - Builder 클래스를 상속받음
     - Product 를 생성하기 위한 빌더 클래스
     - 스텝별로 product 생성하기 위한 conrete 메소드 구현
  4. Director
     - Builder 의 메소드들을 이용하여 실제로 클래스를 생성함
     - 메소드 호출 순서가 정의됨

- object 의 구성방식이 다양할 때 사용
- object construction code 를 own class 안이 아닌 분리된 빌더 객체로 추출
- 모든 스텝을 호출하지 않고 필요한 부분만 스텝만 호출함
- 객체 생성 방식이 변경되면 Builder, Concrete Builder, Product 클래스와 무관하게 Director 클래스의 수정만으로 가능
- 클라이언트는 생성하고 싶은 객체의 concrete builder 와 director 의 호출만으로 객체 생성 가능

### 적용 상황

- 객체 생성 시 10개 이상의 파라미터가 필요할 때
- 돌집과 나무집처럼 생성하고 싶은 객체의 스타일에 따라 구성 방식이 달라질 때
  - base builder 가 모든 construction step 을 정의하고 concrete builder 에서 스타일에 따른 construction 방식 구현
- 매우 복잡한 객체를 생성할 때

### 장점

- 객체를 단계별로 구성 가능
- 객체의 다양한 스타일을 만들 때 동일한 construction code 재사용 가능
- 제품의 비즈니스 로직과 객체 생성 코드를 분리 가능 (SRP)

### 단점

- 여러 개의 새로운 클래스를 생성해야 하므로 코드의 복잡성 증가
