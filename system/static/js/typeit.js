const comments = ["Colegiul National Nichita Stanescu - Ploiesti", 
	"Numai cu o invitatie poti accesa pagina !",
	"Welcome / Bun venit ! "]
new TypeIt(".firstType", {
	strings: comments[Math.floor(Math.random() * comments.length)],
	speed: 75,
	loop: false,
  }).go();
