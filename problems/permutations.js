function permutations(string) {
  // first a type check to make sure we are dealing with a proper var
  if (!string || typeof string !== "string") {
    return "Please enter a string"
  }

  // if the string length is less than 2, then we already know all permutations Ex. 'a'
  if (!!string.length && string.length < 2) {
    return [string]
  }

  let permutationsArr = [];

  for (let i = 0; i < string.length; i++) {
    let char = string[i]

    if (string.indexOf(char) != i) {
      continue;
    }
    // get the remainder of the two sides that the character is inbetween
    let remainder = string.slice(0, i) + string.slice(i + 1);

    // set another for loop iterating over the recursive return values for the permutations array, this time passing in the remainder of the string
    for (let permutation of permutations(remainder)) {
      permutationsArr.push(char + permutation)
    }
  }
  return permutationsArr;
}
console.log(permutations("aabb"))