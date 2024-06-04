const ws = new WebSocket('ws://192.168.7.2:8081');
let counter = 0; // Counter for x-axis labels for chart1
let counter2 = 0; // Counter for x-axis labels for chart2
let counter3 = 0;

var ctx1 = document.getElementById('chart1').getContext('2d');
var ctx2 = document.getElementById('chart2').getContext('2d');
var ctx3 = document.getElementById('chart3').getContext('2d');

var chart1 = new Chart(ctx1, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'Engine Speed in r.p.m.',
            data: [],
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            borderColor: 'rgba(255, 99, 132, 1)',
            borderWidth: 1,
            fill: false
        }]
    },
    options: {
        scales: {
            x: {
                type: 'linear',
                position: 'bottom'
            },
            y: {
                beginAtZero: true
            }
        },
        animation: {
            duration: 0 // Consider disabling animation for faster updates
        },
        maintainAspectRatio: true,
        responsive: true,
        plugins: {
            legend: {
                display: false // Hide legend
            }
        },
        plugins: {
            tooltip: {
                callbacks: {
                    label: function(context) {
                        return 'Engine Speed' + ': ' + context.parsed.y.toFixed(2);
                    }
                }
            }
        }
    }
});

var chart2 = new Chart(ctx2, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'Wheel Based Vehicle Speed in km/hr',
            data: [],
            borderColor: 'rgba(0, 255, 0, 1)',
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            x: {
                type: 'linear',
                position: 'bottom'
            },
            y: {
                beginAtZero: true
            }
        },
        animation: {
            duration: 0 // Consider disabling animation for faster updates
        },
        maintainAspectRatio: true,
        responsive: true,
        plugins: {
            legend: {
                display: false // Hide legend
            }
        },
        plugins: {
            tooltip: {
                callbacks: {
                    label: function(context) {
                        return 'Wheel Based Vehicle Speed' + ': ' + context.parsed.y.toFixed(2);
                    }
                }
            }
        }
    }
});

var chart3 = new Chart(ctx3, {
    type: 'line',
    data: {
        datasets: [{
            label: 'Driver Demand Percentage Torque',
            data: [],
            pointBackgroundColor: 'rgba(75, 192, 192, 0.5)',
            pointRadius: 5,
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            x: {
                type: 'linear',
                position: 'bottom',
            },
            y: {
                beginAtZero: true,
            }
        },
        animation: {
            duration: 0 // Disable animation for faster updates
        },
        responsive: true,
        maintainAspectRatio: true,
        plugins: {
            legend: {
                display: false // Hide the legend for a cleaner look
            }
        }
    }
});

function updateScatterChartData(chart, torque, counterName) {
    if (counterName === 'counter3') {
        const newLabel = ++counter3;
        chart.data.datasets[0].data.push({ x: counter3, y: torque });
        if (chart.data.datasets[0].data.length > 10) {
            chart.data.datasets[0].data.shift();
        }
        chart.update();
        counter3++;
    }
}

function updateChartData(chart, counterName, value) {
    if (counterName === 'counter') {
        const newLabel = ++counter;
        chart.data.labels.push(newLabel);
        chart.data.datasets.forEach((dataset) => {
            dataset.data.push(value);
        });
        chart.data.datasets[0].label = `Engine Speed (r.p.m.): ${value.toFixed(2)}`;
        if (chart.data.labels.length > 50) {
            chart.data.labels.shift();
            chart.data.datasets.forEach((dataset) => {
                dataset.data.shift();
            });
        }
        chart.update();
    } else if (counterName === 'counter2') {
        const newLabel = ++counter2;
        chart.data.labels.push(newLabel);
        chart.data.datasets.forEach((dataset) => {
            dataset.data.push(value);
        });
        chart.data.datasets[0].label = `Wheel Based Vehicle Speed (km/hr): ${value.toFixed(2)}`;
        if (chart.data.labels.length > 50) {
            chart.data.labels.shift();
            chart.data.datasets.forEach((dataset) => {
                dataset.data.shift();
            });
        }
        chart.update();
    }
}

let lastUpdateTime1 = 0;
const updateInterval1 = 250;

let lastUpdateTime2 = 0;
const updateInterval2 = 250;

ws.onmessage = function(event) {
    const message = JSON.parse(event.data);

    if (message.id === 0x0CF00400) {
        const now = Date.now();
        if (now - lastUpdateTime1 < updateInterval1) return;
        lastUpdateTime1 = now;
        const rawData = message.data.data.slice(3, 5).reverse();
        const dataValue = new DataView(new Uint8Array(rawData).buffer).getUint16(0, false) * 0.125;
        updateChartData(chart1, 'counter', dataValue);
        const torque = message.data.data[1] * 1 - 125;
        console.log('Current Val:', torque);
        updateScatterChartData(chart3, torque, 'counter3');
    } else if (message.id === 0x18FEF100) {
        const now = Date.now();
        if (now - lastUpdateTime2 < updateInterval2) return;
        lastUpdateTime2 = now;
        const rawData = message.data.data.slice(1, 3).reverse();
        const dataValue = new DataView(new Uint8Array(rawData).buffer).getUint16(0, false) * 0.003906;
        updateChartData(chart2, 'counter2', dataValue);
    }
};

ws.onerror = function(error) {
    console.log('WebSocket Error:', error);
};