const listOfClasses = ['mxWLOPyckongDCJGBpQK', 'eRstQPMlfBoYsLBVZgMW', 'QFdINEQehJkVrcHZtUJs', 'amcYvyDjbIjNAWyLEwJG', 'anunt'];
document.getElementById('filterButton').addEventListener('click', function(){
    for (var i = 0; i < listOfClasses.length; i++) {
        document.querySelectorAll('.' + listOfClasses[i]).forEach((e) =>{
            if ( listOfClasses[i] == document.querySelector('select').value ) e.style.display = 'block';
            else e.style.display = 'none';
        })
    }
})
console.log('succes');
