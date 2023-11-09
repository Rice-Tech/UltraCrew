var num = 0;


document.addEventListener('DOMContentLoaded', function() {
    onPageLoad()
});

function onPageLoad(){
    var numStationsElement = document.getElementById("numStations")
    numStationsElement.addEventListener("input", (event) => {
        console.log("Hello");
        var numStations = numStationsElement.value;
        var stationsListElement = document.getElementById("stationsListElement");
        stationsListElement.innerHTML = ""
        for (let i = 0; i < numStations; i++)
        {
            num = i;
            var stationInputTemplate = `
                <li>
                    <label for="stationName${i}">Station Name: </label>
                    <input type="text" id="stationName${i}" name="stationName${i}" >
                    <label for="stationDist${i}">Station Distance: </label>
                    <input type="number" id="stationDist${i}" name="stationDist${i}" step=0.1 >
                </li>
            `;
            stationsListElement.innerHTML += stationInputTemplate;
        }
    })
}


