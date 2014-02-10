// swap the following numbers with words, couldn't find a pattern to automate it
var number2word = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    '10': 'ten',
    '11': 'eleven',
    '12': 'twelve',
    '13': 'thirteen',
    '14': 'fourteen',
    '15': 'fifteen',
    '16': 'sixteen',
    '17': 'seventeen',
    '18': 'eighteen',
    '19': 'nineteen',
    '20': 'twenty',
    '30': 'thirty',
    '40': 'forty',
    '50': 'fifty',
    '60': 'sixty',
    '70': 'seventy',
    '80': 'eighty',
    '90': 'ninety',
};

// placements for hundreds, thousands onwards
var placement = {
    '4': 'thousand',
    '3': 'hundred'
};

var wordIt = function(val) {

    var abs_val;
    var len;
    var buff, buff2;
    var tmp;
    var i;

    if (val != parseFloat(val)) {

        return 'Only whole numbers are allowed';

    }
    
    abs_val = Math.abs(parseFloat(val)) + '';
    len = abs_val.length;
    
    if (len > 4) {

        return 'Unsupported number (only supports 0 - 9999)';

    }

    buff = [];

    // hundreds, thousands, etc placement
    for (i = 0; i < (len - 2); i++) {

        if ('0' !== abs_val[i]) {

            if (undefined != placement[len - i]) {

                buff.push(number2word[abs_val[i]] + ' ' + placement[len - i]);

            }

        }

    }

    // tens and ones still remaining
    if (i < len - 1) {

        tmp = parseFloat(abs_val[i] + abs_val[i + 1]);
        buff2 = [];

        // less than 20, combine and check
        if (tmp < 20) {

            if (undefined !== (tmp = number2word[tmp])) {

                buff2.push(tmp);

            }

        }
        else {

            if (undefined !== (tmp = number2word[abs_val[i++] + '0'])) {

                buff2.push(tmp);

            }

            if (undefined !== (tmp = number2word[abs_val[i]])) {

                buff2.push(tmp);

            }

        }

        if (undefined != buff2) {

            if (0 !== buff.length && 0 !== buff2.length) {

                buff.push('and');

            }

            buff2.forEach(function(value, key) {

                buff.push(value);

            });

        }

    }
    else if (i < len) {

        buff.push(number2word[abs_val[i]]);

    }

    return buff.join(' ');

};

var wordLength = function(str) {

   return str.split(' ').join('').length; 

};

var total_len = 0;

for (i = 1; i <= 1000; i++) {

print(i + ", " + wordLength(wordIt(i)));
    total_len += wordLength(wordIt(i));

}

print(total_len);
