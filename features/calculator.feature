Feature: Calculator Functions
	In order to complete ALSD this semester
    As a student
    I want to create a simple calculator to do some simple calculation for the final project.

	Scenario: Add function
    	Given A web calculator
    	When enter "1 + 2"
    	Then get the result is 3

    Scenario: Times funciton
        Given A web calculator
        When enter "5 x 2"
        Then get the result is 10

    Scenario: Times funciton
        Given A web calculator
        When enter "5 + 4 x 3 - 9 / 3"
        Then get the result is 14

    Scenario: Test basic plus formula and some questions
        Given A web calculator
        When enter "(5 + 4) x 3 - 9 / 3"
        Then get the result is 24

