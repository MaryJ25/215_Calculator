# Calculator

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#usage">Usage Example</a></li>
    <li><a href="#functions">Available Functions</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

This is a simple Python Calculator package. The package was made as an exercise in a Data Science course taught by Turing College.
The package allows simple calculations to be made.

<!-- INSTALLATION -->
## Installation

To install use `pip install git+https://github.com/MaryJ25/Calculator.git`

Then to import it use `from calculator.calculator import Calculator`

<!-- USAGE EXAMPLES -->
## Usage Example
```
c = Calculator()
c.start(10)
c.add(10)
c.divide(5)
c.get_current() #output 4
```
<!-- FUNCTIONS -->
## Available Functions
`reset()` - resets the value

`start(10)` - sets the value to 10

`add(10)` - adds 10 to current value

`subtract(10)` - subtracts 10 from current value

`multiply(10)` - multiplies current value by 10

`divide(10)` - divides current value by 10

`power(10)` - exponentiates current value to the 10th power

`root(10)` - gets the 10th root from current value

`get_current()` - returns current value

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.


