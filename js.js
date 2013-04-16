var data;

function createMap(){
  var xy = d3.geo.albersUsa();
  var svg = d3.select("#viz").append("svg");
  svg.attr("id", "mainSVG")
    .attr("width", 800)
    .attr("height", 800);

  var perishes = svg.append("g")
    .attr("id", "perishes");

  d3.json("parishes.json", function(collection){
      data = collection;
      perishes.selectAll("path")
        .data(collection.features)
        .enter().append("path")
        .attr("d", d3.geo.path().projection(xy));
  });

}