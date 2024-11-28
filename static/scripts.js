$(document).ready(function () {
    $("#slow-request").on("click", function () {
        $.get("/api/slow", function (response) {
            $("#api-response").text(response.message);
        });
    });

    $("#thread-simulate").on("click", function () {
        const threads = prompt("Enter number of threads to simulate:", 5);
        if (threads) {
            $.ajax({
                url: "/simulate-multiple-threads",
                method: "POST",
                contentType: "application/json",
                data: JSON.stringify({ threads }),
                success: function (response) {
                    $("#api-response").text(response.message);
                },
            });
        }
    });
});
