#Simple Web Calculator

It is a simple web caculator for Behavior Driven Development (BDD) example.

The app is written in Python with Flask framework and use Ruby's Cucumber to run the step files.

Feature files are put in the "features" folder and step files are in the "features/step_definitions".

### DEMO
[Live Demo on Heroku](http://webcalculator.herokuapp.com/)

### Screenshot
![Screenshot](https://raw.githubusercontent.com/imidya/WebCalculator/master/static/img/screenshot.png)
### Installation
1. You need install Python and Ruby first.
2. Change driectory.

    ```
    $ cd WebCalculator
    ```

3. Install Python required packages.

    ```
    $ pip install -r requirements.txt
    ```

4. Install Cucumber.

    ```
    $ gem install cucumber
    ```

5. Install Watir web driver.

    ```
    $ gem install watir
    ```

6. Install Rspec.

    ```
    $ gem install rspec
    ```

7. Try to run the unit tests. It should all pass.

    ```
    $ py.test CalculatorTest.py
    ```

8. Run web app. The app will run on 127.0.0.1:5000

    ```
    $ python run.py
    ```

9. Run Cucumber.

    ```
    $ cucumber features/calculator.feature
    ```

10. You done!