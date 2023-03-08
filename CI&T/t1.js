// Complete this function to return either
// "Hello, [name]!" or "Hello there!"
// based on the input
const sayHello = name => {
  // You can print to STDOUT for debugging like you normally would:
  console.log(name);
 
  let nome = name == null ? "Hello there!" : `Hello, ${name}!`;
  // but you need to return the value in order to complete the challenge  
  return nome; // TODO: return the correct value
};

sayHello("emerson")
console.log(sayHello("emerson"));
console.log(sayHello());


const sayHell = name => {
  // You can print to STDOUT for debugging like you normally would:
  console.log(name);
 
  let nome = `Hello, ${name}`
  // but you need to return the value in order to complete the challenge  
  return nome; // TODO: return the correct value
};

sayHello("emerson")
console.log(sayHello("emerson"));
console.log(sayHello());