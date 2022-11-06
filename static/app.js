localStorage.setItem("score", 0)

$("#submit_guess").on("submit", async function(e) {
    e.preventDefault();
    const response = await axios("/check-guess", {params: {guess: guess}})

    if(response.data.result === "ok") {
        const word = $("#guess").val()
        console.log("ok")
        const newVal = Number(localStorage.getItem("score")) + word.length;
        $(".score").text(`your score: ${newVal}`)


    } else if(response.data.result === "not-word") {
        console.log("not a word")


    } else if (response.data.result === "not-on-board") {
        console.log("not on board")
    }
})



const disable = function() {
    $("#guess").prop('disabled', true)
    $("#submit").prop('disabled', true)
    $(".timed-out").text("Sorry you ran out of time!")
}

setTimeout(disable, 1000)
