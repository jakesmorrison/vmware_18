var spark_nvme_bw = [];
var spark_nvme_lat = [];
var spark_nvme_iops = [];
var spark_nvdimm_bw = [];
var spark_nvdimm_lat = [];
var spark_nvdimm_iops = [];

function create_spark_line(nvme_bw,nvme_lat,nvme_iops,nvdimm_bw,nvdimm_lat,nvdimm_iops, nvme_or_nvdimm){


    spark_line_options_nvme = {
        type: 'line',
        width: '33%',
        lineColor: '#873299',
        fillColor: '#c39bcc',
        spotColor: undefined,
        minSpotColor: undefined,
        maxSpotColor: undefined,
        highlightSpotColor: undefined,
        highlightLineColor: undefined,
        spotRadius: 0
    }


    if(nvme_or_nvdimm == 1){
        console.log(nvme_or_nvdimm)
        spark_line_options_nvme["lineColor"] = '#00A3E1';
        spark_line_options_nvme["fillColor"] = '#2fc6ff';
    }

    spark_line_options_nvdimm = {
        type: 'line',
        width: '33%',
        lineColor: '#ffb500',
        fillColor: '#ffe099',
        spotColor: undefined,
        minSpotColor: undefined,
        maxSpotColor: undefined,
        highlightSpotColor: undefined,
        highlightLineColor: undefined,
        spotRadius: 0
    }

    if(spark_nvme_bw[spark_nvme_bw.length-1]===nvme_bw){}
    else if(spark_nvme_bw.length>5){spark_nvme_bw.shift(); spark_nvme_bw.push(nvme_bw)}
    else{ spark_nvme_bw.push(nvme_bw)}
    $("#sparkline_bw_nvme").sparkline(spark_nvme_bw, spark_line_options_nvme);

    if(spark_nvdimm_bw[spark_nvdimm_bw.length-1]===nvdimm_bw){}
    else if(spark_nvdimm_bw.length>5){spark_nvdimm_bw.shift(); spark_nvdimm_bw.push(nvdimm_bw)}
    else{ spark_nvdimm_bw.push(nvdimm_bw)}
    $("#sparkline_bw_nvdimm").sparkline(spark_nvdimm_bw, spark_line_options_nvdimm);
    
    if(spark_nvme_lat.length>5 && spark_nvme_lat[spark_nvme_lat.length-1]!=nvme_lat){spark_nvme_lat.shift(); spark_nvme_lat.push(nvme_lat)}
    else{ spark_nvme_lat.push(nvme_lat)}
    $("#sparkline_lat_nvme").sparkline(spark_nvme_lat, spark_line_options_nvme);

    if(spark_nvdimm_lat.length>5 && spark_nvdimm_lat[spark_nvdimm_lat.length-1]!=nvdimm_lat){spark_nvdimm_lat.shift(); spark_nvdimm_lat.push(nvdimm_lat)}
    else{ spark_nvdimm_lat.push(nvdimm_lat)}
    $("#sparkline_lat_nvdimm").sparkline(spark_nvdimm_lat, spark_line_options_nvdimm);
    
    if(spark_nvme_iops.length>5 && spark_nvme_iops[spark_nvme_iops.length-1]!=nvme_iops){spark_nvme_iops.shift(); spark_nvme_iops.push(nvme_iops)}
    else{ spark_nvme_iops.push(nvme_iops)}
    $("#sparkline_iops_nvme").sparkline(spark_nvme_iops, spark_line_options_nvme);

    if(spark_nvdimm_iops.length>5 && spark_nvdimm_iops[spark_nvdimm_iops.length-1]!=nvdimm_iops){spark_nvdimm_iops.shift(); spark_nvdimm_iops.push(nvdimm_iops)}
    else{ spark_nvdimm_iops.push(nvdimm_iops)}
    $("#sparkline_iops_nvdimm").sparkline(spark_nvdimm_iops, spark_line_options_nvdimm);
    
}