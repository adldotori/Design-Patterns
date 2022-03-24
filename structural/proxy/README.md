# Proxy Pattern

https://refactoring.guru/design-patterns/proxy

> ### 객체의 접근 권한을 설정, 캐싱

- 모든 접근이 전부 허용되지 않도록 프록시 클래스가 막아줌
- 기존에 했었던 접근이라면 캐싱된 데이터를 전달하여 객체의 부하를 막음
- 서비스 객체 앞에서 필요한 여러 기능들을 해줄 수 있음

### 적용 상황

- Virtual Proxy: Lazy Initialization 가능
  - 시스템 리소스를 낭비하는 무거운 객체가 있을 때 객체 초기화를 정말 필요할 때까지 연기함
- Protection Proxy: 액세스 제어
  - 클라이언트의 credential이 일치하는 경우에만 서비스 객체에 요청 전달
- Remote Proxy: 원격 서비스의 로컬 실행
  - 서비스 객체가 원격 서버에 있을 때 네트워크를 통해 클라이언트 요청 전달
  - 모든 사이 귀찮은 것들을 핸들링함
  - 일반적으로 네트워크에서 알고 있는 프록시와 유사
- Logging Proxy: 서비스 객체에 대한 기록 유지
- Caching Proxy: 클라이언트 요청의 결과를 캐싱
- Smart Refrence: 서비스를 아무도 사용하지 않고 있을 때 시스템 리소스 해제

### 장점

- 캡슐화 가능
- 서비스 객체의 라이프사이클 조절 가능
- 서비스 객체를 사용 불가능할 때도 프록시는 사용 가능
- OCP: 서비스나 클라이언트를 변경하지 않고 새 프록시 도입 가능

### 단점

- 코드 복잡성 증가
- 서비스 응답속도 증가

### 타 패턴과의 관계

- Adapter는 다른 interface를, Proxy는 동일한 interface를 Decorator는 향상된 interface를 제공함
  - Decorator는 기능 자체가 업그레이드되는 반면, Proxy는 기능 자체는 유지됨
- Facade는 복잡한 엔티티를 버퍼링하고 자체 초기화하는 것이 유사.
- Decorator와 Proxy는 거의 비슷한 구조를 갖고 있으나 Proxy는 자체적으로 서비스 객체의 라이프사이클을 관리하나 Decorator는 항상 클라이언트에 의해 제어됨
