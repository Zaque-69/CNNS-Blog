try{
    const listOfClasses = ['Ve', 'VIIIe', 'IXi2', 'Xi1', 'XIs', 'anunt']; list = [];
    fetch('../static/js/main.json').then(response => response.json()).then(data => {
        for(let i = 0; i < listOfClasses.length; i++) {
            list.push(eval(`data.${listOfClasses[i]}`));
        }
    });

    document.getElementById('filterButton').addEventListener('click', function(){
        for (var i = 0; i < list.length; i++) {
            document.querySelectorAll('.' + list[i]).forEach((e) =>{
                if ( list[i] == document.querySelector('select').value ) e.style.display = 'block';
                else e.style.display = 'none';
            })
        }
    })
}
catch{}
