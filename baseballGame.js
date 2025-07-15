/**
 * @param {string[]} operations
 * @return {number}
 */
var calPoints = function(operations) {
    let record = [];
    operations.forEach((elem) =>{

        if(elem === '+'){
            record.push(record[record.length -1 ] + record[record.length -2]);
        }
        else if (elem === 'D'){
            record.push(record[record.length -1] * 2);
        }
        else if(elem === 'C'){
            record.pop();
        }
        else{
            record.push(parseInt(elem));
        }
    });

    return record.reduce((accumulator, currentValue) => accumulator + currentValue, 0);

};