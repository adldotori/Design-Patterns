# Factory Pattern

https://refactoring.guru/design-patterns/factory-comparison

> ### object 생성

## factory

- 클래스, 메소드, 함수 등 무언가를 생성하는 모든 것을 factory라 함
- 일반적으로는 객체를 생성함.
- 굉장히 넓은 범위의 단어로 포함하고 있는 의미가 많다.

## Creation Method

- 객체를 생성하는 모든 메소드

## Static Creation Method

- 클래스에서 정적으로 객체를 생성하는 메소드
- 다양한 목적을 갖는 여러 생성자가 필요한 경우, 객체 재사용이 필요한 경우 사용

## Simple Factory

- factory method 패턴, abstract factory 패턴의 기초.
- 단일 클래스의 단일 메소드로 구현됨.
- 파라미터를 통해 생성 객체가 정해짐.
