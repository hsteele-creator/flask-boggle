$("#submit-guess").on("submit", function(e) {
    e.preventDefault()
    console.log("hello")
})

$("#submit-guess").prop("disabled", true);
setTimeout(function() {
   $("#submit-guess").prop("disabled", false);
}, 60000);