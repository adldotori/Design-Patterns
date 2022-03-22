# Decorator Pattern

https://refactoring.guru/design-patterns/decorator

> ### wrapper object를 통해 추가 행동 확장

- 일반적으로 객체의 행동 확장을 위해서는 상속이 많이 쓰임. 상속의 단점
  - 상속은 static해서 런타임에서 수정할 수 없다. 다시 만들고 대체해야 한다.
  - 자식 클래스는 단 하나의 부모 클래스만을 가진다.
- 상속 대신 Aggregation 을 사용
- Composite과 마찬가지로 inheritance와 aggregation을 동시에 사용하는 디자인 패턴

  - Association: 부모객체가 자식객체를 소유 + 각자의 라이프사이클을 가짐

    ```
    class Child():
        pass

    class Parent():
        def __init__(self, child):
            self.child = child
    ```

  - Composition: 부모객체가 자식객체를 소유 + 부모객체만 라이브사이클 가짐

    ```
    class Child():
        pass

    class Parent():
        def __init__(self):
            self.child = Child()
    ```

- 필요한 행동이 10개가 있을 때 2\*\*10개 조합의 자식 클래스를 생성하지 말고 10개의 데코레이터만 생성해서 자유롭게 런타임에서 추가, 삭제할 수 있도록 함.

### 적용 상황

- 런타임에서 객체에 행동 추가가 필요할 때
- 상속을 통해 행동 추가가 불가능하거나 어색할 때

### 장점

- 새로운 subclass를 만들지 않고 행동 확장이 가능함
- 런타임에서 객체의 책임을 삭제하거나 추가할 수 있음
- 멀티 데코레이터를 통해 다양한 행동을 조합할 수 있음
- SRP: 모놀리틱 클래스를 다양한 행동들로 쪼갤 수 있음

### 단점

- wrapper가 여러개 있을 때 중간에 있는거 삭제가 어려움
- 데코레이터 스택의 순서에 따라 동작이 달라지지 않을 때 구현하기 어려움
- 데코레이터 초기 구성 코드는 흉할 수 있음

### 타 패턴과의 관계

- Adapter는 존재하는 객체의 인터페이스를 변경하지만 Decorator는 인터페이스 변경 없이 확장한다. Decorator는 recursive composition을 지원한다.
- Adapter는 인터페이스 변경, Proxy는 인터페이스 유지, Decorator는 인터페이스 확장
- TODO: CoR
- open-ended number of objects를 구성하기 위해 Composite, Decorator는 recursive composition 사용
  - Decorator는 Composite과 유사하나 단 하나의 자식 컴포넌트만 갖고 있는 것이 다르다.
  - Decorator는 책임이 추가되지만 Composite는 단순히 더하기만 한다.
  - Composite에서 각 객체의 행동을 확장하기 위해 Decorator 사용 가능
  - open-ended number of objects를 다루는 디자인 패턴에서는 prototype을 같이 사용하면 좋다. 복잡한 구조를 매번 재클론하는 것은 어렵다.
- TODO: Strategy
- TODO: Proxy
