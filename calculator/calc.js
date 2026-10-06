// Simple Calculator - Experiment 11

// Function that performs the arithmetic; a and b are numbers, op is the operation name
function calculate(a, b, op) {
  switch (op) {                                           // Choose the operation based on op
    case "add": return a + b;                             // "add" -> return the sum
    case "sub": return a - b;                             // "sub" -> return the difference
    case "mul": return a * b;                             // "mul" -> return the product
    case "div":                                           // "div" -> division needs a check first
      if (b === 0) throw new Error("Cannot divide by zero");  // Raise an error if the divisor is 0
      return a / b;                                       // Otherwise return the quotient
  }                                                       // End of switch
}                                                         // End of calculate()

// Function called when an operator button is clicked; op tells which button
function showResult(op) {
  const n1 = document.getElementById("num1").value;      // Read the text typed in the first box
  const n2 = document.getElementById("num2").value;      // Read the text typed in the second box
  const result = document.getElementById("result");      // Get the element where the answer is shown

  if (n1 === "" || n2 === "") {                           // If either box is empty...
    result.className = "err";                             // ...use the red error style
    result.textContent = "Please enter both numbers";     // ...show the error message
    return;                                               // ...and stop here
  }                                                       // End of empty-input check
  try {                                                   // Try the calculation (it may throw an error)
    const value = calculate(parseFloat(n1), parseFloat(n2), op);  // Convert text to numbers and calculate
    result.className = "ok";                              // Use the green success style
    result.textContent = "Result: " + value;              // Display the answer
  } catch (e) {                                           // If calculate() threw an error (divide by zero)...
    result.className = "err";                             // ...use the red error style
    result.textContent = "Error: " + e.message;           // ...display the error message
  }                                                       // End of try...catch
}                                                         // End of showResult()

["add", "sub", "mul", "div"].forEach(op => {              // Loop over the ids of the four operator buttons
  document.getElementById(op).addEventListener("click", () => showResult(op));  // On click, call showResult with that operation
});                                                       // End of loop

document.getElementById("clear").addEventListener("click", () => {  // When the Clear button is clicked...
  document.getElementById("num1").value = "";             // ...empty the first box
  document.getElementById("num2").value = "";             // ...empty the second box
  document.getElementById("result").textContent = "";     // ...remove the result text
});                                                       // End of Clear handler