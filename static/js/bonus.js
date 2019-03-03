d3.json('/samples').then(flask_data => {
      
      d3.select('#selDataset')
      .selectAll('option')
      .data(flask_data)
      .enter()
      .append('option')
      .text(r => r.SAMPLE)
      .attr('value', r => r.SAMPLE);
  });
