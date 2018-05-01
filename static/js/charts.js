$(document).ready(function () {

    $('.charts-carousel').carousel({
      interval:false
    })

    if($('.datavalues').length > 0){

    Highcharts.chart('ratingdiv', {

    chart: {
        type: 'gauge',
        plotBackgroundColor: null,
        plotBackgroundImage: null,
        plotBorderWidth: 0,
        plotShadow: false
    },

    title: {
        text: 'Rating'
    },

    pane: {
        startAngle: -150,
        endAngle: 150,
        background: [{
            backgroundColor: {
                linearGradient: { x1: 0, y1: 0, x2: 0, y2: 1 },
                stops: [
                    [0, '#FFF'],
                    [1, '#333']
                ]
            },
            borderWidth: 0,
            outerRadius: '109%'
        }, {
            backgroundColor: {
                linearGradient: { x1: 0, y1: 0, x2: 0, y2: 1 },
                stops: [
                    [0, '#333'],
                    [1, '#FFF']
                ]
            },
            borderWidth: 1,
            outerRadius: '107%'
        }, {
            // default background
        }, {
            backgroundColor: '#DDD',
            borderWidth: 0,
            outerRadius: '105%',
            innerRadius: '103%'
        }]
    },

    // the value axis
    yAxis: {
        min: 0,
        max: 10,

        minorTickInterval: 'auto',
        minorTickWidth: 1,
        minorTickLength: 10,
        minorTickPosition: 'inside',
        minorTickColor: '#666',

        tickPixelInterval: 30,
        tickWidth: 2,
        tickPosition: 'inside',
        tickLength: 10,
        tickColor: '#666',
        labels: {
            step: 2,
            rotation: 'auto'
        },
        title: {
            text: ''
        },
        plotBands: [{
            from: 5.7,
            to: 10,
            color: '#55BF3B' // green
        }, {
            from: 3.5,
            to: 5.7,
            color: '#DDDF0D' // yellow
        }, {
            from: 0,
            to: 3.5,
            color: '#DF5353' // red
        }]
    },

    series: [{
        name: 'Rating',
        data: [$('.datavalues .rating').data()['rating']],
        tooltip: {
            valueSuffix: ''
        }
    }]

}
);

Highcharts.chart('skewness-chart', {
    chart: {
        type: 'bar'
    },
    title: {
        text: ''
    },
    subtitle: {
        text: ''
    },
    xAxis: {
        categories: ['Skewness'],
        title: {
            text: null
        }
    },
    yAxis: {
        min: 0,
        title: {
            text: '',
            align: 'high'
        },
        labels: {
            overflow: 'justify'
        }
    },
    tooltip: {
        valueSuffix: ''
    },
    plotOptions: {
        bar: {
            dataLabels: {
                enabled: true
            }
        }
    },
//    legend: {
//        layout: 'vertical',
//        align: 'right',
//        verticalAlign: 'top',
//        x: -40,
//        y: 80,
//        floating: true,
//        borderWidth: 1,
//        backgroundColor: ((Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF'),
//        shadow: true
//    },
    credits: {
        enabled: false
    },
    series: [{
        name: 'Skewness',
        data: [$('.datavalues .skewness').data()['skewness']]
    }]
});

Highcharts.chart('kurtosis-chart', {
    chart: {
        type: 'bar'
    },
    title: {
        text: ''
    },
    subtitle: {
        text: ''
    },
    xAxis: {
        categories: ['kurtosis'],
        title: {
            text: null
        }
    },
    yAxis: {
        min: 0,
        title: {
            text: '',
            align: 'high'
        },
        labels: {
            overflow: 'justify'
        }
    },
    tooltip: {
        valueSuffix: ''
    },
    plotOptions: {
        bar: {
            dataLabels: {
                enabled: true
            }
        }
    },
//    legend: {
//        layout: 'vertical',
//        align: 'right',
//        verticalAlign: 'top',
//        x: -40,
//        y: 80,
//        floating: true,
//        borderWidth: 1,
//        backgroundColor: ((Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF'),
//        shadow: true
//    },
    credits: {
        enabled: false
    },
    series: [{
        name: 'Kurtosis',
        data: [$('.datavalues .kurtosis').data()['kurtosis']]
    }]
});

Highcharts.chart('sd-chart', {
    chart: {
        type: 'bar'
    },
    title: {
        text: ''
    },
    subtitle: {
        text: ''
    },
    xAxis: {
        categories: ['Standard Deviation'],
        title: {
            text: null
        }
    },
    yAxis: {
        min: 0,
        title: {
            text: '',
            align: 'high'
        },
        labels: {
            overflow: 'justify'
        }
    },
    tooltip: {
        valueSuffix: ''
    },
    plotOptions: {
        bar: {
            dataLabels: {
                enabled: true
            }
        }
    },
//    legend: {
//        layout: 'vertical',
//        align: 'right',
//        verticalAlign: 'top',
//        x: -40,
//        y: 80,
//        floating: true,
//        borderWidth: 1,
//        backgroundColor: ((Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF'),
//        shadow: true
//    },
    credits: {
        enabled: false
    },
    series: [{
        name: 'Standard Deviation',
        data: [$('.datavalues .std_dev').data()['std_dev']]
    }]
});

Highcharts.chart('spread-chart', {
    chart: {
        type: 'bar'
    },
    title: {
        text: ''
    },
    subtitle: {
        text: ''
    },
    xAxis: {
        categories: ['Data Spread'],
        title: {
            text: null
        }
    },
    yAxis: {
        min: 0,
        title: {
            text: '',
            align: 'high'
        },
        labels: {
            overflow: 'justify'
        }
    },
    tooltip: {
        valueSuffix: ''
    },
    plotOptions: {
        bar: {
            dataLabels: {
                enabled: true
            }
        }
    },
//    legend: {
//        layout: 'vertical',
//        align: 'right',
//        verticalAlign: 'top',
//        x: -40,
//        y: 80,
//        floating: true,
//        borderWidth: 1,
//        backgroundColor: ((Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF'),
//        shadow: true
//    },
    credits: {
        enabled: false
    },
    series: [{
        name: 'Data Spread',
        data: [$('.datavalues .spread').data()['spread']]
    }]
});

Highcharts.chart('marketcap-chart', {
    chart: {
        type: 'bar'
    },
    title: {
        text: ''
    },
    subtitle: {
        text: ''
    },
    xAxis: {
        categories: ['Market capital'],
        title: {
            text: null
        }
    },
    yAxis: {
        min: 0,
        title: {
            text: '',
            align: 'high'
        },
        labels: {
            overflow: 'justify'
        }
    },
    tooltip: {
        valueSuffix: 'USD'
    },
    plotOptions: {
        bar: {
            dataLabels: {
                enabled: true
            }
        }
    },
//    legend: {
//        layout: 'vertical',
//        align: 'right',
//        verticalAlign: 'top',
//        x: -40,
//        y: 80,
//        floating: true,
//        borderWidth: 1,
//        backgroundColor: ((Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF'),
//        shadow: true
//    },
    credits: {
        enabled: false
    },
    series: [{
        name: 'Market Capital',
        data: [parseInt($('.datavalues .marketcap').data()['marketcap'])]
    }]
});


Highcharts.chart('dominancediv', {

    chart: {
        type: 'gauge',
        plotBackgroundColor: null,
        plotBackgroundImage: null,
        plotBorderWidth: 0,
        plotShadow: false
    },

    title: {
        text: 'Market Dominance'
    },

    pane: {
        startAngle: -150,
        endAngle: 150,
        background: [{
            backgroundColor: {
                linearGradient: { x1: 0, y1: 0, x2: 0, y2: 1 },
                stops: [
                    [0, '#FFF'],
                    [1, '#333']
                ]
            },
            borderWidth: 0,
            outerRadius: '109%'
        }, {
            backgroundColor: {
                linearGradient: { x1: 0, y1: 0, x2: 0, y2: 1 },
                stops: [
                    [0, '#333'],
                    [1, '#FFF']
                ]
            },
            borderWidth: 1,
            outerRadius: '107%'
        }, {
            // default background
        }, {
            backgroundColor: '#DDD',
            borderWidth: 0,
            outerRadius: '105%',
            innerRadius: '103%'
        }]
    },

    // the value axis
    yAxis: {
        min: 0,
        max: 100,

        minorTickInterval: 'auto',
        minorTickWidth: 1,
        minorTickLength: 10,
        minorTickPosition: 'inside',
        minorTickColor: '#666',

        tickPixelInterval: 30,
        tickWidth: 2,
        tickPosition: 'inside',
        tickLength: 10,
        tickColor: '#666',
        labels: {
            step: 2,
            rotation: 'auto'
        },
        title: {
            text: ''
        },
        plotBands: [{
            from: 20,
            to: 100,
            color: '#55BF3B' // green
        }, {
            from: 5,
            to: 20,
            color: '#DDDF0D' // yellow
        }, {
            from: 0,
            to: 5,
            color: '#DF5353' // red
        }]
    },

    series: [{
        name: 'Dominance',
        data: [$('.datavalues .dominance').data()['dominance']],
        tooltip: {
            valueSuffix: ''
        }
    }]

}
);

Highcharts.chart('popularitydiv', {

    chart: {
        type: 'gauge',
        plotBackgroundColor: null,
        plotBackgroundImage: null,
        plotBorderWidth: 0,
        plotShadow: false
    },

    title: {
        text: 'Popularity by percentage'
    },

    pane: {
        startAngle: -150,
        endAngle: 150,
        background: [{
            backgroundColor: {
                linearGradient: { x1: 0, y1: 0, x2: 0, y2: 1 },
                stops: [
                    [0, '#FFF'],
                    [1, '#333']
                ]
            },
            borderWidth: 0,
            outerRadius: '109%'
        }, {
            backgroundColor: {
                linearGradient: { x1: 0, y1: 0, x2: 0, y2: 1 },
                stops: [
                    [0, '#333'],
                    [1, '#FFF']
                ]
            },
            borderWidth: 1,
            outerRadius: '107%'
        }, {
            // default background
        }, {
            backgroundColor: '#DDD',
            borderWidth: 0,
            outerRadius: '105%',
            innerRadius: '103%'
        }]
    },

    // the value axis
    yAxis: {
        min: 0,
        max: 100,

        minorTickInterval: 'auto',
        minorTickWidth: 1,
        minorTickLength: 10,
        minorTickPosition: 'inside',
        minorTickColor: '#666',

        tickPixelInterval: 30,
        tickWidth: 2,
        tickPosition: 'inside',
        tickLength: 10,
        tickColor: '#666',
        labels: {
            step: 2,
            rotation: 'auto'
        },
        title: {
            text: ''
        },
        plotBands: [{
            from: 20,
            to: 100,
            color: '#55BF3B' // green
        }, {
            from: 5,
            to: 20,
            color: '#DDDF0D' // yellow
        }, {
            from: 0,
            to: 5,
            color: '#DF5353' // red
        }]
    },

    series: [{
        name: 'Popularity by percentage',
        data: [$('.datavalues .popularity').data()['popularity']],
        tooltip: {
            valueSuffix: ''
        }
    }]

}
);

}


    $('.charts-carousel').on('slide.bs.carousel', function (event) {
      if(event.to == 0){

if($('.datavalues').length > 0){
Highcharts.chart('skewness-chart', {
    chart: {
        type: 'bar'
    },
    title: {
        text: ''
    },
    subtitle: {
        text: ''
    },
    xAxis: {
        categories: ['Skewness'],
        title: {
            text: null
        }
    },
    yAxis: {
        min: 0,
        title: {
            text: '',
            align: 'high'
        },
        labels: {
            overflow: 'justify'
        }
    },
    tooltip: {
        valueSuffix: ''
    },
    plotOptions: {
        bar: {
            dataLabels: {
                enabled: true
            }
        }
    },
//    legend: {
//        layout: 'vertical',
//        align: 'right',
//        verticalAlign: 'top',
//        x: -40,
//        y: 80,
//        floating: true,
//        borderWidth: 1,
//        backgroundColor: ((Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF'),
//        shadow: true
//    },
    credits: {
        enabled: false
    },
    series: [{
        name: 'Skewness',
        data: [$('.datavalues .skewness').data()['skewness']]
    }]
});

Highcharts.chart('kurtosis-chart', {
    chart: {
        type: 'bar'
    },
    title: {
        text: ''
    },
    subtitle: {
        text: ''
    },
    xAxis: {
        categories: ['kurtosis'],
        title: {
            text: null
        }
    },
    yAxis: {
        min: 0,
        title: {
            text: '',
            align: 'high'
        },
        labels: {
            overflow: 'justify'
        }
    },
    tooltip: {
        valueSuffix: ''
    },
    plotOptions: {
        bar: {
            dataLabels: {
                enabled: true
            }
        }
    },
//    legend: {
//        layout: 'vertical',
//        align: 'right',
//        verticalAlign: 'top',
//        x: -40,
//        y: 80,
//        floating: true,
//        borderWidth: 1,
//        backgroundColor: ((Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF'),
//        shadow: true
//    },
    credits: {
        enabled: false
    },
    series: [{
        name: 'Kurtosis',
        data: [$('.datavalues .kurtosis').data()['kurtosis']]
    }]
});

Highcharts.chart('sd-chart', {
    chart: {
        type: 'bar'
    },
    title: {
        text: ''
    },
    subtitle: {
        text: ''
    },
    xAxis: {
        categories: ['Standard Deviation'],
        title: {
            text: null
        }
    },
    yAxis: {
        min: 0,
        title: {
            text: '',
            align: 'high'
        },
        labels: {
            overflow: 'justify'
        }
    },
    tooltip: {
        valueSuffix: ''
    },
    plotOptions: {
        bar: {
            dataLabels: {
                enabled: true
            }
        }
    },
//    legend: {
//        layout: 'vertical',
//        align: 'right',
//        verticalAlign: 'top',
//        x: -40,
//        y: 80,
//        floating: true,
//        borderWidth: 1,
//        backgroundColor: ((Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF'),
//        shadow: true
//    },
    credits: {
        enabled: false
    },
    series: [{
        name: 'Standard Deviation',
        data: [$('.datavalues .std_dev').data()['std_dev']]
    }]
});

Highcharts.chart('spread-chart', {
    chart: {
        type: 'bar'
    },
    title: {
        text: ''
    },
    subtitle: {
        text: ''
    },
    xAxis: {
        categories: ['Data Spread'],
        title: {
            text: null
        }
    },
    yAxis: {
        min: 0,
        title: {
            text: '',
            align: 'high'
        },
        labels: {
            overflow: 'justify'
        }
    },
    tooltip: {
        valueSuffix: ''
    },
    plotOptions: {
        bar: {
            dataLabels: {
                enabled: true
            }
        }
    },
//    legend: {
//        layout: 'vertical',
//        align: 'right',
//        verticalAlign: 'top',
//        x: -40,
//        y: 80,
//        floating: true,
//        borderWidth: 1,
//        backgroundColor: ((Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF'),
//        shadow: true
//    },
    credits: {
        enabled: false
    },
    series: [{
        name: 'Data Spread',
        data: [$('.datavalues .spread').data()['spread']]
    }]
});

Highcharts.chart('marketcap-chart', {
    chart: {
        type: 'bar'
    },
    title: {
        text: ''
    },
    subtitle: {
        text: ''
    },
    xAxis: {
        categories: ['Market capital'],
        title: {
            text: null
        }
    },
    yAxis: {
        min: 0,
        title: {
            text: '',
            align: 'high'
        },
        labels: {
            overflow: 'justify'
        }
    },
    tooltip: {
        valueSuffix: 'USD'
    },
    plotOptions: {
        bar: {
            dataLabels: {
                enabled: true
            }
        }
    },
//    legend: {
//        layout: 'vertical',
//        align: 'right',
//        verticalAlign: 'top',
//        x: -40,
//        y: 80,
//        floating: true,
//        borderWidth: 1,
//        backgroundColor: ((Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF'),
//        shadow: true
//    },
    credits: {
        enabled: false
    },
    series: [{
        name: 'Market Capital',
        data: [parseInt($('.datavalues .marketcap').data()['marketcap'])]
    }]
});
      }
      }
      if(event.to == 1){
      if($('.datavalues').length > 0){
        Highcharts.chart('statsdiv', {
    title: {
        text: 'Closing Price Histogram'
    },
    xAxis: [{
        title: { text: 'Data' },
        alignTicks: false
    }, {
        title: { text: 'Histogram' },
        alignTicks: false,
        opposite: true
    }],

    yAxis: [{
        title: { text: 'Data' }
    }, {
        title: { text: 'Histogram' },
        opposite: true
    }],

    series: [{
        name: 'Histogram',
        type: 'histogram',
        xAxis: 1,
        yAxis: 1,
        baseSeries: 's1',
        zIndex: -1
    }, {
        name: 'Data',
        type: 'scatter',
        data: $('.datavalues .prices').data()['prices'],
        id: 's1',
        marker: {
            radius: 1.5
        }
    }]
});
}

      }
    });


});
