$("#submit-guess").on("submit", function(e) {
    e.preventDefault()
    console.log("hello")

    const guess = $("#guess").value

    $.post("process.php", {guess:guess}, function(data) {
        console.log(data)
    })

})