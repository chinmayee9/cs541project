$(document).ready(function() {
$('#currencylist').DataTable({
    "scrollX": true,
    "ajax": "/getlistdata",
    "columns": [
            { "data": "links" },
            { "data": "rating" },
            { "data": "percentPopularity" },
            { "data": "dominance" },
            { "data": "spreadAboutMean" },
            { "data": "kurtosis" },
            { "data": "skewness" }
        ],
    "order": [[ 1, "desc" ]]
});

});
