function line_chart(id, title, yaxis) {
    var fontFamily = 'arial';
    var color = '#58585a'
    var last_point_val;
    return new Highcharts.Chart({
        chart: {
            borderColor: '#58585A',
            borderWidth: 2,
            backgroundColor: null,
            renderTo: id,
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
            text: title,
            style:{
                fontFamily: fontFamily,
                color: color,
                fontSize: '30px',
            }
        },
        legend: {
//            enabled: true,
//            layout: 'vertical',
//            align: 'left',
//            verticalAlign: 'middle',
            itemStyle:{
                fontFamily: fontFamily,
                color: color,
                fontSize: '18px',
            }

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
            opposite: true,
            title: {
                text: yaxis,
                style:{
                    fontFamily: fontFamily,
                    color: color,
                    fontSize: '22px',
                }
            },
            labels: {
                enabled:true,
                formatter: function(){
                    if (title === "IOPS"){
                        return this.value.toLocaleString()
                    }
                    else if(title==="Bandwidth")
                        return this.value.toLocaleString() +" MB/s"
                    else{
                        return this.value.toLocaleString() +" ms"
                    }
                },
                style:{
                    fontFamily: fontFamily,
                    color: color,
                    fontSize: '18px',
                }
            },
        }],
        plotOptions: {
            series:{
                animation: false,
                dataLabels:{
                    enabled: false,
                    style:{
                        fontFamily: fontFamily,
                        color: color,
                        fontSize: '18px',
                    },
                    formatter: function(){
                        return this.y.toLocaleString()
                    }
                }
            },
            line:{
                lineWidth: 5,
                animation: false,
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
            name: 'NVDIMM 1',
            data: [],
            color: '#ffb500',
            type: 'line',
        },{
            name: 'NVDIMM 2',
            data: [],
            color: '#00A3E1',
            type: 'line',
        },{
            name: 'NVMe',
            data: [],
            color: '#873299',
            type: 'line',
        }]
    });
}
