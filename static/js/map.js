//python -m SimpleHTTPServer 8888 &

$(function () {

    Plotly.d3.csv('https://an-app-for-job-seekers.herokuapp.com/static/data/v100_NVDA.csv', function (err, rows) {

        var continent = document.getElementById("geo-graph").getAttribute("continent");
        console.log(continent)

        colorList = [

            'rgb(239,200,255)',
            'rgb(189,215,231)',
            'rgb(107,174,214)',
            'rgb(100,113,181)',
            'rgb(91, 138, 201)',
            'rgb(255,180,220)',
            'rgb(255,210,210)',
            'rgb(255,195,195)',
            'rgb(255,183,183)',
            'rgb(255,157,157)',
            'rgb(254, 157, 153)',
            'rgb(254, 139, 141)',
            'rgb(255, 181, 166)',
            'rgb(254, 210, 184)'
        ]

        function createMonthList(rows) {
            var pattern = /^\d{4}-\d{2}$/gi;
            var reg = new RegExp(pattern);

            colNames = Object.keys(rows[0])
            monthArr = []
            for (var i = 0; i < colNames.length; i++) {
                if (colNames[i].match(reg)) {
                    monthArr.push(colNames[i]);
                }
            }

            return monthArr
        }

        function createColorDictByMonth(monthArr, colorList) {
            colorDict = {};

            for (var i = 0; i < monthArr.length; i++) {
                colorDict[monthArr[i]] = colorList[i]
            }

            return colorDict

        }

        function unpack(rows, key) {
            return rows.map(function (row) { return row[key]; });
        }

        function createScattergeoTraceByMonth(month) {
            var cityOpp = unpack(rows, month);
            citySize = [];
            hoverText = [];

            for (var i = 0; i < cityOpp.length; i++) {
                var currentSize = cityOpp[i] / scale;
                var currentText = cityName[i] + " Jobs: " + Math.round(cityOpp[i]);
                citySize.push(currentSize);
                hoverText.push(currentText);
            }

            var trace = {
                type: 'scattergeo',
                // locationmode: 'USA-states',
                lat: cityLat,
                lon: cityLon,
                hoverinfo: 'text',
                text: hoverText,
                showlegend: true,
                name: month,
                marker: {
                    size: citySize,
                    color: monthColorDict[month],
                    opacity: 0.1,
                    line: {
                        color: 'white',
                        width: 1
                    },
                }
            };

            return trace

        }

        monthList = createMonthList(rows)
        monthColorDict = createColorDictByMonth(monthArr, colorList)

        var cityName = unpack(rows, 'locality'),
            cityLat = unpack(rows, 'lat'),
            cityLon = unpack(rows, 'lon'),
            scale = 100;

        var data = monthList.map(month => createScattergeoTraceByMonth(month))

        console.log(data)

        var layout = {
            geo: {
                scope: continent ? continent : 'usa',
                width: '100%',
                height: '100%',
                showland: true,
                landcolor: 'rgb(217, 217, 217)',
                subunitwidth: 1,
                countrywidth: 1,
                subunitcolor: 'rgb(255,255,255)',
                countrycolor: 'rgb(255,255,255)'
            },
        };

        Plotly.plot("geo-graph", data, layout, { showLink: false });


    });

});
