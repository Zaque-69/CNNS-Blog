console.log(1);
function changeThemes(col1, col2, col3, col4, col5){
    $('nav').css('background-color', col1);
    $('body').css('background-color', col2);
    $('.container').css('background-color', col3);
    $('.background-continut').css('background-color', col4);
    
    const changeTextColor = ['h1', 'h2', 'p'];
    for(let i = 0; i < changeTextColor.length; i++) $(changeTextColor[i]).css('color', col5);
    // #02113D
}
