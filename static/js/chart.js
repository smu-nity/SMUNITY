function drawChart() {
    const visitors = new google.visualization.DataTable();
    visitors.addColumn('string', '날짜');
    visitors.addColumn('number', '방문자 수');
    visitors.addColumn({type:'number', role:'annotation'})
    visitors.addRows(visitors_data);
    const chart = new google.visualization.ColumnChart(document.getElementById('chart_visitors'));
    chart.draw(visitors, options);

    const members = new google.visualization.DataTable();
    members.addColumn('date', '날짜');
    members.addColumn('number', '회원 수');
    members.addRows(members_data);
    const charts = new google.visualization.LineChart(document.getElementById('chart_members'));
    charts.draw(members, options);

    window.addEventListener('resize', drawChart, false)
}

const options = {
    colors: ['rgb(1, 42, 127)'],
    vAxis: {
        minValue: 0
    },
    width: '100%',
    height: 400,
};

google.charts.load('current', {'packages':['corechart', 'bar']});
google.charts.load('current', {packages: ['corechart', 'line']});
google.charts.setOnLoadCallback(drawChart);
