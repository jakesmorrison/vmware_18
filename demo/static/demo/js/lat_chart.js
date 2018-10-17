function lat_chart() {
    return new Highcharts.Chart({
        chart: {
            borderWidth: 0,
            backgroundColor: null,
            renderTo: 'lat',
        },
        exporting: {
            enabled: false
        },
        credits: {
            enabled: false
        },
        tooltip: {
            enabled: false
        },
        title: {
            text: '',
        },
        legend: {
            enabled: false
        },
        xAxis: {
            title: {
                text: '',
            },
            labels:{
                enabled: false
            },
            minorTickLength: 0,
            tickLength: 0,
            lineWidth: 0,
            minorGridLineWidth: 0,
            lineColor: 'transparent',
        },
        yAxis: [{
            min: 0,
            title: {
                text: '',
            },
            labels: {
                enabled:false
            },
            minorTickLength: 0,
            tickLength: 0,
            lineWidth: 0,
            minorGridLineWidth: 0,
            lineColor: 'transparent',
            gridLineColor: 'transparent'
        }],
        plotOptions: {
            columnrange: {
                pointPadding: 0,
                groupPadding: 0,
//                zones:[{
//                    value: 5,
//                    color: '#5FFF5F'
//                },{
//                    value: 10,
//                    color: '#5F5FFF'
//                },{
//                    value: 20,
//                    color: '#FFFF5F'
//                },{
//                    color: '#FF5F5F'
//                }]
            }
        },
        series: [{
            name: 'CPU Utilization',
            data: [],
            color: '#31353a',
            type: 'columnrange',
        }]
    });
}
