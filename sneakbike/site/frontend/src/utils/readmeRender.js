import Mustache from 'mustache';

const partStyle = `<style>
    p,
    span,
    td {
      font-family: 'Lato', sans-serif;
    }

    h4 {
      font-family: 'Vollkorn', serif !important;
    }

    .alert {
      margin-bottom: 0;
    }

    .game-card {
      width: 26rem;
      margin-top: 1rem;
      margin-left: 1rem;
      padding-top: 0.75rem;
      padding-bottom: 0.75rem;
    }

    .slight-indent {
      margin-left: 16px;
      margin-right: 16px;
    }

    .table {
      margin-bottom: 0;
      margin-top: 0.5rem;
    }

    .td-button-col {
      width: 6rem;
    }

    .alert {
      border-radius: 1rem;
    }

    .alert-objective {
      background-color: transparent;
      padding-top: 0;
    }

    .alert-hint {
      background-color: #e0f5e9;
      margin-bottom: 1rem;
    }

    .warning-txt {
      font-size: 0.75rem;
      color: grey;
    }

    .container {
      display: flex;
      flex-wrap: wrap;
      justify-content: flex-start
    }
  </style>`

const header = `
<head>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js"
    integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW"
    crossorigin="anonymous"></script>
  <link rel="preconnect" href="https://fonts.gstatic.com">
  <link
    href="https://fonts.googleapis.com/css2?family=Lato:ital,wght@0,300;0,400;0,700;1,400&family=Vollkorn:wght@600&display=swap"
    rel="stylesheet">
  ${partStyle}
</head>
`

const fullHTML = `
<html>
${header}
{{&body}}
</html>
`

const buttonTable = `
<table class="table table-striped table-sm">
  <tbody>
    {{&controllerHTML}}
  </tbody>
</table>
`

const cardTemplate = `
<div class="card game-card">
  <div class="card-body">

    <div class="alert alert-objective" role="alert">
      <h4>Game {{&gameNum}} Objective</h4>
      <span class="objective-text">{{&objective}}</span>
    </div>
    <div class="slight-indent">
      <div class="alert alert-hint" role="alert">
        <h4>Hints</h4>
        <span>{{&hint}}</span>
      </div>

      <span class="warning-txt">This table may not contain all game controls.</span>
      {{&buttonTable}}
    </div>
  </div>
</div >`

const partBody = `
<body>
  <div class="container">
    {{&cards}}
  </div>
</body>
`

function generateReadmeHTML(numGames, controllerData, objectives, hints) {
  var cardTemplates = []

  for (var idx = 0; idx < numGames; idx++) {

    const currentControllerData = controllerData[idx]
    const currentObjective = objectives[idx]
    const currentHint = hints[idx]

    const currentControllerHTML = Object.entries(currentControllerData).filter(item => item[1] !== '').map(item => `<tr><td class="td-button-col">${item[0]}</td><td>${item[1]}</td></tr>`).join("\n")

    const currentButtonTable = Mustache.render(buttonTable, { controllerHTML: currentControllerHTML })
    const currentCardTemplate = Mustache.render(cardTemplate, { gameNum: idx + 1, objective: currentObjective, hint: currentHint, buttonTable: currentButtonTable })

    cardTemplates.push(currentCardTemplate)
  }

  const cards = cardTemplates.join("\n\n")
  const body = Mustache.render(partBody, { cards: cards })
  const html = Mustache.render(fullHTML, { body: body })

  return html
}

export default generateReadmeHTML


