Gilded Rose Exercise
===========

This is an exercise in using characterization tests and dependency breaking, the shield and the sword.

It is based on the kata "Gilded Rose", named after the inn. The requirements are in the [requirements document](requirements.md), next to this document.

Your first task is to get everything building and running in your development environment. Then you add characterization tests and break dependency.

1. Create a fork so that any changes you push, should you do so, is not mixed with others.
1. Try run the [manual_test.py](manual_test.py). Can you tell from the output if the program works?
1. Run the test [test_gilded_rose.py](test_gilded_rose.py) and measure coverage. 
The script [measure-coverage.sh](measure-coverage.sh) is helpful. [Report will be here](htmlconv/index.html).
See [IntelliJ](IntelliJ.md) on how to get branch coverage.
1. Add characterization tests (shield) until you have total branch coverage. Use the requirements document to find test cases. It is not possible to reach 100%, why?
1. When you reached the good branch coverage, it is time to refactor the code. Start with dependency breaking, the sword. 
1. With the dependency broken, you can refactor your current tests to simplify test data setup. 
1. Time to refactor the current implementation. Keep tests at green all the time. 
Remember, you may not change the [`Item`](item.py) class as it is owned by a Goblin. 
1. Next, create a failing test and then implementation, for the new requirement. 
 
Reflections
------
Note what you learned. 

* Why was the shield used before the sword? 
* Why refactor the current implementation before adding a new requirement?
* How did you feel when the implementation was put under test? 
* When you refactored the implementation, was readability any of your concern? Why?


Credits
-------

* written by [Terry Hughes](https://twitter.com/TerryHughes)
