//functie pentru asteptare timp ( ms )
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}
setTimeout(() => $('.fullscreen').fadeOut(500), 1500)

//funtie pentru a arata comment-urile pentru fiecare postare 
function comment_visualisation(block, id){ 
    if ( block == 1 ){
        document.querySelectorAll('.comment' + id).forEach( (e) => { e.style.display = 'Block'; } )
        document.querySelector(".comment_section_" + id).style.display = "block";
       }
    else { 
        document.querySelectorAll('.comment' + id).forEach((e) =>{ e.style.display = 'none';})
        document.querySelector(".comment_section_" + id).style.display = "none";
    } 
}

//filtru pentru comentarii si postarei pe pagina de profil
function show_dissapear( class_1, class_2 ){
    console.log("da");
    try {
        document.querySelectorAll("." + class_1).forEach((e) => { e.style.display = "none"; })
    } catch { document.querySelector("." + class_1).style.display = "none";}

    try {
        document.querySelectorAll("." + class_2).forEach((e) => { e.style.display = "block"; })
    } catch { document.querySelector("." + class_2).style.display = "block";}
}

//functie care calculeaza inaltimea in PX a ecranului si scade cati PX vrei -> param. 'less'
function page_height_px(element, less){
    try {
        return document.querySelector(element).style.height = window.innerHeight - less + "px"
    }
    catch{
        return 1;
    }
}
page_height_px(".fullscreen", 0)
page_height_px(".form_body", 75)

//functie pentru aratarea textului cand dam 'reload' la pagina
function sleepText(cls){
    let count = 0; 
    $( cls ).each(function() {
        $(this).fadeIn(count * 200);
        count ++ ;
    });
}
sleepText('.CNNSletters');
sleepText('.PL');
sleepText('.Home');
