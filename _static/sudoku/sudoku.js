$(document).ready(function() {
    var counter = 0;
    var game_attempted = 0;
    var game_correct = 0;
    var games = getGames();
    var visit = false;
    $("#total").html("/"+ (games.length-1));

    buildGame();
    var origmin = 29;
    var orisec = 60;
    var countdown = 30*60*1000;
    var timeSpend ="";
    // Update the count down every 1 second
    let timer = setInterval(function() {
        countdown -= 1000;
        // Time calculations for days, hours, minutes and seconds
        let minutes = Math.floor(countdown / (60 * 1000));
        let seconds = Math.floor((countdown - (minutes * 60 * 1000)) / 1000);
        let spmin = origmin - minutes;
        let spsecond = orisec - seconds;
        let convertSecond = parseFloat((spsecond/60).toFixed(2));
        //timeSpend = spmin + " Min " + spsecond + " Seconds ";
        timeSpend = spmin+convertSecond;

        // Display the countdown in the element with id="demo"
        // document.getElementById("demo").innerHTML = minutes + "m " + seconds + "s ";

        // If the count down is finished, write some text
        if (countdown <= 0) {  
            clearInterval(timer)
            if (visit == false){                    
                $('#id_game_attemptted').val(game_attempted);
                $('#id_game_correctted').val(game_correct);
                // $('#id_is_terminated').val("No");
                $('#id_time_spend').val(timeSpend);
                $("#submit").click();
            }
            else{
                $("#submit").click();
            }
        }
    }, 1000);

    //function to transform each game(list fomr) to a two dimensonal array
    function generateGameData(list){
        tdArray = [];
        for (var i = 0; i<4; i++){
            tdArray.push(list.slice(4*i,4*(i+1)));
        };
        return tdArray;
    }

    //function to populate the game board with data
    function buildGame(){
        let data = generateGameData(games[counter])
        for (var r = 0; r<4; r++){
            for (var c = 0; c <4; c++){
                let cellid = "#r" + r +"c" +c;
                $(cellid).html('<input class="sudoku" maxlength="1">')
                if (data[r][c] != ""){
                    $(cellid).html(data[r][c])
                }
            }
        }
    }
    //button click function main function of this javascript
    $("#submit-button").click(function() {
        counter += 1;
        let number_games = counter;
        let userBoard = loadUserBoard();
        if(validateInput(userBoard) && checkUnniqueElement(userBoard)){
            if (sudokuChecker(userBoard)){
                game_attempted += 1;
                game_correct +=1;
            }
            else {
                game_attempted += 1;
            }
        }
        else{
            game_attempted += 1;
        }

        if (counter === games.length-2){
            $('#submit-button').html("סיים");

        }

        if (counter === games.length -1){
            $('#id_game_attemptted').val(game_attempted);
            $('#id_game_correctted').val(game_correct);
            // $('#id_is_terminated').val("No");
            $('#id_time_spend').val(timeSpend)
            number_games = games.length-2;
        }
        number_games += 1;
        $('#label').html(number_games);

        buildGame();
    });
    //button to visit website
    $('#website').click(function() {
        let r = confirm("Are you sure you want to stop the game and visit other websites?")
        if (r){
        visit = true;
        $('#submit-button').prop("disabled", true);
        $('#website').hide();
        $('#stop').hide();
        $('#id_game_attemptted').val(game_attempted);
        $('#id_game_correctted').val(game_correct);
        // $('#id_is_terminated').val("No");
        $('#id_time_spend').val(timeSpend);
        $('#id_visit_websites').val("Yes");
    
        }
    });
    //button to leave the game
    // $('#stop').click(function(){
    //     let r = confirm("Are you sure you want to leave the Experiment?")
    //     if (r){
    //     $('#id_game_attemptted').val(game_attempted);
    //     $('#id_game_correctted').val(game_correct);
    //     $('#id_is_terminated').val("Yes");
    //     $('#id_time_spend').val(timeSpend);
    //     $('#stop').prop("type", "submit")
    //     }
    // });
    function sudokuChecker(array) {
        if (rowSum(array) && colsum(array) && gridSum(array))
            return true;
        return false;
    }

    //function to check sum of row
    function rowSum(array){
        let isCorrect = true;
        for (var i = 0; i<4; i++){
            if(sum(array[i]) !== 10){
                isCorrect = false;
                i = 4;
            }
        }
        return isCorrect;
    }
    //check colmun sum
    function colsum(array){
        let isCorrect = true;
        for (var i = 0; i <4; i++){
            if ((array[0][i] + array[1][i] + array[2][i] + array[3][i]) !== 10) {
                isCorrect = false;
                i = 4;
            }
        }
        return isCorrect;
    }
    //check if the sum of 2x2 grid
    function gridSum(array){
        let isCorrect = true;
        for (var i = 0; i <1; i++){
            if ((array[i][0] + array[i][1] + array[i+1][0] + array[i+1][1] !==10 && array[i][2] + array[i][3] + array[i+1][2] + array[i+1][3] !==10)){
                isCorrect = false;
                i = 2;
            }
        }
        for (var i = 2; i <3; i++){
            if ((array[i][0] + array[i][1] + array[i+1][0] + array[i+1][1] !==10 && array[i][2] + array[i][3] + array[i+1][2] + array[i+1][3] !==10)){
                isCorrect = false;
                i = 3;
            }
        }
        return isCorrect;
     }
    //function to validate input
    function validateInput(array){
        let valid = false;
        for (var i=0; i<4; i++){
                for (var j=0; j<4; j++){
                if (Number.isInteger(array[i][j]) && array[i][j] >= 1 && array[i][j] <= 4){
                    valid = true
                }
                else{
                    valid = false;
                    j = 4;
                    i = 4;
                }
            }
        }
        return valid;
    };
    //get user imports
    function loadUserBoard() {
        let result = [new Array(4), new Array(4), new Array(4), new Array(4)];

        for (var r = 0; r<4; r++){
            for (var c=0; c<4; c++){
                let cellid = "#r" + r +"c" +c;
                let cellValue;
                if ($(cellid).find("input")[0]){
                    cellValue = $(cellid).find("input").val();
                }
                else{
                    cellValue = $(cellid).html();
                }
                result[r][c] = parseInt(cellValue);
            }
        }
        return result
    }

    function sum(array){
        let sum =  0;
        for (var i in array){
            sum += array[i]
        }
        return sum;
    }
    
    function checkUnniqueElement(arr) {
        arr.sort();
        if(arr[0] !== arr[arr.length -1])
            return true;
        return false;
    }

});