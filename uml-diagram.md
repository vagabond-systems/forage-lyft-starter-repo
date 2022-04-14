```mermaid
classDiagram
    Car ..> Engine
    Car ..> Battery
    class Car{
        +Engine engine
        +Battery battery
    }
    class Engine{
        +int mileage
        +bool is_warning_on
        +should_service() bool
    }
    class Battery{
        +datetime installed_date
        +should_service()
    }



   Person <|-- Student
   Person <|-- Professor
   Person : +String name
   Person : +String phoneNumber
   Person : +String emailAddress
   Person: +purchaseParkingPass()
   Address "1" <-- "0..1" Person:lives at
   class Student{
      +int studentNumber
      +int averageMark
      +isEligibleToEnrol()
      +getSeminarsTaken()
    }
    class Professor{
      +int salary
    }
    class Address{
      +String street
      +String city
      +String state
      +int postalCode
      +String country
      -validate()
      +outputAsLabel()
    }
```

The current service criteria are as follows:

- Engines
  - Capulet Engine - should be serviced once every 30,000 miles
  - Willoughby Engine - should be serviced once every 60,000 miles
  - Sternman Engine - should be serviced only when the warning indicator is on
- Batteries
  - Spindler Battery - should be serviced once every 2 years
  - Nubbin Battery - should be serviced once every 4 years

The current car models are as follows:

- Calliope
  - Capulet Engine
  - Spindler Battery
- Glissade
  - Willoughby Engine
  - Spindler Battery
- Palindrome
  - Sternman Engine
  - Spindler Battery
- Rorschach
  - Willoughby Engine
  - Nubbin Battery
- Thovex
  - Capulet Engine
  - Nubbin Battery
