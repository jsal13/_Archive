import { reshape } from "mathjs";
import cardList from "./cardListALTTP"; // TODO: Generalize this.
import signature from "./bingoCardSignatures";

// Generate a QuerySeed, which will be used to share the seed.
function getQuerySeed() {
  const urlParams = new URLSearchParams(window.location.search);
  const myParam = urlParams.get("seed");
  if (myParam === null) {
    return Math.floor(Math.random() * 1000000);
  }
  return myParam;
}

const querySeed = getQuerySeed();

// Seed sets the prng function here.  It's "random enough".
const seed = Math.floor(querySeed);
function random() {
  const x = Math.sin(seed + 1) * 10000;
  return x - Math.floor(x);
}

function getRandomSubarray(arr, size) {
  const shuffled = arr.slice(0);
  let i = arr.length;
  while (i > 0) {
    const index = Math.floor((i + 1) * random());
    const temp = shuffled[index];
    shuffled[index] = shuffled[i];
    shuffled[i] = temp;
    i -= 1;
  }
  return shuffled.slice(0, size);
}

const currentSignature = signature[Math.floor(random() * signature.length)];
const numEasy = currentSignature.filter(x => x === 1).length;
const numMedium = currentSignature.filter(x => x === 2).length;
const numDifficult = currentSignature.filter(x => x === 3).length;

const valuesEasy = getRandomSubarray(cardList[1], numEasy);
const valuesMedium = getRandomSubarray(cardList[2], numMedium);
const valuesDifficult = getRandomSubarray(cardList[3], numDifficult);

function getBingoCardValues() {
  const mappedBingo = currentSignature.map(n => {
    if (n === 1) {
      return valuesEasy.pop();
    }
    if (n === 2) {
      return valuesMedium.pop();
    }
    return valuesDifficult.pop();
  });

  return { bingoCard: reshape(mappedBingo, [5, 5]), signature: querySeed };
}

export default getBingoCardValues;
