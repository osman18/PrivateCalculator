var result = '';
var formula = '';
var isNewCalculate = false;

$(document).ready(function() {

    var update = function() {
        $('#result-float').html('');
        $('#result-int').html(formula);
    }

    var enter = function(text) {
        formula += text;
        update();
    }

    var checkLastOperator = function() {
        var lastOperator = '';
        isNewCalculate = false;
        if (formula.length > 3) {
            lastOperator = formula.substr(formula.length - 2);
        }
        if (lastOperator.indexOf('+') > -1 ||
            lastOperator.indexOf('-') > -1 ||
            lastOperator.indexOf('x') > -1 ||
            lastOperator.indexOf('÷') > -1) {
            
            return true;
        }
        return false;
    }

    var checkNewCalculate = function() {
        if (isNewCalculate) {
            formula = '';
            update();
            isNewCalculate = false;
        }
    }
    
    $('#btn-0').click(function() {
        checkNewCalculate()
        enter('0');
    });
    $('#btn-1').click(function() {
        checkNewCalculate()
        enter('1');
    });
    $('#btn-2').click(function() {
        checkNewCalculate()
        enter('2');
    });
    $('#btn-3').click(function() {
        checkNewCalculate()
        enter('3');
    });
    $('#btn-4').click(function() {
        checkNewCalculate()
        enter('4');
    });
    $('#btn-5').click(function() {
        checkNewCalculate()
        enter('5');
    });
    $('#btn-6').click(function() {
        checkNewCalculate()
        enter('6');
    });
    $('#btn-7').click(function() {
        checkNewCalculate()
        enter('7');
    });
    $('#btn-8').click(function() {
        checkNewCalculate()
        enter('8');
    });
    $('#btn-9').click(function() {
        checkNewCalculate()
        enter('9');
    });
    $('#btn-dot').click(function() {
        var separators = ['\\\+', '-','x', '÷'];
        var lastNumber = formula.split(new RegExp(separators.join('|'), 'g')).pop();
        if (lastNumber.indexOf('.') <= -1) {
            enter('.');
        }
    });
    $('#btn-add').click(function() {
        if (!checkLastOperator()) {
            enter(' + ');
        }
    });
    $('#btn-minus').click(function() {
        if (!checkLastOperator()) {
            enter(' - ');
        }
    });
    $('#btn-times').click(function() {
        if (!checkLastOperator()) {
            enter(' x ');
        }
    });
    $('#btn-divided').click(function() {
        if (!checkLastOperator()) {
            enter(' ÷ ');
        }
    });
    $('#btn-equal').click(function() {
        formula = formula.replace(/x/g, '*').replace(/\÷/g, '/').replace(/\(/g, '(').replace(/\)/g, ')');
        var resultAll;

        $.ajax({
            url: '/cal',
            data: {'formula': formula},
            type: 'POST',
            success: function(data, message) {
                resultAll = data.result;
                if (resultAll % 1 === 0) {
                    $('#result-int').html(resultAll);
                } else {
                    resultAll = resultAll.toFixed(3);
                    var resultInt = resultAll.split('.')[0];
                    var resultFloat = resultAll.split('.')[1];
                    $('#result-int').html(resultInt);
                    $('#result-float').html('.' + resultFloat);
                }
                $('#formula').html(formula);
                formula = resultAll;
                isNewCalculate = true;
            }
        });
    });
    $('#btn-LParenthesis').click(function() {
        enter('(');
    });
    $('#btn-RParenthesis').click(function() {
        enter(')');
    });
    $('#btn-clear').click(function() {
        $('#result-int').html('0');
        $('#result-float').html('');
        $('#formula').html('');
        formula = '';
        result = '';
    });
    $('#btn-back').click(function() {
        formula = formula.substring(0, formula.length - 1);
        update();
    });
});