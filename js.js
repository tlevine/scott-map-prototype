//For testing
var data;

//Creates the basic map
function createMap(){
  var xy = d3.geo.albersUsa();
  var svg = d3.select("#viz").append("svg");
  svg.attr("id", "mainSVG")
    .attr("width", 940)
    .attr("height", 940)

  var perishes = svg.append("g")
    .attr("transform", function(d) { return "scale(5)"})
    .append('g')
      .attr("id", "perishes")
      .attr("transform", function(d) { return "translate(-500, -300)"})

  d3.json("parishes.json", function(collection){
      data = collection;
      perishes.selectAll("path")
        .data(collection.features)
        .enter().append("path")
        .attr("d", d3.geo.path().projection(xy))
        .attr("fill", function(perish){ return colorPicker(perish)})
  });

}

//Figures out the color of the perish
function colorPicker(perish){
  return 'grey';
}

window.onload = createMap
