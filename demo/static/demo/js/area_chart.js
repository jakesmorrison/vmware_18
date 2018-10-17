function my_chart() {
    return new Highcharts.Chart({
        chart: {
            borderWidth: 0,
            backgroundColor: null,
            renderTo: 'chart',
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
            enabled: true
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
                text: 'Transactions',
                style: {
                    fontSize: '20px',
                }
            },
            labels: {
                style: {
                    fontSize: '15px',
                }
            }
        },{
            min: 0,
            max: 100,
            lineWidth: 0,
            minorGridLineWidth: 0,
            lineColor: 'transparent',
            gridLineWidth: 0,
            tickPositions: [0, 20, 40, 60, 80, 100],
            opposite: true,
            title: {
                text: 'CPU Utilization',
                style: {
                    fontSize: '20px',
                }
            },
            labels: {
                style: {
                    fontSize: '15px',
                },
                formatter: function(){
                    val = this.value;
                    return ''+val.toLocaleString()+'%'
                }
            }
        }],
        plotOptions: {
            areaspline: {
                fillOpacity: 0.45,
                lineWidth: 4,

            },
            spline: {
                lineWidth: 4,
                marker: {
                    enabled: false,
                    states: {
                        hover:{
                            enabled: false
                        }
                    }
                }
            },
              line: {
                lineWidth: 4,
                marker: {
                    enabled: false,
                    states: {
                        hover:{
                            enabled: false
                        }
                    }
                }
            }
        },
        series: [{
            name: 'Transactions',
            data: [],
            color: '#5F5FFF',
            type: 'areaspline',
        },{
            name: 'CPU Utilization',
            data: [],
            color: '#ff5f5f',
            zIndex: 10,
            type: 'line',
            yAxis: 1,
        }]
    });
}
