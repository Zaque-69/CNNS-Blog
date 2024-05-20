//function pentru alegere aleatorie dintr o lista -> pentru fundalurile SVG din CSS   
function getRandomElement(list) {
    console.log("dadadadada")
    const randomIndex = Math.floor(Math.random() * list.length);
    return list[randomIndex];
}
document.querySelector("body").classList.add(getRandomElement(["svg_background", "svg_background_2", "svg_background_3", "svg_background_4", "svg_background_5"]))
