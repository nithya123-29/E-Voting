async function capture()
{
    var interface = document.getElementById('interface').value;
    var time = document.getElementById('captureTime').value;
    if(time == 0){
        let a = await eel.CheckInterfaceAndCap(interface)();
        document.getElementById('packetsCaptured').innerHTML = a + " packets are captured";
    }
    else{
        let a = await eel.CheckInterfaceAndCap_Any(interface, time)();
        document.getElementById('packetsCaptured').innerHTML = a + " packets are captured";
    }

    reader();
}

async function reader()
{
  let report = await eel.reader()();
  alert(report);
}

$(function(){
  $("#includeIoGraph").load("iograph.html");
});

$(function(){
  $("#includeSrcGraph").load("srcIPOccurance.html");
});
$(function(){
  $("#includefrequencyProtocol").load("frequencyProtocol.html");
});


//$('#interface').on('change', function() {
//  alert(interface);
//  var interface = this.val();
//  if(interface == 'others'){
//    $("#othersInterface").prop('disabled', true);
//});
