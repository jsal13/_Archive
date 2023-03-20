function GetRandomCards(numCards) {
    let cards = [];
    let cardMAX = 22;

    for (var i = 0; i < numCards; i++) {
        while (true) {
            let newCard = Math.floor(Math.random() * cardMAX) + 1;
            if (!cards.includes(newCard)) {
                cards.push(newCard);
                break;
            }
        }
    }
    cardStrings = cards.map(num => { return num.toString().padStart(2, "0") })
    console.log(cardStrings)
    return cardStrings;
}