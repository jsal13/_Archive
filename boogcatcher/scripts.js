window.locsAndItems = {}

function locsAndItemsParser(txt) {
  const json = JSON.parse(txt);
  json.forEach((it) => {
    // window.importantItems defined in `importantItems.js`
    if (window.importantItems.includes(it.item)) {
      const loc = window.roomMap[window.friendlyRoomToRoomMap[it.location]["SceneName"]];

      let itemName = it.item;

      if (Object.keys(window.progressiveItemBase).includes(it.item)) {
        itemName = window.progressiveItemBase[it.item];
      }

      // TODO: Make this "defaulted" to an empty list instead of this gross if statement.
      if (!(loc in window.locsAndItems)) {
        window.locsAndItems[loc] = [itemName];
      } else {
        window.locsAndItems[loc].push(itemName);
      };
    }
  })

  var divAreas = document.getElementById("areas");

  Object.keys(window.locsAndItems).forEach(key => {
    var div = document.createElement("div");
    var tag = document.createElement("h2");
    var text = document.createTextNode(`${key}`);
    div.appendChild(tag);
    tag.appendChild(text);
    divAreas.appendChild(div);

    window.locsAndItems[key].forEach(item => {
      var checkbox1 = document.createElement("input");
      checkbox1.setAttribute("type", "checkbox");
      checkbox1.setAttribute("value", "1");
      var label1 = document.createElement("label");
      label1.setAttribute("class", "item");
      label1.innerText = item;

      if (["Dreamer", "Monomon", "Herrah", "Lurien"].includes(item)) {
        label1.setAttribute("class", "dreamer item");
      }

      var tag1 = document.createElement("p");
      tag1.appendChild(checkbox1);
      tag1.appendChild(label1);

      div.appendChild(tag1);
    })
  });
}

function dropHandler(ev) {
  console.log('File(s) dropped');
  ev.preventDefault();

  if (ev.dataTransfer.items[0]) {
    // Delegates file reading to `readFile()`.
    const reader = new FileReader();
    reader.addEventListener("load", () => { locsAndItemsParser(reader.result); }, false);

    const f = ev.dataTransfer.items[0].getAsFile();
    reader.readAsText(f);

    hideDropper();
  }
}

function hideDropper() {
  var dropZone = document.getElementById("drop-zone");
  dropZone.style.display = "none";
}

function dragOverHandler(ev) {
  console.log('File(s) in drop zone');
  ev.preventDefault();
}
