# Adapter Pattern

https://refactoring.guru/design-patterns/adapter

> ### 호환되지 않는 인터페이스와 호환되도록

- adapter로 객체를 감싸고 외부에서는 wrapping 여부를 모르게
- adapter를 이용해 서비스의 specific한 메소드를 자유롭게 클라이언트가 호출할 수 있게 함

### 적용 상황

- 이미 존재하는 클래스가 인터페이스와 호환이 되지 않을 때
- 부모클래스에 추가할 수 없는 자식클래스의 메소드를 재사용하고 싶을 때

### 장점

- SRP: 프로그램의 기본 비즈니스 로직과 인터페이스 분리
- OCP: 기존 클라이언트 코드를 수정하지 않고 어댑터만 수정하여 적용 가능

### 단점

- 복잡성 증가
