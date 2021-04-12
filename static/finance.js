function totalRevenue(results) {
    var element = document.getElementById("totalRevenue");
    element.innerHTML = "";
    var tag = document.createElement("h2");
    var text = document.createTextNode(results.totalRevenue);
    tag.appendChild(text);
    element.appendChild(tag);
  }
  
  function COGS(results) {
    var element = document.getElementById("COGS");
    element.innerHTML = "";
    var tag = document.createElement("h2");
    var text = document.createTextNode(results.COGS);
    tag.appendChild(text);
    element.appendChild(tag);
  }
  
  function deprecAndAmort(results) {
    var element = document.getElementById("deprecAndAmort");
    element.innerHTML = "";
    var tag = document.createElement("h2");
    var text = document.createTextNode(results.deprecAndAmort);
    tag.appendChild(text);
    element.appendChild(tag);
  }
  
  function grossMargin(results) {
    var element = document.getElementById("grossMargin");
    element.innerHTML = "";
    var tag = document.createElement("h2");
    var text = document.createTextNode(results.grossMargin);
    tag.appendChild(text);
    element.appendChild(tag);
  }
  
  function grossMarginPercentage(results) {
    var element = document.getElementById("grossMarginPercentage");
    element.innerHTML = "";
    var tag = document.createElement("h2");
    var text = document.createTextNode(results.grossMarginPercentage);
    tag.appendChild(text);
    element.appendChild(tag);
  }
  
  function opEX(results) {
    var element = document.getElementById("opEX");
    element.innerHTML = "";
    var tag = document.createElement("h2");
    var text = document.createTextNode(results.opEX);
    tag.appendChild(text);
    element.appendChild(tag);
  }
  function operatingIncomePercentage(results) {
    var element = document.getElementById("operatingIncomePercentage");
    element.innerHTML = "";
    var tag = document.createElement("h2");
    var text = document.createTextNode(results.operatingIncomePercentage);
    tag.appendChild(text);
    element.appendChild(tag);
  }
  function operationIncome(results) {
    var element = document.getElementById("operationIncome");
    element.innerHTML = "";
    var tag = document.createElement("h2");
    var text = document.createTextNode(results.operationIncome);
    tag.appendChild(text);
    element.appendChild(tag);
  }
  function opExToRevenue(results) {
    var element = document.getElementById("opExToRevenue");
    element.innerHTML = "";
    var tag = document.createElement("h2");
    var text = document.createTextNode(results.opExToRevenue);
    tag.appendChild(text);
    element.appendChild(tag);
  }
  function COGSPerCompany(results) {
    var chartDom = document.getElementById("COGSPerCompany");
    var myChart = echarts.init(chartDom, null, { renderer: "svg" });
    var option;
  
    option = {
      toolbox: {
        show: true,
        feature: {
          saveAsImage: {
            title: "save",
            type: "svg",
          },
        },
      },
      title: {
        text: "COGS Per Company",
      },
      tooltip: {
        trigger: "axis",
        axisPointer: {
          type: "shadow",
        },
      },
      grid: {
        left: "3%",
        right: "3%",
        bottom: "3%",
        containLabel: true,
      },
      xAxis: [
        {
          type: "category",
          axisLabel: { interval: 0, rotate: 60 },
          data: results.COGSPerCompany.index,
          axisTick: {
            alignWithLabel: true,
          },
        },
      ],
      yAxis: [
        {
          type: "value",
        },
      ],
      series: [
        {
          type: "bar",
          barWidth: "60%",
          data: results.COGSPerCompany.data,
        },
      ],
    };
    option && myChart.setOption(option);
    window.addEventListener("resize", function () {
      myChart.resize();
    });
  }

  function getData() {
    var getData = $.get("/data/finance");
    getData.done(function (results) {
      try{
        totalRevenue(results);
      }
      catch(err){
        console.log(err);
      }
      try{
        COGS(results);
      }
      catch(err){
        console.log(err);
      }
      try{
        deprecAndAmort(results);
      }
      catch(err){
        console.log(err);
      }
      try{
        grossMargin(results);
      }
      catch(err){
        console.log(err);
      }
      try{
        grossMarginPercentage(results);
      }
      catch(err){
        console.log(err);
      }
      try{
        opEX(results);
      }
      catch(err){
        console.log(err);
      }
      try{
        opExToRevenue(results);
      }
      catch(err){
        console.log(err);
      }
      try{
        operatingIncomePercentage(results);
      }
      catch(err){
        console.log(err);
      }
      try{
        operationIncome(results);
      }
      catch(err){
        console.log(err);
      }
      try{
        deprecAndAmort(results);
      }
      catch(err){
        console.log(err);
      }
      try{
        COGSPerCompany(results);
      }
      catch(err){
        console.log(err);
      }
    });
  }