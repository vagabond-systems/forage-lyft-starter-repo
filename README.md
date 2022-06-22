# Starter Repo

This repo has everything you need to get started on the program, good luck!

The component is responsible for determining whether cars in Lyft’s new rental fleet should be serviced when they are returned. Whether or not a car should be serviced depends on two factors at the moment - the engine and battery.

There are five car models in Lyft’s fleet, each with a different engine-battery combination.

Each of the three types of engines has its own criteria for determining when it should be serviced. The same applies to each type of battery.

These service criteria will change somewhat frequently in the future, and new car models are bound to be added to the fleet.

With this in mind, it’s very important that the component is extensible and easy to modify, so new service criteria can be added quickly and efficiently.

Just today, you learned that the system must also take tires into account when determining if a car should be serviced in the future. Tacking this functionality onto the current system would be difficult and messy - instead, you have been instructed to take the time to refactor the codebase prior to making the change.

The first step of this process is to draft up a new (clean) system architecture that will allow for the seamless inclusion of the new functionality. Your task is to draft and submit a class diagram that maps out how the system will be reorganized.

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

3. Draft a new architecture

Now that you have a good handle on the current system, think through the best way to reorganize it. Your plan should allow easy extensibility going forward. It should be trivial to add new service criteria and change which parts each car model includes (e.g. change the battery installed on the Thovex from a Nubbin to a Spindler). Additionally, making a change to the service criteria for a given car part should only require making a change in one place. If you are having trouble coming up with a good design, take a look at the resources linked below for inspiration. Once you have an idea of how to organize the system, draft a UML class diagram and submit it below. The intent of the class diagram is to convey intent, worry more about your design, and less about proper UML syntax.

When you’re finished, convert your class diagram to a PDF and submit it below.
