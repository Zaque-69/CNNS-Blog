const comments = ["Colegiul National Nichita Stanescu - Ploiesti", 
	"Only with an invitation code you can acces the website !",
	"Welcome / Bun venit ! "]
new TypeIt(".firstType", {
	strings: comments[Math.floor(Math.random() * comments.length)],
	speed: 75,
	loop: false,
  }).go();
