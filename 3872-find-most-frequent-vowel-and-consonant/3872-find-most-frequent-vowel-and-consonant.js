function maxFreqSum(s) {
  const vowels = { a: 0, e: 0, i: 0, o: 0, u: 0 };
  const letters = 'abcdefghijklmnopqrstuvwxyz'.split('');

  // Get consonants (letters not in vowels)
  const consonants = {};
  for (const letter of letters) {
    if (!(letter in vowels)) {
      consonants[letter] = 0;
    }
  }

  // Count frequencies
  for (const k of s) {
    if (k in vowels) {
      vowels[k]++;
    } else if (k in consonants) {
      consonants[k]++;
    }
  }

  // Get max values
  const maxVowel = Math.max(...Object.values(vowels));
  const maxConsonant = Math.max(...Object.values(consonants));

  return maxVowel + maxConsonant;
}
