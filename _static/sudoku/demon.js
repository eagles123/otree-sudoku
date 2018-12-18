$(document).ready(function() {
    $('#next').attr("disabled", true);
    var number = 1;
    var game1 = [[3,0,2,0],[0,2,0,0],[0,0,1,0],[0,1,0,4]];
    var answer1 = [[3,4,2,1],[1,2,4,3],[4,3,1,2],[2,1,3,4]];
    var game2 = [[1,4,0,0],[0,2,0,0],[0,0,2,1],[0,0,4,0]];
    var answer2 = [[1,4,3,2],[3,2,1,4],[4,3,2,1],[2,1,4,3]];
    var clicked = 0;
    var startTime1 = new Date();
    var startTime2 = new Date();
    
    
    buildGame(game1);

    //function to transform each game(list fomr) to a two dimensonal array
    function generateGameData(list){
        tdArray = [];
        for (var i = 0; i<4; i++){
            tdArray.push(list.slice(4*i,4*(i+1)));
        };
        return tdArray;
    }


    //function to populate the game board with data
    function buildGame(game){
        for (var r = 0; r<4; r++){
            for (var c = 0; c <4; c++){
                let cellid = "#r" + r +"c" +c;
                $(cellid).html('<input class="sudoku" maxlength="1">')
                if (game[r][c] != ""){
                    $(cellid).html(game[r][c])
                }
            }
        }
    }

    $("#check").click(function(){
        let userBoard = loadUserBoard();
        if (number === 1){
            let endTime1 = new Date();
            let demoTime1 = ((endTime1 - startTime1)/1000)/60;
            if (clicked === 0){
            $('#id_demo1_button_sequence').val("Attempt First")
            }
            if (check(userBoard) === true){
                clicked += 1;
                $('#next').attr("disabled", false);
                $('#id_first_demo').val(clicked)
                $("#check").attr("disabled", true);
            }
            else{
                clicked += 1;
            }
            $('#id_first_demo_time').val(demoTime1.toFixed(2));
            

        }
        if (number === 2){
            let endTime2 = new Date();
            let demoTime2 = ((endTime2 - startTime2)/1000)/60;
            if (clicked === 0){
            $('#id_demo2_button_sequence').val("Attempt First")
            }
            if (check(userBoard) === true){
                clicked += 1;
                $('#next').attr("disabled", false);
                $('#id_second_demo').val(clicked)
                $('.otree-btn-next').attr("disabled", false);
                $("#check").attr("disabled", true);
            }
            else{
                clicked += 1;
            }
            $('#id_second_demo_time').val(demoTime2.toFixed(2));                    
            
        }
    });

    function check(board) {
        if(validateInput(board)){
            if (sudokuChecker(board)){
               // alert("It is Correct!")                            
               alert("נכון!");
               return true;
            }
            else {
                //alert("It is not correct!")     
                alert("לא נכון");                       
                return false;
            }
        }
        else{
            //alert("It is not correct!")                        
            alert("לא נכון");
            return false; 
        }
    };

    $("#next").click(function (){
        $("#next").hide();
        $("#check").attr("disabled", false);
        buildGame(game2);
        $('#label').html("ננסה עוד דוגמא")
        $('#button').css("display", 'block');
        $('.otree-btn-next').attr("disabled", true);
        $('#answer').attr("disabled", false);
        $("#check").attr("disabled", false);
        number = 2;
        clicked = 0;
        startTime2 = new Date();
    });


    $("#answer").click(function () { 
        $('#next').attr("disabled", false);
        $("#check").attr("disabled", true);
        if (number ===1 ){
            let endTimeOne = new Date();
            let demoTimeOne = ((endTimeOne - startTime1)/1000)/60;
            if (clicked === 0){
            $('#id_demo1_button_sequence').val("Get Answer First")
            $('#id_first_demo').val("No attemps")
            $('#id_first_demo_time').val(demoTimeOne.toFixed(2));
            }
            else{
                $('#id_first_demo').val(clicked)
            }
            buildGame(answer1);
            $('#answer').attr("disabled", true);
        }
        if (number ===2){
            let endTimeTwo = new Date();
            let demonTimeTwo = ((endTimeTwo - startTime2)/1000)/60;
            if (clicked === 0){
            $('#id_demo2_button_sequence').val("Get Answer First")
            $('#id_second_demo').val("No attemps")
            $('#id_second_demo_time').val(demonTimeTwo.toFixed(2));
            }
            else{
                $('#id_second_demo').val(clicked)
            }
            $('.otree-btn-next').attr("disabled", false);
            buildGame(answer2);
            $('#answer').attr("disabled", true);
        }
     });
    function sudokuChecker(array) {
        if (rowSum(array) && colsum(array) && gridSum(array))
            return true;
        return false;
    }

    //function to check if the answer is correct
    function rowSum(array){
        let isCorrect = true;
        for (var i = 1; i<5; i++){
            if(sum(array[i]) !== 10){
                isCorrect = false;
                i = 5;
            }
        }
        return isCorrect;
    }
    //check colmun sum
    function colsum(array){
        let isCorrect = true;
        for (var i = 0; i <4; i++){
            if ((array[1][i] + array[2][i] + array[3][i] + array[4][i]) !== 10) {
                isCorrect = false;
                i = 4;
            }
        }
        return isCorrect;
    }
    //check if the sum of 2x2 grid
    function gridSum(array){
        let isCorrect = true;
        for (var i = 1; i <2; i++){
            if ((array[i][0] + array[i][1] + array[i+1][0] + array[i+1][1] !==10 || array[i][2] + array[i][3] + array[i+1][2] + array[i+1][3]) !==10){
                isCorrect = false;
                i = 3;
            }
        }
        for (var i = 3; i <4; i++){
            if ((array[i][0] + array[i][1] + array[i+1][0] + array[i+1][1] !==10 || array[i][2] + array[i][3] + array[i+1][2] + array[i+1][3] !==10)){
                isCorrect = false;
                i = 4;
            }
        }
        return isCorrect;
     }
    //function to validate input
    function validateInput(array){
        let valid = false;
        for (var i=1; i<5; i++){
                for (var j=0; j<4; j++){
                if (Number.isInteger(array[i][j]) && array[i][j] >= 1 && array[i][j] <= 4){
                    valid = true
                }
                else{
                    valid = false;
                    j = 5;
                    i = 5;
                }
            }
        }
        return valid;
    };
    //get user imports
    function loadUserBoard() {
        let result = new Array(1)
        for (var r = 0; r<4; r++){
            let temp = new Array(4);
            for (var c=0; c<4; c++){
                let cellid = "#r" + r +"c" +c;
                let cellValue;
                if ($(cellid).find("input")[0]){
                    cellValue = $(cellid).find("input").val();
                }
                else{
                    cellValue = $(cellid).html();                                
                }
                temp[c] = parseInt(cellValue);
            }
            result.push(temp);
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