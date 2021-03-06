# Singleton Pattern

https://refactoring.guru/design-patterns/singleton

> ### 어떤 클래스에 대해 단 하나의 객체만 생성되는 것을 보장

- 데이터베이스나 파일처럼 공유된 자원에 대한 접근을 컨트롤하기 위해 사용
- 새로운 객체 생성 시도 시 기존 생성된 객체를 반환함
- 클라이언트는 요청한 객체가 전부 같은 객체임을 모를 수도 있음

### 적용 상황

- 모든 클라이언트에 대해 단 하나의 인스턴스만 존재해야 할 때
- 전역 변수 컨트롤을 위해 한 인스턴스만 필요할 때

### 장점

- 단일 인스턴스 생성 보장

### 단점

- 싱글톤 패턴 테스트하기 어려움
- 의존성 문제가 가려지기 쉬움
