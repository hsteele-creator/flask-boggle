$("#submit_guess").on("submit", async function(e) {
    e.preventDefault();
    const response = await axios("/check-guess", {params: {guess: guess}})

    if(response.data.result === "ok") {
        console.log("ok")
    } else if(response.data.result === "not-word") {

        console.log("not a word")

    } else if (response.data.result === "not-on-board") {
        console.log("not on board")
    }
})
