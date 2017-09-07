var resetBtn = document.querySelector('#resetBtn');
var cells = document.querySelectorAll('td');

// Add handlers
function game_reset () {
    cells.forEach(function(cell) {
        cell.innerText = '';
    });
}

function make_a_move(event) {
    var cell = event.target;
    switch (cell.innerText) {
        case 'X':
            cell.innerText = 'O';
            break;
        case 'O':
            cell.innerText = '';
            break;
        default:
            cell.innerText = 'X'
            break;
    }
}

// Add listeners
resetBtn.addEventListener('click', game_reset);
cells.forEach(function(cell) { cell.addEventListener('click', make_a_move)});
